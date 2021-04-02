
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
