
---
author: Jon Nordby <jon@soundsensing.no>
date: March 25, 2021
css: style.css
width: 1920
height: 1080
margin: 0
pagetitle: 'TinyML Summit 2021: Environmental Sound Classification on microcontrollers'
---

<section class="titleslide level1" data-background-image="./img/soundsensing-withlogo.jpg" style="background: rgba(255, 255, 255, 0.3); padding-top: 1.7em;" >

<h1 style="">Environmental Sound Classification on microcontrollers</h1>

<p>
Jon Nordby</br>
jon&#64;soundsensing.no</br>
tinyML Summit 2021</br>
</p>

</section>

# Introduction

::: notes

Jon Nordby</br>
Head of Data Science</br> 
Soundsensing AS

- 2010. B.Eng in **Electronics**
- **Software** developer. **Embedded** + **Web**
- 2019. M. Sc in **Data Science**


TODO: add picture(s)

Provide **Noise Monitoring** and Audio **Condition Monitoring** solutions
that are used in Real-Estate, Industry, and Smart Cities.

Critical part of this is Machine Learning for Audio Classification,
as well as Anomaly Detection.

Try to do as much as possible **on sensor**.
:::

## Environmental Noise Pollution

![](./img/noise-map-barcelona-day.png){width=50%}

The environmental pollution that affects most people in Europe

* 13 million suffering from sleep disturbance
* 900'000 disability-adjusted life years (DALY) lost


::: notes

https://ajuntament.barcelona.cat/mapes-dades-ambientals/soroll/en/

EEA
https://www.eea.europa.eu/themes/human/noise/noise-2

Burden of Disease WHO
http://www.euro.who.int/__data/assets/pdf_file/0008/136466/e94888.pdf

TODO: add picture

:::

## Occupational Noise-induced Hearing Loss

![](./img/Manufacturing-Noise-small.jpeg){width=50%}

The most prevalent occupational disease in the world

* 40 million affected by hearing loss from work
* 4 million disability-adjusted life years (DALY) lost


::: notes

TODO: add picture, person holding

The global burden of occupational noise-induced hearing loss
Nelson, D. I., Nelson, R. Y., Concha-Barrientos, M., & Fingerhut, M. (2005).
DOI 10.1002/ajim.20223

:::

## Noise Monitoring with Machine Learning


![](./img/soundsensing-solution.svg.png){width=100%}

::: notes

EEA
https://www.eea.europa.eu/themes/human/noise/noise-2

Burden of Disease WHO
http://www.euro.who.int/__data/assets/pdf_file/0008/136466/e94888.pdf

:::


## Wireless Audio Sensor Networks

![](img/sensornetworks.png){width=85%}

::: notes


:::


::: notes

Environmental Sound Classification

![](img/urbansound8k-examples.png){width=100%}

Examples from open dataset *Urbansound8k*


* Widely researched. 1000 hits on Google Scholar
* Datasets. **Urbansound8k** (10 classes), ESC-50, AudioSet (632 classes)
* 2017: Human-level performance on ESC-50

Classes from an urban sound taxonomy,
based on noise complains in New York city

Most sounds around 4 seconds. Some classes around 1 second

Foreground/background

https://github.com/karoldvl/ESC-50

:::


## Model Constraints { data-background-image="./img/chip.jpg" }

<!--  <section class="level2" data-background="./img/chip.jpg"> 

<h2 style="">Device constraints</h2>
-->

<p>
Example target: STM32L476 microcontroller.
With 50% of capacity:

* 64 kB RAM</br>
* 512 kB FLASH memory</br>
* 4.5 M operations/second</br>
</p>

<!--  </section> -->


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



## Small models Urbansound8K { data-background-image="" }

![Green: Feasible region on device. 2021 results not published.](img/urbansound8k-existing-models-logmel.png){width=100%}

::: notes

eGRU: running on ARM Cortex-M0 microcontroller, accuracy 61% with **non-standard** evaluation

Assuming no overlap. Most models use very high overlap, 100X higher compute

:::







# Shrinking </br> Convolutional Neural Networks</br> for TinyML Audio

How to did we make the model fit on device?

## Pipeline

![](img/classification-pipeline.png){width=50%}

Typical audio pipeline. Spectrogram conversion, CNN on overlapped windows.

## Reduce input dimensionality

![](img/input-size.svg){width=70%}

- Lower sample rate
- Lower frequency range
- Lower frequency resolution
- Lower time duration in window
- Lower time resolution

~10x reduction i compute. And easier to learn!

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

## Use a small model!

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

## Depthwise-separable Convolution


![](img/depthwise-separable-convolution.png){width=90%}

MobileNet, "Hello Edge", AclNet. 3x3 kernel,64 filters: 7.5x speedup
 
::: notes

* Much fewer operations
* Less expressive - but regularization effect can be beneficial



Spatially-separable Convolution

![](img/spatially-separable-convolution.png){width=90%}

EffNet, LD-CNN. 5x5 kernel: 2.5x speedup

Not as efficient
:::



## Downsampling using max-pooling

![](img/maxpooling.png){width=100%}

Wasteful? Computing convolutions, then throwing away 3/4 of results!

::: notes
TODO: include striding in diagram
:::

## Downsampling using strided convolution

![](img/strided-convolution.png){width=100%}

"Learned" downsampling. Striding 2x2: Approx 4x speedup 

::: notes
TODO: merge into previous slide
:::

## Quantization

![](img/quantization.png){width=80%}

- Using int8 instead of float32.
- 4x improvement in weights (FLASH) and activations (RAM) 
- 4.6X improvement in runtime using CMSIS-NN *SIMD* 

Ref "CMSIS-NN: Efficient Neural Network Kernels for ARM Cortex-M CPUs"

## Latest developments

* Binary network quantization 
* Neural Architecture Search
* Streaming inference
* Learned filterbanks
* Hardware acceleration
* Learned pooling

TinyML very actively researched, rapid improvements

::: notes

Quantized NNs as the definitive solution for inference on low-power ARM MCUs?: work-in-progress
CODES 2018
Q = 1 native instructions can be used, yielding an energy and latency reduction of ~3.8× with respect to CMSIS-NN
https://dl.acm.org/doi/abs/10.5555/3283568.3283580

https://blog.tensorflow.org/2021/02/accelerated-inference-on-arm-microcontrollers-with-tensorflow-lite.html

:::

::: notes

EnvNet-v2 got 78.3% on Urbansound8k with 16 kHz
:::

::: notes

Time-frequency with convolutions

- Preprocessing. Mel-spectrogram: **60** milliseconds
- CNN. Stride-DS-24: **81** milliseconds w/o quantization
- With quantization, spectrogram conversion is the bottleneck!
- Convolutions can be used to learn a Time-Frequency transformation.
- Especially interesting with CNN hardware acceleration.
- Will it be faster without NN hardware?? Not established

:::

# Outro

## Noise Monitoring example

![Automated documentation of noise footprint wrt regulations](./img/noise-monitoring-report.png){width=50%}

* Based on Noise Event Detection & Classification
* Tested successfully at shooting range
* Expanding now to Construction and Industry noise

::: notes

TODO: add pictures of PNB, traffic, construction

:::

## Condition Monitoring example

![](./img/soundsensing-condition-monitoring.svg.png){width=100%}

Condition Monitoring of technical equipment using sound.</br>
Developed based on experience from Noise Monitoring.

## Conclusions

1. Audio classification of Environmental Noise can be done directly on sensor
2. Made possible with a range of efficient CNN techniques
3. Integrated into Soundsensing IoT sensors 
4. Used for Noise Monitoring & Condition Monitoring


## {data-background="./img/soundsensing-withlogo.jpg" style="background: rgba(255, 255, 255, 0.3);"}


We are open for partners and pilot projects</br>
Get in touch!</br>
contact@soundsensing.no</br>
</br>
</br>

<h1>Questions ?</h1>

<em>TinyML Summit 2021: Environmental Sound Classification on microcontrollers</em>

<p>
Jon Nordby
</br>jon&#64;soundsensing.no
</p>


# Bonus

Bonus slides after this point

# Thesis results

## All the info

> Thesis: Environmental Sound Classification
> on Microcontrollers
> using Convolutional Neural Networks

![Report & Code: https://github.com/jonnor/ESC-CNN-microcontroller](./img/thesis.png){width=30%}

## All models

![](img/models-list.png)

::: notes

* Baseline is outside requirements
* Rest fits the theoretical constraints
* Sometimes had to reduce number of base filters to 22 to fit in RAM

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


