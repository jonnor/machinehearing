
import pandas

def load():

    path = 'youtube_data.csv'
    df = pandas.read_csv(path)

    return df
