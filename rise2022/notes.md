
# TODO

- Import slides from EuroPython 2019
- Finish first slide
- Add QA slides
- Add ending slide
- Add introduction slides
- Import slides from AD/CM slidedeck
- Make reference slides pointing to other works

14.45, join
- https://rise.zoom.us/j/208117140


# Title
Monitoring noise, machinery and processes using sound and machine learning 

# Related

- 2022-02-24: Dan Stowell, Tilburg University. Deep models of animal listening perceptual tasks
- 2021-11-18: Martin Willbo, RISE. Few-shot learning for sound event detection
- 2021-11-04: Tuomas Virtanen, Tampere University. Machine learning for acoustic scene analysis

# Bio

Jon is a Machine Learning Engineer that specializes in audio and IoT applications.
He has a Master in Data Science and a Bachelor in Electronics Engineering,
and has worked as a software engineer in electronics and web projects for 10 years.
Since 2019 he is the Head of Machine Learning and Data Science at Soundsensing,
a provider of IoT sensors for sound with built Machine Learning capabilities


# Abstract

Many physical events and processes create sound, often in the hearable spectrum.
This makes sound an interesting source of information about such processes.
By combining sound sensors with machine learning, these can be tracked and analyzed.
Here we will discuss how we have applied this combination for several different usecases, including:
Noise Monitoring of shooting ranges and construction sites,
Process Monitoring of coffeebean cracking during roasting,
and Condition Monitoring of equipment such as pumps and ventilation.
We will discuss some of the techniques in use,
such as Convolutional and Recurrent Neural Networks, spectrogram pre-processing,
and edge computing on embedded devices and microcontrollers.
We will also discuss some of the challenges that come when deploying continious monitoring,
such as data collection, heavily imbalanced data and preserving privacy.

# Disposition

## Primer on Audio ML 
10 minutes
Ref EuroPython 2019
Ref EuroPython 2021

- Sound is a mixture
- Digital audio
- Analysis windows
- Spectrograms
- Common classification models
(Convolutional Neural Networks, Recurrent Neural Networks)
- Temporal aggregation
- Common task formulations
(Audio Classification, Sound Event Detection, Anomaly Detection)
- Q & A

Out-of-scope.
Speech/language modelling. Music modelling.
Tasks like speech enhancement. Source separation.

## Process Monitoring
Coffeebean cracking
10 min
Ref TinyML EMEA 2021

- Q & A

## Noise Monitoring
Shooting range activity
10 min
Ref ICSV27
Ref EuroNoise 2021

- Noise Monitoring
- Q & A

## Condition Monitoring
Of machinery
10 min

Ref DCASE 2021, Task 2

- Rotating machinery
- Vibration analysis
- Data collection
- Q & A

## Topics

Usecases

- Noise Monitoring, shooting range activity
- Process Monitoring, coffee
- Condition Monitoring, machines

Audio ML

- Spectrograms
- Time-windows
- Convolutional Neural Networks

Task formulations

- Audio Classification
- Sound Event Detection
- Anomaly Detection

Continious monitoring challenges

- Privacy
- Compute contraints on edge devices
- Class imbalance
- Out of distribution
- Minimizing false positives

Out-of-scope

- Time alignment in asyncronous wireless (acoustic) sensor networks
- Interpretable models
- Labling data. 


## Challenges

### Privacy

On-sensor preprocessing.
Low-resolution spectrograms

On-sensor classification

## Edge compute constraints

Device classes

- Microcontroller
- Single board embedded
- Phone

"TinyML"

### Class imbalance

Determine natural balance.
Sample randomly, label.
Estimate from things known about the system
Typical number of occurrences
Typical duration per occurrence

Sound events: Short in time (< 1 second)
Machine failures. Very rare (< 1 per month)

31 million seconds in a year
PNB example
2 mill events per year max
0.2 sec duration
Best case imbalance of 78x


Lower temporal resolution
Aggregate in time
Illustration


Minority class upsamling with data augmentation

Synthetic sound mixtures
Especillay for Sound Event Detection
Scaper Python library


Eliminate times where output cannot be valid
May be outside of model, in the higher level sytem
Example Roest:
know that cracks cannot happen until beans have been heated up
know that cracks after beans have been dropped, ignored

Roest - with only relevant period
>>> (5*60)/(0.1*200)
15.0

### Out of distribution

Multi-label classification.
Use sigmoid instead of softmax.
Set threshold on probability instead of just picking highest

Integrate outlier detection
Can be a separate model
Running in parallel, before or after
Can also use the embedding layer of classifier

Monitoring. MLops style
Input statistics distribution
Output statistics distribution
Set alarms on deviations
Example: over 1 week at PNB, the number of events is typically be between X and Y
Large deviations a

Across all machine rooms for a customer,
number of anomaly alarms is typically between X and Y per month


Quantifying uncertainty with neural network
Monte Carlo dropout
Have not seen it used for audio/IoT/time-series

## Reducing false positives

Use simple explainable models as pre/post-filter "common sense"
Soundlevel and soundlevel rate-of-change
Cannot be gunshot/explosion type noise, if it is not a noise or impulsive noise at all
Example PNB

Eliminate times (mentioned under data distribution)

Secondary classifier.
Check agaist known-false-positives
Typically kNN
Supress alarm in this case
Especially useful for unsupervised / anomaly detection
Becomes labeled data for validation or semi-supervised train set


## Other presentations

- EuroPython 2019, Audio Classification
- EuroPython 2021, Sound Event Detection
- TinyML 2021, microcontroller CNNs, Environmental Sound Classification
- TinyML EMEA 2021, Roest coffeebean cracking
- EuroNoise 2021 paper/presentation
- ICSV27 paper/presentation
- Master thesis


## Goals

- Attract potential R&D collaborators
Joint funding opportunities
Internships this summer

## Audience prerequisites

- Application oriented talk.
Practical use-cases, practical challenges and solutions

- Do not need to know much about sound
- Familiarity with time-series beneficial


## Audience goals

- Know what Soundsensing does / offers
- Know some application/usecases of Audio ML - especially outside of speech/music
- Know basics of modern Audio ML for Audio Classification/Sound Event Detection/Anomaly Detection
- Know some of the challenges in continious monitoring

Conclusions

- Usecases should be treated briefly (ref separate talks/papers)
- Not so much on optimizing CNNs for TinyML use (ref talks/thesis)
- 




