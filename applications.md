
# Applications

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
* Acoustic triggering of camera traps

[On the Design of a Bioacoustic Sensor for the Early Detection of the Red Palm Weevil](https://www.researchgate.net/publication/325006988_Sound_Analysis_and_Detection_and_the_Potential_for_Precision_Livestock_Farming_-_A_Sheep_Vocalization_Case_Study). Detecting a pest that attacks palm trees.


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

### Birds

Datasets

* http://www.kaggle.com/c/the-icml-2013-bird-challenge
* https://www.kaggle.com/c/mlsp-2013-birds/
* https://www.xeno-canto.org/


[Robust feature representation for classification of bird song syllables](https://asp-eurasipjournals.springeropen.com/articles/10.1186/s13634-016-0365-8). Maria Sandsten, EURASIP Journal on Advances in Signal Processing, 2016.
A novel feature set for low-dimensional signal representation, designed for classification or clustering of non-stationary signals with complex variation in time and frequency. Applied to birdsong and *within-species* classification.
Ambiguity spectrum. Multitapers. Singular Value Decomposition.

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

### Agriculture

Machinery

"Real-Time Acoustic Monitoring of Cutting Blade Sharpness in Agricultural Machinery"

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


# Music

Musical composition

* [Harmonizing Pop Melodies using Hidden Markov Models](https://luckytoilet.wordpress.com/2017/04/25/ai-project-harmonizing-pop-melodies-using-hidden-markov-models/)

Music or not?

* [Changing FM stations on ads!](https://medium.com/@kshitij.d1989/deep-learning-experiment-changing-fm-stations-on-ads-c1a0a1f96bf1).
Binary classification, music or ad. Based on radio station.
2x100 samples. 80% val acc. Keras. MFCC. Code and dataset available.

Music remixing

* [Audio AI: isolating vocals from stereo music using Convolutional Neural Networks](https://towardsdatascience.com/audio-ai-isolating-vocals-from-stereo-music-using-convolutional-neural-networks-210532383785)
* [Audio AI: isolating instruments from stereo music using Convolutional Neural Networks](https://towardsdatascience.com/audio-ai-isolating-instruments-from-stereo-music-using-convolutional-neural-networks-584ababf69de)

