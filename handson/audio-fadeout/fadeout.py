import librosa
import numpy
import soundfile


def apply_fadeout(audio, sr, duration=3.0):
    # convert to audio indices (samples)
    length = int(duration*sr)
    end = audio.shape[0]
    start = end - length

    # compute fade out curve
    # linear fade
    fade_curve = numpy.linspace(1.0, 0.0, length)

    # apply the curve
    audio[start:end] = audio[start:end] * fade_curve


path = librosa.ex('brahms')
orig, sr = librosa.load(path, duration=5.0)
out = orig.copy()
apply_fadeout(out, sr, duration=2.0)

soundfile.write('original.wav', orig, samplerate=sr)
soundfile.write('faded.wav', out, samplerate=sr)
