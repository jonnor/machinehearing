
# Talk proposals

## Title

Sound Event Detection with weakly labeled data
Sound Event Detection from weakly labeled data

Learning from weakly labeled data for Sound Event Detection

## Tweet abtract
Detecting events in sound using machine learning typically
requires precisely annotating all sound events in the training set.
We will show how to get away with more coarse labels,
which are faster to make, by applying weakly supervised learning.

## Abstract

Detecting events in sound can be done very effectively using a deep learning model,
and can be used in applications such as noise monitoring and monitoring of machines and processes.
The straightforward method to learn such a model uses supervised learning,
where each instance of a sound event has been labeled individually.
However, labeling a suitably large dataset in this manner is very time-consuming.
In this presentation, we will explain and demonstrate how one can
learn event detection models from datasets which does not have per-event labels,
only labels that cover longer sections of time - so called weakly supervised learning.
While the talk focuses on applications for sound,
the techniques shown can be transferred over to other domains,
especially those that also use multi-variate time-series data.

## Description

Sound events are short sounds with a distinct start and end,
typically ranging from some milliseconds to a few seconds.
Sound Event Detection (SED) is the task of detecting such events,
and returning the precise time-stamps of each event.

Some practical applications we have used this for include:
detection of coffee bean cracking for automatic coffee roasting,
be the detection of gunshots and alarms for noise monitoring,
and detection of bubbles during fermentation for tracking of beer brewing.

Using supervised learning of deep neural networks,
it is now possible to make precise, efficient and robust classifiers for such tasks
- assuming that a suitable labeled dataset is available for training.

However, the standard supervised learning setup requires that there exists a one-to-one mapping between a label and each instance to predict.
For Sound Event Detection, this means that each event needs to be precisely annotated in time.
Such fine-grained labeling requires considerable human effort,
and it can be challenging to have consistent labeling in ambiguous cases.
This makes it is time-consuming and costly.

Recent progress in machine learning has now made it possible to learn from "weak" labels:
Labels that are less precise, more noisy or otherwise limited compared to regular (“strong”) labels.
This learning setup is referred to as "weak supervision", "weakly supervised learning".
Here we will focus on labels that have lower temporal resolution:
Instead of labeling the time location of each event,
the labels will be on a longer audio clip of multiple seconds or minutes
(potentially containing multiple sound events).
This greatly reduces the effort needed to annotate the data.
Different kinds of information can be encoded in the labels:
Binary event present/not,
number of events,
and class proportion (amount of time containing event).

The talk will be practically oriented,
showing how to apply these techniques can be applied to example applications from the real world.

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

- Weakly Labeled data: when the labels are of lower (temporal) resolution than our desired model output
- It is possible to learn event detectors without needing to label each and every event instance
- Labeling data with weak labels is much less time-consuming than strong labels
- Audio signals are processed as a series of (overlapped) fixed size analysis windows
- The same event detection model is used for each analysis window (shared weights)
- Combining the predictions from multiple windows can be done using a pooling operator
- The temporally pooled prediction can be compared with a clip-level label, and used for supervised learning
- In TensorFlow / Keras, we can implement this clip-level model using TimeDistributed layer
- Weak supervision for event detection is still under active research, but can be used practically today

## Notes for organizers

I have given some talks previously on related topics

Audio Classification with Machine Learning (EuroPython 2019)
https://www.youtube.com/watch?v=uCGROOUO_wY
Got great response at the conference, and also a large amount of views afterwards

Sound Event Detection using Machine Learning (EuroPython 2021)
https://www.youtube.com/watch?v=JrhsFfCOL-s

The talk is organized to be standalone from earlier presentations.


## Keywords

- Neural Networks / Deep Learning
- Time Series
- Predictive Modelling

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


# Notes

Ref also brewaed/doc/weak_supervision.md

https://en.wikipedia.org/wiki/Weak_supervision

Aka
Weakly supervised learning


noisy, limited, or imprecise sources
Focus on imprecise - lower temporal resolution


Topics

Motivation
    Cost of strongly annotated data
    Savings from going to weakly annotated data
    Might be possible to derive the weak labels. Auto/semi-automatically
        from data collection process. Ex. Mark the event class, then do XX repeats of the event
        from other data sources. Ex: Activity logbooks
        from prior knowledge. Ex: the BPM of brewing starts low, goes high, then low again
        from simple heuristics. Ex: 

Weakly labeled data
    Weakly labeled data in time-series / sequences
    Examples from other domains.
    Weakly Supervised Object Detection (images)

    Present/not. Tagging
    Number of events. Class proportions

Connection to semi-supervised learning, pseudo labeling

Imbalanced data
    Strategies to deal with it

Overfitting / spurious correlations
    Things going on in the background migth be picked up
    Shared weights / distribute model across time
    Limit input to model as much as possible
    Use data augmentation
    

Sparse signals
    

Evaluation
    May still want a strongly labeled validation set


Leveraging Weakly Supervised Data to Improve End-to-End Speech-to-Text Translation
https://arxiv.org/abs/1811.02050

http://dcase.community/challenge2018/task-large-scale-weakly-labeled-semi-supervised-sound-event-detection

Multiple Instance Learning MIL
 


Applications

- Coffee roasting
- Gunshot detection for Noise Monitoring
- Beer brewing

What you will learn

- What weakly labeled data is, and how to setup deep learning models that can learn from such data
Using Tensorflow and Keras

Transferrability

Other multi-variate event detection probject.

- Accelerometer. Human Activity Recognition
- Electroencephalography (EEG)
- Video. Action Localization
- Speech aido. Phoneme level output



