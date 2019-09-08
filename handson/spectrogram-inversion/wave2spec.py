
import librosa
import numpy
import skimage

def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

def spectrogram_image(y, sr, out, hop_length, n_mels):
    # use log-melspectrogram
    mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                            n_fft=hop_length*2, hop_length=hop_length)
    mels = numpy.log(mels + 1e-9) # add small number to avoid log(0)

    # min-max scale to fit inside 8-bit range
    img = scale_minmax(mels, 0, 255).astype(numpy.uint8)
    img = numpy.flip(img, axis=0) # put low frequencies at the bottom in image
    img = 255-img # invert. make black==more energy

    # save as PNG
    skimage.io.imsave(out, img)


def parse():
    import argparse
    parser = argparse.ArgumentParser(description='Convert an audio waveform to a spectrogram image')

    a = parser.add_argument

    # positional
    a("input", help="Input audio file. Must be loadable by librosa. Ex: wav|mp3|m4a etc")
    a("out", help="Output image. Should be .png")

    # options
    a('--mels', type=int, default=128,
        help='Number of Mel bands')
    a('--hop', type=int, default=512,
        help='Samples per spectrogram time-step')
    a('--window', type=int, default=1280,
        help='Number of time-steps in analysis window')
    a('--samplerate', type=int, default=22050,
        help='Samplerate used for processing')

    parsed = parser.parse_args()
    return parsed


if __name__ == '__main__':
    args = parse()

    # settings
    hop_length = args.hop
    time_steps = args.window

    # load audio. Using example from librosa
    path = librosa.util.example_audio_file()
    y, sr = librosa.load(args.input, sr=args.samplerate)

    # extract a fixed length window
    start_sample = 0 # starting at beginning
    length_samples = time_steps*hop_length
    window = y[start_sample:start_sample+length_samples]
    
    # convert to PNG
    spectrogram_image(window, sr=sr, out=args.out, hop_length=hop_length, n_mels=args.mels)
    print('wrote file', args.out)

