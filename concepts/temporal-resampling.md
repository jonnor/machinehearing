
# Temporal resampling in Machine Learning

Focused mostly on audio.
But these considerations are of critical importance to any other application of Machine Learning
on time-series.

With time-series
regular sampling


## Typical duration of various acoustical phenomena


Phoneme. 75 - 200 ms.
Impulse noise in a room. Reverberation time
Impulsive noise outdoors. Echo
Word 100 ms - 1000 ms
Sentence 2 - 10 seconds 10-25 words @ 120-200 wpm 
Room reverberaton time 500 - 2000 ms.

Notes in music 31 ms - 1000 ms
1/32 @ 200 BPM, 1/4 at 60 bpm
Bar in music. 1 - 4 second

## Pipeline

- Pre-processing
- Machine Learning model
- Post-processsing

There could be resampling in any or all of these steps.
(if using continious time representations it would be infinite.
But since we use discrete time and integer fractions, there is a bounded but quite large of possible combinations) 

ML model here can be a classifier, a clustering algorithm, regression etc.

Many traditional ML algorithms do not support resampling,
they always output.
This includes classics like Linear Regression, Support Vector Machines, RandomForest, k-Nearest Neighbours etc.
So for these the downsampling step will be fixed as 1x.

Deep learning models however, can generally perform an abitrary change in input to output dimensions (including for time),
and using arbitrarily complex functions.

and give us as designers great flexibility in how to do so.
Popular architecture for time-series would be Recurrent Neural Networks, Convolutional Neural Networks

This can sometimes blur the lines between pre/post.
But the conceptual framework is still useful.
And a mindful approach to temporal resampling even more so, since there are so many design choices.


### Pre-processing

Can be very simple operations.
Such as averaging.

Can be a complex deterministic transformation.
Waveform -> spectrogram
Waveform -> MFCC

Can also be a learned function. Now locked.
Example: Using a pretrained neural network to extract features.
OpenL3. 960 ms

### Post-processing

Can also be a very simple operation.
Such as averaging.
Exponential Moving Average
Median filter.

Or could be a complex algorithm, such as Viterbi decoding.

Could in theory be some learned function.
Pre-trained to clean up outputs.
If there is a way to rank multiple different interpretations, can do a search.
Though I have not yet seen this?
Post-processing tends to be quite application specific.

Morphological operations. Erode/dilate. Open/close. Requires binary representation.

Hidden Markov Model. Cleanup states.

Can be class-dependent.
Ex for Sound Event Detection where durations of classes differ a lot.
Gunshot. <300 ms. Remove/truncate/breakup events longer than this.
Music. >1000 ms. Remove any events shorter than this.

Different probability threshold per class.
Reflecting different desired operating points wrt False Alarms / Missed Detections

Pre-padding. To ensure that whole start of event is included.
Post-padding. To ensure that whole end is included.

https://www.mdpi.com/2076-3417/12/5/2626/htm
Halved the error rate (ER) using post-processing with median filtering, using class-dependenth lengths.

You Only Hear Once: A YOLO-like Algorithm for Audio Segmentation and Sound Event Detection 
Segmentation. Using regression to predict start/end of segments.
https://www.mdpi.com/2076-3417/12/7/3293


### Example. Voice Activity Detection
Common tool and component in a speech processing pipeline.

Input resolution. Audio sample rate. 16000 Hz - 48000 Hz (62 us - 20us)
Output resolution. 10 Hz - 100 Hz (100 ms - 10 ms)

This is a downsampling factor between 160-4800x. 

Examples of existing approaches





## References

Digital Signal processing inspirations.
Low/high pass filters
Morphonogical operators
Periodicity.

Critically sampled
Undersampled/oversampled

Statisitics
Meaures of central tendency. Mean, Median
Measures of spread. Standard-deviation, Inter Quartile Ratio (IQR)

Stationarity.


