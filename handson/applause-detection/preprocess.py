
import os

import pandas
import structlog

# Using https://github.com/jonnor/dominant-sound repo

from src.utils.fileutils import ensure_dir_for_file, ensure_dir
from src.data.annotations import load_dataset_annotations
from src.features.soundlevel import soundlevel_for_file
from src.features.spectrogram import spectrogram_for_file
from src.utils.dataframe import flatten_dataframes

log = structlog.get_logger()

def compute_soundlevels(files, **kwargs):

    def get_soundlevels(audio_path) -> pandas.DataFrame:
        df, meta = soundlevel_for_file(audio_path, **kwargs)
        # we assume mono here
        assert len(df.columns) == 1, df.columns
        df = df.rename(columns={0: 'level'})
        return df, meta

    out = []
    for path in files:
        assert os.path.exists(path), path
        ss = get_soundlevels(path)
        log.info('compute-soundlevel', path=path, results=len(ss[0]))
        out.append(ss)

    df = pandas.DataFrame(out, index=files.index, columns=['soundlevels', 'meta'])
    out = flatten_dataframes(df.soundlevels)

    return out


def preprocess_soundlevels(files, soundlevels_dir, configurations, dataset='default'):
    """
    Compute and store soundlevels for the datasets
    """

    for name, config in configurations.items():
        out_path = os.path.join(soundlevels_dir, f'{name}.parquet')
        ensure_dir_for_file(out_path)
        df = compute_soundlevels(files, **config)
        df['config'] = name
        df['dataset'] = dataset
        df = df.reset_index().set_index(['config', 'dataset', 'clip', 'time'])
        df.to_parquet(out_path)
        log.info('preprocess-soundlevels-store', out=out_path, results=len(df), config=name)


def compute_spectrograms(files, **kwargs):

    out = []
    for idx, row in files.iterrows():

        ss, _ = spectrogram_for_file(audio_path, **kwargs)
        ss.columns = [ str(c) for c in ss.columns ]

        log.info('compute-spectrogram', path=audio_path, results=len(ss))
        out.append(ss)

    #df = pandas.concat(out)
    ss = pandas.Series(out, index=files.index, name='spectrograms')
    out = flatten_dataframes(ss)
    return out

def preprocess_spectrograms(files, configurations):
    """
    Compute and store spectrograms for the datasets
    """

    for name, config in configurations.items():
        df = compute_spectrograms(audio_root, files, **config)

        df['config'] = name
        df = df.reset_index().set_index(['config', 'dataset', 'clip', 'time'])
        out_path = os.path.join(soundlevels_dir, f'{name}.parquet')
        ensure_dir_for_file(out_path)
        df.to_parquet(out_path)
        log.info('preprocess-spectrogram-store', out=out_path, results=len(df), config=name)


def compute_store_embeddings(generator, embedding_path, clip, dataset='default'):
    
    for _, chunk in enumerate(generator):
        scores, embedding = chunk
        # TODO: support storing scores
        #scores['dataset'] = dataset
        #scores['clip'] = clip
        #scores = scores.reset_index().set_index(['dataset', 'clip', 'time'])
    
        embedding['dataset'] = dataset
        embedding['clip'] = clip
        embedding = embedding.reset_index().set_index(['dataset', 'clip', 'time'])
        embedding_chunk_path = os.path.join(embedding_path, f'dataset={dataset}-clip={clip}-chunk={i}.part')        

        ensure_dir(embedding_path)        
        embedding.to_parquet(embedding_chunk_path)


def preprocess_embeddings(files, out, input_column='path', configurations=None):
    """
    Compute and store embeddings for the datasets
    """

    for name, config in configurations.items():
        out = os.path.join(out_dir, f'{name}.parquet')
        ensure_dir_for_file(out_path)

        for idx, path in files:
            audio_path = path

            # TODO: support other models
            if config['model'] == 'yamnet':
                from src.features import yamnet_embeddings
                generator = yamnet_embeddings.process_audio_file(audio_path)

                compute_store_yamnet(audio_path, row['dataset'], row['clip'], embedding_path=out_path)

            elif config['model'] == 'panns':

                from src.features import panns_embed
                generator = panns_embed.process_audio_file(audio_path)
                # TODO: use same mechanism as for YAMNet
                raise NotImplementedError("PANNs storing not supported")
            else:
                raise ValueError("Unsupported model")

        log.info('preprocess-spectrogram-store', out=out_path, config=name)


def main():

    import dataset
    files = dataset.load_files()

    audio_dir = 'data/audio/'
    audio_ext = '.opus'
    files['audio_path'] = audio_dir + files.identifier + audio_ext
    clips = files.rename(columns={'identifier': 'clip'}).set_index('clip')

    clips = clips.iloc[1:2]

    print(clips)

    soundlevel_configurations = {
        'LAF': dict(mono=True, time='fast'),
        #'LAS': dict(mono=True, time='slow'),
    }

    embedding_configurations = {
        'yamnet-1': dict(model='yamnet'),
        #'panns-1': dict(model='panns'),
    }
    spectrogram_configurations = {
        'logmels-64bands-256hop-sr16000': dict(hop_length=256, n_mels=64, sr=16000),
        #'logmels-32bands-1024hop': dict(hop_length=1024, n_mels=32),
    }

    out_dir = 'data/preprocessed/'

    preprocess_soundlevels(clips.audio_path, os.path.join(out_dir, 'soundlevels'), soundlevel_configurations)
    preprocess_spectrograms()
    preprocess_embeddings()


if __name__ == '__main__':
    main()
