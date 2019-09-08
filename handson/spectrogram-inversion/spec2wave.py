
import sys

import numpy
import skimage
import librosa
import soundfile

# inverse is only in very new librosa
try:
    from librosa.feature import inverse
except ImportError as e:
    print('Unable to import librosa.feature.inverse - Is librosa version 0.7.0 or higher?')
    print(e)
    sys.exit(2)


def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

def log_melspectrogram_to_audio(mels, sr, hop_length, n_iter):
    n_fft = hop_length * 4

    # Use floating point
    mels = mels.astype(float) / numpy.max(mels)

    # inverse of log
    # FIXME: totaly fails to converge, leading to a lot of white noise
    mels = numpy.exp(mels + 1e-6) - 1.0
    print(numpy.min(mels), numpy.max(mels), numpy.mean(mels))

    # invert to get waveform
    y = inverse.mel_to_audio(mels, sr=sr, hop_length=hop_length, n_fft=n_fft, n_iter=n_iter)

    # Normalize audio amplitude?
    print(numpy.min(y), numpy.max(y), numpy.mean(y))

    norm_factor = 0.5 / max(numpy.min(y), numpy.max(y)) 
    print('norm', norm_factor)
    y = y * norm_factor

    return y

def parse():
    import argparse
    parser = argparse.ArgumentParser(description='Convert an audio waveform to a spectrogram image')

    a = parser.add_argument

    # positional
    a("input", help="Input spectrogram image. Typically a .png file.")
    a("out", help="Output audio file. Should be .wav")

    # options
    a('--hop', type=int, default=512,
        help='Samples per spectrogram time-step')
    a('--iterations', type=int, default=32,
        help='Number of iterations for Griffin-Lim algorithm')
    a('--samplerate', type=int, default=22050,
        help='Samplerate used for processing')

    parsed = parser.parse_args()
    return parsed


if __name__ == '__main__':
    args = parse()

    # load spectrogram from image
    img = skimage.io.imread(args.input)

    assert len(img.shape) == 2, 'Spectrogram image must be grayscale, not RGB'

    audio = log_melspectrogram_to_audio(img, sr=args.samplerate,
                                hop_length=args.hop, n_iter=args.iterations)

    # save as audio
    soundfile.write(args.out, audio, samplerate=args.samplerate)

    print('wrote file', args.out)

