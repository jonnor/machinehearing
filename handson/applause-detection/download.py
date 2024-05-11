
import os
import subprocess

import dataset

def download_audio(identifier,
        out_dir,
        template="%(id)s.%(ext)s",
        format='opus',
        quality=5):

    args = [
        'yt-dlp',
        '--extract-audio',
        '--audio-format', format,
        '--audio-quality', str(quality),
        '-o', os.path.join(out_dir, template),
        identifier,
    ]
    cmd = ' '.join(args)
    print(cmd)
    subprocess.check_output(args)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():

    files = dataset.load_files()

    print(files.head(5))
    #download_audio

    out_dir = 'data/audio'
    ensure_dir(out_dir)

    for idx, file in files.iterrows():
        download_audio(file['identifier'], out_dir=out_dir)



if __name__ == '__main__':
    main()
