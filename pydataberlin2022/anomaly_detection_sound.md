

# Talk proposals

What problem is your talk addressing
(are you talking about a well known problem or have you found something new during a project)

Why is the problem relevant to the audience

What is(are) your solution(s) to the problem,
or are you simply pointing out the fact there is an issue we should be aware of (this is also extremely useful)

What are the main takeaways from your talk?
For tutorial submission this is extremely important, please specify 

what people will have learned at the end of the tutorial session.

## Keywords

- Neural Networks / Deep Learning
- Time Series

## Track
PyData: Deep Learning

## Talk Type
Talk 45 minutes


## Bio

Jon is a Machine Learning Engineer that specializes in audio and IoT applications.
He first learned Python back in 2008 to contribute to open source software projects.
He has a Master in Data Science and a Bachelor in Electronics Engineering,
and has worked as a software engineer in electronics and web projects for 10 years.
Since 2019 he is the Head of Machine Learning and Data Science at Soundsensing,
a provider of IoT sensors for sound with built Machine Learning capabilities.

## Title

Anomaly Detection for sound


## Tweet astract
60 - 280 chars


## Abstract
Between 200 and 1500 characters.



## Description
Between 400 and 50000 characters


Our toolkit will be Tensorflow with Keras for deep learning,
Librosa for audio feature extraction,
along with common PyData libraries
including Pandas and Numpy general data processing,
with Seaborn and Matplotlib for data visualization.

We assume basic familiarity with Python programming the PyData stack,
along with supervised machine learning and basics of deep learning (ant framework).
Familiarity with time-series or audio data is beneficial, but not necessary.

The approaches shown here can be transferred to event detection tasks
in other multi-variate time-series, for example:
Human Activity Detection using accelerometer data,
neurological disease evaluation using Electroencephalography (EEG) data,
and Action Localization in videos.

Main takeaways

- 

## Notes for organizers

I have given some talks previously on related topics

Audio Classification with Machine Learning (EuroPython 2019)
https://www.youtube.com/watch?v=uCGROOUO_wY
Got great response at the conference, and also a large amount of views afterwards

Sound Event Detection using Machine Learning (EuroPython 2021)
https://www.youtube.com/watch?v=JrhsFfCOL-s

The talk is organized to be standalone from other presentations.


# Notes

## Anomaly Detection using Sound
Acoustic Anomaly Detection

DCASE2020 Task2 / DCASE2021 Task2

Representations. log mel spectrogram
Represenation learning

Take aways

- Anomaly Detection in complex multi-variate data can be done with AutoEncoders
- In an Autoencoder, the reconstruction error is basis for the anomaly score
- The approaches shown here can transfer across from audio to other multivariate time-series

Outline

- Anomaly Detection
How is it different from (binary classification)
Unsupervised learning does not mean unsupervised/unlabeled evaluation
- Audio representations
Fixed-width analysis windows
Spectrograms
log-mel spectrograms
- (reconstructing) AutoEncoder
- Interpolation AutoEncoder
- DCASE / MMI / dataset


