
import io

import pandas
import numpy
import librosa


def read_data(f, date_format):
    df = pandas.read_csv(f, sep=',')

    # Use proper pandas datatypes
    df['Time'] = pandas.to_datetime(df['DateTimeStamp'], format=date_format)
    df['Duration'] = pandas.to_timedelta(df['Duration ms'], unit='ms')
    df = df.drop(columns=['DateTimeStamp', 'Duration ms'])

    # Compute start and end time of each segment
    # audio starts at time of first segment
    first = df['Time'].iloc[0]
    df['Start'] = df['Time'] - first
    df['End'] = df['Start'] + df['Duration']

    return df

def extract_segments(y, sr, segments):
    # compute segment regions in number of samples
    starts = numpy.floor(segments.Start.dt.total_seconds() * sr).astype(int)
    ends = numpy.ceil(segments.End.dt.total_seconds() * sr).astype(int)

    # slice the audio into segments
    for start, end in zip(starts, ends):
        audio_seg = y[start:end]
        print('extracting audio segment:', len(audio_seg), 'samples')

## Reproducible example
data = io.StringIO("""DateTimeStamp,Action,Duration ms
04/16/20 21:25:36:241,A,502
04/16/20 21:25:36:317,B,2253
04/16/20 21:25:36:734,X,118
04/16/20 21:25:36:837,C,10
04/16/20 21:25:37:537,D,797
04/16/20 21:25:37:606,X,70
04/16/20 21:25:37:874,A,1506
""")

segments = read_data(data, date_format="%m/%d/%y %H:%M:%S:%f")
print(segments)

path = librosa.util.example_audio_file()
y, sr = librosa.load(path, sr=16000, duration=10)
extract_segments(y, sr, segments)

