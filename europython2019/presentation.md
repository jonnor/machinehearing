
---
author: Jon Nordby @jononor
date: EuroPython 2019, Basel
title: Audio Classification using Machine Learning
width: 1920
height: 1080
margin: 0
css: style.css
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

Goal

> a machine learning practitioner
> 
> without prior knowledge about sound processing
> 
> can solve basic Audio Classification problems

Outline

- Introduction
- Audio Classification pipeline
- Tips & Tricks
- Pointers to more information

Slides and more: [https://github.com/jonnor/machinehearing](https://github.com/jonnor/machinehearing)

::: notes

Very practically oriented

Recommended background knowledge

:::

<!--




## Why Audio Classification

- Rich source of information
- Any physical motion creates sound
- Sound 
- Good compliment to image/video
- Humans use our hearing

-->

## Applications

Audio sub-fields

- Speech Recognition. Keyword spotting.
- Music Analysis. Genre classification.
- **General** / other

Examples

* Eco-acoustics. Analyze bird migrations
* Wildlife preservation. Detect poachers in protected areas
* Manufacturing Quality Control. Testing electric car seat motors
* Security: Highlighting CCTV feeds with verbal agression
* Medical. Detect heart murmurs

<!--
* Process industry. Advance process once audible event happens (popcorn)
-->

# Digital sound primer

## Audio Mixtures

![Sounds mix together](./img/sound-sources.png){width=80%}

::: notes

https://www.researchgate.net/profile/Raimund_Dachselt/publication/228715257/figure/fig1/AS:301960805797899@1449004474993/Reverberant-rooms-with-walls-and-openings-For-overlapping-areas-a-parameter-called.png

Channel effects

- Noise
- Frequency response
- Reverberation

:::

<!--

## Human hearing

Two ears (Binaural). Frequencies approx 20Hz - 20kHz. 

A non-linear system

* Loudness is not linear with sound pressure
* Loudness is frequency dependent 
* Compression. Sensitivity lowered when loud
* Masking. Close sounds can hide eachother

::: notes
:::
-->

## Audio acquisition

![](img/audio-aquisition.svg){width=80%}

## Digital sound representation

* Quantized in time (ex: 44100 Hz)
* Quantizied in amplitude (ex: 16 bit)
* N channels. **Mono**/Stereo
* Uncompressed formats: PCM **.WAV**
* Lossless compression: .FLAC
* Lossy compression: .MP3

## Spectrogram

Computed using Short-Time-Fourier-Transform (STFT)

![A frog croaking with ciccadas in background](img/frog_spectrogram.png){width=60%}




# Practical example

## Environmental Sound Classification

> Given an audio signal of environmental sounds,
> 
> determine which class it belongs to

* Widely researched. 1000 hits on Google Scholar
* Open datasets. ESC-50, Urbansound8k (10 classes), AudioSet (632 classes)
* 2017: Human-level performance (on ESC-50)

::: notes

Finite set of classes

https://github.com/karoldvl/ESC-50

:::


## Urbansound8k 

![10 classes, ~8k samples, ~4s long. ~9 hours total](img/urbansound8k-examples.png){width=80%}

State-of-the-art accuracy: 79% - 82%

::: notes 

- Classes from an urban sound taxonomy,
- Based on noise complains in New York City
- Most sounds around 4 seconds.
- Some classes around 1 second
- Saliency annotated  (foreground/background)

:::


# Basic Audio Classification pipeline

## Pipeline

![](img/classification-pipeline.svg){width=70%}

## Analysis windows

![Splitting audio stream into windows of fixed length, with overlap. Image: Sajjad2019](img/framing.png){width=80%}

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

![Mel-scale triangular filters. Applied to linear spectrogram (STFT) => mel-spectrogram](img/melfilters.png){width=80%}

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

![Salamon & Bello, 2016](img/sbcnn.svg){height=80%,max-width=100%}


::: notes

40 mels
61 frames


:::

## Keras model

```python
from keras.layers import ...

def build_model(...):

    block1 = [
        Convolution2D(filters, kernel, padding='same', strides=strides,
                      input_shape=(bands, frames, channels)),
        MaxPooling2D(pool_size=pool),
        Activation('relu'),
    ]
    block2 = [
        Convolution2D(filters*kernels_growth, kernel, padding='same', strides=strides),
        MaxPooling2D(pool_size=pool),
        Activation('relu'),
    ]
    block3 = [
        Convolution2D(filters*kernels_growth, kernel, padding='valid', strides=strides),
        Activation('relu'),
    ]
    backend = [
        Flatten(),

        Dropout(dropout),
        Dense(fully_connected, kernel_regularizer=l2(0.001)),
        Activation('relu'),

        Dropout(dropout),
        Dense(num_labels, kernel_regularizer=l2(0.001)),
        Activation('softmax'),
    ]
    layers = block1 + block2 + block3 + backend
    model = Sequential(layers)
    return model
```

## Aggregating analysis windows

```python
from keras import Model
from keras.layers import Input, TimeDistributed, GlobalAveragePooling1D

def build_multi_instance(base, windows=6, bands=32, frames=72, channels=1):

    input = Input(shape=(windows, bands, frames, channels))

    x = input
    x = TimeDistributed(base)(x)
    x = GlobalAveragePooling1D()(x)
    model = Model(input,x)
    return model
```

*GlobalAveragePooling* -> "Probabilistic voting"

::: notes 

* Max pooling
* Majority vote
* Trained classifier

:::

# Demo

## Demo video

<video src="demo.mp4" type="video/mp4" controls/>
</video>

## Environmental Sound Classification on Microcontrollers using Convolutional Neural Networks

![Report & Code: https://github.com/jonnor/ESC-CNN-microcontroller](./img/thesis.png){height=600px}



# Tips and Tricks


## Normalization

- log-scale compression
- Subtract mean
- Standard scale

![](img/spectrograms.svg){width=60%}

::: notes

Per recording or per analysis window

Global clip/dataset analysis for normalization not possible when streaming

:::

## Data Augmentation

![](img/dataaugmentations.png){width=100%}

* Adding noise. Random/sampled

::: notes

Mostly done in time-domain,
but can also be done in spectrograms

:::

## Mixup

![Mixup: Create new sample using weighted combination of two samples. Image: Xu2018](./img/mixup.jpg){width=60%}

::: notes

Xu2018:
https://arxiv.org/abs/1805.07319

:::


<!--

## SpecAugment

![SpecAugment: Mask spectrogram sections to augment. Image: Neurohive](./img/specaugment.png){width=60%}

::: notes

https://neurohive.io/en/news/specaugment-new-and-simple-data-augmentation-technique-for-audio-data/

:::

-->

## Transfer Learning from images

Pre-trained model ImageNet


- Transfer Learning from image data works OK


`TODO: code example using Keras Applications MobileNet ?`

::: notes

Problem: Images are usually 3 channels (RGB), spectrogram only has 1 channel


:::


## Audio Embeddings

Model pretrained for sound

Look, Listen, Learn ({L^3})

OpenL3

`TODO: code example using OpenL3 ?`

::: notes

Uses a CNN under the hood

Only need to add a simple classifier!
Linear.

??? Could classifying across N frames give good perf.
??? What about adding difference vector

EdgeL3
SoundNet

:::


# Outro

## Summary

`FIXME: style sensibly`

Pipeline

- Fixed-length analysis windows
- log-mel spectrograms
- ML model
- Aggregate analysis windows

Models

1. Audio Embeddings (OpenL3) + simple model (scikit-learn)
2. Convolutional Neural Networks with Transfer Learning (ImageNet etc)
3. ... train **simple** CNN from scratch ... 

Data Augmentation

1. Time-shift
2. Time-stretch, pitch-shift, noise-add
3. Mixup, SpecAugment



## More learning

Slides and more: [https://github.com/jonnor/machinehearing](https://github.com/jonnor/machinehearing)

Hands-on: [TensorFlow tutorial, Simple Audio Recognition](https://www.tensorflow.org/tutorials/sequences/audio_recognition)

Book: Computational Analysis of Sound Scenes and Events (Virtanen/Plumbley/Ellis, 2018) 

<!--
![Computational Analysis of Sound Scenes and Events. Tuomas Virtanen, Mark D. Plumbley, Dan Ellis. 2018.](./img/cassebook.jpg){width=20%}
-->

## Questions

Slides and more: [https://github.com/jonnor/machinehearing](https://github.com/jonnor/machinehearing)

<h1 style="padding: 100px">?</h1>

Interested in Audio Classification or Machine Hearing generally? Get in touch!

Twitter: @[jononor](https://twitter.com/jononor)

# BONUS

## Audio Event Detection

> Return: time something occurred.

* Ex: "Bird singing started", "Bird singing stopped"
* Classification-as-detection. Classifier on short time-frames
* Monophonic: Returns most prominent event

Aka: Onset detection

::: notes

- Avoid time-shift augmentation

:::

## Segmentation

> Return: sections of audio containing desired class

* Postprocesing on Event Detection time-stamps
* Pre-processing to specialized classifiers


::: notes

Eg: Extract only birdcall audio, then perform bird species identification

- Can alternatively be done unsupervised
- Can be real-time / single-pass, or multi-pass

:::

## Tagging

> Return: All classes/events that occurred in audio.

Approaches

* separate classifiers per 'track'
* joint model: multi-label classifier


## Streaming

Real-time classification

`TODO: document how to do in Python`

<!--

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

-->

## Annotating audio

![](./img/audacity.png){width=100%}

```python
import pandas

labels = pandas.read_csv(path, sep='\t', header=None,
                        names=['start', 'end', 'annotation'],
                        dtype=dict(start=float,end=float,annotation=str))
```

::: notes

- Use Audacity
- Label track
- Keyboard shortcuts to add
- Annotation file is a basic CSV
- Tools. Editing. Spectrogram view. Noise removal

:::


## Mel-Frequency Cepstral Coefficients (MFCC)

* MFCC = DCT(mel-spectrogram)
* Popular in Speech Detection
* Compresses: 13-20 coefficients
* Decorrelates: Beneficial with linear models 

On general audio, with strong classifier, performs worse than log mel-spectrogram

## End2End learning

Using the raw audio input as features with Deep Neural Networks.

Need to learn also the time-frequency decomposition,
normally performed by the spectrogram. 

Actively researched using advanced models and large datasets.

`TODO: link EnvNet`


