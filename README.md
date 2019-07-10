# Machine Hearing

## Environmental Sound Classification on Microcontrollers using Convolutional Neural Networks

<a href="https://github.com/jonnor/ESC-CNN-microcontroller">
<img src="https://github.com/jonnor/ESC-CNN-microcontroller/raw/master/report/img/frontpage.png" height="200" alt="Github: jonnor/ESC-CNN-microcontroller">
</a>

Master thesis. Report and code available in the [Github repository](https://github.com/jonnor/ESC-CNN-microcontroller).

## EuroPython2019: Audio Classification using Machine Learning

<!-- FIXME: link properly to slides and notes -->

<a href="https://github.com/jonnor/machinehearing/tree/master/europython2019">
<img src="https://github.com/jonnor/machinehearing/raw/master/europython2019/slides.png" height="200" alt="Github: jonnor/ESC-CNN-microcontroller">
</a>

Presentation at EuroPython2019. [Notes](./europython2019)

## Notes

Rough notes on various topics.

* [Applications](./applications.md). Practical applications of Machine Hearing
* [Tasks](./tasks.md). Established problem formulations
* [Features](./features.md). Feature representations
* [Preprocessing](./preprocessing.md). Preprocessing techniques
* [DCASE2018](./dcase2018.md). Notes from DCASE2018 challenge and conference
* [Commercial solutions](./commercial.md). Companies and products in Machine Hearing
* [Compressive Sensing](./compressive-sensing.md).

## Resources

Useful resources to learn more.


### Books

* Computational Analysis of Sound Scenes and Events. Tuomas Virtanen, Mark D. Plumbley, Dan Ellis. 2018.
* Human and Machine Hearing - Extracting Meaning from Sound. Richard F. Lyon. 2017, revised 2018.
* An Introduction to Audio Content Analysis - Applications in Signal Processing and Music Informatics. Alexander Lerch. 2012.
Companion website: https://www.audiocontentanalysis.org/
* Machine Learning for Audio, Image and Video Analysis: Theory and Applications (Advanced Information and Knowledge Processing). Francesco Camastra, 
3 sections. From Perception to Computation, Machine Learning, Applications.

### Online courses

* CSC 83060: Speech and Audio Understanding. http://mr-pc.org/t/csc83060/
Brooklyn College (CUNY).

### Phd thesis

*  Real-time Speech and Music Classification by Large Audio Feature Space Extraction.
Describes OpenSMILE. Florian Eyben. 2016.
https://www.amazon.com/Real-time-Classification-Feature-Extraction-Springer/dp/3319272985

### Lists

* https://github.com/ybayle/awesome-deep-learning-music
* [Fast.ai forums: Deep Learning with Audio](https://forums.fast.ai/t/deep-learning-with-audio-thread/38123).
Large lists of resources, both in first post and "popular links". Feb 2019, 315 replies over 4 months.



## Software

Feature extraction

* [librosa](http://librosa.github.io). The go-to Python module.
* essentia. C++ library. Lots of Music Analysis extractors. Used by FreeSound.
* [kapre](https://github.com/keunwoochoi/kapre). On-demand GPU computation of melspectrograms, for Keras

Data Augmentation

* [muda: Python library for augmenting annotated audio data](https://github.com/bmcfee/muda)

# Lecture notes

Audio Classification.
http://www.cs.tut.fi/~sgn24006/PDF/L04-audio-classification.pdf
Covers low-level features, MFCC. Classification by distance metrics. GMM. HMM.

[Speech Signal Analysis, Lecture 2](https://www.inf.ed.ac.uk/teaching/courses/asr/2016-17/asr02-signal-handout.pdf).
January 2017, Hiroshi Shimodaira and Steve Renals.
! great diagrams of audio discretization, mel filters, wide versus narrow-band spectrograms.


## Online Communities

* https://mircommunity.slack.com/ - Music Information Retrieval

## Competions

* Kaggle Whale detection
* Kaggle FreeSound tagging 2018
* Kaggle FreeSound
* DCASE2014
* DCASE2018
* DCASE2019 


