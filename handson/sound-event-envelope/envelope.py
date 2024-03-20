
import librosa
import pandas
import numpy

from matplotlib import pyplot as plt

def amplitude_envelope(signal, frame_size, hop_length, sr) -> pandas.Series:
    """Calculate the amplitude envelope of a signal

    Returns the envelope values and timestamps
    """
    amplitude_envelope = []
    
    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length): 
        amplitude_envelope_current_frame = max(signal[i:i+frame_size]) 
        amplitude_envelope.append(amplitude_envelope_current_frame)
    
    values = numpy.array(amplitude_envelope)
    times = librosa.frames_to_time(numpy.arange(1, len(values)+1), hop_length=hop_length, sr=sr)
    series = pandas.Series(values, index=times, name='envelope')
    return  series

# load audio file
path = librosa.example('sweetwaltz')
audio, sr = librosa.load(path, duration=5.0)

# compute envelope
envelope = amplitude_envelope(audio, frame_size=1024, hop_length=512, sr=sr)

# extract only a certain time
event_envelope = envelope.loc[0.37:0.600]

ax = plt.subplot(3, 1, 1)
librosa.display.waveshow(audio, alpha=0.5)
plt.plot(event_envelope.index, event_envelope.values, color="r")
plt.savefig('event-env.png', bbox_inches='tight')


