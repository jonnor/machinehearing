
import utils

import scipy.stats
import pandas
import numpy


def synthesize_fermentation_rate(max_rate=100, duration_minutes=120*60):
    # Inspired by plots found on Google images
    
    
    # XXX: smoothness is very dependent on size / bins relation
    # fitting and sampling from a KDE might allow better control over this 
    data_gamma = scipy.stats.gamma.rvs(a=4, size=100000*2)

    bins = 200
    a = scipy.stats.relfreq(data_gamma, numbins=bins)
    f = pandas.Series(a.frequency, name='frequency')
    
    # scale to fit max rate
    f *= (max_rate / f.max())
    df = f.to_frame()

    # scale to fit time
    t = (numpy.arange(0, len(df)) / bins) * duration_minutes
    df['time'] = pandas.to_timedelta(t, unit='min')
    df = df.set_index('time')
    
    return df

def generate_events(distances, variation=0.05):
    times = []
    
    starts = distances.index
    ends = distances.shift().index
    start_dists = distances
    end_dists = distances.shift()
        
    current = 0.0
    for start, end, s_dist, e_dist in zip(starts, ends, start_dists, end_dists):
        #print(start, end, dist)
        
        while (current < end.total_seconds()):
            # use linear interpolation to compute dist
            dist = utils.map_linear(current,
                                    start.total_seconds(), end.total_seconds(),
                                    s_dist, e_dist)
            
            #print(current, start.total_seconds(), end.total_seconds(), s_dist, e_dist)
            
            d = dist + numpy.random.normal(0.0, variation)
            #print(current, d)
            current += d
            
            t = pandas.to_timedelta(current, unit='s')
            times.append(t)
    
    df = pandas.Series(times, name='time').to_frame()
    return df
