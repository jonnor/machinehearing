
# EuroPython 2019

[Presentation video (YouTube)](https://youtu.be/2FmMESSD2CM?t=8470)
[Slides](,/slides.html)

# Proposal

45 minute session

## Audio Classification with Machine Learning
Learn how to classify sound using Convolutional Neural Networks

### Short abstract
Sound is a rich source of information about the world around us with many applications within music and speech domains, as well as specific tasks in industry and science.

This talk will show you how to build practical models for sound classification, using Convolutional Neural Networks on audio spectrograms.
Tricks for dealing with small amounts of data will also be covered, including transfer learning, audio embeddings and data augmentation.

### Long abstract
Sound is a rich source of information about the world around us.
Modern deep learning approaches can give human-like performance on a range of sound classifiction tasks.
This makes it possible to build systems that use sound to for example:
understand speech, to analyze music, to assist in medical diagnostics, detect quality problems in manufacturing, and to study the behavior of animals.

This talk will show you how to build practical machine learning models that can classify sound.
We will convert sound into spectrograms, a visual representation of sound over time,
and apply machine learning models similar to what is used to for image classification.
The focus will be on Convolutional Neural Networks, which have been shown to work very well for this task.
The Keras and Tensorflow deep learning frameworks will be used.
Some tricks for getting usable results with small amounts of data will be covered,
including transfer learning, audio embeddings and data augmentation.

A basic understanding of machine learning is recommended.
Familiarity with digital sound is a bonus.

## Bio
Engineer with several years of experience as a Software Developer within Embedded Systems and Digital Signal Processing.
These days focusing on Machine Learning for Internet of Things, and recently completed a Master in Data Science.

Jon loves making things and teaching others to do the same, and is very active in the maker scene in Oslo, Norway.

### Tags
Data Science
Machine Learning
Deep Learning


# Presentation

## Format

- 30 minutes.
30 slides
- 10 minutes. Q/A 


## Outline

Introduction

- About me
- Talk outline
- Example applications
- Digital audio

Audio Classification pipeline

- Analysis-windows
- mel-spectrogram
- CNN for audio

Better models

- Audio Embeddings
- Transfer Learning
- Data Augmentation

Outro

- Summary
- More info

BONUS

- Own dataset
- Streaming
- Audio Event Detection
- Weakly labeled data
- Tagging
- Segmentation

Out-of-scope

- CNN details
- Fourier Transform


## Notes

Example applications

Know your problem.
How often do you want outputs
Classification vs Event/onset detection
(weakly labeled, multi-instance)

Streaming.
Listening continiously
Word-error-rate, false-predictions per hour

Tasks that build upon classification
Segmentation.
Novelty/anomaly detection
(not: search/fingerprinting, )

DO:
Use (log-mel) spectrograms
Divide into analysis windows. Overlap optional
Use AudioSet audio-embeddings, with RF/SVM
https://github.com/marl/openl3

Use CNN, transfer learning from ImageNet

Use basic data augmentation. Time-shift! Time-stretch, pitch-shift. Try Mixup!
(but careful about time-shift for AED)
