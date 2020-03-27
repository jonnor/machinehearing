# Machine Hearing

## Classifying sound using Machine Learning

<a href="https://www.youtube.com/watch?v=1H63PewtDbo">
<img src="https://github.com/jonnor/machinehearing/raw/master/knowit2020/video.png" height="200" alt="Youtube: Audio Classification using Machine Learning by Jon Nordby, EuroPython 2019">
</a>

At KnowIt Oslo, 2020. [Video recording](https://www.youtube.com/watch?v=1H63PewtDbo), [slides](https://jonnor.github.io/machinehearing/knowit2020/slides.html), [notes](./knowit2020)

## Environmental Sound Classification on Microcontrollers using Convolutional Neural Networks

<a href="https://github.com/jonnor/ESC-CNN-microcontroller">
<img src="https://github.com/jonnor/ESC-CNN-microcontroller/raw/master/report/img/frontpage.png" height="200" alt="Github: jonnor/ESC-CNN-microcontroller">
</a>

Master thesis. Report and code available in the [Github repository](https://github.com/jonnor/ESC-CNN-microcontroller).

## EuroPython2019: Audio Classification using Machine Learning

<a href="https://www.youtube.com/watch?v=uCGROOUO_wY">
<img src="https://github.com/jonnor/machinehearing/raw/master/europython2019/video.png" height="200" alt="Youtube: Audio Classification using Machine Learning by Jon Nordby, EuroPython 2019">
</a>

Presentation at EuroPython2019. [Video recording](https://www.youtube.com/watch?v=uCGROOUO_wY), [notes](./europython2019)

## PyCode2019: Recognizing sounds with Machine Learning and Python

<a href="https://jonnor.github.io/machinehearing/pycode2019/slides.html">
<img src="https://github.com/jonnor/machinehearing/raw/master/pycode2019/slides.png" height="200" alt="Slides">
</a>

<!--
<a href="https://youtu.be/2FmMESSD2CM?t=8470">
<img src="https://github.com/jonnor/machinehearing/raw/master/europython2019/video.png" height="200" alt="Youtube: Audio Classification using Machine Learning by Jon Nordby, EuroPython 2019">
</a>
-->

Presentation at PyCode Conference 2019 in Gdansk.
[Slides](https://jonnor.github.io/machinehearing/pycode2019/slides.html),
[notes](./pycode2019)

Video recording. Coming, maybe in November.

## SenseCamp2019: Classification of Environmental Sound using IoT sensors

<a href="https://jonnor.github.io/machinehearing/sensecamp2019/slides.html">
<img src="https://github.com/jonnor/machinehearing/raw/master/sensecamp2019/slides.png" height="200" alt="Slides">
</a>

Presentation at SenseCamp 2019 hosted by FORCE Technology Senselab.
Slides: [web](https://jonnor.github.io/machinehearing/sensecamp2019/slides.html),
[.PDF](https://github.com/jonnor/machinehearing/raw/master/sensecamp2019/slides.pdf)


## NMBU lecture on Audio Classification

Report and lecture at [NMBU](https://nmbu.no) Data Science.

[Report](https://github.com/jonnor/datascience-master/raw/master/dat390/merged.pdf) |
[Slides](https://jonnor.github.io/datascience-master/dat390/slides.html)


## Stack Overflow answers

With example code in Python

* [Loading Youtube audio data with youtube-dl and librosa](https://stackoverflow.com/a/57832701/1967571)
* [Extracting fixed-size analysis windows from audio](https://stackoverflow.com/a/54326750/1967571)
* [Classifying an audio clip of many analysis windows using Keras Timedistributed and GlobalAveragePooling](https://stackoverflow.com/a/55286629/1967571)
* [Classifying an audio clip by voting over analysis windows](https://stackoverflow.com/a/55267520/1967571). Mean/majority voting.
* [Annotating/labeling audio data using Audacity](https://datascience.stackexchange.com/a/56372/54096)
* [Preprocessing audio into mel-spectrograms](https://stats.stackexchange.com/a/403051/201327)
* [Multi-core preprocessing of audio files using joblib](https://stackoverflow.com/a/55680757/1967571)
* [Compute MFCC or mel-spectrogram from existing STFT spectrograms](https://stackoverflow.com/a/57833078/1967571)
* [Converting mel-spectrograms into PNG images](https://stackoverflow.com/a/57204349/1967571)
* [Converting mel-spectrogram or MFCC back to audio waveform using librosa](https://stackoverflow.com/a/57323359/1967571)

<!--
https://stackoverflow.com/questions/57443870/stream-binary-audio-data-from-http-request-for-librosa-analysis/57672134#57672134

Streaming audio from HTTP to for audio classification. Supports real-time streaming

Chunk download audio from Youtube.
Benefit: Can classify in parallel.
Can get a particular location in time

https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command

-->

## Notes

Rough notes on various topics.

* [Applications](./applications.md). Practical applications of Machine Hearing
* [Tasks](./tasks.md). Established problem formulations
* [Audio Quality](./audio-quality.md). Metrics for measuring audio quality
* [Features](./features.md). Feature representations
* [Preprocessing](./preprocessing.md). Preprocessing techniques
* [DCASE2018](./dcase2018.md). Notes from DCASE2018 challenge and conference
* [Commercial solutions](./commercial.md). Companies and products in Machine Hearing
* [Speech](./speech.md). Speech-specific techniques and applications
* [Music](./music.md). Music-specific techniques and applications
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


## Software

Feature extraction

* [librosa](http://librosa.github.io). The go-to Python module.
* [essentia](https://essentia.upf.edu). C++ library, with Python bindings. Lots of Music Analysis extractors. Used by FreeSound and Acousticbrainz.
* [kapre](https://github.com/keunwoochoi/kapre). On-demand GPU computation of melspectrograms, for Keras
* [torchaudio](). 

Data Augmentation

* [muda: Python library for augmenting annotated audio data](https://github.com/bmcfee/muda)

# Lecture notes

* Audio Classification.
http://www.cs.tut.fi/~sgn24006/PDF/L04-audio-classification.pdf
Covers low-level features, MFCC. Classification by distance metrics. GMM. HMM.
* [Speech Signal Analysis, Lecture 2](https://www.inf.ed.ac.uk/teaching/courses/asr/2016-17/asr02-signal-handout.pdf).
January 2017, Hiroshi Shimodaira and Steve Renals.
! great diagrams of audio discretization, mel filters, wide versus narrow-band spectrograms.

## Competions

* Kaggle Whale detection
* Kaggle FreeSound tagging 2018
* Kaggle FreeSound
* DCASE2014
* DCASE2018
* DCASE2019 

## Datasets

* [Audio cats and dogs (Kaggle)](https://www.kaggle.com/mmoreaux/audio-cats-and-dogs)
* [Heartbeat anomalies (Kaggle)](https://www.kaggle.com/kinguistics/heartbeat-sounds).
* [Respiratory sounds (Kaggle)](https://www.kaggle.com/vbookshelf/respiratory-sound-database)

## Online Communities

* https://mircommunity.slack.com/ - Music Information Retrieval

### Lists

* [Awesome Deep Learning Music](https://github.com/ybayle/awesome-deep-learning-music)
* [Fast.ai forums: Deep Learning with Audio](https://forums.fast.ai/t/deep-learning-with-audio-thread/38123).
Large lists of resources, both in first post and "popular links". Feb 2019, 315 replies over 4 months.




