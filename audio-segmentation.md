
# Audio Segmentation

## Applications

- Voice Activity Detection / Speech Activity Detection
- Dataset curation
Starting point for labeling. For Sound Event Detection etc
- Pre-filter for SED/classification model
High recall. Low precision 

## Introduction material

Problem definition

- Binary vs one-class vs multi-class vs multi-track segmentation
- How do we know how well we are doing? Evaluation and metrics. sed_eval
- Simple usecases. Sound present vs not present. Events, voice
- From continious time-series to discrete segments

Baselines approaches

- Using a simple threshold
- Using threshold with hysteresis
- Setting threshold values. Manual, heuristics, learned
- Selecting time-periods

A slightly better version

- Stateful model with learned thresholds
Gaussian Hidden Markov Model
- Pre- and post-processing steps.
Removal of too short segments.
- Simple feature representations and transformations.
RMS, ZCR. dB transformation. Frequency-weigting
- Ensembling of models using time-shifting.
Test-time data augmentation

Doing better on speech. Voice Activity Detection
- Voice energy bands
- Learned speech models

Alternative approaches

- Segmentation using distance functions
- Segmentation using labeled examples. KNN for few-shot learning

Useful tools

- Extract individual segments, as separate files.
- Extract single class, into continious file


Note. Approaches are highly relevant to segmentation of other time-series
such as accelerometer data, EEG data etc.


## Commandline API

How it could look for a hypothetical command-line tool

python -m audiosegment.analyze

    --in folder/*.wav | .mp3 | .ogg | .flac | .m4a

    --out segments.csv

    --classes silence,other
    --classes speech,other
    --classes speech,silence,music,other

    --hop 0.1
    --min-duration silence=0.1,other=1.0
    --max-duration 10.0

    --proportions silence=0.9

    --examples speech=sometext.wav

segments.csv
path,class,start,end


python -m audiosegment.cut

    --in segments.csv

    --out audio/{file}_{class}_{segment}.wav
    --out audio/

    --mode split
    --mode concatenate

    --classes x,y,z

    --pad-start 0.1
    --pad-end 0.1


### Approaches

### Segmentation using distances

Divide into time windows. Compare consecutive time windows using a distance function.
Often done with divisive clustering.
Binary subdivision of non-overlapping consecutive windows in order to maximize distance function.
Ends when the windows have reached a minimum length.
Can be seen as a large number of potential cut-points.

Distance metrics

- Euclidean distance
- Bayesian information criterion (BIC)
- Gaussian likelihood ratio (GLR)
- Kullback Leibler KL2 distance
- Hotelling T2 statistic
- cosine distance (with self-similarity analysis)
- Learned distances (using neural networks)


### Segmentation by classification

Segmentation performed by classifying consecutive fixed-length segments. 

### Resegmentation
Common with both kind of approaches.
Can be done with HMM.
Or heuristics such as removing segments below certain length.

Agglomarotive clustering can be used, considers merging consecutive clusters if similar enough.


### Datasets

- Albayzín 2010
- Albayzín 2012
- MIREX 2018

### Misc

MaxEnt / Maximum Entropy Classifier.
Same as Logistic Regressions.
Or conditional exponential classifier

### Answers needed

How to use HMM model for audio segmentation
https://stackoverflow.com/questions/66817625/how-to-use-hmm-model-for-audio-segmentation
No answers

https://thesoundofai.slack.com/archives/C012B5736N5/p1646151141304619


https://opendata.stackexchange.com/questions/9080/open-audio-segmentation-datasets
looking for speech/music audio segmentation datasets

Few good answers
https://dsp.stackexchange.com/questions/9980/speech-segmentation-for-speaker-recognition
https://dsp.stackexchange.com/questions/508/how-to-segment-phone-call-audio-into-silence-non-silence

### Forced alignment

Segmenting audio and aligning it with text
https://github.com/readbeyond/aeneas
https://github.com/lowerquality/gentle
Is/was commonly used to make speech datasets with word-level text annotations.

### Speech Segmentation

BIC-based speech dialogue segmentation 
https://www.programmersought.com/article/81806889517/

https://dsp.stackexchange.com/questions/9980/speech-segmentation-for-speaker-recognition
Adaptive Thresholding is the most common way to segment audio.
While there are more accurate methods out there for segmenting,
adaptive thresholding is fast and very accurate, and uses simple features such as zero-crossings, energy, and entropy.
Same principle as is used in computer vision.

Adaptive threshold method for real-time audio segmentation
December 2005
https://ieeexplore.ieee.org/abstract/document/1415134/

Automatic speech segmentation using average level crossing rate information
https://www.researchgate.net/publication/286073350_Adaptive_threshold_method_for_real-time_audio_segmentation
2015

Speech segmentation without speech recognition
https://ieeexplore.ieee.org/abstract/document/1198819/
2015

A robust algorithm for accurate endpointing of speech signals
MH Savoji
1989
https://www.sciencedirect.com/science/article/pii/0167639389900678


### References

Software
https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation
Shows unsupervised and supervised segmentation
As well as Speaker Diarization, and Audio thumbnailing

https://github.com/amsehili/auditok/
An audio/acoustic activity detection and audio segmentation tool
Uses energy as feature, and requires specifying a dB threshold manually


https://hal.archives-ouvertes.fr/hal-00957418/document
HMM has a fixed structure, decomposing into silent,transient,tonal,residual

Joint Segmentation and Classification
https://www.sciencedirect.com/book/9780080993881/introduction-to-audio-analysis
https://www.sciencedirect.com/topics/engineering/audio-segmentation
Dynamic programming, Viterbi

An Overview of Automatic Audio Segmentation
October 2014
https://www.researchgate.net/publication/287718330_An_Overview_of_Automatic_Audio_Segmentation
Reviews about 15 articles, listing 10 different datasets.

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

Audio segmentation-by-classification approach based on factor analysis in broadcast news domain
https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-014-0034-5
2014
Segmentation-by-classification approach based on factor analysis.
The proposed technique compensates the within-class variability by using class-dependent factor
loading matrices and obtains the scores by computing the log-likelihood ratio for the class model to a non-class model over fixed-length windows.
Segment and classify audios coming from TV shows into five different acoustic classes: speech, music, speech with music, speech with noise, and others


BIC-based audio segmentation by divide-and-conquer
https://www.researchgate.net/publication/224762256_BIC-based_audio_segmentation_by_divide-and-conquer
2008
Among existing audio segmentation approaches, the BIC-based approach proposed by Chen and Gopalakrishnan is most well-known for its high accuracy. However, this window-growing-based segmentation approach suffers from the high computation cost.
In this paper, we propose using the efficient divide-and-conquer strategy in audio segmentation.

Multiclass audio segmentation based on recurrent neural networks for broadcast domain data
https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-020-00172-6
2020
Using bidirectional long short-term Memory (BLSTM).
RNN is complemented by a resegmentation module, gaining long term stability by means of the tied state concept in hidden Markov models.

Deep Convolutional Neural Networks for Heart Sound Segmentation
https://ieeexplore.ieee.org/document/8620278

Different temporal modeling schemes are applied to the output of the proposed neural network,
which induce the output state sequence to be consistent with the natural sequence of states within a heart sound signal
(S1, systole, S2, diastole).
In particular, convolutional neural networks are used in conjunction with underlying hidden Markov models and hidden semi-Markov models to infer emission distributions. The proposed approaches are tested on heart sound signals from the publicly available PhysioNet dataset, and they are shown to outperform current state-of-the-art segmentation methods by achieving an average sensitivity of 93.9% and an average positive predictive value of 94% in detecting S1 and S2 sounds.


