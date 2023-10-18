
import pandas
import numpy

def make_continious_labels(events, length, time_resolution):
    """
    Create a continious vector for the event labels that matches the time format of our spectrogram
    
    Assumes that no annotated event means nothing occurred.
    """

    freq = pandas.Timedelta(seconds=time_resolution)
    
    # Create empty covering entire spectrogram
    duration = length * time_resolution
    ix = pandas.timedelta_range(start=pandas.Timedelta(seconds=0.0),
                    end=pandas.Timedelta(seconds=duration),
                    freq=freq,
                    closed='left',
    )
    ix.name = 'time'
    df = pandas.DataFrame({}, index=ix)
    assert len(df) == length, (len(df), length)
    df["event"] = 0
    
    # fill in event data
    for start, end in zip(events['start'], events['end']):
        s = pandas.Timedelta(start, unit='s')
        e = pandas.Timedelta(end, unit='s')

        # XXX: focus just on onsets
        e = s + pandas.Timedelta(0.100, unit='s') 
        
        match = df.loc[s:e]
        df.loc[s:e, "event"] = 1
    
    return df

# extract overlapped time-windows for spectrograms and labels
def compute_windows(arr, frames, pad_value=0.0, overlap=0.5, step=None):
    if step is None:
        step = int(frames * (1-overlap))
        
    windows = []
    index = []
        
    width, length = arr.shape
    
    for start_idx in range(0, length, step):
        end_idx = min(start_idx + frames, length)

        # create emmpty
        win = numpy.full((width, frames), pad_value, dtype=float)
        # fill with data
        win[:, 0:end_idx-start_idx] = arr[:,start_idx:end_idx]

        windows.append(win)
        index.append(start_idx)

    s = pandas.Series(windows, index=index)
    s.index.name = 'start_index'
    return s

def dataset_split_sequentially(data, val_size=0.25, test_size=0.25, random_state=3, column='split'):
    """
    Split DataFrame into 3 non-overlapping parts: train,val,test
    with specified proportions
    
    Returns a new DataFrame with the rows marked by the assigned split in @column
    """
    train_size = (1.0 - val_size - test_size)

    train_stop = int(len(data) * train_size)
    val_stop = train_stop + int(len(data)*val_size)
    
    train_idx = data.index[0:train_stop]
    val_idx = data.index[train_stop:val_stop]
    test_idx = data.index[val_stop:-1]
    
    data = data.copy()
    data.loc[train_idx, column] = 'train'
    data.loc[val_idx, column] = 'val'
    data.loc[test_idx, column] = 'test'
    
    return data

def build_sednet(input_shape, filters=128, cnn_pooling=(5, 2, 2), rnn_units=(32, 32), dense_units=(32,), n_classes=1, dropout=0.5):
    """
    SEDnet type model

    Based https://github.com/sharathadavanne/sed-crnn/blob/master/sed.py
    """
    
    from tensorflow.keras import Model
    from tensorflow.keras.layers import Input, Bidirectional, Conv2D, BatchNormalization, Activation, \
            Dense, MaxPooling2D, Dropout, Permute, Reshape, GRU, TimeDistributed
    
    spec_start = Input(shape=(input_shape[-3], input_shape[-2], input_shape[-1]))
    spec_x = spec_start
    for i, pool in enumerate(cnn_pooling):
        spec_x = Conv2D(filters=filters, kernel_size=(3, 3), padding='same')(spec_x)
        spec_x = BatchNormalization(axis=1)(spec_x)
        spec_x = Activation('relu')(spec_x)
        spec_x = MaxPooling2D(pool_size=(1, pool))(spec_x)
        spec_x = Dropout(dropout)(spec_x)
    spec_x = Permute((2, 1, 3))(spec_x)
    spec_x = Reshape((input_shape[-3], -1))(spec_x)

    for units in rnn_units:
        spec_x = Bidirectional(
            GRU(units, activation='tanh', dropout=dropout, recurrent_dropout=dropout, return_sequences=True),
            merge_mode='mul')(spec_x)

    for units in dense_units:
        spec_x = TimeDistributed(Dense(units))(spec_x)
        spec_x = Dropout(dropout)(spec_x)

    spec_x = TimeDistributed(Dense(n_classes))(spec_x)
    out = Activation('sigmoid', name='strong_out')(spec_x)
    
    model = Model(inputs=spec_start, outputs=out)
    
    return model


def build_sedgru(input_shape, filters=128, reduction_units=(16,), rnn_units=(32, 32), dense_units=(32,), n_classes=1, dropout=0.5):
    """
    """
    
    from tensorflow.keras import Model
    from tensorflow.keras.layers import Input, Bidirectional, Conv2D, BatchNormalization, Activation, \
            Dense, MaxPooling2D, Dropout, Permute, Reshape, GRU, TimeDistributed
    
    spec_start = Input(shape=(input_shape[-2], input_shape[-1]))
    spec_x = spec_start

    # Dimensionality reduction with dense layers
    for units in reduction_units:
        spec_x = TimeDistributed(Dense(units, activation='relu'))(spec_x)
    
    for units in rnn_units:
        spec_x = Bidirectional(
            GRU(units, activation='tanh', dropout=dropout, recurrent_dropout=dropout, return_sequences=True),
            merge_mode='mul')(spec_x)

    for units in dense_units:
        spec_x = TimeDistributed(Dense(units))(spec_x)
        spec_x = Dropout(dropout)(spec_x)

    spec_x = TimeDistributed(Dense(n_classes))(spec_x)
    out = Activation('sigmoid', name='strong_out')(spec_x)
    
    model = Model(inputs=spec_start, outputs=out)
    
    return model

def weighted_binary_crossentropy(zero_weight, one_weight):
    """
    Loss with support for specifying class weights
    """
    import tensorflow.keras.backend as K
    
    def weighted_binary_crossentropy(y_true, y_pred):

        # standard cross entropy
        b_ce = K.binary_crossentropy(y_true, y_pred)

        # apply weighting
        weight_vector = y_true * one_weight + (1 - y_true) * zero_weight
        weighted_b_ce = weight_vector * b_ce

        return K.mean(weighted_b_ce)

    return weighted_binary_crossentropy

def merge_overlapped_predictions(window_predictions, window_hop, time_resolution):
    
    # flatten the predictions from overlapped windows
    predictions = []
    for win_no, win_pred in enumerate(window_predictions):
        win_start = window_hop * win_no
        for frame_no, p in enumerate(win_pred):
            s = {
                'frame': win_start + frame_no,
                'probability': p,
            }
        
            predictions.append(s)
        
    df = pandas.DataFrame.from_records(predictions)
    df['time'] = pandas.to_timedelta(df['frame'] * time_resolution, unit='s')
    df = df.drop(columns=['frame'])
    
    # merge predictions from multiple windows 
    out = df.groupby('time').median()
    return out


def compute_class_weights(y_train):
    from sklearn.utils import class_weight
    y_train = numpy.squeeze(y_train).astype(int)
    y_train = numpy.any(y_train, axis=1)
    w = class_weight.compute_class_weight('balanced', classes=numpy.unique(y_train), y=y_train)
    #w_dict = dict(zip(numpy.unique(y_train), w))
    return w


def events_from_predictions(pred, threshold=0.5, label='yes', event_duration_max=1.0):
    """
    Discretize predictions into events
    """
    import copy
    
    event_duration_max = pandas.Timedelta(event_duration_max, unit='s')
    
    events = []
    inside_event = False
    event = {
        'start': None,
        'end': None,
    }
    
    for t, r in pred.iterrows():
        p = r['probability']

        # basic state machine for producing events
        if not inside_event and p > threshold:
            event['start'] = t
            inside_event = True
            
        elif inside_event and ((p < threshold) or ((t - event['start']) > event_duration_max)):
            event['end'] = t
            events.append(copy.copy(event))
            
            inside_event = False
            event['start'] = None
            event['end'] = None
        else:
            pass
    
    if len(events):
        df = pandas.DataFrame.from_records(events)
    else:
        df = pandas.DataFrame([], columns=['start', 'end'], dtype='timedelta64[ns]')
    df['label'] = label
    return df


def to_sed_eval_events(e, label='label', end='end', start='start'):
    """
    Convert event lists to format expected by sed_eval
    """
    import dcase_util
    
    sed = e.copy()
    sed = e.rename(columns={
        label: 'event_label',
        end: 'event_offset',
        start: 'event_onset',
        #'file': 'source',
    })
    #print(sed)
    c = dcase_util.containers.MetaDataContainer(sed.to_dict(orient='records'))
    return c
    
def evaluate_events(ref, pred, threshold=0.5, tolerance=0.100):
    
    import sed_eval

    # Convert to sed_eval formats
    ref = to_sed_eval_events(ref, label='event')

    estimated = events_from_predictions(pred, threshold=threshold)
    estimated['start'] = estimated['start'].dt.total_seconds()
    estimated['end'] = estimated['end'].dt.total_seconds()
    est = to_sed_eval_events(estimated)

    # Compute metrics 
    metrics = sed_eval.sound_event.EventBasedMetrics(
        evaluate_onset=True,
        evaluate_offset=False, # only onsets
        event_label_list=ref.unique_event_labels,
        t_collar=tolerance,
        percentage_of_length=1.0,
    )
    metrics.evaluate(
        reference_event_list=ref,
        estimated_event_list=est,
    )
    
    # Extract metrics as flat series
    m = metrics.results_overall_metrics()
    s = pandas.Series({
      'f_measure': m['f_measure']['f_measure'],
      'precision': m['f_measure']['precision'],
      'recall': m['f_measure']['recall'],
      'error_rate': m['error_rate']['error_rate'],
      'substitution_rate': m['error_rate']['substitution_rate'],
      'deletion_rate': m['error_rate']['deletion_rate'],
      'insertion_rate': m['error_rate']['insertion_rate'],
    })
    
    return s


def compute_pr_curve(annotations, pred, thresholds=50, tolerance=0.1):

    df = pandas.DataFrame({
        'threshold': numpy.linspace(0.0, 1.0, thresholds),
    })

    metrics = df.threshold.apply(lambda t: evaluate_events(annotations, pred, threshold=t, tolerance=tolerance))
    df = pandas.merge(df, metrics, right_index=True, left_index=True)
    
    return df