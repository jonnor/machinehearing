

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


## Tweet abstract
60 - 280 chars


## Abstract
Between 200 and 1500 characters.



## Description
Between 400 and 50000 characters

Anomaly Detection 
It is highly related to the tasks of
Outlier Detection and Novelty Detection.


Our toolkit will be Tensorflow with Keras for deep learning,
Librosa for audio feature extraction,
along with common PyData libraries
including Pandas and Numpy general data processing,
with Seaborn and Matplotlib for data visualization.

We assume basic familiarity with Python programming the PyData stack,
along with supervised machine learning and basics of deep learning (ant framework).
Familiarity with time-series or audio data is beneficial, but not necessary.

The approaches shown here can be transferred to anomaly detection tasks
in other multi-variate time-series with regular patterns.
This could be vibration analysis using accelerometer data,
motor analysis using high-resolution current measurements.

Anomaly Detection can also be a powerful tool for monitoring
a machine learning classification/regression pipeline,
to spot data drift and/or out-of-distribution samples.

Takeaways

- Anomaly Detection is done using a one-class modelling approach,
assuming that the vast majority of training data is from the "normal" class
- While the training data does not need to be labeled,
it strongly recommended to have a labeled set for validation and testing
- Audio streams and long clips can be processed as set of fixed-length analysis windows
- Spectrogram representation of audio lends itself well to anomaly detection task
- Anomaly Detection in complex multi-variate data can be done with Autoencoders
- In an Autoencoder, the reconstruction error used as base for the anomaly score


## Notes for organizers

I have given some talks on related topics previously

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

http://dcase.community/challenge2020/task-unsupervised-detection-of-anomalous-sounds
http://dcase.community/challenge2021/task-unsupervised-detection-of-anomalous-sounds




Outline

- Anomaly Detection
How is it different from (binary classification)
Unsupervised learning does not mean unsupervised/unlabeled evaluation

- DCASE challenge dataset
MMI / ToyAMOS
At the moment not so many other anomaly detection datasets for sounds

- Audio representations
Fixed-width analysis windows
Spectrograms
log-mel spectrograms

- Reconstructing AutoEncoder

- Interpolation AutoEncoder

- Choosing decision boundaries


