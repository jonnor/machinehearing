
import librosa
import numpy
import matplotlib.pyplot as plt

# Normalized and not
def plot_melfilters(sr=16000, n_fft=512, n_mels=10, fmin=0, fmax=None):
    
    mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels, fmin=fmin, fmax=fmax, norm=None)
    mel_norm = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels, fmin=fmin, fmax=fmax, norm=1)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    
    fig, (base_ax, norm_ax) = plt.subplots(2, figsize=(16,8))

    base_ax.plot(freqs, mel.T)
    base_ax.set_title('Mel filters')
    
    norm_ax.plot(freqs, mel_norm.T)
    norm_ax.set_title('Mel filters normalized (area=1)')
    
    base_ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)    
    norm_ax.set_xlabel('Frequency (Hz)')    
    
    return fig

if __name__ == '__main__':

    path = 'img/melfilters.png'
    f = plot_melfilters()
    f.savefig(path, bbox_inches='tight', pad_inches=0)
    print('wrote {}'.format(path))
