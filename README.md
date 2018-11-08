# Machine hearing


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

[Awesome Bioacoustic](https://github.com/ybayle/awesome-bioacoustic). List of resources by  Yann Bayle. Lots on birds, underwater species.

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

Smart home. Extending voice assistants

## Test cases

* Detect clapping and its sound level, for instance in a conference
* Detect clap versus snapping of fingers.


### Feature representations

* Energy
* Chroma.
* Spectrograms. Linear/log. Mel, bark, constant-Q.
* MFCC
* modulation spectrogram
* Scattering transform



Summarization, pooling
Typically across a set of frames

* Min/max
* Mean/stdev

Delta-frames, delta-delta frames.
Change and change-rate. Common with MFCC

* Bag of frames

Nice summary of feature calculation in Python 'from scratch'.
http://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html

[](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182309).
Using SIF features, spectrograms downscaled. 720 features per frame.
Used one frame energy summary feature. 
Shows SIF-SVM performing almost as good as SIF-CNN and SIF-DNN, and favorable under high noise.



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

* Cepstral Mean Normalisation (CMN): subtract the average feature value from each feature, so each feature has a mean value of 0.
makes features robust to some linear filtering of the signal (channel variation).
* Cepstral Variance Normalisation (CVN): Divide feature vector by standard deviation of feature vectors, so each feature vector element has a variance of 1.
* For real-time, need to compute a moving average.
* RMS normalization
* Gaussianization, mapping to Gaussian distribution

[Speech Signal Analysis, Lecture 2](https://www.inf.ed.ac.uk/teaching/courses/asr/2016-17/asr02-signal-handout.pdf).
January 2017, Hiroshi Shimodaira and Steve Renals.
! great diagrams of audio discretization, mel filters, wide versus narrow-band spectrograms.

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

### Generating sound

[Roundtripping data via spectrograms in Python](https://timsainb.github.io/spectrograms-mfccs-and-inversion-in-python.html),
has code for converting (Mel) spectrogram back to audio.



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

[Non-Negative Matrix Factorization And Its Application to Audio](https://www.cs.cmu.edu/~bhiksha/courses/mlsp.fall2009/class16/nmf.pdf). Tuomas Virtanen.
Easy to follow introduction.
References many works on applying NMF to audio.

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

Random Features

[DCASE 2017 TASK 1: Acoustic Scene Classification Using Shift-Invariant Kernels and Random Features](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/challenge_technical_reports/DCASE2017_Jimenez_186.pdf). 6k random features. Performed 4% points better than baseline with Gaussian kernel. Random features can be used as privacy measure, keeping the W,b parameters private.
[Another copy](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/workshop_presentations/DCASE2017Workshop_Jimenez_195_presentation.pdf).
[ACOUSTIC SCENE CLASSIFICATION USING DISCRETE RANDOM HASHING FOR LAPLACIAN KERNEL MACHINES](http://www.mirlab.org/conference_papers/international_conference/ICASSP%202018/pdfs/0000146.pdf). IEEE paper.
Uses a linear SVM with random features to approximate a non-linear kernel SVM. Avoids expensive computation of high-dimensional kernel.
Approximates a shift-invariant kernel, like Gaussian, Laplacian and Cauchy.
Allows XOR Hamming distance based similarity calculation. 
With hashing, can reduce data by 2**6 / 64 with minor loss in performance.


[YouTube: Scattering Invariants for Audio Classification](https://www.youtube.com/watch?v=W_Wbnp_uw-o).
Associated paper: Deep Scattering Spectrum.
Classic approach: Construct an intermediate representation.
Conservative approach: Remove transformations which dont change the class.
Time-shifting. Want invariant. Want to be stable across time-warping (including dilation).
Can be done with Mels, want constant-Q at high frequencies.
Actually comes from biology/psycoacoustics, but has the good mathematical property of time-shift invariance.
8:55. Alternate way to get equivalent data of Mel spectrogram. Convolve filters, then time average them.
Can be seen as a wavelet transform. Constant-Q 'wavelet' filterbank.
But inveriance depends on frame size, and at large frame sizes loses temporal structure.
Want to relieve the model/classifier of having to learn temporal dynamics (equivalence)
Modulation spectrograms, one approach.
Wavelet Modulus Transform. Scattering Cascade.
Basically a convolutional network. Stages of filters and non-linearity (modulus).
Not learned coefficients, but comes from invariants.
Complimentary, CNN does then need to learn these. 
Typically wavelets per octave. 8,4,2 typical in stage 0,1,2.
Energy decays quickly with stages. Most info in 1-2 stages.
First order: Excitation info, Second order: modulation. 
Typical dimensions. 30-80 wavelet in first order, 100 in second order. 
Transform is O(n log n).
Possible to get a rough inverse of the scattering transform.
Frequency-transposition. Different formants can be seen as frequency warping.
Want to be stable for frequency warping for speech signals, often.
Joint (time-frequency) scattering. With a 2d wavelet.

[FEATURE LEARNING WITH DEEP SCATTERING FOR URBAN SOUND ANALYSIS](https://www.researchgate.net/profile/Justin_Salamon/publication/278019931_Feature_Learning_with_Deep_Scattering_for_Urban_Sound_Analysis/links/5578aec208aeacff200287c5.pdf). 2015.
Evaluate the scattering transform as an alternative signal representation to the mel-spectrogram
in the context of unsupervised feature learning for urban sound classification.
Comparable (or better) performance using the scattering transform whilst reducing
both the amount of training data required for feature learning and the size of the learned codebook by an order of magnitude.
Note that in practice computing the scattering transform will take longer than computing the mel-spectrogram
by a multiplicative factor proportionate to the dimensionality of the scattering output.

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

[Multiscale approaches to music audio feature learning](https://biblio.ugent.be/publication/4152117). 2013.
Music audio exhibits structure on multiple timescales, which are relevant for different MIR tasks to varying degrees.
We develop and compare three approaches to multiscale audio feature learning using the spherical K-means algorithm.

[A support vector machine (SVM) classifier was built on the sparse representation for acoustic event detection](https://ieeexplore.ieee.org/abstract/document/6854807). 2014.
Bag of spectral patch exemplars. k-means clustering based vector quantization (VQ) was applied on the whitened spectral patches.
sparse feature representation is extracted based on the similarity measurement to the learned exemplars.
A support vector machine (SVM) classifier was built on the sparse representation for acoustic event detection.

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

### Computer-aided auscultation
Electronic stethoscope. Transferred over Bluetooth or cable.
Detecting and characterizing heart murmurs / cardiac murmurs.
"automatic heart sound analysis"
Much cheaper than echocardiography (ECG).
Murmurs classified as innocent/physiological/functional or pathological/abnormal
Descriptive murmur information like murmur timing, grading, positions of the S1/S2 heart sounds.
Analysis stages.
1. Heart rate detection
2. Heart sound segmentation. Identify two main phases of heart. Styole,diastole.
3. Feature extraction
4. Feature classification.

Auscultation of the respiratory sounds.
Diagnosing cardio-pulmonary disorders using lung sounds from chest and back.
Asthmaic breath sounds.

Lots of research in 2017 on using smartphones, machine learning, low-cost portable devices.


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

[Inverting spectrogram after Binary Masking](https://stackoverflow.com/questions/51655119/how-do-i-apply-a-binary-mask-and-stft-to-produce-an-audio-file/51773435#51773435).

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

http://cochlear.ai
Founded in 2017. 6 employees.
Seoul, South Korea

https://www.soundintel.com/
Founded in 2000. 50+ employees?
SigardTM, detects verbal aggression. For use with video surveillance
Utrecht, Netherlands.

## Interesting software

* [librosa](http://librosa.github.io).
* essentia
* [muda: Python library for augmenting annotated audio data](https://github.com/bmcfee/muda)
* [kapre](https://github.com/keunwoochoi/kapre). On-demand GPU computation of melspectrograms, for Keras

## Smart home assistants

[Whisper to Alexa, and She’ll Whisper Back](https://developer.amazon.com/blogs/alexa/post/c0e7798d-32bc-4549-9c24-97d204a7bf3a/whisper-to-alexa-and-she-ll-whisper-back). Tech details from researcher on whisper detection

## Human Activity Detection

* Audio-Based Human Activity Recognition Using Non-Markovian Ensemble Voting. 2012. Johannes A. Stork. 50 citations.
* Audio-Based Human Activity Recognition with Robots. 2011. Johannes A. Stork.
* [Transfer Learning for Improved Audio-Based Human Activity Recognition](www.mdpi.com/2079-6374/8/3/60/pdf). 2018.
* A Similarity Analysis of Audio Signal to Develop a Human Activity Detection. 2017, A García-Hernández.

Context aware services. Social robots, domotics/smart-home.

## Fault detection
In machinery/parts.
Fault diagnosis
Anomaly detection
