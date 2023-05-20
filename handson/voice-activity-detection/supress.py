
import math
import numpy
import pandas
import librosa
import soundfile
from speechbrain.pretrained import VAD
import matplotlib
import matplotlib.pyplot as plt

def detect_voice(
    path,
    activation_threshold = 0.70,
    deactivation_threshold = 0.25,
    min_pause = 0.200,
    min_activation = 0.100,
    save_dir = 'model_dir',
    segment_pre = 0.0,
    segment_post = 0.0,
    double_check_threshold = None,
    parallel_chunks = 4,
    chunk_size = 1.0,
    overlap_chunks = True,
    ):

    # do initial, coarse-detection
    vad = VAD.from_hparams(source="speechbrain/vad-crdnn-libriparty", savedir=save_dir)

    probabilities = vad.get_speech_prob_file(path,
        large_chunk_size=chunk_size*parallel_chunks,
        small_chunk_size=chunk_size,
        overlap_small_chunk=overlap_chunks)

    thresholded = vad.apply_threshold(probabilities,
        activation_th=activation_threshold,
        deactivation_th=deactivation_threshold).float()

    boundaries = vad.get_boundaries(thresholded)

    # refine boundaries using energy-based VAD
    boundaries = vad.energy_VAD(path, boundaries,
            activation_th=activation_threshold,
            deactivation_th=deactivation_threshold)

    # post-process to clean up
    if min_pause is not None:
        boundaries = vad.merge_close_segments(boundaries, close_th=min_pause)

    if min_activation is not None:
        boundaries = vad.remove_short_segments(boundaries, len_th=min_activation)

    if double_check_threshold:
        boundaries = vad.double_check_speech_segments(boundaries, speech_th=double_check_threshold)

    # convert to friendly pandas DataFrames with time info 
    events = pandas.DataFrame(boundaries, columns=['start', 'end'])
    events['class'] = 'speech'

    p = numpy.squeeze(probabilities)
    times = pandas.Series(numpy.arange(0, len(p)) * vad.time_resolution, name='time')
    p = pandas.DataFrame(p, columns=['speech'], index=times)

    return p, events



def apply_gain(path, segments, default=0.0, out=None, sr=None):

    audio, sr = soundfile.read(path, always_2d=True)

    # compute gain curves
    gains = numpy.full_like(audio, librosa.db_to_power(default)) 

    for idx, seg in segments.iterrows():

        s = math.floor(sr * seg['start'])
        e = math.ceil(sr * seg['end'])
        gain = librosa.db_to_power(seg['gain'])

        gains[s:e, :] = gain

    # apply to audio
    audio = audio * gains

    if out is not None:
        soundfile.write(out, audio, samplerate=sr)


    return audio, sr


def plot_spectrogram(ax, path, sr=16000, hop_length=1024):

    audio, sr = librosa.load(path, sr=sr)
    S = librosa.feature.melspectrogram(y=audio, sr=sr, hop_length=hop_length)
    S_db = librosa.power_to_db(S, ref=numpy.max)

    librosa.display.specshow(ax=ax, data=S_db,
            sr=sr, hop_length=hop_length,
            x_axis='time', y_axis='mel')

    return S_db

def plot_vad(input_path, probabilities, boundaries, output_path):

    fig, (input_spec_ax, vad_ax, output_spec_ax) = plt.subplots(3, figsize=(10, 5), sharex=True)

    # show spectrogram
    plot_spectrogram(ax=input_spec_ax, path=input_path)


    # show VAD results
    probabilities.reset_index().plot(ax=vad_ax, x='time', y='speech')

    for start, end in zip(boundaries['start'], boundaries['end']):
        vad_ax.axvspan(start, end, alpha=0.3, color='green')

    vad_ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1.0))
    vad_ax.grid(True, which='minor', axis='x')
    vad_ax.grid(True, which='major', axis='x')

    # show modified audio
    plot_spectrogram(ax=output_spec_ax, path=output_path)


    fig.tight_layout()
    return fig


# XXX: model only supports 16k samplerate
# If input is another samplerate, have to resample it first
path = 'voiceandnot_16k.wav'
prob, segments = detect_voice(path)

segments['gain'] = 0.0

out_path = 'voice-supressed.wav'
apply_gain(path, segments, default=-20.0, out=out_path)

fig = plot_vad(path, prob, segments, out_path)
fig.savefig('vad-output.png')




