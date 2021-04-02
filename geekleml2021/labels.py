
"""
Read and write Audacity compatible label files

These files have 3 columns of data:
- start (in seconds)
- end (in seconds)
- annotation (string)

In the files, values are tab separated.
There is no header.

Copyright 2019 Jon Nordby <jononor@gmail.com>
License: MIT
"""

import pandas

import os.path
from io import StringIO


def write(df, path_or_buf=None):
    """Write a label file that is compatible with Audacity"""

    # pick out relevant columns
    sub = pandas.DataFrame({
        'start': df['start'].astype(float),
        'end': df['end'].astype(float),
        'annotation': df['annotation'].astype(str),
    })
    
    sub = sub.sort_values('start', ascending=True)
    dtypes = dict(start=float, end=float, annotation=str)
    
    ret = sub.to_csv(path_or_buf,
                    sep='\t', index=False, header=None)

    return ret

def read(path):

    file = None
    with open(path, 'r') as f:
        contents = f.read()
        lines = contents.split('\n')
        lines = [ line for line in lines if not line.startswith('\\\t') ]
        contents = '\n'.join(lines)
        file = StringIO(contents)

    labels = pandas.read_csv(file, sep='\t', header=None,
                            names=['start', 'end', 'annotation'],
                            dtype=dict(start=float,end=float,annotation=str))

    labels = labels.sort_values('start', ascending=True)

    return labels    



def test_write_labels_simple():
    
    import numpy

    # point in time. start==end
    marker_starts = numpy.linspace(1.0, 2.0, 5)
    markers = pandas.DataFrame({
        'start': marker_starts,
        'end': marker_starts,
        'annotation': ['mark'] * len(marker_starts)
    })
    
    # region with start and end
    region_starts = numpy.linspace(3.0, 4.0, 5)    
    regions = pandas.DataFrame({
        'start': region_starts,
        'end': region_starts + 0.01,
        'annotation': ['region'] * len(region_starts)
    })
    
    df = pandas.concat([regions, markers])
    df.sort_values('start', ascending=True, inplace=True)

    here = os.path.dirname(__file__)
    test_data_dir = os.path.join(here, '../tests/out')
    if not os.path.exists(test_data_dir):
        os.makedirs(test_data_dir)
    out_file = os.path.join(test_data_dir, 'test.labels.txt')
    if os.path.exists(out_file):
        os.remove(out_file)
    write(df, out_file)
    assert os.path.exists(out_file)

    read_df = read(out_file)

    numpy.testing.assert_allclose(df.start, read_df.start)
    numpy.testing.assert_allclose(df.end, read_df.end)
    assert list(df.annotation) == list(read_df.annotation)


test_write_labels_simple()
    



