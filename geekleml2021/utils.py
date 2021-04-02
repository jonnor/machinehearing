
import pandas
import numpy

def mark_onoff(series, on_threshold, off_threshold, initial=0, on_state=1, off_state=0):
    #print(series)
    state = initial
    times = []
    events = []
    
    values = []
    value_times = []
    
    for idx, data in zip(series.index, series):
        if state == off_state and data > on_threshold:
            state = on_state
            times.append(idx)
            events.append(state)          
        elif state == on_state and data < off_threshold:
            state = off_state
            times.append(idx)
            events.append(state)
        else:
            pass
        
        value_times.append(idx)
        values.append(0 if state == off_state else 1)
        
    sparse = pandas.Series(events, index=times)
    dense = pandas.Series(values, index=value_times)
    return sparse, dense
    
def matplotlib_time(pandas_time):
    import matplotlib.dates as mdates
    val = mdates.date2num(pandas_time)
    return val


def join_events(series):
    starts = series[series == 1]
    ends = series[series == 0]
    
    df = pandas.DataFrame({
        'start': starts.index,
        'end': ends.index,
    })
    return df

def merge_consecutive(df, col='class'):
    
    # Group where consequtive values are the same
    groups = df.groupby((df[col].shift() != df[col]).cumsum())
    
    dist = df.reset_index().diff()['index'].iloc[-1]
    
    outs = []
    for idx, g in groups:
        #print('fff')
        start, end = g.index[0], (g.index[-1] + dist)
        val = g[col].iloc[0]
        
        outs.append({
            'start': start,
            'end': end,
            col: val,
        })
        
        #print(idx, val, g.index[0], g.index[-1])

    df = pandas.DataFrame.from_records(outs)
    return df


def map_linear(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    if leftSpan == 0.0:
        valueScaled = 0.0
    else:
        valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def constrain(value, lower, upper):

    if value > upper:
        value = upper
    if value < lower:
        value = lower

    return value
    


