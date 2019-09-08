
import numpy
import librosa
import soundfile

# parameters
sr = 22050
n_mels = 128
hop_length = 512
n_iter = 32
n_mfcc = None # can try n_mfcc=20

# load audio and create Mel-spectrogram
path = '436951__arnaud-coutancier__old-ladies-pets-and-train-02.flac'
y, _ = librosa.load(path, sr=sr)
S = numpy.abs(librosa.stft(y, hop_length=hop_length, n_fft=hop_length*2))
mel_spec = librosa.feature.melspectrogram(S=S, sr=sr, n_mels=n_mels, hop_length=hop_length)

# optional, compute MFCCs in addition
if n_mfcc is not None:
    mfcc = librosa.feature.mfcc(S=librosa.power_to_db(S), sr=sr, n_mfcc=n_mfcc)
    mel_spec = librosa.feature.inverse.mfcc_to_mel(mfcc, n_mels=n_mels)

# Invert mel-spectrogram
S_inv = librosa.feature.inverse.mel_to_stft(mel_spec, sr=sr, n_fft=hop_length*4)
y_inv = librosa.griffinlim(S_inv, n_iter=n_iter,
                            hop_length=hop_length)

soundfile.write('orig.wav', y, samplerate=sr)
soundfile.write('inv.wav', y_inv, samplerate=sr)

