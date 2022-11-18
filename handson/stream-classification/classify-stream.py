
import argparse
import queue
import sys
import datetime
import time
import os
import logging

import matplotlib.pyplot as plt
import numpy
import sounddevice
import pandas
import seaborn


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def parse():

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    parser.add_argument(
        'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
        help='input channels to plot (default: the first)')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-r', '--samplerate', type=float, help='sampling rate of audio device')

    parser.add_argument(
        '--overlap', type=float, default=0.5,
        help='how much overlap between consequctive windows to classify')

    args = parser.parse_args()
    if any(c < 1 for c in args.channels):
        parser.error('argument CHANNEL: must be >= 1')

    return parser, args


class SoundcardInput():

    def __init__(self, device, samplerate=16000, channels=[1]):

        self.channels = channels

        self.device = device
        self.samplerate = samplerate
        self.audio_queue = queue.Queue()
        self.stream = None

    def open(self):

        def audio_callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)

            mapping = [c - 1 for c in self.channels]  # Channel numbers start with 1

            # Make sure to copy input
            data = indata[:, mapping].copy()
            self.audio_queue.put(data)

        self.stream = sounddevice.InputStream(
            device=self.device, channels=max(self.channels),
            samplerate=self.samplerate, callback=audio_callback)

        # TODO: use a custom context manager that wraps stream
        return self.stream

class AudioChunker():
    """
    Create fixed-length audio analysis windows from an input stream.

    Window can be overlapping. 
    """
    def __init__(self, window_size, window_hop):
        self.window_size = window_size
        self.window_hop = window_hop

        # output
        self.window_queue = queue.Queue()

        # internal
        self.audio_buffer = numpy.zeros(shape=(window_size,))
        self.new_samples = 0

    def push_audio(self, data):
        # move existing data over
        self.audio_buffer = numpy.roll(self.audio_buffer, len(data), axis=0)
        # add the new data
        self.audio_buffer[len(self.audio_buffer)-len(data):len(self.audio_buffer)] = data

        # check if we have received enough new data to output a new window
        self.new_samples += len(data)
        #print('push', self.new_samples)
        if self.new_samples >= self.window_hop:
            w = self.audio_buffer.copy()
            self.window_queue.put(w)
            self.new_samples -= self.window_size 


def spectrum_stft(audio, sr, n_fft, window):
    """Method 1: Compute magnitude spectrogram, average over time"""
    import librosa
    S = librosa.stft(y=audio, n_fft=n_fft, window=window)
    S_db = librosa.amplitude_to_db(numpy.abs(S*S), ref=0.0, top_db=120)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    spectrum = numpy.mean(S_db, axis=1)
    return pandas.Series(spectrum, index=freqs)

def spectrum_welch(audio, sr, n_fft, window):
    """Method 2: Use Welch method. Uses overlapped complex spectrum"""
    import scipy.signal
    import librosa
    freqs, power = scipy.signal.welch(audio, fs=sr, nfft=n_fft, window=window,
        scaling="spectrum", average='median')
    db = librosa.power_to_db(power, ref=0.0, top_db=120)
    return pandas.Series(db, index=freqs)

def soundlevel(audio, sr, length=0.125):
    import librosa
    frame_length = int(length * sr)
    rms = librosa.feature.rms(y=audio, frame_length=frame_length)
    db = librosa.power_to_db(rms, ref=0.0, top_db=120)
    db = numpy.squeeze(db)
    return db

def freq_response_configure_xaxis(ax, fmin=10, fmax=22000):
    import matplotlib.ticker as ticker

    # X axis
    ax.set_xlabel('Frequency (Hz)')
    ax.set(xlim=(fmin, fmax), xscale='log')
    f_major = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    ax.xaxis.set_major_locator(ticker.FixedLocator(f_major))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(f_major))
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=10, numticks=10))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())   
    ax.grid(visible=True, axis='x')

def butter_bandpass(lowcut, highcut, fs, order=5):
    import scipy.signal
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    import scipy.signal
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = scipy.signal.lfilter(b, a, data)
    return y


def estimate_limits(v, sigma=3, min=None, max=None):
    mean, std = numpy.mean(v), numpy.std(v)
    std_margin = sigma * std
    minmax_margin = 0.2
    upper = numpy.maximum(mean + std_margin, numpy.max(v)*(1.0+minmax_margin))
    lower = numpy.minimum(mean - std_margin, numpy.min(v)*(1.0-minmax_margin))
    if min is not None:
        lower = numpy.minimum(min, lower)
    if max is not None:
        upper = numpy.maximum(max, upper)
    return lower, upper

class Analyzer():

    def __init__(self, samplerate, history_steps, hop_length):

        self.samplerate = samplerate
        self.history_steps = history_steps
        self.hop_length = hop_length

        self.features = {
            'soundlevel.typical': [],
            'spectrum.lower': [],
            #'spectrum.upper': [],
        }

        rows = [ 'spectrum' ] + list(self.features.keys()) + [ 'anomaly', 'dist' ] 
  
        fig, axs  = plt.subplots(nrows=len(rows), figsize=(6, 3))

        self.fig = fig
        self.axes = { k: v for k, v in zip(rows, axs) }        

        self.anomaly_scores = []

    def push_features(self, features):
        steps = self.history_steps

        for name, value in features.items():

            s = self.features.get(name)
            if s is None:
                continue

            # in the start, fill everything with same value
            if len(s) == 0:
                s = [ value ] * steps
            else:
                # in normal case, shift old data, append new
                s = s[1:]
                s.append(value)

            assert len(s) == steps, (len(s), steps)

            self.features[name] = s


    def push_audio(self, w):
        samplerate = self.samplerate
        n_fft = 1024*8

        w = butter_bandpass_filter(w, lowcut=20, highcut=4000, fs=samplerate, order=5)

        update_start_time = time.time()

        # Analyze the new audio

        #print('window', w.shape)
        spectrum = spectrum_welch(w, sr=samplerate, n_fft=n_fft, window='hann')

        #sl = soundlevel(w, sr=samplerate, length=0.125)
        #sl = pandas.Series(sl)

        #cum = spectrum.cumsum() / spectrum.sum()

        #print(cum[(cum < 0.10)])
        #upper = cum[(cum > 0.50)].index[0]
        #lower = cum[(cum < 0.10)].index[-1]

        import librosa
        S = librosa.stft(y=w, n_fft=n_fft)
        S = numpy.abs(S)
        #print(S.shape)
        #S = numpy.expand_dims(spectrum, 1)
        #print(S.shape)
        # FIXME: rolloff broken with Welch spectrum
        lower = librosa.feature.spectral_rolloff(S=S, n_fft=n_fft, sr=samplerate, roll_percent=0.20)
        lower = numpy.median(lower)

        upper = librosa.feature.spectral_rolloff(S=S, n_fft=n_fft, sr=samplerate, roll_percent=0.50)
        upper = numpy.median(upper)

        # Compute colors for features, so they can be consistent whenever the feature is used
        palette = seaborn.color_palette('tab10')
        feature_colors = { k: palette[i] for i, k in enumerate(self.features.keys()) }

        #energy = numpy.sum(S, axis=0)
        #sl = librosa.power_to_db(energy, ref=0.0)
        #sl_typical = numpy.quantile(sl, 0.5) 

        sl_typical = spectrum.quantile(0.90)

        f = {
            'soundlevel.typical' : sl_typical,
            'spectrum.lower' : lower,
            'spectrum.upper' : upper,
        }
        #print('features', f)
        self.push_features(f)

        # Run anomaly detection
        from sklearn.ensemble import IsolationForest
        from sklearn.neighbors import LocalOutlierFactor
        from sklearn.preprocessing import RobustScaler
        from sklearn.pipeline import make_pipeline
        from sklearn.covariance import EllipticEnvelope

        #est = IsolationForest(n_estimators=50)
        est = make_pipeline(
            RobustScaler(),
            LocalOutlierFactor(n_neighbors=5, novelty=True),
        )
        est = make_pipeline(
            #RobustScaler(),
            EllipticEnvelope(),
        )

        X = pandas.DataFrame(self.features)
        X = X + (0.01+numpy.random.random(size=X.shape))
        est.fit(X)
        scores = est.score_samples(X)

        # Update user interface
 

        # Spectrum view
        #print(spectrum)
        spectrum_ax = self.axes['spectrum']
        spectrum_ax.clear()
        spectrum_ax.plot(spectrum.index, spectrum.values, color='black')
        freq_response_configure_xaxis(spectrum_ax, fmax=(self.samplerate/2))
        spectrum_ax.set_ylabel("Audio spectrum")

        # Mark features in spectrum view
        for name in ['spectrum.lower', 'spectrum.upper']:
            if not self.features.get(name):
                continue
            color = feature_colors[name]
            spectrum_ax.axvline(f[name], color=color, alpha=0.5)

        for name in ['soundlevel.typical']:
            color = feature_colors[name]
            spectrum_ax.axhline(f[name], color=color, alpha=0.5)

        hop_duration = float(self.hop_length) / self.samplerate


        # TODO: mark X axis with negative time. Maybe share X axis for multiple
        # Plot all the features as timeline
        for feature_name in self.features.keys():
            ax = self.axes[feature_name]
            ax.clear()

            color = feature_colors[feature_name]
            y = self.features[feature_name]
            t = numpy.arange(-len(y), 0, 1) * hop_duration

            ax.plot(t, y, color=color)
            ax.set_ylabel(feature_name)

            upper, lower = numpy.quantile(y, 0.75), numpy.quantile(y, 0.25)
            ax.axhline(upper, ls='--', color=color, alpha=0.5)
            ax.axhline(lower, ls='--', color=color, alpha=0.5)
            ax.fill_between(t, lower, upper, color=color, alpha=0.2)

            # do not show time labels
            ax.tick_params(axis='x', bottom=False, labelbottom=False)

        update_end_time = time.time()

        #timeline_ax.plot(t, y)
    
        # Compute anomaly scores
        self.anomaly_scores = []


        # LocalOutlierFactor
        #scaled = -1.0 * (scores + 1.5)
        #scaled *= 0.5

        #print(scores)

        # EllipticEnvelope
        scaled = -1.0 * (scores)
        scaled *= 0.005

        # isolationforest
        #scaled = -1.0 * (scores + 0.5)
        #scaled *= 2.0
        norm_scores = numpy.clip(scaled, 0.0, 1.0)

        if len(self.anomaly_scores) == 0:
            self.anomaly_scores = norm_scores
        else:
            self.anomaly_scores = self.anomaly_scores[1:] 
            self.anomaly_scores.append(norm_scores[-1])

        threshold = 0.2

        # Show anomaly scores
        anomaly_ax = self.axes['anomaly']
        anomaly_ax.clear()
        anomaly_ax.plot(t, self.anomaly_scores, color='black', alpha=0.5)
        anomaly_ax.fill_between(t, 0, self.anomaly_scores, interpolate=True, color='red')
        anomaly_ax.set_ylim(0.0, 1.0)
        anomaly_ax.set_ylabel('Anomaly score')
        anomaly_ax.set_xlabel("Time")

        anomaly_ax.axhline(threshold, ls='--', alpha=0.2, color='red')
    
        scatter_ax = self.axes['dist']
        y_feature = 'soundlevel.typical'
        x_feature = 'spectrum.lower'

        scatter_ax.clear()

        r, g, b = 0, 0, 0


        # Plot bi-variate
        anomalies = self.anomaly_scores > threshold

        alphas = numpy.linspace(0.05, 0.8, len(self.features[x_feature]))
        color = [ (0, 0, 0, a) if s < threshold else (0.8, 0, 0, a) for s, a in zip(self.anomaly_scores, alphas)  ]
        scatter_ax.scatter(self.features[x_feature], self.features[y_feature], color=color)

        x_lim = estimate_limits(self.features[x_feature], min=0)
        y_lim = estimate_limits(self.features[y_feature], min=0)

        scatter_ax.set_xlim(x_lim)
        scatter_ax.set_ylim(y_lim)
    

        dur = update_end_time - update_start_time
        print(f'Update {dur*1000:.0f}ms')



def main():
    parser, args = parse()

    if args.list_devices:
        print('list')
        print(sounddevice.query_devices())
        parser.exit(0)

    if args.samplerate is None:
        device_info = sounddevice.query_devices(args.device, 'input')
        args.samplerate = device_info['default_samplerate']

    samplerate = args.samplerate

    stream = SoundcardInput(device=args.device, channels=args.channels, samplerate=samplerate)

    duration = 1.0
    overlap = args.overlap
    hop_duration = duration * (1-overlap)
    hop_length = int(samplerate * hop_duration) 


    chunker = AudioChunker(window_size=int(duration*samplerate), window_hop=hop_length)

    history = 20.0
    history_steps = int(history / hop_duration)

    analyze = Analyzer(samplerate=samplerate, history_steps=history_steps, hop_length=hop_length)

    chunk_no = 0
    with stream.open():
        while True:
            data = stream.audio_queue.get()
            data = numpy.squeeze(data)
            
            #print('audio', data.shape)
            chunker.push_audio(data)

            w = None
            try:
                w = chunker.window_queue.get(block=False)
            except queue.Empty as e:
                pass
            if w is not None:
                chunk_no += 1
                # potentially ignore first chunks,
                # since audio data often has not quite settled
                if chunk_no > 0:
                    analyze.push_audio(w)


            plt.pause(0.001)

    print('stopped')

if __name__ == '__main__':
    main()
