
import sys
import time

import tensorflow
import tensorflow_hub
import pandas
import numpy
import librosa
import structlog

log = structlog.get_logger()


def embed_audio_file(path, save_embedding=None, save_spectrogram=None):

    # load model
    model_load_start = time.time()
    yamnet_model = tensorflow_hub.load('https://tfhub.dev/google/yamnet/1')
    model_load_end = time.time()

    # load audio
    audio_load_start = time.time()
    audio, sr = librosa.load(path, sr=16000) # yamnet works with 16khz only
    audio_load_end = time.time()

    # generate embeddings
    embed_start = time.time()
    _scores, embedding_tensor, spectrogram = yamnet_model(tensorflow.convert_to_tensor(audio))
    del _scores # free memory
    embeddings = embedding_tensor.numpy()
    embed_end = time.time()

    # sanity checks
    hop_duration = 0.480
    frame_duration = 0.010
    effective_hop = (len(audio)/sr) / embeddings.shape[0]
    effective_frame = (len(audio)/sr) / spectrogram.shape[0]
    assert abs(effective_hop-hop_duration) < 0.01
    assert abs(effective_frame-frame_duration) < 0.01

    # save outputs
    save_start = time.time()
    emb = pandas.DataFrame(embeddings, columns=[f'e{i}' for i in range(embeddings.shape[1])])
    emb['time'] = numpy.arange(0, len(emb)) * hop_duration
    del embeddings # free memory

    spec = pandas.DataFrame(spectrogram, columns=[f's{i}' for i in range(spectrogram.shape[1]) ])
    spec['time'] = numpy.arange(0, len(spec)) * frame_duration
    del spectrogram # free memory

    if save_spectrogram is not None:
        spec.to_parquet(save_spectrogram)

    if save_embedding is not None:
        emb.to_parquet(save_embedding)
    save_end = time.time()

    # diagnostics
    model_load_duration = model_load_end-model_load_start
    audio_load_duration = audio_load_end-audio_load_start
    embed_duration = embed_end-embed_start
    save_duration = save_end-save_start

    log.info('embed-audio-file',
        path=path,
        audio_length=len(audio)/sr,
        model_load=round(model_load_duration, 3),
        audio_load=round(audio_load_duration, 3),
        save=round(save_duration, 3),
        embedding=round(embed_duration, 3),
    )

    return emb, spec

def main():

    path = sys.argv[1]
    _, _ = embed_audio_file(path, save_embedding='embedding.parquet', save_spectrogram='spec.parquet')



if __name__ == '__main__':
    main()
