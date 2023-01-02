
## Application ideas

Fun stuffs

* Detect clapping and its sound level in a conference

## [Machine Hearing](https://github.com/jonnor/machine-hearing)

General info

* Blog: http://www.machinehearing.org/
Book: Human and Machine Hearing: Extracting Meaning from Sound
[Paper in IEEE, 2010](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36608.pdf)
Key ideas. Modelling human hearing. Reusing machine vision learnings by representing sound as (moving) images.
Combined audiovisual models.
* [What’s wrong with CNNs and spectrograms for audio processing?](https://towardsdatascience.com/whats-wrong-with-spectrograms-and-cnns-for-audio-processing-311377d7ccd). Challenges:
Sounds intermix/blend into eachother, ie are "transparent".
Can also have complex relationships like phase cancellation.
Directions in spectogram have different meansings. Frequency,time. Features not invariant wrt to frequency, but generally wrt time.
Activations in the spectrogram are non-local, eg formants.
Sound information is serial 'events', observed only in one instance of time. Not visual stationary 'objects'.
If freezing time, cannot understand much of the information present (compared with video).
Temporal patterns are critical.


## Keyword spotting
Aka "wake word detection"

Existing work on microcontrollers

* [ML-KWS-for-MCU](https://github.com/ARM-software/ML-KWS-for-MCU/tree/master/Deployment).
Speech recognition on microcontroller.
Neural network trained with TensorFlow, then deployed on Cortex-M7, with FPU.
Using CMSIS NN and DSP modules.
* [CASE2012](http://elaf1.fi.mdp.edu.ar/electronica/grupos/lac/pdf/lizondo_CASE2012.pdf).
Implemented speech recognition using MFCC on 16-bit dsPIC with 40 MIPS and 16kB RAM.
A Cortex-M3 at 80 MHz should have 100+MIPS.
* [An Optimized Recurrent Unit for Ultra-Low-Power Keyword Spotting](https://arxiv.org/abs/1902.05026). February 2019.
Introduces `eGRU`, claimed to be 60x faster and 10x smaller than standard GRU cell.
Omits the `reset` gate (and assosicaed weights W_r).
Uses `softsign` instead of sigmoid and tanh. Faster, less prone to saturation.
Uses fixed-point integer operations only. Q15, bitshifts for divide/mul.
3-bit exponential weight quantization. -1,-0.5,-0.25,0,0.25,0.5,1.0. Bitwise operations, no lookup table.
Uses a quantization-aware training. Quantized in forward pass, full precision in backward (for gradient).
Evaluated on Keyword Spotting, Cough Detection and Environmental Sound Classification.
Sampling rate 8kHz. 128 samples STFT window, no overlap. 64 bands. No mel filtering!
250 timesteps for Urbansound8k.
eGRU_opt Urbansound8k scores 61.2%. 3kB model size.
eGRU_arc Urbansound8k score of 72%. Indicates 8kHz enough!

* [How to Achieve High-Accuracy Keyword Spotting on Cortex-M Processors](https://community.arm.com/processors/b/blog/posts/high-accuracy-keyword-spotting-on-cortex-m-processors).
Reviews many deep learning approaches. DNN, CNN, RNN, CRNN, DS-CNN.
Considering 3 different sizes of networks, bound by NN memory limit and ops/second limits. Small= 80KB, 6M ops/inference.
Depthwise Separable Convolutional Neural Network (DS-CNN) provides the best accuracy while requiring significantly lower memory and compute resources.
94.5% accuracy for small network. ARM Cortex M7 (STM32F746G-DISCO).
8-bit weights and 8-bit activations, with KWS running at 10 inferences per second.
Each inference – including memory copying, MFCC feature extraction and DNN execution – takes about 12 ms.
10x inferences/second. Rest sleeping = 12% duty cycle.
* [QuickLogic partners with Nordic Semiconductor for its Amazon Alexa-compatible wearables reference design using Voice-over-Bluetooth Low Energy](https://www.nordicsemi.com/News/News-releases/Product-Related-News/QuickLogic-partners-with-Nordic-Semiconductor-for-its-Amazon-Alexa-compatible-wearables-reference-design-using-Voice-over-Bluetooth-Low-Energy). 2017/11
Always-on wake word detection at 640uWatt typical.
nRF51822 with **external MCU**. EOS S3 SoC’s (Cortex M4F) hardware integrated Low Power Sound Detector.
* [Convolutional Recurrent Neural Networks for Small-Footprint Keyword Spotting](https://arxiv.org/abs/1703.05390).
Uses Per-Channel Energy Normalization on mel spectograms. CRNN with ~230k parameters, acceptably low latency on mobile devices.
Achieves 97.71% accuracy at 0.5 FA/hour for 5 dB signal-to-noise ratio. Down to 45k parameters tested.




General

* [Audio classification overview](http://www.nyu.edu/classes/bello/ACA_files/8-classification.pdf)
Criterias for good features,
PCA/LDA for dimensionality reduction. Sequential forward/backward selection
* [Environmental sound recognition: a survey](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S2048770314000122) (2014).
Mentiones MPEG-7 based features, efficient and perceptual.
* [Dolph-Chebyshev Window](http://practicalcryptography.com/miscellaneous/machine-learning/implementing-dolph-chebyshev-window/),
good window function for audio. C reference implementation.
* [Voice Activity Detection, tutorial](http://practicalcryptography.com/miscellaneous/machine-learning/voice-activity-detection-vad-tutorial/)
Using 5 simple features.
* [Machine Learning for Audio, Image and Video Analysis](http://www.dcs.gla.ac.uk/~vincia/textbook.pdf).
* [Notes on Music Information Retrieval](https://musicinformationretrieval.com/index.html), series of Jupyter notebooks.
Lots of goodies, from feature extraction to high-level algorithms.
* [Detection and Classification of Acoustic Scenes and Events](https://hal.archives-ouvertes.fr/hal-01123760/document). 2014
Review of state of the art in machine listening.
Problem 1: Acoustic scene classification,
Characterize acoustic environment of an audio stream by selecting a semantic label for it.
Single-label classification. Similar to: Music genre recognition. Speaker recognition.
Also similar to other time-based classification, ie in video.
Approach 1. Bag of frames. Long-term statistical distribution of local spectral features. Ex MFCC.
Compare feature distributions using GMM.
Approach 2. Intermediate representation using higher level vocabulary/dictionary of "acoustic atoms".
Problem 2. Acoustic event detection. Label temporal regions within an audio recording; start time, end time and label for each event instance.
Related to. Automatic music transcription. Speaker diarisation.
Typically treated as monophonic problem, but polyphonic is desirable.
More challening that scene classification.
One strategy to handle polyphonic signals is to perform audio source separation, and then to analyse the resulting signals individually.

Efficiency

* [A multi-layered energy consumption model for smart wireless acoustic sensor networks](https://arxiv.org/abs/1812.06672). Gert Dekkers, 2018.
MATLAB code: https://github.com/gertdekkers/WASN_EM



## Acoustic event detection (AED)

Aka

- Sound Event Detection
- Automatic Environmental Sound Recognition (AESR)


* Competitions: CLEAR "Classification of Events, Activities and Relation-
ships". DCASE Detection and Classification of Acoustic Scenes and Events (2016,2013)
[website](http://www.cs.tut.fi/~heittolt/research-sound-event-detection) shown progress on same dataset up to modern methods with f1-score=69.3%
using Convolutional Recurrent Neural Networks. Dataset TUT-SED2009 TUT-CASA2009
* [https://ieeexplore.ieee.org/document/7933055/](Bag-of-Features Methods for Acoustic Event Detection and Classification). Grzeszick, 2014/2017.
Features are calculated for all frames in a given time window.
Then, applying the bag-of-features concept, these features are quantized with respect to a learned codebook and a histogram representation is computed.
Bag-of-features approaches are particularly interesting for online processing as they have a low computational cost.
Using GCFF Gammatone frequency cepstral coefficients, in addition to MFCC.
Codebook quantizations used: soft quantization, supervised codebook learning, and temporal modeling.
Using DCASE 2013 office live dataset and the ITC-IRST multichannel.
BoF principle: Learn intermediate representation of features in unsupervised manner. Clustering like k-means
Hard-quantization: All N*K feature vectors are clustered. Only cluster centroids are of interest. Assign based on minimum distance.
Soft-quantization: GMM with expectation maximation. Codebook has mean,variance.
Supervized-quantization. GMM per class, concatenated.
Re-introducing temporality. Pyramid scheme, feature augumentation by adding quantizied time coordinate.
SVM classification. Multiclass. Linear, RBF. *Histogram-intersection kernel* works well.
Random Forests. Works well for AED. Frame size = 1024samples@44.1kZ=22.3 ms
The current python implementation uses a single core on a standard desktop machine and requires less than 20% of the real time for computation.

* [Bird Audio Detection using probability sequence kernels](http://machine-listening.eecs.qmul.ac.uk/wp-content/uploads/sites/26/2017/02/badChallenge_iitMandi.pdf)
Judges award DCASE2016 for most computationally efficient.
MFCC features (voicebox), GMM, SVM classifier from libsvm with probability sequence kernel (PSK).
AUC of 73% without short-term Gaussianization to adapt to dataset differences.

* LEARNING FILTER BANKS USING DEEP LEARNING FOR ACOUSTIC SIGNALS. Shuhui Qu.
Based on the procedure of log Mel-filter banks, we design a filter bank learning layer.
Urbansound8K dataset, the experience guided learning leads to a 2% accuracy improvement.

* [Automatic Environmental Sound Recognition: Performance Versus Computational Cost](https://ieeexplore.ieee.org/abstract/document/7515194/). 2016. Sigtia,...,Mark D. Plumbley
Results suggest that Deep Neural Networks yield the best ratio of sound classification accuracy across a range of computational costs,
while Gaussian Mixture Models offer a reasonable accuracy at a consistently small cost,
and Support Vector Machines stand between both in terms of compromise between accuracy and computational cost.
! No Convolutional Neural networks. ! used MFCC instead of mel-spectrogram

* [EFFICIENT CONVOLUTIONAL NEURAL NETWORK FOR AUDIO EVENT DETECTION](https://www.researchgate.net/publication/320098222_Efficient_Convolutional_Neural_Network_For_Audio_Event_Detection). Meyer, 2017.
structural optimizations. reduce the memory requirement by a factor 500,
and the computational effort by a factor of 2.1 while performing 9.2 % better.
Final weights are 904 kB. Which fits in progmem, but not in RAM on a ARM Cortex M7.
Needs 75% of theoritical performance wrt MACs, which is likely not relalizable.
They suggest use of a dedicated accelerator chip.

* [Robust Audio Event Recognition with 1-Max Pooling Convolutional Neural Networks](https://arxiv.org/pdf/1604.06338.pdf).
! Very shallow network performs similar to state-of-the art in event detection on very noisy datasets.
Convolution (3..25 wide x 52 tall) -> MaxPool per frame -> Softmax across frames.
Claims to also outperform with a single filter width setting.
Also uses window averaging to downsample spectrogram bins to 52 bins instead of typical triangular mel.
This arcitecture should be suitable also for Acoustic Scene Classification?

* [Baby Cry Sound Detection: A Comparison of Hand Crafted Features and Deep Learning Approach](https://link.springer.com/chapter/10.1007/978-3-319-65172-9_15). 2017
Shows that hand-crafted features can give same performance as state-of-art CNN at 20x the computational cost.
Features: Voiced unvoiced counter (VUVC), Consecutive F_0 (CF0), Harmonic ratio accumulation (HRA).
Classifier: Support Vector Data Description (SVDD).
"Further research should investigate ways of reducing complexity of CNN, by decreasing the number of filters and their size"
Dataset was constructed from http://www.audiomicro.com and https://www.freesound.org
Approx 1 hour cry, 1 hour non-cry for training.
! Testing set has only 26 baby cry events (15 min) as base. Upsampled by mixing in noise at 18dB.
Makes 4h of sound with sparse amounts of target event, and 2 hours without.

* [SwishNet: A Fast Convolutional Neural Network for Speech, Music and Noise Classification and Segmentation]()
1D Convolutional Neural Network (CNN). Operates on MFCC, 20 band.
Uses combinations of 1x3 and 1x6 convolutions. Only convolutions across temporal bands.
? Gated activations between each step.
? skip connections with Add.
Architecture inspired by Inception and WaveNet architecture.
Optionally use distilled knowledge from MobileNet trained on ImageNet.
Tested on MUSAN, GTZAN.
! used background noise removal
5k and 18k parameters. Versus 220k for MobileNet.
1ms prediction time for 1 second window on desktop CPU.
! simple problems, GMM baseline performed 96-99% and 90%,
MobileNet Random initialized 98-00% and 94-96%

* Kaggle: The Marinexplore and Cornell University Whale Detection Challenge
[Features & classification approaches](https://www.kaggle.com/c/whale-detection-challenge/discussion/4156).
Many approached used with good results.
Large range in feature sets. Mostly deep learning and tree ensembles, some SVM.
Winner used image template on spectograms with a GradientBoostingClassifier.



## Environmental sound monitoring
Aka

- Environmental Noise Monitoring
- Noise source identification

Datasets

* [Urbansound-8k](https://serv.cusp.nyu.edu/projects/urbansounddataset/urbansound8k.html).
8k samples, 10 classes. Compiled from freesound.org data
* [ESC-50: Dataset for Environmental Sound Classification](https://github.com/karoldvl/ESC-50).
2k samples, 40 classes in 5 major categories. Compiled from freesound.org data
* DCASE 2013. Audio Event Detection. Indoor office sounds. 16 classes. Segmented. 19 minutes total.
* [Google AudioSet](https://research.google.com/audioset/). 2,084,320 human-labeled 10-second sounds, 632 audio event classes. 

Papers

* [Acoustic Event Detection Using Machine Learning: Identifying Train Events](http://cs229.stanford.edu/proj2012/McKennaMcLaren-AcousticEventDetectionUsingMachineLearningIdentifyingTrainEvents.pdf). Shannon Mckenna,David Mclare.
Using RMS over 0.125 seconds and 1/3 octave frequency bands. Classify individual time instances as train-event,
then require a cluster of 3 train events successive. 
"Performance of our classifier was significantly increased when we normalized the noise levels by
subtracting out the mean noise level of each 1/3 octave band and dividing by the standard deviation"
Used Logistic Regression and SVM. From 0.6 to 0.9 true positive rate (depending on site), with `<0.05` false positive rate.
Tested across 10 sites.

* [Detection of Anomalous Noise Events on Low-Capacity Acoustic Nodes
for Dynamic Road Traffic Noise Mapping within an Hybrid WASN](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5948866/)

## Speech commands

Datasets

* [Speech Commands Data Set](https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data).
Kaggle competition required submissions to run in below 200ms on a Raspberry PI3.
* [NOIZEUS: A noisy speech corpus for evaluation of speech enhancement algorithms](http://ecs.utdallas.edu/loizou/speech/noizeus/)
30 sentences corrupted by 8 real-world noises. 
* Mozilla [Common Voice](https://voice.mozilla.org), crowd sourcing. Compiled dataset [on Kaggle](https://www.kaggle.com/mozillaorg/common-voice), 


## Speaker detection

* [VoxCeleb](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/), 100k utterances for 1251 celebrities.
* [Speakers in the Wild](https://www.sri.com/work/publications/speakers-wild-sitw-speaker-recognition-database)

## Bird audio detection


* DCASE 2018. Audio Event Detection, single-class: bird-present. 6 datasets of some k samples each.
* [BirdCLEF 2016](http://www.imageclef.org/lifeclef/2016/bird). 24k audio clips of 999 birds species


## Research questions

* How can one perform environmental monitoring tasks on audio without invading privacy?
Issues: capturing conversations, identifying/tracking speakers.
Possible mitigations.
Use very short recording windows, and sparse sampling to avoid recording (intelligeble) speech?
Can one detect speech and avoid recording in those cases? / discard sample.
Process classification etc on the fly, and do not store the audio recordings?
Device firmware verifiable.
Indicator light on when recording. Can be hardwired to the microphone subsystem power.
Pause mode? Activate to avoid capture for NN minutes. 
* How can one enable continious environmental monitoring using audio in a Wireless Sensor Network?
What is a realistic power budget?. Outdoor, Indoor. Rural, Urban.
What is the power usage of existing solutions/works? Non-edge ML, deep learning edge ML.
How much can power usage be reduced by machine learning?
How would the sensor network architecture look like?
* Energy efficiency of deep learning
How does end2end learned systems compare in number of instructions
versus standard feature engineering?
Can one adopt feature learnings to hand-coded systems to improve efficiency?

Neural Networks for Machine Hearing

* Can Data Augmentation be applied successfully to (mel)spectrogram representation instead of raw audio?
Mixup/between-class.
See: `SpecAugment`

* How to find the most efficient feature representation for audio classification.
Ex: Time window range, time resolution, frequeny range, frequency resolution.
Answer may be class dependent, but also inter-class. Can one do a per-class search to simplify?
Sparsity constraints on initial filters in end2end model. Grouped.

Keywords

* Energy efficiency, energy budget
* Communication link budget
* Privacy
* Cost


## Book reviews

#### Computational Analysis of Sound Scenes and Events
Notes.

Ch11. Computational Bioacoustic Scene Analysis


Ch12. 24/7 AER systems. Smart home applications.
Ch12.2.1. User concept of "event" may comprise several acoustic events taken together. 
Ch12.2.2. Real life AER as an open-set problem, unbounded number of classes.
"binary 1-vs-set" as extension of standard 1-class classifiers.
24/7 AER exposed to ever growing number of non-target events. Prior probability ->1 for on-target, ->0 for target.
Poses challenge for classic metrics like accuracy,f-score. False alarm rate per unit of time can be used instead.
Detection error trade-off (DET) curve, used in keyword spotting.
Ch12.2.3. Current Far-field technology (microphone arrays etc) geared towards speech. Generalization to AER understudied.
Devices have limited compute and memory capacity. 
Introducing Computational cost into Evaluation. References a comparative study. GMM low-cost baseline. SVM similar accuracy, higher cost.
ReLu activation particularly interesting on devices, cheap to compute.
Ch12.3.1. User experience depends to large extent on reliability. Users will not know/care about which subsystem failed.
AER most interesting for remote monitoring. User would need to double check event in order to evaluate reliability.
Missing detections very hard to verify for user. But can be critical for user experience when event was important (broken window during breakin).
Standard measures may not be good predictors of user experience.
Take the place of user. Encourage academic researchers to build sound recognition systems.
Opinion scoring as method for assessing user experience.
Can be included into design of end-user application, to capture data from production system.
Operating point, threshold for positive detection used to tradeoff FP/FN (false alarm / missed detection).
Discrete Cost Function (CDF) can be used to include relative cost of FA/MD.
Ch12.4.2. Privacy of environmental audio data.
GDPR defines level of data privacy. Personal data, sensitive data, confidential data. Profiling: inferring sensitive data from derived data.
Sensitive and confidential data should not be collected/stored. Personal may, if for a specific usage and given permission, and no profiling is done.

Ch13. 24/7 AER systems. Smart cities. Noise pollution, surveillance.
Urban environments more anthrophony than geophony/biophony.
Voice, traffic, construction, signals, machines, music, etc.
Patterns of activity. Daily,weekly,monthly,yearly.
Microphones less affected than cameras by fog,pollution,rain, daily changes in light conditions.
Less succeptible to occlusion, are capapable of omnidirectional sensing.

Noise pollution. Complaints biased by location, socieconomic status, source type.

Ch13.3 Acoustic Sensor networks
Ch13.3.1 Mobile sound sensing. Using existing smartphones to capture,analyze sound.
Many crowdsourcing efforts exists for SPL measurements, geo-tagged.
Some also include subjective data, allows filing complaints.
OnoM@p atempts cross-calibration to avoid erronous data.
Ch13.3.2 Static sound sensing.
Commercial solutions from 560USD - 10k+ for recording SPL. Some examples down to 150 USD.
Desirable to have low-cost, powerful sensor nodes to support computational sound analysis.
Ch13.3.3 Designing a low-cost acousting sensing device.
SONYC project. Raspberry PI + MEMS microphone with onboard MCU. Dynamic range 30-120dBA.
MEMS board on a flexible gooseneck for positioning.
Sensor cost 83USD EX construction and deployment (Dec 2006).
Node requires continious power supply and WiFi connection.
Ch13.3.4 Network Design.
Mounted at 4 meters above street level, every 150m.
Audio data is captured in 10sec, lossless FLAC compressed and encrypted, interleaved with random durations of time(??).
Transfers to control server, then storage servers, for further analysis.
Sensor node also sends status ping every minute.
VPN network for SSH access.
Future versions will utilize mesh networking and reduce power consumption to enable battery powered, energy harvesting.
Many more deployment possibilities become available.
Ch13.4. Lists some 7 datasets with lots of Urban Soundscape data.
Ch13.4.1. Sound source identification, in urban environment.
Proposed urban sound taxonomy. UrbanSound8k dataset implements this.
Reviews performance. MFCC-SVM baseline, SKM-mel-RF, SKM-scattering-SVM, mel-CNN.
SKM-mel-RF had best results with 370ms,16-frame patches. Dictionary of 2000 words.
Deep learning methods needed data augmentation to perform better than SKM.
Scattering transform. Can be seen as extension of mel-spectrogram, computes modulation spectrum coefficients of multiple orderings
through cascades of vavelet convolutions and modulus operators. Convolving then averaging over time using a low-pass filter.
Phase-invariant convolutional layer, capture amplitude modulations in time-shift invariant manner.
Basically same perf as SKM-mel-RF. But dictionary size of only 200. "finding motivates further exploration using deep convolutional approaches"
mel-CNN used 5x5 perceptive field.

Ch14.2.1. Manually designing audio label/class vocabularies.
Ch14.2.1.2 Mining audio data to build vocabularies. Two step process: generate candidates, then filter.
Can used Verb-Noun pairs and Adjective-Noun pairs as names.
Ch14.2.2.2. Using video with audio as basis for learning.
Ch14.2.3. Active learning. Maxizing human effort
14.2.4 Unsupervised Data. Can be basis for annotation effort via similarity metrics
Weak labelling. Multiple-instance-learning.
14.2.5 Evaluation tasks. AudioSet as a potential standard. 10s exerpts, 100 examples, 500 sound categories.

14.3.2 Future approaches. Mid-sized embedding continious spaces.
Triplet loss. Only needs same/different annotation for pairs instead of class label per instance.
Transfer learning. Can be based on embeddings
Source separation, joint estimation.

#### Human and Machine Hearing

Ch3.1. Page51. Great diagram of relationship between log,exp,pow(...) as expanding or contracting non-linear functions.

Ch5.5. Page 98. Power-law compression of mel-spectrogram with exponents 0.25-0.67 can be better than log or lin.

MFCC sometimes used for pitch tracking, easy to split out fundamental.

Ch7.11. IIR filter standard forms. Direct1, direct2. Second order needs 2 delay elements and 5 multiplications.
Larger filters often a cascade of 2-order, favorable for numerical stability and modularity.

Ch7.13. Shows speech with two spectrograms. One with high frequency resolution, other with high temporal resolution.

Ch9. Gammatone and related filters.
Ch9.4. Real gammatone has impulse response of a gammatone distribution times a sinousoid.
Order N, dampening factor, gammatone phase. Orders 3-5 typical for auditory filters.
Ch9.4. All-pole gammatone filter (APGF). No zeroes. One zero gammatone filter (OZGF). Asymmertric
Gammatone filters are special case of gammachirp. Easier to control asymmetry.

Ch10. Nonlinear sytems. Cannot be fully described by responses to sinewaves.
But often characterised by response to sines at different levels, and pairs of sinewaves.
Ch10.1. Volterra Series. Linear convolution model plus corretion terms. (also Wiener series)
Zero term: constant. First term: Linear response. Second term: Product response. Third order: cubic.
Ch10.3-10.4. Essential nonlinearities (in the ear).
Fig10.2. Measurements on live cochlea demonstrating non-linearity.
Two-tone supression.
Intermodulation distortion.

Ch11. Automatic gain control.

Ch21. Stabilized Audatory Image (SAI)

Ch22. Binaural spatial hearing.

Head-related transfer function. Acoustic reason for differences in sound from different sides.
Neural extraction of interaural differences.

How we can localize sound even in reverberant conditions.
Precedence effect. Law of first waveform. Haas effect. 

Ch23.1. Scene analysis.
CASA: Computational Auditory Scene Analysis.

Ch23.2 Attention and Stream Segregation
Separating pieces of sound into different tracks.
Pay 'attention' to particular streams
Following Gestalt principles: common-fate etc
time-frequency masks. Binary masks.

Ch24. Learning and applications

Application: Hearing aids

Ch25.3 Bandpass power and Quadratic Features
Autocorrelation coefficients, power spectra equivalent.
Direct learning of waveform filters. Filter learning.
RElies on a nonlinearity of some kind, quadratic or other,
to rectify filter output or choose sparsity based on outputs with highest power.

Cascading layers of bandpass quadraticfeature extraction,
using wavelet transforms with power detection: Wavelet modulus operators.

Ch28.5 Medial diagnostics through sound. `auscultation`
Heart murmurs. Lung.
The relevant range of frequencies for hearts is lower than normal human hearing. `<20Hz`.

Fault detection in machinery by technicians often also use sound.


## Multi-channel audio

Stereo. Binaural.
Many-channels. Microphone array.

Input represenations

- Left, right. L-R (absolute) difference.
- Phase and magnitude spectrograms.
- Reference audio,

Strategies

- Early fusion. Multiple spectrogram as input to first layer.
- Intermediate fusion. Multi-head Neural Network.
- Late fusion. Concatenation of features, then classifiers backend.
- Ensembling. Multiple separate neural networks. Results combined.


