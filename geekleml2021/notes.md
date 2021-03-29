
# Meta
30 minute slot.
20-25 minutes presentation
Pre-recorded talk. Live Q&A

12:45 — 13:15 CEST
https://python.geekle.us/agenda#!/tab/292052184-1

Approx half the content of EuroPython

# Abstract

Audio Events, or Acoustic Events, are individual distinct sounds.
Audio Event Detection (AED) is the task of detecting such sounds, returning precise times that each kind (class) of sound occurs.
This can be anything from detecting coffee-beans cracking while roasting, to gunshots on a shooting range, to noise made by construction works - all these are real applications the presenter has developed.
This practical talk will show how you can build such a system in Python, using machine learning models applied to audio.
The general approaches shown can also be applied to other sensor data such as vibrations, pressure etc.

# Extended Abstract

Audio Events, or Acoustic Events, are individual distinct sounds.
This could be the pop of popcorn kernels in a popcorn machine,
the cough of a patient,
a car that is passing by on a road,
or the sound of an alarm in an office building.

Audio Event Detection (AED) is the task of detecting such sounds,
returning precise times that each kind (class) of sound occurs.
It finds uses in music analysis, manufacturing, medicine and building management.

Steps
- Set up the supervised learning task from a collected dataset.
- Extract spectrogram features from audio waveforms.
- Train a Convolutional Neural Network (CNN) and Recurrent Neural Network (RNN).
- Run the trained model on an real-time audio stream.
- Process model output probabilties into discrete events.
- Evaluate the performance of the resulting AED system.

Example code in Python covering these aspects will be provided.
Libraries used with be Keras, TensorFlow and scikit-learn for machine learning,
and pysoundfile, PyAudio and librosa for audio processing,
with some numpy and pandas for general data manipulation.

Some general familiarity with supervised Machine Learning is recommended.
Familiarity with time-series or audio is a bonus, but not a pre-requisite.

# Calls to Action

Interested in working on Audio and ML?
- Apply at Soundsensing

Looking for monitoring solutions using Audio?
Use Soundsensing IoT sensors and Audio ML platform



# Demo

Ideal demo

- Concrete usecase
- Simple phenomenon
- Relatable, familiar
- Can use detected events to illustrate/uncover differences
Different event rates say something about other (potentially hidden) process variables.
Ie popcorn. Different brand of popcorn. Different conditions, ie humidity. Amount of beans
Change in events say when something has started or stopped.
- Can show detecting working in real-time
- Can share the data
- Data is easily accessible
- Labeled data exists already
Bird call?
- Fun and geeky


Tracking beer brewing via sound

Rate of fermentation over time
mol/sec

https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FNadia-Musco%2Fpublication%2F282402373%2Ffigure%2Ffig1%2FAS%3A613907060240428%401523378257552%2FIn-vitro-cumulative-gas-production-Panel-A-and-fermentation-rate-Panel-B-over-time.png&imgrefurl=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FIn-vitro-cumulative-gas-production-Panel-A-and-fermentation-rate-Panel-B-over-time_fig1_282402373&tbnid=Gsp5YMmGHkG1bM&vet=12ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygFegUIARCuAQ..i&docid=WvHXcTxPacLZDM&w=709&h=975&itg=1&q=rate%20of%20fermentation%20over%20time&hl=en&ved=2ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygFegUIARCuAQ

https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FFederico-Infascelli%2Fpublication%2F41394048%2Ffigure%2Ffig1%2FAS%3A669993146519561%401536750222607%2FTrend-of-fermentation-rate-over-time.png&imgrefurl=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FTrend-of-fermentation-rate-over-time_fig1_41394048&tbnid=R7LwBqk0XIpDCM&vet=12ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygAegUIARCkAQ..i&docid=Z_pUBmtVx2iewM&w=850&h=397&q=rate%20of%20fermentation%20over%20time&hl=en&ved=2ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygAegUIARCkAQ


https://www.google.com/search?q=rate+of+fermentation+over+time&tbm=isch&ved=2ahUKEwjU3r32jdTvAhXSxSoKHaDrCxEQ2-cCegQIABAA&oq=rate+of+fermentation+over+time&gs_lcp=CgNpbWcQAzoCCAA6BAgAEENQkUVYqVFgnlJoAHAAeACAAViIAe8FkgECMTCYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=4QxhYJTqLNKLqwGg16-IAQ&bih=985&biw=1918&hl=en#imgrc=EKf6aNkBtPCGPM

# TODO

- Collect initial audio data
- Run through standard classifiers, see how they do
- Run through spectrogram
- Run through soundlevels
- Label some 10-100 events per track, evaluate performance



# Outline

- Definition
- Motivating applications
- Audio pipeline
- Data and labels
- Training
- Evaluate performance
- Running real-time 

Style.
Show the output/demo first.
Then walk through how to make it?
Complete code in a Github, ideally

# Applications

Aka Sound Event Detection
Present/not.

Similar to.
Audio classification
Keyword spotting

## Data requirements

Go for at least 100 events
1 per second, 2 minutes

Baseline simple. Soundlevel/freq, RF
Baseline advanced. Pretrained audio CNN
Custom. Own CNN/RNN on spectrogram

# Planning
What people need to understand

- Audio events
What is an audio event.
Onset/offset
Definition of AED task. Input/outputs

- Typical audio ML pipeline
Analysis windows
Features over time
Spectrogram

- How to evaluate performance
Window-wise vs event-wise
sed_eval: https://tut-arg.github.io/sed_eval/
tolerances

What we will (mostly) assume that people know

- Basic digital audio
- Basic Machine Learning. Supervised classification
- Typical Neural Networks. CNN/RNN ?

Refer to EuroPython talk.


What people do not need to understand

- ? Weakly labeled data 
- Making efficient networks

Undecided

- Post-processing.
Counting. Threshold above X
Event-rate

Tips & tricks

- Error analysis
Manually examining mistakes that your algorithm is making

- Labeling strategies
Unsupervised learning. HMM GMM
Weakly labeled data
Semi-supervised
Alignment tools

- Pretrained model
OpenL3 / YAMNET / PANN

Challenges

- Out-of-distribution data
Device. Environment. 

## Requirements for AED

- Resolution of output. 
- Detection delay
- False Positive Rate / False Negative Rate
- Precision / recall

Things to consider
- Length of events. Min,max,median. Should fit into one window

## Examples

- Popcorn popping. Or coffeebeans
- Gunshot detection
- Bird call
- Cough
- Umm/aaa speech patterns
- Drum hit
- Alarm goes off
- Car passing
- Plop from alcohol fermentation lock

## Events vs not-events
Need to have a well-defined duration
Start-end. Onset/offset
Or at least a clear start

If events are overlapping a lot, might not make sense as events anymore
One hand clap versus clapping

For events one can count the number of occurrences
Classification might instead count number of seconds instead

## Approach
AED as classification of short independent time-windows
Uniform probability of event occuring.

Not considering sequences, or states, in the detector
Ie in speech recognition certain sequences of phonemes are more probable

Monophonic.
Binary classification

Requires that each event is clearly audible and understandable - without context
Low-to-no overlap

## Characteristics of Audio Events

- Duration
- Tonal/atonal
- Temporal patterns
- Percussive
- Frequency content
- Temporal envelope
- Foreground vs background
- Signal to Noise Ratio

Some events are short
Gunshot
Bark

Some are bit longer
Cat mjau

Some events are percussive / atonal.
Cough,  etc

Some have temporal patterns
Some are more tonal
Alarms

Transitions. Into state. Out of state.


### Popcorn-popping

https://www.youtube.com/watch?v=6aAuwZfJTkc
actually happens so close that might not be well approximated as individual events
Get a "cling" from things hitting

10 hours of popcorn popping
https://www.youtube.com/watch?v=--pvwC3yO3Q
inside a micro
popping in bag.
Thuds

https://www.youtube.com/watch?v=Y0xh95oTjG4
open frying pan
popcorns put in over time
makes cling sound
relatively slow event rate
sounds of kernels hitting eachother
flying out of pan and hitting stove


### 
Fermentation
Brewing
Air lock 

Brewers speak of
bubbles per minute 


Event length around 200 ms

Watch an Airlock Bubbling During Mead Fermentation - Entertainment for Brewers
https://www.youtube.com/watch?v=p0jtxp5nWms
5 minutes
Quite regular events
Not so loud events
Quite high ambient noise


ASMR | Homebrewing Airlock Symphony
https://www.youtube.com/watch?v=MN0Mg1uyznU
16 minutes
3-5 different airlocks. Sound different
One has highest event rate
Low ambient noise

https://www.youtube.com/watch?v=by0e-EkAsOE
60 minutes

https://www.youtube.com/watch?v=q2srYoC3FOo
2 hours 20

Every 20 minutes there is another event


Professional acoustic monitoring of brewing.
Using piezo element. Tzero
https://www.fierceelectronics.com/sensors/high-tech-meets-taproom-acoustic-fermentation-sensor
https://www.tzerobrew.com/monitor

DIY bubble logger. IR photometer based
https://www.sparkfun.com/tutorials/131

DIY hygrometer
https://www.hackster.io/135387/homebrew-fermentation-monitor-9df83e

## Post-processing

Counting. Threshold above X
Event rate. Count / time


# Other


## Error analysis

False Negatives / False Positives. Rank by probability
Can be generalized to multi-class. For example using pairwise-confusions. Expected-Actual


Bias/variance diagnostics
High Variance problem: Training error much lower than test error
High Bias problem: Both training and test error high
Different strategies to fix the two cases

Diagnostic
Convergence failure.
Optimizing wrong loss function. 

Lecture 11.2 — Machine Learning System Design | Error Analysis — [ Machine Learning | Andrew Ng ]
https://www.youtube.com/watch?v=k1JGvqr56Yk

DeepLearningAI: Carrying Out Error Analysis (C3W2L01)
https://www.youtube.com/watch?v=JoAxZsdw_3w

Debugging ML Models and Error Analysis | Stanford CS229 | Andrew Ng
https://www.youtube.com/watch?v=ORrStCArmP4

Machine Learning System Design | Error Analysis
https://www.coursera.org/lecture/machine-learning/error-analysis-x62iE

Microsoft Error Analysis toolkit.

https://erroranalysis.ai/


# Resources

https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection
Using PANNsCNN14Att
Shows training with weak supervision
Part of Cornell Birdcall Identification challenge
https://www.kaggle.com/c/birdsong-recognition

Was used as inspiration for the winning entry
https://www.kaggle.com/c/birdsong-recognition/discussion/183208
DenseNet with focal/BCELoss
SpecAugment, Mixup
Ensemble of 4 models

Attention based pooling
https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection/comments#962915
tahn instead of softmax

Attention-based Deep Multiple Instance Learning
https://arxiv.org/abs/1802.04712
Maximilian Ilse
ICML 2018



