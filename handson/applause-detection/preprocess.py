
import os

import pandas
import structlog

# Using https://github.com/jonnor/dominant-sound repo

from src.utils.fileutils import ensure_dir_for_file, ensure_dir
from src.data.annotations import load_dataset_annotations
from src.features.soundlevel import soundlevel_for_file
from src.features.spectrogram import spectrogram_for_file
from src.utils.dataframe import flatten_dataframes
from parallel import ProgressParallel, joblib

log = structlog.get_logger()


def compute_store_embeddings(generator, embedding_path, ids):
    
    assert os.path.exists(embedding_path), embedding_path

    for _, chunk in enumerate(generator):
        scores, embedding = chunk
    
        # add indexing info
        for k, v in ids.items():
            embedding[k] = v

        embedding = embedding.reset_index().set_index(['dataset', 'clip', 'time'])
        embedding_chunk_path = os.path.join(embedding_path, f'chunk={i}.part')        

        embedding.to_parquet(embedding_chunk_path)


def compute_soundlevel(audio_path, out_dir, ids, config={}):

    df, meta = soundlevel_for_file(audio_path, **config)
    # XXX: we assume mono here
    #assert len(df.columns) == 1, df.columns
    df = df[[0]].rename(columns={0: 'level'})

    log.info('compute-soundlevel', path=audio_path, results=len(df))

    # add indexing info
    for k, v in ids.items():
        df[k] = v

    print
    df.to_parquet(os.path.join(out_dir, 'data.part'))

def compute_spectrogram(audio_path, out_dir, ids, config={}):

    df, _ = spectrogram_for_file(audio_path, **config)
    df.columns = [ str(c) for c in df.columns ]

    log.info('compute-spectrogram', path=audio_path, results=len(df))

    # add indexing info
    for k, v in ids.items():
        df[k] = v

    df.to_parquet(os.path.join(out_dir, 'data.part'))


def yamnet_embed(audio_path, out_dir, ids, config={}):
    from src.features import yamnet_embeddings

    generator = yamnet_embeddings.process_audio_file(audio_path)

    compute_store_embeddings(audio_path, embedding_path=out_path)

def panns_embed(audio_path, out_dir, ids, config={}):
    from src.features import panns_embed

    generator = panns_embed.process_audio_file(audio_path)
    # TODO: use same mechanism as for YAMNet
    raise NotImplementedError("PANNs storing not supported")
    compute_store_embeddings(audio_path, embedding_path=out_path)


PROCESSORS = {
    'soundlevel': compute_soundlevel,
    'spectrogram': compute_spectrogram,
    'yamnet': yamnet_embed,
    'pann': panns_embed,
}

def merge_dicts(x, y):
    return {**x, **y}

def process_clips(configurations, clips, out_dir, verbose=1, parallel_jobs=4):

    # TODO: check whether any files are missing
    
    log.info('process-clips-start')

    for config_name, config in configurations.items():
        log.info('process-clips-config-start', config=config_name)

        # prepare output
        config_out_dir = os.path.join(out_dir, f'{config_name}.parquet')
        ensure_dir(config_out_dir)

        # set up configuration
        n_jobs = config.pop('jobs', parallel_jobs)
        processor = config.pop('processor')

        process_func = PROCESSORS[processor]
        common_ids = { 'dataset': 'default', 'config': config_name }

        # process files in a parallel manner, with progress indicator
        def make_job(clip_id, clip_path):
            job = joblib.delayed(process_func)(clip_path,
                config_out_dir,
                ids=merge_dicts(common_ids, dict(clip=clip_id)),
                config=config
            )
            return job
        jobs = [ make_job(clip_id, path) for clip_id, path in clips.items() ]

        executor = ProgressParallel(n_jobs=n_jobs, verbose=verbose, total=len(jobs))
        results = executor(jobs)

    log.info('process-clips-end')


def main():

    import dataset
    files = dataset.load_files()

    audio_dir = 'data/audio/'
    audio_ext = '.opus'
    files['audio_path'] = audio_dir + files.identifier + audio_ext
    clips = files.rename(columns={'identifier': 'clip'}).set_index('clip')
    print(clips)

    parallel_jobs = 4

    configurations = {
        'LAF': dict(processor='soundlevel', time='fast'),
        #'LAS': dict(mono=True, time='slow'),

        #'yamnet-1': dict(processor='yamnet', jobs=1),
        #'panns-1': dict(processor='panns'),

        'logmels-64bands-256hop-sr16000': dict(processor='spectrogram',
            hop_length=256, n_mels=64, sr=16000),
        #'logmels-32bands-1024hop': dict(hop_length=1024, n_mels=32),
    }


    out_dir = 'data/preprocessed/'

    process_clips(configurations, clips['audio_path'], out_dir,
         parallel_jobs=parallel_jobs)



if __name__ == '__main__':
    main()
