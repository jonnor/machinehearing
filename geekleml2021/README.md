
# Machine Learning

## Meta
40 minute slot
35 minutes presentation
Pre-recorded talk.
Live Q&A

13:45 — 14:25 CEST
https://python.geekle.us/agenda#!/tab/292052184-1

## Abstract

Audio Events, or Acoustic Events, are individual distinct sounds.
Audio Event Detection (AED) is the task of detecting such sounds, returning precise times that each kind (class) of sound occurs.
This can be anything from detecting coffee-beans cracking while roasting, to gunshots on a shooting range, to noise made by construction works
- all these are real applications the presenter has developed.
This practical talk will show how you can build such a system in Python, using machine learning models applied to audio.
The general approaches shown can also be applied to other sensor data such as vibrations, pressure etc.

## Extended Abstract

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


