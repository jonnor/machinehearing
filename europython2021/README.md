
# Sound Event Detection with Machine Learning

To be presented at EuroPython July 2021.
https://ep2021.europython.eu/talks/9cE22Ve-sound-event-detection-with-machine-learning/

Project with accompanying code etc can be found at:
[https://github.com/jonnor/brewing-audio-event-detection](https://github.com/jonnor/brewing-audio-event-detection)


## Short Abstract
Suggested size: <500 chars.

Sound Events are individual distinct sounds,
and Sound Event Detection (SED) is the task of detecting such sounds,
returning the precise times that each kind (class) of sound occurs.
This can be anything from detecting coffee-beans cracking while roasting,
to gunshots on a shooting range, to noise made by construction works - real applications the presenter has developed.
This practical talk will show how you can build such a system in Python,
using machine learning models applied to audio.


## Long Abstract
Suggested size: 1500 chars.
Be sure to include the goals and any prerequisite required to fully understand it.

Sound Events (or Audio Events or Acoustic Events) are individual distinct sounds.
This could be the pop of roasting popcorn kernels,
the cough of a patient, a car that is passing by on a road,
or the sound of an alarm in an office building.
Sound Event Detection (SED) is the task of detecting such sounds,
returning precise times that each kind (class) of sound occurs.
It finds uses in music analysis, manufacturing, medicine and noise monitoring.

We will show how to realize a basic Sound Event Detection system in Python,
using fermentation tracking of beer brewing as a fun and practical example.
The talk will cover all major parts of such a system, including:

- Collecting and exploring a custom dataset
- Setting up the supervised learning task from the dataset
- Extracting spectrogram features from audio waveforms
- Training a Convolutional Neural Network (CNN) and Recurrent Neural Network (RNN)
- Running the trained model on an real-time audio stream
- Processing model output probabilties into discrete events
- Evaluate the performance of the resulting SED system

Example code in Python covering these aspects will be provided.
Libraries used with be Keras, TensorFlow and scikit-learn for machine learning,
and pysoundfile, sounddevice and librosa for audio processing,
with some numpy and pandas for general data manipulation.

## Prerequisites

Being comfortable to read and understand Python code snippets heavily recommended.
Some general familiarity with supervised Machine Learning is recommended.
Familiarity with time-series or audio is a bonus, but not a pre-requisite.

## Tags
Machine Learning
Data Science
Deep Learning
Data
Sensors

## Additional information

At EuroPython 2019 I had a talk about Audio Classification, a related task to Sound Event Detection.
The presentation was very well received, both at the event and on Youtube afterwards.
There were many excellent questions in the QA, and discussions continued after the session was over. 
On Youtube the recordings (couple of copies) have been watched over 20'000 times.
So it seems there is good amount of interest for such a domain/task-focused content.
Link to previous talk: https://www.youtube.com/watch?v=uCGROOUO_wY

I have also given other talks on Audio Machine Learning,
like this one from TinyML - which is much more compressed, and less pedagogical in focus
https://www.youtube.com/watch?v=cARhrotq5HA

An early version of this talk was given at Python for ML and AI 2021.
I will improve the presentation and adjust it based on feedback that I got there.

