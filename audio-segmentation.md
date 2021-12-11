
## Audio Segmentation

## Applications

- Voice Activity Detection / Speech Activity Detection

### Voice Activity Detection

Real-time versus offline.


https://www.sciencedirect.com/science/article/abs/pii/S0885230813000533
NIST
Compares with Statistical Model (SM) based VAD and Gaussian Mixture Model (GMM) based VAD

(1) noise reduction is vital for energy-based VAD under low SNR;
(3) spectral subtraction makes better use of background spectra
than the likelihood-ratio tests in the SM-based VAD

Datasets

Can use any dataset that has marked time regions for speech.
Important is how noisy the datasets are, ie how much non-speech content exists.
Like for example music.

### Implementations

### WebRTC VAD
Code exists inside the Chromium tree, under webrt/modules/audio_processing/vad

A fork has been created that separates out just the VAD as a C library. 
https://github.com/dpirch/libfvad

Available for Python in [py-webrtcvad](https://github.com/wiseman/py-webrtcvad).
Expects int16 input of the audio waveform.
Needs some massaging to work with typical floating point input. TODO, link

The WebRTC VAD model is described in 2.3 of [Voice Activity Detection Scheme by Combining DNN Model with GMM Model](https://arxiv.org/abs/2005.08184).
Is based on a two-mixture Gaussian Mixture Model (noise and speech).
The input features are 6 frequency sub-bands.
Does online updating of the GMM, with different update coefficients for the GMM coefficients,
such that noise would increase slowly, but decrease quickly.
With the assumption that the sound is mostly noise, and occationally speech segments.

Works well at speech vs silence.
But does poorly with music or other noise, will often get flagged as speech.

### inaSpeechSegmenter
CNN-based audio segmentation toolkit.
Primarily for performing gender detection (tuned for French),
but has also a model that distinguishes between music, speech and noise.
Uses a 4 layer CNN per frame.
Per frame predictions are then combined using a Hidden Markov Model.
Has command-line tools for processing a whole batch.

https://github.com/ina-foss/inaSpeechSegmenter


### Opus VAD
The Opus audio codec includes a Voice / Music detector,
which is used in the encoder to switch between speech optimized encoding (SILK)
and music/general encoding (CELT).
In Opus v1.1 it used a multilayer perceptron followed by a Hidden Markov Model.
Since [Opus v1.3](https://jmvalin.ca/opus/opus-1.3/) (October 2018)
it is based on a RNN using Gated Recurrent Units.
The RNN has around 5000 weights, with 8 bit quantization.
This network has two outputs, one for Voice and one for Music.
So a low output on both

The [opus_sm](https://github.com/jzombi/opus_sm) fork has a commandline tool of the old Opus 1.1
sound/music detector.
No-one has described how to us the Opus 1.3 detector in another application?
One [question](http://lists.xiph.org/pipermail/opus/2019-September/004386.html) on mailing list.

### Microcontroller device models

[Voice activity detection for low-resource settings](http://cs230.stanford.edu/projects_winter_2020/reports/32224732.pdf). Abhipray Sahoo, Stanford CS230.
Used a 3 layer RNN on log mel spectrogram with 40 bands, and using 32 ms windows.
Trained and evaluated on a dataset made by combining VCTK with Noisex-92.
Large improvements against WebRTC VAD under noisy conditions.


[Voice Activity Detector (VAD) Based on Long-Term Mel Frequency Band Features](https://link.springer.com/chapter/10.1007/978-3-319-45510-5_40).
VAD using long-term 200 ms Mel frequency band statistics, auditory masking, and a pre-trained two level decision tree ensemble based classifier.
Near 100 % acceptance of clear voice for English, Chinese, Russian, and Polish speech and 100 % rejection of stationary noises independently of loudness.
Reuses short-term FFT analysis (STFFT) from ASR frontend with additional 2 KB memory and 15 % complexity overhead.

### Speaker dependent models

[Personal VAD: Speaker-Conditioned Voice Activity Detection](https://arxiv.org/abs/1908.04284)
Personal VAD outputs the probabilities for three classes: non-speech, target speaker speech, and non-target speaker speech.
Combined with Speaker Verification System.
No online / real-time adaptation to speakers.
Seems to need to be pre-trained for a particular speaker.

## Non-open
### Silero VAD
https://github.com/snakers4/silero-vad

Released as pretrained PyTorch models.
Training setup not released.
Train/test dataset not released.
Does not specify which PyTorch versions to use.
Not installable as a pip library.
Latest models ("big") not publically available.
Has some nice examples of real-time.


### Approaches

### Segmentation and classification
Aka distance-based-segmentation.

First segmentation, then classification.

Distance metrics

- Euclidean distance
- Bayesian information criterion (BIC)
- Gaussian likelihood ratio (GLR)
- Kullback Leibler KL2 distance
- Hotelling T2 statistic
- cosine distance (with self-similarity analysis)
- Learned distances (using neural networks)


- Hidden Markov Model (HMM)


### Segmentation by classification

Segmentation performed by classifying consecutive fixed-length segments. 

### Resegmentation
Common with both kind of approaches.
Can be done with HMM.
Or heuristics such as removing segments below certain length.



### Datasets

- Albayzín 2010
- Albayzín 2012
- MIREX 2018

### Misc

MaxEnt / Maximum Entropy Classifier.
Same as Logistic Regressions.
Or conditional exponential classifier

### References

https://www.programmersought.com/article/81806889517/

How to use HMM model for audio segmentation
https://stackoverflow.com/questions/66817625/how-to-use-hmm-model-for-audio-segmentation
No answers

https://hal.archives-ouvertes.fr/hal-00957418/document
HMM has a fixed structure, decomposing into silent,transient,tonal,residual


Joint Segmentation and Classification
https://www.sciencedirect.com/book/9780080993881/introduction-to-audio-analysis
https://www.sciencedirect.com/topics/engineering/audio-segmentation
Dynamic programming, Viterbi

An Overview of Automatic Audio Segmentation
October 2014
https://www.researchgate.net/publication/287718330_An_Overview_of_Automatic_Audio_Segmentation

Optimized Audio Classification and Segmentation Algorithm by Using Ensemble Methods
https://www.hindawi.com/journals/mpe/2015/209814/
2015

https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-020-00172-6
EURASIP
2020
RNN is complemented by a resegmentation module,
gaining long term stability by means of the tied state concept in hidden Markov models
Explore different neural architectures introducing temporal pooling layers to reduce the neural network output sampling rate

Improving automated segmentation of radio shows with audio embeddings
https://arxiv.org/abs/2002.05194
ICASSP
2020




