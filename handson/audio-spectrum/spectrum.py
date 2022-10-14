
import librosa # for loading example audio
from matplotlib import pyplot as plt
import scipy.signal
import pandas
import numpy

def spectrum_stft(audio, sr, n_fft, window):
    """Method 1: Compute magnitude spectrogram, average over time"""
    S = librosa.stft(audio, n_fft=n_fft, window=window)
    S_db = librosa.amplitude_to_db(numpy.abs(S*S), ref=0.0, top_db=120)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    spectrum = numpy.mean(S_db, axis=1)
    return pandas.Series(spectrum, index=freqs)

def spectrum_welch(audio, sr, n_fft, window):
    """Method 2: Use Welch method. Uses overlapped complex spectrum"""
    freqs, power = scipy.signal.welch(audio, fs=sr, nfft=n_fft, window=window,
        scaling="spectrum", average='median')
    db = librosa.power_to_db(power, ref=0.0, top_db=120)
    return pandas.Series(db, index=freqs)


fft_length = 512*16
window = "hann"


# load some short example audio
path = librosa.example("trumpet")
audio, sr = librosa.load(path)
section = audio[int(1.0*sr):int(2.0*sr)]

# compute the spectrums
w = spectrum_welch(section, sr=sr, n_fft=fft_length, window=window)
s = spectrum_stft(section, sr=sr, n_fft=fft_length, window=window) - 65.0

# plot it
fig, ax = plt.subplots(1)
w.plot(ax=ax, label="welch")
s.plot(ax=ax, label="STFT")
ax.legend()
fig.tight_layout()
fig.savefig("spectrum.png")

