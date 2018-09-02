# Machine hearing


## Research questions

* How can one perform environmental monitoring tasks on audio without invading privacy?
Can one use very short recording windows, and sparse sampling to avoid recording intelligble speech?
Can one also avoid speaker detection.
Can one detect speed and avoid recording in those cases?
How realistic is it to not store any audio recordings, only perform classification? 
* How can one enable continious environmental monitoring using audio in a Wireless Sensor Network?
What is a realistic power budget?. Outdoor, Indoor. Rural, Urban.
What is the power usage of existing solutions/works? Non-edge ML, deep learning edge ML.
How much can power usage be reduced by machine learning?
How would the sensor network architecture look like?
* Energy efficiency of deep learning
How does end2end learned systems compare in number of instructions
versus standard feature engineering?
Can one adopt feature learnings to hand-coded systems to improve efficiency?

Keywords

* Energy efficiency, energy budget
* Communication link budget
* Privacy
* Cost

## Data collection

Wireless Sensor Network for Acoustic monitoring.
Ex: Bird detection

Sample period: 10 sec? 1 sec?
Sample frequency: continious?

Every M minutes send:
S: number of samples taken
start,endtime for reporting period
classifications for all S samples
features for every S/60 samples
full audio for every S/60*60 samples

MQTT communication w/TLS

Ideally solar powered.
https://www.banggood.com/6V-1_1W-200mA-Mini-Solar-Panel-Photovoltaic-Panel-p-1003920.html?rmmds=search&stayold=1&cur_warehouse=CN
https://www.banggood.com/8000mAh-Solar-Power-Bank-Dual-USB-Battery-Charger-Set-For-Mobile-Phone-p-1111247.html?rmmds=search&ID=229&cur_warehouse=CN


* Microphone. 1-2 pieces. I2S, PDM or analog?
* Microcontroller. ESP32?
* GSM modem.
* RTC.
* Power source. Solar+battery

## Background


## Usecases

Bioacoustics/ecoacoustics. 
Passive acoustic monitoring.
Biomonitoring.
Animal population estimation/census.

Birds. Wolves. Insects.

Trigger for camera trap?

Livestock
Poultry,swine,sheep,diary cows.

Grazing/feeding behavior.
Heat detection.
Respiratory disease detection.
Stress detection.
Chase away wild animals/birds from fields.
Insect detection.
Food quality analysis.

[Acoustic monitoring system to quantify ingestive behavior of free-grazing cattle](https://www.sciencedirect.com/science/article/pii/S016816991100024X)
[A real-time algorithm for acoustic monitoring of ingestive behavior of grazing cattle](https://www.sciencedirect.com/science/article/pii/S0168169916303076).
[Formant-based acoustic features for cow's estrus detection in audio surveillance system](https://www.semanticscholar.org/paper/Formant-based-acoustic-features-for-cow%27s-estrus-in-Lee-Zuo/ed1251d3c162bb45c4d9ce84d6826fe5ffc86a23). Heat detection is critical to breeding programs.
[Sound analysis in dairy cattle vocalisation as a potential welfare monitor](https://www.sciencedirect.com/science/article/pii/S0168169915002549). 2015. It might be possible to apply call recognition to determine cattle welfare.
Early recognition of bovine respiratory disease in calves using automated continuous monitoring of cough sounds

[A real-time monitoring tool to automatically measure the feed intakes of multiple broiler chickens by sound analysis](https://www.sciencedirect.com/science/article/pii/S0168169915000733). Detect the pecking sounds of multiple broiler chickens

Cough sound analysis to identify respiratory infection in pigs.

[Detecting symptoms of diseases in poultry through audio signal processing](https://ieeexplore.ieee.org/document/7032298/).
Detects rales, gurgling noises that are a distinct symptom of common respiratory diseases in poultry.

[Stress Detection and Classification of Laying Hens by Sound Analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4341110/). 2015.

[On the Design of a Bioacoustic Sensor for the Early Detection of the Red Palm Weevil](https://www.researchgate.net/publication/325006988_Sound_Analysis_and_Detection_and_the_Potential_for_Precision_Livestock_Farming_-_A_Sheep_Vocalization_Case_Study). Detecting a pest that attacks palm trees.

Detect illegal hunting and logging.

Machinery
Real-Time Acoustic Monitoring of Cutting Blade Sharpness in Agricultural Machinery.

Fish farming


Gunshot detection.

Non-destructive testing
Acoustic Emissions Testing. Acoustic Emission Testing is performed by applying a localized external force such as an abrupt mechanical load or rapid temperature or pressure change to the part being tested. 
Acoustic Resonance Testing.

Testing of cast-iron castings
Concrete.

[Acoustic methods for the nondestructive testing of concrete: A review of foreign publications in the experimental field](https://link.springer.com/article/10.1134/S1061830913020034)


Structural monitoring.

Buildings.
Bridges.

[Acoustic techniques for structural health monitoring](https://aip.scitation.org/doi/10.1063/1.2902603)
Structural health monitoring of bridges using acoustic emission

## Test cases

* Detect clapping and its sound level, for instance in a conference


### Feature representations

* Spectrograms. Linear/log
* MFCC
* Bag of frames
* Chroma. 
* Learned features

Summarization, pooling
Typically across a set of frames

* Min/max
* Mean/stdev

Delta-frames, delta-delta frames.
Change and change-rate. Common with MFCC

Nice summary of feature calculation in Python 'from scratch'.
http://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html

### Preprocessing

* A-weighting
* Log transform
* Harmonic-percussive-residual source separation. Especially for music.
* Per-channel energy normalization (PCEN).
Static version exists as [librosa.pen](https://librosa.github.io/librosa/generated/librosa.core.pcen.html).
Can also be learned as a neural network layer, see arXiv:1607.05666v1
* Whitening. Eg PCA.
Removes redundancies in spectrogram. For each frame in spectogram

Normalization

* RMS normalization
* Gaussianization, mapping to Gaussian distribution

### Blind source separation

* Subspace based approaches. Aims to partition the mixture space into source dominant spaces.
Learns the source specific filters/dictionaries/basis that span those spaces.
Examples.
Principal Component Analysis (PCA),
Independent Component Analysis (ICA),
Subspace analysis
* Decomposing and grouping approaches.
The mixture spectrogram is divided into small time-frequency bins
and individual sources are then recovered using a masking.
Masking is is learned using the acoustic properties of the sources.
Examples:
Adaptive Wiener filtering/rules.
Ideal Binary Masking (IBM),
Computational Auditory Scene Analysis (CASA)
* Model based approaches.
Models of the sources are built/learned.
Examples: Non Negative Matrix Factorization (NMF),
Non Negative Sparse Coding (NNSC)

Singular Value Decomposition (SVD),
Eigen Value Decomposition (EVD)
Spectral decomposition
Factorial HMM


### Temporal coherence

Speech has strong correlation (2nd order dependency) among adjacent Time-Frequency (T-F) slots in both time
and frequency. A T-F slot can be described as a pixel (or a set of adjacent pixels) in a power
spectrogram.

! Want to utilize this to classify, but many algorithms don't natively.

### Non Negative Matrix Factorization
Non-negativity constraint of NMF only allows additive combinations (not subtractive),
in contrast to ICA/PCA.
Leads to a parts-based representation.
Recommended to impose constraints like sparseness, orthogonality, or smoothness to get more interesting basis vectors.

Many factorization approaches. Gradient descent. Multiplicative update rules, easy to implement.
Semi-supervised method possible with Schmidt2007 "Wind Noise Reduction using Non-negative
Sparse Coding".


### Noise types
Biophony, geophony, and anthrophony

* Biophony refers to any sound produced by biological agents: in the forest major biophonies are birds, insects, frogs/toads, and mammals.
Because we are only interested in acoustic activity of birds, all other biological sounds are categorised as noise
* Geophony refers to all non-biological, natural sounds in the environment such as
wind and its effect on trees, rain, thunder, and running water.
* Anthrophony refers to all sound generated from human-made machines such as
aircraft, vehicles, wind turbines, and the recording device (microphone, recorder hum)

Characterises the noise according to its properties into:

* White noise has equal energy at all frequencies, meaning that the power spectrum is flat.
In practice, noise is only white over a limited range of frequencies.
While not all white noise is Gaussian, natural white noise can often be modelled as such.
* Coloured noise shows a non-uniform power spectrum, with the energy generally decreasing in proportion to the frequency f.
Common types of coloured noise include pink (power ∝1f) and brown (power ∝1f2).
* Impulsive noise refers to sudden click like sounds that last for a very short period of time (milliseconds), such as switching noise.
An ideal impulse generates a horizontal line in the power spectrum because these sharp pulses contain all frequencies equally.
* Narrow-band noise such as microphone hum shows a small range of frequencies.
* Transient noise is a burst of noise that occurs for some time, and then disappears.

### Noise reduction
Time domain
Frequency domain
Spectrogram domain
Cepstrum domain

Spectral median filtering

RASTA-filtering.

Uses bandpass filtering in the log spectral domain, removes slow channel variations.
It has also been applied to cepstrum feature-based preprocessing with both log spectral and cepstral domain filtering.



## Birdcalls
Wide range of characteristics

## Other datasets
http://www.kaggle.com/c/the-icml-2013-bird-challenge
https://www.kaggle.com/c/mlsp-2013-birds/
https://www.xeno-canto.org/

## Literature review

### Topics

Birdsong denoising
Birdsong source separation
bioacoustic denoising 

Passive acoustic monitoring.

Time-frequency (TF) analysis of non-stationary signals.

### Books

* Computational Analysis of Sound Scenes and Events. Tuomas Virtanen, Mark D. Plumbley, Dan Ellis. 2018.
* Human and Machine Hearing - Extracting Meaning from Sound. Richard F. Lyon. 2017, revised 2018.

### Bioacoustics

[Computational Bioacoustic Scene Analysis](https://link.springer.com/chapter/10.1007%2F978-3-319-63450-0_11). D. Stowell, from book, 2017.
Ecoacoustics.



### Prior challenges

[Bird Audio Detection: tips on building robust detectors](http://machine-listening.eecs.qmul.ac.uk/2016/11/bird-audio-detection-tips-on-building-robust-detectors/)
Filtering.
Noise reduction.
Data normalization. Amplitude normalized. Spectral whitening. Linear predictive coding filtering.
Representation. Default: Spectrogram, MFCC. Not getting good improvements by changing?
Data augmentation.
Self-adaptation.
Regularisation.
Combining models.

[Bird Audio Detection: baseline tests – and the problem of generalisation](http://machine-listening.eecs.qmul.ac.uk/2016/10/bird-audio-detection-baseline-generalisation/). First baseline of MFCCs and GMM method generalizes very badly to samples from unseen training sets.
Second baseline of spherical k-means feature learning, followed by a Random Forest classifier still managed 80% on unseen training sets.


[Bird detection in audio: a survey and a challenge](https://arxiv.org/abs/1608.03417). D.Stowell, 2016. Introducing DCASE2016.
Usecases: Unattended monitoring, prefiltering step before other automatic analyses such as bird species classification.
Detection types:
Presence/absence in a given sound clip: a detector outputs a zero if none of the target species are detected, and a one otherwise.
Monotonic segmentation. Partition the time axis into positive and negative regions. Analogous to voice activity detection (VAD).
Methods:
Energy thresholding.
Spectrogram cross-correlation.
Hidden Markov Models.
Template matching with Dynamic Time Warping.
Open question whether the various different approaches (for single species detection)
can simply be aggregated under a meta-algorithm to produce species-agnostic output.
Sinousoidal tracks.

[Detection and Classification of Acoustic Scenes and Events: Outcome of the DCASE 2016 Challenge](https://ieeexplore.ieee.org/document/8123864/).
November 2017.

2018 BirdCLEF Baseline System. [Paper](https://arxiv.org/pdf/1804.07177.pdf).
[Github](https://github.com/kahst/BirdCLEF-Baseline)
Feature extraction: https://github.com/kahst/BirdCLEF-Baseline/blob/master/utils/audio.py#L115
Use a high-pass and a low-pass filter with cut-off frequencies of 300 Hz and 15 kHz
Uses a simple SNR estimation to not train on samples with bad signal2noise ratio.
Based on median filtering and morphological operations on spectogram.
Very low score => unlikely to contain any birds.

### Feature learning

Aka, related

* Representation learning
* Dictionary learning
* Codebook learning

Unsupervised

* Restricted Boltzman machine
* Non-negative factorization
* Clustering-based
Spherical k-means.

Supervised

* Supervised Non-negative factorization


[Automatic large-scale classification of bird sounds is strongly improved by unsupervised feature learning](https://peerj.com/articles/488/).
D. Stowell, 2014. Classifier got strongest audio-only results in LifeCLEF2014.
Inspired by techniques that have proven useful in other domains.
Compare twelve different feature representations derived from the Mel spectrum, using four large and diverse databases of bird vocalisations. Classified using a random forest classifier.
"in our classification tasks, MFCCs can often lead to worse performance than the raw Mel spectral data from which they are derived"
"unsupervised feature learning provides a substantial boost over MFCCs and Mel spectra without adding computational complexity after the model has been trained"
Using spherical k-means, adapted to run in streaming fashion using online Hartigan k-means. Using two passes, first with reservoir subsampling.
Birdsong often contains rapid temporal modulations, and this information should be useful for identifying species-specific characteristics.
feature learning is that it can be applied not only to single spectral frames, but to short sequences (or “patches”) of a few frames.
Also tested a two-layer version, second layer downsampled projected data by 8 then applying feature learning again. 

[A joint separation-classification model for sound event detection of weakly labelled data](https://arxiv.org/abs/1711.03037)

[Unsupervised dictionary extraction of bird vocalisations and new tools on assessing and visualising bird activity](https://www.sciencedirect.com/science/article/pii/S1574954115000102?via%3Dihub). I.Potamitis, March 2015, Ecological Informatics.
Tool 1) Report if a recording is void or not of any birds' vocalisation activity (binary classification).
Shows 3 related methods based on image-processing of the spectrogram to create a codebook with regions-of-interests.
Regions-of-interests are then cross-correlated with samples. ROI aka spectral templates, spectral blobs, acoustic atoms.


[Classification of Bird Sounds Using Codebook Features](https://link.springer.com/chapter/10.1007/978-3-319-75417-8_21). Alfonso B. Labao, Feb 2018, ACIIDS 2018.
The codebook approach on MFCC features with a Random Forest classifier performs best with an accuracy of 93.62%.
100 to 500 codebook clusters are formed from raw features, a “one-step” approach.
Compared features, increasing complexity.
1. Spectral center and bandwidth. 
2. Histogram of spectral center and bandwidth. Frequency 100 bins, bandwidths 50 bins. N=5000. Normalize to a PDF.
3. Codebook of spectral densities. k-means clustering, 100-500. Count number of frames that hit. Normalize to a PDF.
4. Codebook of Mel frequencies
5. Summarized MFCC coefficients
6. Codebook of MFCC coefficients

[Weakly supervised scalable audio content analysis](https://ieeexplore.ieee.org/abstract/document/7552989/).
Kumar, 2016. Audio Event Detection

[Robust feature representation for classification of bird song syllables](https://asp-eurasipjournals.springeropen.com/articles/10.1186/s13634-016-0365-8). Maria Sandsten, EURASIP Journal on Advances in Signal Processing, 2016.
A novel feature set for low-dimensional signal representation, designed for classification or clustering of non-stationary signals with complex variation in time and frequency. Applied to birdsong and *within-species* classification.
Ambiguity spectrum. Multitapers. Singular Value Decomposition.

### Passive monitoring

Wireless Acoustic Sensor Network

[Random Forest for improved analysis efficiency in passive acoustic monitoring](https://www.sciencedirect.com/science/article/pii/S1574954113001234). June 2013.
Used simple (bandpass?) detectors to generate events, then used Random Forest on a set of statistical features calculating during the event time.
Was able to reduce false positives by 80-90%.

[An FPGA-Based WASN for Remote Real-Time Monitoring of Endangered Species: A Case Study on the Birdsong Recognition of Botaurus stellaris](http://www.mdpi.com/1424-8220/17/6/1331). Wireless Acoustic Sensor Networks (WASN). #TODO

[Applications and trends in wireless acoustic sensor networks: a signal processing perspective](https://www.researchgate.net/publication/248702130_Applications_and_trends_in_wireless_acoustic_sensor_networks_A_signal_processing_perspective).
Considers WSN for microphone arrays. 2011. 103 citations.

[Wireless Acoustic Sensor Networks and Applications](https://www.hindawi.com/journals/wcmc/si/493820/).
Special issue in Wireless Communications and Mobile Computing.
[introduction](https://www.hindawi.com/journals/wcmc/2017/1085290/)

[Design and Implementation of a Robust Acoustic Recognition System for Waterbird Species using TMS320C6713 DSK](https://www.igi-global.com/gateway/article/176715). A. Boulmaiz. International Journal of Ambient Computing and Intelligence (IJACI), 2017. 
Tonal region detector (TRD) using a sigmoid function.
Mel Frequency Cepstral Coefficients, Spectral Subtraction. Support Vector Machine. #TODO

[Audio Classification of Bird Species: A Statistical Manifold Approach](https://www.researchgate.net/publication/220765656_Audio_Classification_of_Bird_Species_A_Statistical_Manifold_Approach) #TODO

[Robust acoustic bird recognition for habitat monitoring with wireless sensor networks](https://link.springer.com/article/10.1007%2Fs10772-016-9354-4). Amira Boulmaiz. International Journal of Speech Technology, September 2016.
Tonal region detector (TRD) using sigmoid function is proposed.
Once the tonal regions in the noisy bird sound are detected, the features gammatone teager energy cepstral coefficients (GTECC).
TRD–GTECC.
Quantile-based cepstral dynamics normalization (QCN) for noise reduction. Extending ideas from computationally inexpensive normalizations of
spectral subtraction (SS), cepstral mean and variance (CMVN), and recently introduced cepstral gain normalization (CGN).
Compares MFCC, perceptual-MVDR (PMVDR) and power-normalized cepstral coefficients (PNCC).
Using different feature normalizations; SS, CMVN, CGN, and QCN.
GTECC had the best recognition rate, while being slightly less computationally intensive than MFCC.



### Source separation and denoising

[Vocal source separation using spectrograms and spikes, applied to speech and birdsong](https://www.research-collection.ethz.ch/handle/20.500.11850/175085). PhD thesis, ETH Zurich, 2017.
Audio source separation methods (ASS). Monaural source separation (MSS) special-case of ASS where only a single mixture is observed.
Spectral subtraction, Wiener filtering, and subspaces used in speech enhancement.
Ideal Binary Mask (IBM) used in auditory scene analysis (CASA).
Deep Neural Networks have been used to learn binary and soft masks, with state of art reslults.
This thesis presents novel linear and non-linear methods to address MSS in a supervised scenario

Three linear methods proposed in the thesis are:
1) Eigenmode analysis of covariance difference (EACD).
This method identifies spectro-temporal features associated with large
variance for one source and small variance for the other source.
2) Maximum likelihood demixing (MLD).
In this method, the mixture is modelled as the sum of two Gaussian signals
and maximum likelihood is used to identify the most likely sources.
3) Suppression-regression (SR).
Autoregressive models trained to reproduce one source but suppress the other.
4) A non-linear method called Multi-layered Random Forest (MLRF).
MLRF is an ensemble method that trains decision trees for each frequency band.
Given a mixture spectrogram, these trees classify individual T-F bin as belonging
to one of the speakers thus returning an estimate of the IBM.
An estimated IBM in a given layer is used to train a RF classifier in the next higher layer.
Outperforms a deep learning based method in terms of SNR of reconstructed audio.

[Birdsong Denoising Using Wavelets](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4728069/).
Using wavelets as alternative to bandpass. Not considering any source separation techniques.
Wavelet avoids the fundamental tradeoff between temporal and frequency resolution in Fourier spectrogram.
Nice background info on birdsong, including typical characteristics.

[Adaptive energy detection for bird sound detection in complex environments](https://www.sciencedirect.com/science/article/pii/S0925231214017068?via%3Dihub). Xiaoxia Zhang, Neurocomputing, 2015.
The noise spectrum of each band was estimated and the existent probability of the foreground bird sound for each band was computed to serve for the adaptive threshold of energy detection.
These foreground bird sound signals were detected and selected via adaptive energy detection from the bird sounds with background noises.
Features of Mel-scaled Wavelet packet decomposition Sub-band Cepstral Coefficient (MWSCC).
Moreover, the differences of recognition performance were implemented on 30 kinds of bird sounds at different Signal-to-Noise Ratios (SNRs)
under different noisy environments, before or after adaptive energy detection.
Classified with Support Vector Machine.

[Blind Source Separation With Non-stationary Mixing Using Wavelets](http://www.robots.ox.ac.uk/~sjrob/Pubs/addison_roberts.pdf)
ICA that uses wavelet representation. Uses a sliding-window ICA, assuming that mixing process changes slowly enough wrt window size.
"however seen that despite the best efforts of our proposed algorithm there are still difficulties with the permutation problem.
The choice of window size is also arbitrary". Proposes a Baysian framework as further work

[Trainable Frontend For Robust and Far-Field Keyword Spotting](https://arxiv.org/pdf/1607.05666.pdf). Yuxuan Wang, 2016.
Introduces Per-Channel Energy Normalization (PCEN).
Several issues with the log function.
1. First, a log has a singularity at 0.
Common methods to deal with the singularity are to use either
a clipped log (i.e. log(max(offset, x))) or a stabilized log (i.e. log(x+offset)).
However, the choice of the offset in both methods is ad hoc and may have different performance impacts on different signals.
2. Second, the log function uses a lot of its dynamic range on low level, such as silence,
which is likely the least informative part of the signal.
3. Third, the log function is loudness dependent.
With different loudness, the log function can produce different feature values even when the underlying
signal content (e.g. keywords) is the same,
which introduces another factor of variation into training and inference.
Although techniques such as mean–variance normalization and cepstral mean normalization can be used to alleviate this issue
to some extent, it is nontrivial to deal with time-varying loudness in an online fashion.

Simple feed-forward automatic gain control (AGC), which dynamically stabilizes signal levels.
Further propose to implement PCEN as neural network operations/layers and jointly optimize various PCEN.
Operation is causal and is done for each channel independently, making it suitable for real-time implementation.
The AGC emphasizes changes relative to recent spectral history and adapts to channel effects including loudness.
Following the AGC, we perform a stabilized root compression to further reduce the dynamic range using offset δ and exponentr.
We note that the offset δ introduces a flat start to the stabilized root compression curve,
which resembles an optimized spectral subtraction curve.
It is worth noting that the main parameters in PCEN are the AGC strength α and smoothing coefficient s,
whose choices depend on the loudness distribution of data.
In addition, PCEN tends to enhance speech onsets, which are important for noise and reverberation robustness.

To improve noise robustness, we perform multi-condition
training by artificially corrupting each utterance with various interfering
background noises and reverberations, where the noise
sources contain sounds sampled from daily-life environments
and YouTube videos. To further improve loudness robustness,
we also perform multi-loudness training by scaling the loudness
of each training utterance to a randomly selected level ranging
from −45 dBFS to −15 dBFS.

## Audio Event Recognition

[Audio Event Recognition in the Smart Home](https://link.springer.com/chapter/10.1007/978-3-319-63450-0_12)
Very nice background to the Smart Home topic and role of Audio.
"AI applied in the audio domain has become a key driver of the smart home market",
due to home assistant devices such as Amazon Alexa and Google Home.
Contains a number of example applications.

[Machine learning in low-power devices brings sound recognition to the smart home market](https://community.arm.com/processors/b/blog/posts/machine-learning-in-low-power-devices-brings-sound-recognition-to-the-smart-home-market). Whitepaper. ARM, Audio Analytic. 2017.
"Amazon Echo, Google Home and most mobile phones are using microphone arrays to “target” people’s speech through a technique called beamforming,
the vast majority of Consumer Electronics and Smart Home devices are still natively using mono audio capture"
On-edge Audio Event Detection. A clip of the sound is sent along with event (if 512 KB RAM available).
Can support 3 event profiles on Cortex M4, 6 on Cortex M7.

[Sound Event Recognition in Unstructured Environments using Spectrogram Image Processing](http://www.ntu.edu.sg/home/aseschng/Thesis/JohnDennis_PhDThesis2014.pdf). PhD thesis, Jonathan William Dennis, 2014. 200 pages.

[Spectrogram Image Feature for Sound Event Classification in Mismatched Conditions](https://www.researchgate.net/publication/224206697_Spectrogram_Image_Feature_for_Sound_Event_Classification_in_Mismatched_Conditions). Jonathan Dennis, 2011.
Splits spectrogram into 3 bins. 
Linear spectrogram better than log spectrogram in presence of noise.



[RNNoise](https://people.xiph.org/~jm/demo/rnnoise/).
Using deep learning combined with conventional signal processing.
Tuned for real-time usage, 10ms lookahead.
GRU type of RNN.
Split into 22 filterbanks, roughly following Bark scale.
42 inputs features.
Computes outputs: (1) Voice Activity Detection, (22) gains for filterbanks
Training using synthesized data. Adding noise to speech. Adding filters.
C code available, BSD licensed. 7x realtime on RPi.
Has 'donate your noise' collection for a noise dataset. Is it available anywhere?


## Commercial available solutions

Audio Analytic.
https://www.silicon.co.uk/software/audio-analytic-startup-224583
"we started looking at the professional security arena.
This caught the attention of companies in the smart home marketplace which were creating domestic security applications"
40 people in 2017.

IDC executive brief. [Needs registration](https://www.audioanalytic.com/idc-executive-brief-sound-recognition/)


## Interesting software

[librosa: Vocal separation](http://librosa.github.io/librosa/auto_examples/plot_vocal_separation.html#sphx-glr-auto-examples-plot-vocal-separation-py). Simple technique for separating vocals (and other sporadic foreground signals) from accompanying instrumentation.
Foreground/background separation.

[librosa: Harmonic-percussive source separation](https://librosa.github.io/librosa/auto_examples/plot_hprss.html?highlight=harmonic).
Including a margin-based approach which also separates out noise.

[librosa: enhanced Chroma](http://librosa.github.io/librosa/auto_examples/plot_chroma.html#sphx-glr-auto-examples-plot-chroma-py).
Using harmonic-percussive separation, non-local filtering and median-based filtering.

[muda: Python library for augmenting annotated audio data](https://github.com/bmcfee/muda)



