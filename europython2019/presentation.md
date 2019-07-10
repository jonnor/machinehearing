
---
author: Jon Nordby @jononor
date: EuroPython 2019, Basel
margin: 0
css: style.css
title: Audio Classification using Machine Learning
---

# Introduction

## Me

Internet of Things specialist

- B.Eng in **Electronics**
- 9 years as **Software** developer. **Embedded** + **Web**
- M. Sc in **Data** Science


## Soundsensing

![](img/soundsensing-logo.png)

Sensor Systems for Noise Monitoring

- Supported by Norwegian Research Council
- Pilot project with Oslo Kommune
- Accepted to incubator at StartupLab

## This talk

Very practically oriented

TODO: describe scope

Recommended background knowledge

Audio sub-fields

- Speech (Speech Recognition)
- Music (Music Information Retrieval)
- **General** / other

# Background

## Why Audio Classification

- Rich source of information
- Any physical motion creates sound
- Sound 
- Good compliment to image/video
- Humans use our hearing

## Audio aquisition

![](img/audio-aquisition.svg){width=100%}


# Practical example

## Environmental Sound Classification

> Given an audio signal of environmental sounds,
> determine which class it belongs to

* Widely researched. 1000 hits on Google Scholar
* Datasets. ESC-50, Urbansound8k (10 classes), AudioSet (632 classes)
* 2017: Human-level performance (on ESC-50)

::: notes

Finite set of classes

https://github.com/karoldvl/ESC-50

:::


## Urbansound8k 

![](img/urbansound8k-examples.png){width=100%}

::: notes 

Classes from an urban sound taxonomy,
based on noise complains in New York city

Most sounds around 4 seconds. Some classes around 1 second

Foreground/background annotated

:::


# Audio Classification

## Pipeline

![](img/classification-pipeline.svg){width=80%}

## Analysis windows

![Splitting audio stream into windows of fixed length, with overlap. Image: Sajjad2019](img/framing.png)

::: notes

Image:
https://www.researchgate.net/figure/Framing-the-input-audio-signal-into-several-frames-s-s-1-with-appropriate_fig1_332553888

@misc{Sajjad2019,
  author = {Abdoli, Sajjad and Cardinal, Patrick and Koerich, Alessandro},
  year = {2019},
  month = {04},
  pages = {},
  title = {End-to-End Environmental Sound Classification using a 1D Convolutional Neural Network}
}


Hyperparameters:

- Window length
- Window hop / overlap


Depends primarily on how often you want predictions
but beneficial to limit window size:

- lower input dimensionality, easier to learn
- smaller model size
- lower inference time
- lower RAM consumption

+ pretrained image models often want rectangular inputs.
Ex: 128x128

if using a short window compared to label/prediction time,
need to aggregate the predictions somehow

if we want output on a shorter time-basis than labels are available for,
we have a 'weak labeling' scenario

:::

## Mel-filters

![Mel-scale triangular filters. Applied to linear spectrogram (STFT) => mel-spectrogram](img/melfilters.png){width=100%}

::: notes

Hyperparameters:

- Samplerate
(44.1/48kHz originals. 22kHz commonly used, 16 kHz sometimes)
- Mel filters
- Hop length
- Filter frequency range

(window function: Hann, overlap 50%)

In Python:

- librosa.feature.melspectrogram()
CPU only. Numpy
- Kapre Melspectrogram layer.
GPU. Using Tensorflow STFT operation

:::

## Feature preprocessing

`FIXNE: finish code example`

```python
import librosa

y, sr = librosa.load('audio/0001.wav')
mels = librosa.feature.melspectrogram(y, sr)
```

`TODO: image of chopped spectrogram?`

## Convolutional Neural Network

1: Spectrograms are *image-like* 

2: CNNs are best-in-class for image-classification

=> Will CNNs work well on spectrograms?

<p class="fragment fade-in" style='padding-top: 30px'>Yes!</p>

<p class="fragment fade-in" style='padding-top: 30px'>A bit suprising?</p>

::: notes

Suprising?

- Spectrogram axes not equivalent to eachother.
One is frequency, other is time.
Shifting does not mean the same in each axis.
- No direct ability to model larger frequency patterns (overtones, formants)
- Longer-term time information is lost
- Convolutional Recurrent Neural Networks (CRNN)

Benefits:

- Practices from image classification apply!
Much bigger field.

:::

## SB-CNN

![](img/sbcnn.svg){height=100%,max-width=100%}


## Training setup

Multiple-instance

TimeDistributed in Keras


## Aggregating predictions

* Majority vote
* Mean voting
* Max




# More advanced uses


## Normalization

![](img/spectrograms.svg){width=100%}

Mean-subtract 
Per recording or per analysis window

Global analysis not possible when streaming

## Transfer Learning from images

Pre-trained model ImageNet


- Transfer Learning from image data works OK

::: notes

Problem: Images are usually 3 channels: RGB
Spectrogram only has 1 channel

:::



## Data Augmentation

![](img/dataaugmentations.png){width=100%}

::: notes

Mostly done in time-domain,
but can also be done in spectrograms

TODO: mention noise addition. White noise
TODO: mention Mixup

TODO: mention Cutout, SpecAugment

:::



# Summary

## Summary

Pipeline

- Audio stream
- Fixed-length analysis windows (overlapping)
- log-mel spectrograms
- ML model
- Aggregate using mean

Models

1. Audio Embeddings (OpenL3) + simple model (scikit-learn)
2. Convolutional Neural Networks with Transfer Learning (ImageNet etc)
3. ... train CNN from scratch ... 

Tricks

1. Time-shift data augmentation
2. Time-stretch, pitch-shift, noiseaddition
3. Mixup, SpecAugment


# BONUS

## Audio Event Detection

Onset detection

- Can use a Classifier
- Shorter time-windows
- Avoid time-shift augmentation

## Segmentation

Cutting up a long audio recording into smaller audio snippets of interest.

Often part of a workflow for more complex cases.
Eg: Extract only birdcall audio, then perform bird species identification

::: notes

- Can alternatively be done unsupervised

:::

## Tagging

Output multiple sounds that occur in audio.

Multi-class classification


## Streaming

Real-time classification


## Creating datasets

::: notes

Use lossless compression
Make sure autogain is off (smartphones)

Make a plan for how to record

Capture information about recording setup.
Recording equipment. Recording settings.
System under test.
Environmental conditions.
Take pictures.
Keep a written log of things that happen during recording.
Timestamp important events.

:::

## Annotating audio

- Use Audacity
- Label track
- Keyboard shortcuts to add
- Annotation file is a basic CSV
- Tools. Editing. Spectrogram view. Noise removal


## Mel-Frequency Cepstral Coefficients (MFCC)


