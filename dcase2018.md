
# DCASE2018 workshop notes

## Overall
150 attendees.
90 last year.

## Keynote Monday
Herve Glotin

Bioacoustics

Physteter
Biggest  dolphin
up to 20 meters
endangered

Hear sonar
clicks

dive 1000 meters deep
studying them

sound consists of multiple pulses


### 1d tracking.
Long-term spectral average
Jan Schuter

### Stereoscoptic
Dual hydrophone, 1.83m aperture
Placed at the entrance of national park
Using time-delay to detect crossing and direction. TDOA
Counting waves going in and out

### Quadrophonic
JASON sound card
5 channel, 1MSamples/channel
antenna with 4 hydrophones,
another nea surface
using 9-DOF MPU to know position of

clicks increase in frequency
when no clicks, eating the prey
3-dimensional tracking of whale.
Show in rich 3d animation
3 kilometers away

Denoising TDOA with Autoencoder
Stereo autoencoder
Creates an latent representation, embeddings
Unsupervised learning
Using T-SNE in 2d to plot clusters
2dB SNR robustness improvement

Noise from boats

### Welcome to collaborate
http://sabiod.org

### Questions

What is the calibrated precision of the system?

Can it be that one is hearing the reflections,
from the cliffs/bottom, and not directly the animal?

Sperm whales also recycle air.
Can it be that some silences are for this reason, not for foraging?

To which extent do these techniques apply in air?

343 m/s in air; it travels at 1,480 m/s in water

## DCASE challenge 2018

Growing year over year. 2013,2016,2017, 2018

81 participating teams

Tasks organized by different teams,

Welcome proposals on new tasks.

### Task 1. Acoustic Scene Classiication
10 classes. 3 subtasks.

A) single device
B) mismatched devices
C) with A, but allowing external data

Recordings from many places in Europe.

### Task2. 

Frederic Font
UPF. Barcelona
Maintain Freesound
Improve free software
AudioSet release
Kaggle/Google wanted audio challenges

41 categories
multi-class classification. Plan for multi-label tagging

558 teams on Kaggle. Only 20 for DCASE.
Lots of people shared their code,knowledge in Kaggle forums


### Task3. Bird audio detection

Generalization task. Mismatched.
Huge variation between different sets.

### Task4. Domestic
Weak labels. Small labeled.
10 classes, selected from AudioSet.
Not so much source code submitted. Want more of that.

### Task5
Microphone array.
Unknown locationzation relative to sound source.
Spectral and Spatial information.
4-channels arrays. 7 arrays. Some for test, some only for validation.1
12 team totals.
Only 4 teams used spatial features.
Graph of mismatched performance. Dev versus test.

### Making sense of sound challenge
High-level classes. Broad "categories"
Based on lower-level classes. Dendrogram
From FreeSound

## Mosquito detection

Mosquittos kill 750k people every year
Some particular species carry
Want a map of where mosquittoes are

Mosquittoe use sound to communicate to eachother
Trained mosquitto researches can detect mosquitto subfamilies
3500 species
Mosquitto 'flight tone'. Harmonic structure.
Many very challenging.

Mozz Wear mobile app.

Capture mosquttios, record their sound.
Some tens,hundreds
Need to bait with humand or cows.

Prefer mel-spectrogram.
Performs similar to MFCC, but more interpretable.

0.1 second audio clips.
7-way species classification.
60% accuracy.

Want early warning systems.
Using 20 dollar smart-phones.

### Questions
How to avoid False Positive from non-Mosquitto sound?
Currently not comparing for . Small dataset. 

Emitting carbon dioxide attacts the mosquittos.
Use dry-ice for this.

Interesting to have an autonomous sensor device?
Needs continious production of CO2.


## lasseck 
Highest performing system DCASE2018.

Animal Sound Archive, Museam fuer Naturekunde Berlin.
Focus on data augmentation

Split folds by dataset, to estimate handling mismatch.
2 folds with 2+1.

Cutoff 2kHz.

Pre-trained networks. InceptionV3,ResNet152.
Replaced fully connected layer.
Fine-tuned the model

ImageNet not allowed! Had to re-train from scratch

4 second audio chunks. Selected randomly inside 10 second.
Resized to fit image input. 

### Data augmentation
Jitter audio chunk length.
TIme stretching. Global, piecewise local.
Frequency stretching. Global, piecewise local.
! nice GIF animations showing the augmentations.
Adding chunks with same labels.

LifeCLEF paper has details on augmentations used.
+14% total accuracy improvement total.

### Questions/suggestions

Error analysis bird detection.
Not performed.
D.Stowell. Extremely brief vocalization at low SNR, are typically what strong models confuse.
Ex. Raindrops.

## Domain adaptation for birdsound audio detection
Uni Kentucky
Non-passerine birds. Much more low frequncy information.
Background in bioacoustics. Marine, elephants,
Used for a long time Hidden Markov Models.

* Adjust time,frequency resolution
bulbul used 45ms. Used very shorter. HMM typical 5ms.
bulbul used 80 bands.
* Signal enhancement
Noise different for different sets.
Hypothosis: Reducing noise, 
LSA with IMCRA noise tracking.
* Direct domain enhancement
From image classification litterature.
Used CORAL. 'Whitening'. Recolors second-order statistics
Normalized in the frequency domain.
Tranfered "to" the warblr set, from each dataset.

Within-dataset performance, cross-dataset performance

### Domain adaptations
Individually, did not really improve?

### Ensembles
Boosting. 86% -> 90%


## Dealing with weakly labeled

10-class problem.

Baseline model.
3 layer CNN.
Semi-supervised method: Two-pass
First pass with model trained on weak labels.
Use this model to annotate unlabeled set.
Train second, stronger model.
F1 7.5% first pass, 11% second pass.
Best system: F1 32.4%

### MMM loss function
Veronica Morfi

MMM loss function. Uses min, mean/2, max
Also tested mean/2 + max, which did basically as well


## Keynote Day 2
Fraunhofer IDMT. Erlangen

Acoustic condition monitoring. Condition=some process or states
Sound -> Hearing -> Consideration -> Decison 
Sound -> Sensor -> Apprisal -> Processing -> Decision

Motivation: Increase efficient, product flexibility
Challenes: Complexity, invesments, security

Monitoring systems.
Auality Assurance. Predictive maintenance, end-of-line testing
Acoustic Control advantages: non-destructive, contactless, retrofittable

What model to choose?
Training data?
Expert annotations?
Data aquisition? Costumer constaints?
Online, offline decision making?
Sensitive data. What data can be transmitted/stored?
Expected quality? What quality is useful?
Deployment, integration

Privacy & Security
- Secure data aquisition, transmission, storage
- Avoidance of data corruption (sensor identification)
- Decoupling real and pseudonym identity (pauth)

Data aquisition.
Their approach: get sample data as soon as possilbe.
Even if low quality, ie customer smartphone

Expert annotation is the bottleneck.
Can use side-information from existing monitoring system. ("oracle")

How to detect early that unable to meet needed quality, to avoid wasting time/money


### Usecase: Stadlarm project 'city noise'
Embedded. Sensor Network.
City of Jena.
Noise exposure: 3 residential areas surrounding
Systematic,distributed, continious acoustic noisemonitoring
Want objective measurement
Want to know why it was too loud

Do full analysis on acoustic sensor.
Transmit noise noise level, category classification.

Sensor Unit.
Based on Raspberry PI 3 Compute Module.
Industrial rated components
M.2 slot for modem
Hanging from a lamp. Gets power during the night.
Battery keeps it running during the day 
Microphone at the bottom

Noise measurements.
German DIN normas. TA-Larm
Law defines sound event level, average sound level
8 measurements per second

Classification.
14 classes.
5 scenes. Msuice Event, Public, Place, Roadworks, Sports Event, Traffic
... events.

Use data augmentation a lot.

Hybrid DNN. inspired by Trakashi, INterspeech 2016.
VGG architecture. 3layers

Used an audio clip 'medley' of noise sources,
plotted together with the activations of different classes.

Web application with full database available to the city.
Real-time and historical.
Merging event calendar.
Planned to be release to the public.

Now running a 6 month testing phase.
Plant o keep it running for at least one more year.

Future directions
Traffic mnitoring. Speed, vehicle type, count
Touristic recommendations

### Usecase: End of line test of motorized car seats.

Listening to the car seat.
Analysis is done on conveyer belt.
8 omni microphones.
Need to make decision right away:
Product is either accepted or rejected

Customer requirements: C library for LabVIEW.
Using small neural networks.
Models specific to motor types.

### Usecase: Tunnel digging machine
Single machine that digs the entire tunell.
Huge. Lots of different parts. People working around.

Work in crews on shifts. Each shift gets a different number of meters.
Want to have measurements that can explain this variatio.

Training models specific to each tool.
Inferring from the activity, what the crew is doing.

Acoustic monitoring is a big topic right now. "will be much bigger"

Hanna Lukashevich.
Hanna.Lukashevich@idmt.fraunhofer.de

### Questions
VGG style network on RPi. Was it hard to make it work?
Not a big challenge. Using a small network.
Running on standard Keras. Some optimization. 



# Model complexities

For the various parts of DCASE2018 challenge.
Looking to find more efficient models.

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

