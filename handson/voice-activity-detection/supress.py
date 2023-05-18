
import librosa
import soundfile
from speechbrain.pretrained import VAD

def detect_voice(
    path,
    activation_threshold = 0.80,
    deactivation_threshold = 0.25,
    min_pause = 0.250,
    min_activation = None,
    save_dir = 'model_dir',
    segment_pre = 0.0,
    segment_post = 0.0,
    ):

    # FIXME: support resampling

    # do initial, coarse-detection
    vad = VAD.from_hparams(source="speechbrain/vad-crdnn-libriparty", savedir=save_dir)

    probabilities = vad.get_speech_prob_file(path)

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


    return probabilities, boundaries


def plot_vad(audio_path, probabilities, boundaries, sr=16000):

    # show spectrogram
    audio, sr = librosa.load(audio_path, sr=sr)
    S = librosa.feature.melspectrogram(y=audio, sr=sr)
    S_db = librosa.power_to_db(S, ref=numpy.max)

    librosa.display.specshow(spec_ax, S_db, sr=sr)

    # show VAD results


def apply_gain(path, segments, out=None, sr=None):

    audio, sr = librosa.load(audio_path, sr=sr, mono=False)
    print('app', audio.shape, sr)    

    for seg in segments:

        s = math.floor(sr * seg['start'])
        e = math.ceil(sr * seg['end'])
        gain = librosa.db_to_power(seg['gain'])

        audio[s:e, :] = gain * audio[s:e, :]

    if out is not None:
        soundfile.write(out, audio, samplerate=sr)


    return audio, sr

# FIXME: resample audio to temp-file, if not supported samplerate

supported_samplerate = 16000

path = 'voiceandnot.wav'
prob, segments = detect_voice(path)
print(prob)
print(segments)
plot_vad(path, prob, segments)

segments.loc[, 'gain'] = -40.0

# TODO: apply to audio. 


