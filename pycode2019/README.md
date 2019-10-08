
# PyCode Conference 2019

https://pycode-conference.org/

- October 14-16
- Gdansk, Poland

# Proposal

## Recognizing sounds with Machine Learning and Python

### Abstract
Sound is a rich source of information about the world around us with many applications within music and speech domains, as well as specific tasks in industry and science.

This talk will show you how to build practical models for sound classification, using Convolutional Neural Networks on audio spectrograms.
Tricks for dealing with small amounts of data will also be covered, including transfer learning, audio embeddings and data augmentation.

A basic understanding of machine learning is recommended.

## Bio
Jon started to program in Python in 2009.
Since then he has worked as a Software Developer and Data Engineer within Embedded Systems and Software-as-a-Service projects.
With a Bachelor in Electronics Engineering and a Master in Data Science,
he is an expert on Machine Learning applied to the Internet of Things.

These days Jon is the CTO of Soundsensing, and also does freelance consulting on Machine Learning, audio processing and Internet of Things.

# Meta

## Format
30 minutes. 25 minutes talk, 5 min questions.



## Call to Action

Get in touch if you are interested in applying machine learning to sound!
I love to discuss challenges, usecases and approaches.

Twitter. @jononor

jon@soundsensing.no


## Audience

People that can program in Python.
But not neccesarily a Machine Learning practitioner.

Needs to be a bit more approachable than EuroPython talk,
which assumed ML practitioner experience...

Need to cut down content. 30 minutes instead of 45 minutes.

Goal:

> Audience knows how do a basic audio classification problem

- How to design a system that solves this problem
- How to set it up with common ML framework
- Available tools, tips and tricks.

Need to

- Define the relevant ML terms.
- Ground it in a concrete example. Environmental Sound Classification?
- Give practical and actionable recommendations


Kill:

- Applications
- Details on Mel-filters, normalization


Things to skip?

- Hyperparameter tuning
- Loss functions
- Gradient decent
- Backprop
- Weak labeling

### How system works

We want a system that.
When hearing a sound, can categorize what it is.

How to do this? Using Machine Learning

Supervised Learning.
Train with labels (targets=.
Validation set. Unseen during training. Used for checking generalization, hyperparameter tuning.
Test set. Used for evaluating performance of final model.

Optimize a chosen metric. E.g. 

Split audio stream into short time-frames. Say 1 second.
Convert audio waveform to log Mel-spectrogram.
Classify each such time-window



### Convolutional Neural Network

- 



## TODO

- Test OpenL3 on Urbansound8k?


