
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
- Use Soundsensing IoT sensors and Audio ML platform


# Outline

Style.
Show the output/demo first.
Then walk through how to make it
Complete code in a Github, ideally

- Introduction
- About Soundsensing
- Audio Event Detection. Task definition
- Application example. Tracking Beer Fermentation
- Data gathering. Hunting Youtube. youtube-dl
- Exploratory Data Analysis. Spectrograms. Audacity, librosa
- Labeling data. Audacity
- Audio ML pipeline. System diagram
- Pre-processing? Analysis windows. (spectrograms, already covered)
- Training & evaluation. CNN, RNN. Keras
- Post-processing?
- Results
- Streaming inference. Running in real-time 


# TODO

Presentation

- Setup slides skeleton
- Find/make pictures
- Finish slides
- Make git repo for demo code
- Record presentation video 

Demo code

- Run label gen on 3 files
- Verify/clean the labels in Audacity
- Setup pipeline with baseline classifier. MFCC,LogisticRegression
- Add neural network to pipeline. mel-spectrogram with CNN/RNN
- Setup code to run on live input. Test with Monitor playing videos


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
Data augmentation

# Outline


## Audio Event Detection

Aka Sound Event Detection
Present/not.

Similar to.
Audio classification
Keyword spotting

Audio Classification with Machine Learning (Jon Nordby, EuroPython 2019)
https://www.youtube.com/watch?v=uCGROOUO_wY

## Events vs not-events

Events need to have a well-defined duration
Start-end. Onset/offset
Or at least a clear start

If events are overlapping a lot, might not make sense as events anymore
Isolated claps (event) versus clapping (ongoing, class)

For events one can count the number of occurrences
Classification might instead count number of seconds instead



## Brewing alcohol

When brewing alcoholic beverages
such as beer, cider or wine
one puts together a compoud with yeast and (the wort)
into a vessel

IMAGE: fermentation vessel with airlock

After some hours or days the fermentation starts
CO2 is produced by the yeast eating the sugars
The Co2 escapes the tank through the airlock
and this makes an audible "plop" 

AUDIO/VIDEO: airlock plopping

## Fermentation tracking

Several things can go wrong

- fermentation fails to start
- fermentation is too active. Blowout
- fermentation stops abruptly

So brewers try to check in .

The fermentation activity can also be an estimator for the alcohol produced.
Though measuring the specific gravity is better for this

Beer and wine makers track this in terms of Bubbles Per Minute (BPM) 

IMAGE: fermentation activity graph over time

Of course there are existing devices dedicated to this task. 
Such as a Plaato Airlock.
But for fun and learning we will do this using sound.

Our goal.
Make a system that can track fermentation activity,
by using Machine Learning to count the "plops".
This is an Audio Event Detection problem

## Overall System

IMAGE: system architecture

- Brew with a typical airlock
In an environment without too much noise
- Sensor with microphone and Internet connectivity
Like a Raspberry PI, runs Python.
Could alternatively be smartphone, Soundsensing, ESP32. Needs couple more deployment steps
- Database for keeping track of the BPM data.
Brewfather
- Device for observing the data
Typically smartphone



## Data requirements

Should have a minimum of 100 events.
1 per second, just 2 minutes

1000 events better.
Much more stable performance metrics
10'000 probably overkill

Want realistic data. Capturing 

- natural variation in the event sound
- natural variation in recording devices
- natural variation in recording environment

Especially if there are other event-like noises

## Data collection

Searched on Youtube.

- Preferably couple of minutes long, minimum 15 seconds 
- No talking
- Mostly stationary camera
- No audio editing/effects
- One or more airlocks bubbling
- Bubbling can be heard by ear

Making note of

- Bubbling rate
- Clarity of bubble sound
- Other noise around

Maybe 1000 videos reviewed.
End up with around 100 potentialy useful
Many hours of work

Up to 100 recording devices and 100 environments. Maybe 2000 events
Some recordings very long, several hours. Maybe 5000 events

Using youtube-dl to download
youtube-dl --extract-audio $URL

https://youtube-dl.org/
https://github.com/ytdl-org/youtube-dl/

## Exploratory Data Analysis

Always inspect at the data
Listen to audio, look at spectrogram
Audacity open-source software

Characteristics of the sound
Write down notes about it

- Event length
- Distance between events
- Variation in the event sound
- Changes over time
- Differences between recordings
- Background noises
- Other events that could be easily confused

Event length around 200 ms


IMAGE: spectrograms in Audacity

VIDEO? many events from different clips. 1 second each


### Labeling data

Manually using Audacity

"How to Label Audio for Deep Learning in 4 Simple Steps"
Miguel Pinto
TowardsDataScience.com
https://towardsdatascience.com/how-to-label-audio-for-deep-learning-in-4-simple-steps-6a2c33b343e6
Shows how to use Audacity to label.
Including switching to spectrograms,
annotating a frequency range,
exporting the labels to files,
and importing the label files in Python.

IMAGE: Audacity with labels

Semi-automatically with GMM-HMM
First running it, generating label files
Then reviewing and editing the labels in Audacity

Gaussian Mixture Model, Hidden Markov Model
from hmmlearn
https://github.com/hmmlearn/hmmlearn
Using Mel-Frequency-Cepstral-Coefficiants as features
Lossy compression on top of a mel-spectrogram

IMAGE: 

## Audio ML pipeline

AED as classification of short independent time-windows.
Uniform probability of event occuring.

Not considering sequences, or states, in the detector
Ie in speech recognition certain sequences of phonemes are more probable

Single audio stream. Monophonic.
Single event class. Binary classification

Requires that each event is clearly audible and understandable - without context
Low-to-no overlap between events.

## Analysis windows

Bit longer than the event length

Overlap maybe at 10%


## Evaluation

Multiple levels

Window-wise
- False Positive Rate / False Negative Rate
- Precision / recall

Might be overly strict. Due to overlap, can afford to miss a couple of windows 

- Event-wise

- Blops per Minute
Errors within +- 10%?

Should be able to miss a couple of events without loosing track of the BPM
But short clips of just some seconds will have some spread probably

Other desirable properties
- Resolution of output. 
- Reporting delay
- Length of events. Min,max,median. Should fit into one window


## Models

Baseline simple. Logistic Regression on MFCC
Advanced. Own CNN/RNN on spectrogram


## Post-processing

Counting.
Threshold the probability above X

Median filtering.
Reject time-difference values outside of IQR.

Event rate. Count / time

Maybe give a range.
Confidence Interval of the mean
Student-T extimation

## Detection results

IMAGE: precision/recall or TPR/FPR curve

Correctness in


## Streaming inference

Operator does not care about each and every blop
BPM changes slowly and (normally) quite evently

Want ability to check a that fermentation is progressing OK.
Will maybe check couple of times per day 
Can have many minutes, perhaps up to 1 hour lag
Brewfather limits updates to once per 15 minutes

But can be useful when setting up, to verify detection
And makes for nicer demo :)

Key: Chopping up incoming stream into (overlapping) audio windows



## What will you make?

Some other ideas for Audio Event Detection

- Popcorn popping
- Bird call
- Cough
- Umm/aaa speech patterns
- Drum hits
- Car passing

::: notes

Not-events.
Alarm goes off.
Likely to persist (for a while)

:::


## Continious Monitoring using Audio ML

If you want deploy Continious Monitoring using Audio,
consider using Soundsensing sensors and data-platform.

- Built-in cellular connectivity.
- Rugged design for industrial and outdoor usecases.
- Can run Machine Learning both on-device or in-cloud
- Supports Audio Event Detection, Audio Classification, Audio Anomaly Detection


## Questions


# Bonus

## Synthesize data

TEASER

What to do if wanting to estimate performance on tricky scenarios?

What to do if one does not have sufficient data?

Especially to handle different background noises

Using scaper
https://github.com/justinsalamon/scaper

Mix in diffent kinds of background noise.
Vary Signal to Noise ratio

## Event Detection with Weakly Labeled data

TEASER

What if there was a way to learn Audio Event Detectors
without needing to annotated labels for each and every event?

Weekly labeled Audio Event Detection.
Feed in longer clips that either have the event(s) or not - without information about how many or where

Active area of research. DCASE
Speech recognition systems. Can give phone level output with sentence-level annotations 

Multiple Instance Learning
Principle model architecture with neural networks
Each (overlapped) analysis window in a clip goes through same neural network.
Outputs are pooled across time to make prediction of event present-or-not.
Common pooling operation: max, or softmax
More advanced. Attention pooling, or Autopool (softmax generalization)




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
Cough, etc

Some have temporal patterns
Some are more tonal
Alarms

Transitions. Into state. Out of state.


# Other




## Error analysis

False Negatives / False Positives. Rank by probability
Can be generalized to multi-class. For example using pairwise-confusions. Expected-Actual



### Bias/variance diagnostics

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



