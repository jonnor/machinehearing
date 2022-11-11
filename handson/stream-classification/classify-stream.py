
import argparse
import queue
import sys
import datetime

import matplotlib.pyplot as plt
import numpy
import sounddevice
import pandas

import os
import logging

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
    S = librosa.stft(audio, n_fft=n_fft, window=window)
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



def main():
    parser, args = parse()

    print('list')

    if args.list_devices:
        print(sounddevice.query_devices())
        parser.exit(0)

    if args.samplerate is None:
        device_info = sounddevice.query_devices(args.device, 'input')
        args.samplerate = device_info['default_samplerate']

    samplerate = args.samplerate

    stream = SoundcardInput(device=args.device, channels=args.channels, samplerate=samplerate)

    duration = 1.0
    overlap = args.overlap
    hop_length = int(duration*samplerate) * (1-overlap)

    n_fft = 1024*8

    chunker = AudioChunker(window_size=int(duration*samplerate), window_hop=hop_length)

    with stream.open():
        while True:
            data = stream.audio_queue.get()
            data = numpy.squeeze(data)
            
            print('audio', data.shape)
            chunker.push_audio(data)

            w = None
            try:
                w = chunker.window_queue.get(block=False)
            except queue.Empty as e:
                pass
            if w is not None:
                print('window', w.shape)
                s = spectrum_welch(w, sr=samplerate, n_fft=n_fft, window='hann')
                print(s)

    print('stopped')

if __name__ == '__main__':
    main()
