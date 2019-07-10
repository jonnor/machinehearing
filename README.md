# Machine hearing

## Tasks

Established problem formulations

General

* Audio Classification
* Audio Segmentation
* Audio Source Separation
* Audio Fingerprinting
* Audio Retrieval

Music

* Beat Tracking
* Music Recommendation
* Music Retrieval
* Music Transcription
* Automatic Music Tagging

Speech

* Automatic Transcription
* Speaker Recognition
* Diarization

## Resources

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
* [Fast.ai forums: Deep Learning with Audio](https://forums.fast.ai/t/deep-learning-with-audio-thread/38123). Large lists of resources, both in first post and "popular links". Feb 2019, 315 replies over 4 months.

### Online Communities

* https://mircommunity.slack.com/

## Applications

* Manufacturing. Quality control.
* Medical. Diagnostics. Compliance tracking.
* Agriculture. Domestic animal monitoring, disease detection.
* Construction. Structural integrity monitoring.
* Wildlife. Monitoring animals. 
* Security. Event detection in surveillance cameras.



### Bioacoustics / ecoacoustics

[Awesome Bioacoustic](https://github.com/ybayle/awesome-bioacoustic). List of resources by  Yann Bayle. Lots on birds, underwater species.

Bioacoustics/ecoacoustics. 

* Biomonitoring
* Animal population estimation/census. Dirds. Wolves. Insects.
* Trigger for camera trap?

[On the Design of a Bioacoustic Sensor for the Early Detection of the Red Palm Weevil](https://www.researchgate.net/publication/325006988_Sound_Analysis_and_Detection_and_the_Potential_for_Precision_Livestock_Farming_-_A_Sheep_Vocalization_Case_Study). Detecting a pest that attacks palm trees.

### Agriculture

Machinery

"Real-Time Acoustic Monitoring of Cutting Blade Sharpness in Agricultural Machinery"

### Monitoring of domestic animals

Livestock

* Poultry,swine,sheep,diary cows.
* Grazing/feeding behavior.
* Heat detection.
* Respiratory disease detection.
* Stress detection.
* Chase away wild animals/birds from fields.
* Insect detection.
* Food quality analysis.

[A real-time algorithm for acoustic monitoring of ingestive behavior of grazing cattle](https://www.sciencedirect.com/science/article/pii/S0168169916303076).
[Formant-based acoustic features for cow's estrus detection in audio surveillance system](https://www.semanticscholar.org/paper/Formant-based-acoustic-features-for-cow%27s-estrus-in-Lee-Zuo/ed1251d3c162bb45c4d9ce84d6826fe5ffc86a23). Heat detection is critical to breeding programs.
[Sound analysis in dairy cattle vocalisation as a potential welfare monitor](https://www.sciencedirect.com/science/article/pii/S0168169915002549). 2015. It might be possible to apply call recognition to determine cattle welfare.
Early recognition of bovine respiratory disease in calves using automated continuous monitoring of cough sounds

[A real-time monitoring tool to automatically measure the feed intakes of multiple broiler chickens by sound analysis](https://www.sciencedirect.com/science/article/pii/S0168169915000733). Detect the pecking sounds of multiple broiler chickens

Cough sound analysis to identify respiratory infection in pigs.

[Detecting symptoms of diseases in poultry through audio signal processing](https://ieeexplore.ieee.org/document/7032298/).
Detects rales, gurgling noises that are a distinct symptom of common respiratory diseases in poultry.

[Stress Detection and Classification of Laying Hens by Sound Analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4341110/). 2015.

[Compressive sensing in wireless sensor network for poultry acoustic monitoring](http://www.ijabe.org/index.php/ijabe/article/view/2148). 2017.
Zigbee based network.

### Monitoring of wildlife

[Compressive Sensing for Efficiently Collecting Wildlife Sounds with Wireless Sensor Networks](https://ieeexplore.ieee.org/abstract/document/6289298/). 2012. !!
Determine a sparse base that best represents the audio information used for identifying the target species. As a proof-of-concept, we focus on anuran (frogs and toads). 98% classification rate can be achieved by using as little as 10% of the original data.

[On the effect of compression on the complexity characteristics of wireless acoustic sensor network signals](https://www.sciencedirect.com/science/article/pii/S0165168414003752). Tatlas, 2015. Wireless acoustic sensor network for environmental monitoring is considered.

[Evaluation of MPEG-7-Based Audio Descriptors for Animal Voice Recognition over Wireless Acoustic Sensor Networks](http://www.mdpi.com/1424-8220/16/5/717/htm). Joaquín Luque. Use of generic descriptors based on an MPEG-7 standard. Demonstrate it to be suitable to be used in the recognition of different patterns

[Wireless sensor networks for environmental research: A survey on limitations and challenges](https://ieeexplore.ieee.org/abstract/document/6624996/). 2013.


### Poaching detection
Detect illegal hunting and logging.

[Optimization of sensor deployment for acoustic detection and localization in terrestrial environments](https://zslpublications.onlinelibrary.wiley.com/doi/full/10.1002/rse2.97).
We developed probabilistic algorithms for near‐optimal placement of sensors,
and for localization of the sound source as a function of spatial variation in sound pressure.
We employed a principled‐GIS tool for mapping soundscapes to test the methods on a tropical‐forest case study using gunshot sensors.
On hilly terrain, near‐optimal placement halved the required number of sensors compared to a square grid.
Using a Greedy heuristic for near‐optimal placement of detectors.

TMNR is a 25‐km2 area of mature tropical moist forest on undulating topography of 100–400 m elevation.
Detection frequently possible up to 500 m distance from a gun, but much rarer above 1000 m.
Predicted 79 devices within TMNR when applied to the soundscape from 829 gunshots on a 200‐m grid.
50 devices within TMNR (on a 750‐m grid) would achieve a residual detection‐failure probability of 0.237,
which is just bettered by near‐optimal placement of only 26 devices. 

onitoring in the Korup National Park in Cameroon using 12 passive acoustic devices
continuously recording for 2 years detected a high level of shooting within a 54‐km2 grid.

ew advances in radio communication promise the future capability for real‐time detection and localization of exploitation activity,
by linking networked devices to a base station. And are undergoing development for open‐source AudioMoth sensors (Hill et al. 2018)

### Medical

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

### Acoustic Emission monitoring
Using the emission of acoustic waves from materials under load/stress/failure.
Alternative to ultrasonic testing in some cases.

### Structural health monitoring

Buildings. Bridges.

[Acoustic techniques for structural health monitoring](https://aip.scitation.org/doi/10.1063/1.2902603)
Structural health monitoring of bridges using acoustic emission

### Quality control.

* Non-destructive testing
* Acoustic Emissions Testing.
* Acoustic Resonance Testing.

Acoustic Emission Testing is performed by applying a localized external force such as an abrupt mechanical load or rapid temperature or pressure change to the part being tested. 

* Testing of cast-iron castings
* Concrete.

[Acoustic methods for the nondestructive testing of concrete: A review of foreign publications in the experimental field](https://link.springer.com/article/10.1134/S1061830913020034)


## Process monitoring and regulation

Structural health monitoring (SHM),

System feedback
Process monitoring

May require capture rates of 100-500kHz.


## Fault detection
In machinery/parts.
Fault diagnosis
Anomaly detection

Acoustic method for detecting defects in concrete bridges.
[1](https://phys.org/news/2017-08-acoustics-early-bridges.html).
[2](https://news.unl.edu/newsrooms/today/article/how-acoustics-can-be-an-early-warning-system-for-bridges/)
Dragging balls on string along the concrete, recording with contract microphone.

## Early warning systems
Natural disasters etc.

[An acoustic emission landslide early warning system for communities in low-income and middle-income countries](https://link.springer.com/article/10.1007/s10346-018-0977-1). 2018.
Research and field trials have demonstrated conclusively that
acoustic emission (AE) monitoring can be an effective approach to detect accelerating slope movements
and to subsequently communicate warnings to users.
Cost constrained to a few hundred dollars.
[New acoustic early warning system for landslide prediction](https://www.lboro.ac.uk/service/publicity/news-releases/2010/164_ALARMS.html). 2010.
Details on an acoustic sensor. Steel waveguide. ! nice diagram.
[paper](https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=36220).


[Underwater acoustic sensor network for early warning generation](https://ieeexplore.ieee.org/document/6405009). 2012.
Underwater wireless sensor network (UWSN).
This paper highlights the physical layer challenges in establishing a reliable,
low power consuming and long life UWSN system for early warning generation.

## Context aware computing

Context aware services. Social robots, domotics/smart-home.

Human Activity Detection

* Audio-Based Human Activity Recognition Using Non-Markovian Ensemble Voting. 2012. Johannes A. Stork. 50 citations.
* Audio-Based Human Activity Recognition with Robots. 2011. Johannes A. Stork.
* [Transfer Learning for Improved Audio-Based Human Activity Recognition](www.mdpi.com/2079-6374/8/3/60/pdf). 2018.
* A Similarity Analysis of Audio Signal to Develop a Human Activity Detection. 2017, A García-Hernández.


## Techniques

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


## Fun stuffs

* Detect clapping and its sound level, for instance in a conference


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
* How to find the most efficient feature representation for audio classification.
Ex: Time window range, time resolution, frequeny range, frequency resolution.
Answer may be class dependent, but also inter-class. Can one do a per-class search to simplify?

Keywords

* Energy efficiency, energy budget
* Communication link budget
* Privacy
* Cost


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

CARFAC aka CAR-FAC, Cascade of Asymmetric Resonators with Fast-Acting Compression

* [Using a Cascade of Asymmetric Resonators with Fast-Acting Compression as a Cochlear Model for Machine-Hearing Applications](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/37215.pdf). Richard F. Lyon, 2011.
* Coclear model. PZFC. Pole-zero filter cascade.
Non-linearity. Feedback in AGC models saturation.
Computational load, approx that of a second-order filter per output channel.
Typical number of channels = 7?
* Converted to Stablilized Audatory Image (SAI). Using STFT?
* Local multi-scale sparse features.
Using Vector Quantization. Bag of Features representation of a file.
High dimesionality, 100'000 dimensions.
Fast online training using Passive Agressive classifier
* [CARFAC reference implementation in C++](https://github.com/google/carfac)


### Directional Derivative Features
A generalization of delta-features for arbitrary angles.

Comparing Time-Frequency Representations for Directional Derivative Features
https://www.researchgate.net/publication/269097301_Comparing_Time-Frequency_Representations_for_Directional_Derivative_Features
Found cube-root compression to be good, both on Gammatone and Mels.
Directional Derivative Features computed from a Steerable Pyramid Filter-bank.


### Preprocessing

* A-weighting
* Log transform
* Harmonic-percussive-residual source separation. Especially for music.
* Per-channel energy normalization (PCEN).
Static version exists as [librosa.pen](https://librosa.github.io/librosa/generated/librosa.core.pcen.html).
Can also be learned as a neural network layer, see arXiv:1607.05666v1
[Per-Channel Energy Normalization: Why and How](www.justinsalamon.com/uploads/4/3/9/4/4394963/lostanlen_pcen_spl2018.pdf).

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




### Feature learning

Feature learning

* Aka feature construction
* Supervised/unsupervised dictionary learning
* Sparse coding. Unsupervised
* Non-negative matrix factorization. Unsupervised
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

[On Random Weights and Unsupervised Feature Learning](http://www.robotics.stanford.edu/~ang/papers/nipsdlufl10-RandomWeights.pdf).
ICML2011. References works showing that random convolutional kernels can do suprisingly well.
Suggesting that one important baseline should be random + linear classifier.
Uses this for fast CNN architecture search.

[DCASE 2017 TASK 1: Acoustic Scene Classification Using Shift-Invariant Kernels and Random Features](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/challenge_technical_reports/DCASE2017_Jimenez_186.pdf). 6k random features. Performed 4% points better than baseline with Gaussian kernel. Random features can be used as privacy measure, keeping the W,b parameters private.
[Another copy](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/workshop_presentations/DCASE2017Workshop_Jimenez_195_presentation.pdf).
[ACOUSTIC SCENE CLASSIFICATION USING DISCRETE RANDOM HASHING FOR LAPLACIAN KERNEL MACHINES](http://www.mirlab.org/conference_papers/international_conference/ICASSP%202018/pdfs/0000146.pdf). IEEE paper.
Uses a linear SVM with random features to approximate a non-linear kernel SVM. Avoids expensive computation of high-dimensional kernel.
Approximates a shift-invariant kernel, like Gaussian, Laplacian and Cauchy.
Allows XOR Hamming distance based similarity calculation. 
With hashing, can reduce data by 2**6 / 64 with minor loss in performance.


Papers

* Learning Sparse Adversarial Dictionaries For Multi-Class Audio Classification. 2017.
Uses adverserial and reconstructive learning, and can be directly used as a classifier.
* Dictionary Learning for Bioacoustic monitoring with applications to species classification


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

Hierarchical representation learning using spherical k-means for segmentation-free word spotting
https://www.sciencedirect.com/science/article/pii/S0167865517304166
For Handwriting recognition.

[Learning Feature Representations with K-means](https://cs.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf). Adam Coates, Andrew Ng. 2012.
Best practices for unsupervised learning of convolutional kernels using K-means.
Contrast/mean normalization. ZCA whitening.
6x6 to 8x8 image patches work well, with 500'000 examples, and 256 size codebook.
Suggest 2x2 or 3x3 average pooling.
Tips for multi-resolution and pooling.
Deep models using a 'receptive field' learning scheme. Tested on CIFAR-10.
! Suggests feature learning in separate image regions where they are expected to differ significantly.
This would be case along frequency axis in spectrograms.



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

Sound Intelligence
https://www.soundintel.com/
Founded in 2000. 50+ employees?
SigardTM, detects verbal aggression. For use with video surveillance
Utrecht, Netherlands.

Auphonic
Automatic audio post production web service.
Has desktop and mobile apps also.
http://auphonic.com/
Levelling, audio restoration,
Encoding.
Metadata insertion, chapter marks.
Content deployment.
1-2 USD per hour processed.

## Interesting software

* [librosa](http://librosa.github.io).
* essentia
* [muda: Python library for augmenting annotated audio data](https://github.com/bmcfee/muda)
* [kapre](https://github.com/keunwoochoi/kapre). On-demand GPU computation of melspectrograms, for Keras

## Smart home assistants

[Whisper to Alexa, and She’ll Whisper Back](https://developer.amazon.com/blogs/alexa/post/c0e7798d-32bc-4549-9c24-97d204a7bf3a/whisper-to-alexa-and-she-ll-whisper-back). Tech details from researcher on whisper detection


# Lecture notes

Audio Classification.
http://www.cs.tut.fi/~sgn24006/PDF/L04-audio-classification.pdf
Covers low-level features, MFCC. Classification by distance metrics. GMM. HMM.



# DCASE2018 model complexities

## Task1a
C: 5k - 256M. Most models 1M++.
Best performing: 81%, 1M size.

Interesting

* Fraile_UPM_task1a_1		62.7 %	5k. MLP.
* Waldekar_IITKGP_task1a_1		69.7 %	20k. SVM, 3 ensembles.
* DCASE2018 baseline		61.0 %	116k. CNN. 

## Task1b
C: 20k - 22M. Most models 1-10M. Best: 62%. 

Interesting

* Waldekar_IITKGP_task1b_1 56.2%	20k. SVM, 3 ensembles.
* Ren_UAU_task1b_1 60.5 %	616k. CNN.

## Task2
C: - 425M. Best: 0.9538 mAP@3, 
Almost all models had 0.90-0.94 perf. 1M++ complexity.

Interesting

* Han_NPU_task2_1	0.8723  24k. CNN, 2 ensembles.
* Nguyen_NTU_task2_2	0.9251. 652k. CNN	

## Task3
Missing complexity data!

## Task4
C: 126k - 24M.

Interesting

* Koutini_JKU_task4_1		21.5 %	126k
* Liu_USTC_task4_2		28.8 %	534k


### Compressed sensing
Aka compressive sensing.

[A Systematic Review of Compressive Sensing: Concepts, Implementations and Applications](). 2018, IEEE Access. MEENU RANI.
Accessible intro, good diagrams. Table over Number of Required Compressive Measurements with different random methods.
Including structured random and determenistic, which does not have to be sent along with signal.
Acquisition strategies: RANDOM DEMODULATOR, MODULATED WIDEBAND CONVERTER (MWC), RANDOM MODULATION PRE-INTEGRATOR (RMPI), RANDOM FILTERING,
COMPRESSIVE MULTIPLEXER, RANDOM EQUIVALENT SAMPLING (RES), RANDOM CONVOLUTION, QUADRATURE ANALOG-TO-INFORMATION
CONVERTER (QAIC), RANDOM TRIGGERING-BASED MODULATED WIDEBAND COMPRESSIVE SAMPLING (RT-MWCS).
! Random Filtering seems easy and applicable to streaming data.
Recovery methods.
Basis Pursuit, Basis Pursuit Denoising (BPDN), Dantzig Selector, Total Variation Denoising (TV).
Convex optimization: BP simplex, BP interior...
Greedy algorithms. Faster but requires knowledge of signal sparsity.
Matching Pursiot, Orthongonal Matching Pursuit.
Compressive sampling matching pursuit (CoSaMP) and subspace pursuit (SP).
Iterative hard thresholding (IHT), Iterative soft thresholding (IST), approximate message passing (AMP).
Fourier sampling, heavy hitters on steroids (HHS), chaining pursuits and sparse sequential matching pursuit. 

Applications in MRI, 3d-imaging, hyperspectral imaging, ultrasound imaging.
DiffuserCam, [Lensless single exposure 3d-imager](http://nuit-blanche.blogspot.com/2017/10/diffusercam-lensless-single-exposure-3d.html).
[3d-ultrasound with single sensor](http://nuit-blanche.blogspot.com/2017/12/compressive-3d-ultrasound-imaging-using.html)

[Introduction to Compressed Sensing](http://www.dfg-spp1324.de/download/preprints/preprint093.pdf). !!

[Compressed Sensing: The big picture](https://sites.google.com/site/igorcarron2/cs).
Acquiring and recovering a sparse signal in the most efficient way possible (subsampling) with the help of an incoherent projecting basis.
Buildling sensing hardware that can directly produced such compressed signals.
Sparse means signal of interest is compressible. Challenge: Need to know with which family of functions it is sparse.
Fourier,polynomials,wavelets.
Many approaches to finding sparse representations/sparse dictionaries. Page lists 11.
Donoho-Tanner phase transition diagram, tool for evaluating whether a signal is compressible with an L1 solver.
Lists a set of 10 different conditions needed to enable sparse recovery.
Lists some 40 different solvers, until 2013.

[Convolutional Dictionary Learning: A Comparative Review and New Algorithms](https://arxiv.org/abs/1709.02893). 2018.

[Single-sensor multispeaker listening with acoustic metamaterials](http://people.duke.edu/~yx35/reprints/Cocktail_party_listener_PNAS2015.pdf)
Hardware approach to multi-source separation. Using 3d-printed waveguides, single sensor.

[Compressive Sensing](https://link.springer.com/referenceworkentry/10.1007%2F978-0-387-92920-0_6). 2011.
Introduction and overview on both theoretical and numerical aspects of compressive sensing

[Compressive Sensing by Random Convolution](https://epubs.siam.org/doi/abs/10.1137/08072975X). 2009. !!
Demonstrates that convolution with random waveform followed by random time-domain subsampling is a universally efficient compressive sensing strategy. 

[Distributed Compressive Sensing](https://arxiv.org/abs/0901.3403). 2009.

[Sparse Representations, Compressive Sensing and dictionaries for pattern recognition](https://ieeexplore.ieee.org/abstract/document/6166711/).
2011, Vishal M. Patel. !!
Compressive Sensing (CS), Sparse Representation (SR) and Dictionary Learning (DL). 
Recent works in SR and CS have shown that if sparsity in the recognition problem is properly harnessed then the choice of features is less critical. What becomes critical, however, is the number of features and the sparsity of representation

Practical Compressed Sensing: modern data acquisition and signal processing. 2011. Becker.
One of the world’s first compressed sensing hardware devices, the random modulation pre-integrator (RMPI). The RMPI

[COMPRESSED SENSING OF AUDIO SIGNALS USING MULTIPLE SENSORS](https://www.researchgate.net/publication/257304755_Compressed_sensing_of_audio_signals_using_multiple_sensors). 2008. Anthony Griffin and Panagiotis Tsakalides.
Compares Signal Distortion Ratio (SDR) of Speech,Music,Birdcall,Impulsive type audio with DCT/DWT and basis/orthononal matching pursuit.
! Birdcall shows very high SDR, when using DCT. Good for denoising? 

[Effect of downsampling and compressive sensing on audio-based continuous cough monitoring](https://ieeexplore.ieee.org/abstract/document/7319816/). 2015. 98% at full rate. Undersampling to 400Hz 90%. Sampling with compressive sensing at 100Hz also 90%.


[A Comparative Study of Audio Compression Based on Compressed Sensing and Sparse Fast Fourier Transform (SFFT): Performance and Challenges](https://arxiv.org/abs/1403.3061).
References two other papers about compressed sensing in audio compression.
To obtain exact recovery, the rule of thumb is to apply incoherent sampling and taking measurements 4 times the sparsity level of the signal.
Orthogonal Matching Pursuit one algorithm for doing recovery.
Sparse Fast Fourier Transform can transform in sub-linear time.
Binning Fourier coefficients into a small number of buckets.
The recovery process reduces to extracting the location of the non-zero (index) elements in the matrix A and use them to order the sparse K signal, embed zeros in the other locations and perform inverse FFT.
Considerably simpler than the general compressed sensing case.
Propose an innovative way to embed the indices in the extracted largest frequency bins to relax the need for extra coded values.
! Only tested on a single, unspecified audio file, 15 seconds long.

[A compressive beamforming method](https://ieeexplore.ieee.org/abstract/document/4518185/). Direction of Arrival estimation.

