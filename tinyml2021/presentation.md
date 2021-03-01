
---
title: Environmental Sound Classification on microcontrollers
author: Jon Nordby <jon@soundsensing.no>
date: March 25, 2021
css: style.css
width: 1920
height: 1080
margin: 0
pagetitle: 'TinyML Summit 2021: Environmental Sound Classification on microcontrollers'
---


# Introduction

##  Jon Nordby.

- 2010. B.Eng in **Electronics**
- **Software** developer. **Embedded** + **Web**
- 2019. M. Sc in **Data Science**

Now: CTO, Soundsensing

::: notes

TODO: add picture(s)

Provide **Noise Monitoring** and Audio **Condition Monitoring** solutions
that are used in Real-Estate, Industry, and Smart Cities.

Critical part of this is Machine Learning for Audio Classification,
as well as Anomaly Detection.

Try to do as much as possible **on sensor**.
:::

## Soundsensing

![](./img/soundsensing-withlogo.png){width=100%}

::: notes

In Europe

* 13 million suffering from sleep disturbance (EEA)
* 900'000 DALY lost (WHO)

https://www.eea.europa.eu/themes/human/noise/noise-2

Burden of Disease WHO
http://www.euro.who.int/__data/assets/pdf_file/0008/136466/e94888.pdf

## Dashboard

![Pilot projects with customers Now - 2020](img/what-we-do.png)

TODO: simplify picture

:::


## TinyML for Wireless Audio Sensor Networks

![](img/sensornetworks.png){width=70%}

TODO: highlight tinyML case, bottom
TODO: highlight costs/advantages. Privacy, data/energy efficiency

::: notes


:::


## Environmental Sound Classification

![](img/urbansound8k-examples.png){width=100%}

* Widely researched. 1000 hits on Google Scholar
* Datasets. **Urbansound8k** (10 classes), ESC-50, AudioSet (632 classes)
* 2017: Human-level performance on ESC-50

::: notes

Classes from an urban sound taxonomy,
based on noise complains in New York city

Most sounds around 4 seconds. Some classes around 1 second

Foreground/background

https://github.com/karoldvl/ESC-50

:::




## Device constraints

STM32L476. With 50% of capacity:

* 64 kB RAM
* 512 kB FLASH memory
* 4.5 M MACC/second

TODO: add picture of microcontroller

::: notes

STM32L476

ARM Cortex M4F
Hardware floating-point unit (FPU)
DSP SIMD instructions
80 MHz CPU clock 
1024 kB of program memory (Flash)
128 kB of RAM.

25 mWatt max

- TensorFlow Lite for Microcontrollers (Google)
- ST X-CUBE-AI (ST Microelectronics)

:::



## Existing models

![Green: Feasible region on device](img/urbansound8k-existing-models-logmel.png){width=100%}

TODO: add in our best model results

::: notes

eGRU: running on ARM Cortex-M0 microcontroller, accuracy 61% with **non-standard** evaluation

Assuming no overlap. Most models use very high overlap, 100X higher compute

:::







# Shrinking Convolutional Neural Networks for TinyML Audio

How to make the model fit on device?

## Pipeline

![](img/classification-pipeline.png){max-height=100%}

Typical audio pipeline. Spectrogram conversion, CNN on overlapped windows.

## Reduce input dimensionality

![](img/input-size.svg){width=70%}

- Lower sample rate
- Lower frequency range
- Lower frequency resolution
- Lower time duration in window
- Lower time resolution

~10x reduction

::: notes

Directly limits time and RAM use first few layers.

Follow-on effects.
A simpler input representation is (hopefully) easier to learn
allowing for a simpler model

:::

## Reduce overlap

![](img/framing.png){width=80%}

Models in literature use 95% overlap or more. 20x penalty in inference time!

Often small performance benefit. Use 0% (1x) or 50% (2x).

<!--
## Regular 2D-convolution

![](img/convolution-2d.png){width=100%}

::: notes

TODO: illustrate the cubical nature. Many channel

:::
-->

## Depthwise-separable Convolution


![](img/depthwise-separable-convolution.png){width=90%}

MobileNet, "Hello Edge", AclNet. 3x3 kernel,64 filters: 7.5x speedup
 
::: notes

* Much fewer operations
* Less expressive - but regularization effect can be beneficial

:::

## Spatially-separable Convolution

![](img/spatially-separable-convolution.png){width=90%}

EffNet, LD-CNN. 5x5 kernel: 2.5x speedup


## Downsampling using max-pooling

![](img/maxpooling.png){width=100%}

Wasteful? Computing convolutions, then throwing away 3/4 of results!

## Downsampling using strided convolution

![](img/strided-convolution.png){width=100%}

Striding means fewer computations and "learned" downsampling

TODO: merge into previous slide


## Quantization

Use 8 bit integers instead of 32 bit floats

- 1/4 the size for weights (FLASH) and activations (RAM) 
- 8bit **SIMD** on ARM Cortex M4F: 1/4 the inference time

TODO: add a picture

::: notes


:::

::: notes

EnvNet-v2 got 78.3% on Urbansound8k with 16 kHz
:::

## ConvolutionWaveform input to model

- Preprocessing. Mel-spectrogram: **60** milliseconds
- CNN. Stride-DS-24: **81** milliseconds w/o quantization
- With quantization, spectrogram conversion is the bottleneck!
- Convolutions can be used to learn a Time-Frequency transformation.

TODO: add a picture. Learned filterbanks instead of STFT


::: notes
- Especially interesting with CNN hardware acceleration.

:::


# Summary

## Conclusions

- Convolutional Neural Networks widely used for audio classification
- Well known techniques to shrink down by 100x
- Cam fit onto in TinyML devices (ARM Cortex M4F)
- Able to perform Environmental Sound Classification at `~ 10mW` power,

- Highest reported Urbansound8k on microcontroller (over eGRU 62%)


## Details on results

Thesis

> Environmental Sound Classification
> on Microcontrollers
> using Convolutional Neural Networks

![Report & Code: https://github.com/jonnor/ESC-CNN-microcontroller](./img/thesis.png){width=30%}

::: notes

More potential work

- Neural Network co-processor
- Streaming classification
- Adaptive sampling

:::





## Questions

<h1 style="padding: 100px">?</h1>

Email: <jon@soundsensing.no>

TODO: add TinyML picture

# Bonus

Bonus slides after this point

# Thesis results

## All models

![](img/models-list.png)

::: notes

* Baseline is outside requirements
* Rest fits the theoretical constraints
* Sometimes had to reduce number of base filters to 22 to fit in RAM

:::

## Models

<!--
Based on SB-CNN (Salamon+Bello, 2016)
-->

![](img/models.svg){width=70%}


::: notes

Baseline from SB-CNN

Few modifications

* Uses smaller input feature representation
* Reduced downsample factor to accommodate

CONV = entry point for trying different convolution operators

:::


## Model comparison

![](img/models_accuracy.png){width=100%}

::: notes

- Baseline relative to SB-CNN and LD-CNN is down from 79% to 73%
Expected because poorer input representation.
Much lower overlap 

:::



## List of results

![](img/results.png){width=100%}


## Confusion

![](img/confusion_test.png){width=70%}

## Grouped classification

![](img/grouped_confusion_test_foreground.png){width=60%}

Foreground-only

## Unknown class

![](img/unknown-class.png){width=100%}

::: notes

Idea: If confidence of model is low, consider it as "unknown"

* Left: Histogram of correct/incorrect predictions
* Right: Precision/recall curves
* Precision improves at expense of recall
* 90%+ precision possible at 40% recall

Usefulness:

* Avoids making decisions on poor grounds
* "Unknown" samples good candidates for labeling->dataset. Active Learning 
* Low recall not a problem? Data is abundant, 15 samples a 4 seconds per minute per sensor

:::



# Thesis Methods

Standard procedure for Urbansound8k

- Classification problem
- 4 second sound clips
- 10 classes
- 10-fold cross-validation, predefined
- Metric: Accuracy

## Training settings

![](img/training-settings.png)

## Training

- NVidia RTX2060 GPU 6 GB
- 10 models x 10 folds = 100 training jobs
- 100 epochs
- 3 jobs in parallel
- 36 hours total

::: notes 

- ! GPU utilization only 15%
- CPU utilization was near 100%
- Larger models to utilize GPU better?
- Parallel processing limited by RAM of biggest models
- GPU-based augmentation might be faster

:::

## Evaluation

For each fold of each model

1. Select best model based on validation accuracy
2. Calculate accuracy on test set

For each model

- Measure CPU time on device

## Mel-spectrogram

![](img/spectrograms.svg)


## More resources

Machine Hearing. ML on Audio

- [github.com/jonnor/machinehearing](https://github.com/jonnor/machinehearing)

Machine Learning for Embedded / IoT

- [github.com/jonnor/embeddedml](https://github.com/jonnor/embeddedml)

Thesis Report & Code

- [github.com/jonnor/ESC-CNN-microcontroller](https://github.com/jonnor/ESC-CNN-microcontroller)


