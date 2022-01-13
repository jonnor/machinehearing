
# Title
Monitoring noise, machinery and processes using sound and machine learning 

# Related

- 2022-02-24: Dan Stowell, Tilburg University. Deep models of animal listening perceptual tasks
- 2021-11-18: Martin Willbo, RISE. Few-shot learning for sound event detection
- 2021-11-04: Tuomas Virtanen, Tampere University. Machine learning for acoustic scene analysis


# Abstract

Many physical events and processes create sound, often in the hearable spectrum.
This makes sound an interesting source of information about such processes.
By combining sound sensors with machine learning, these can be tracked and analyzed.
Here we will discussed how we have applied this to several different usecases, including:
Noise Monitoring of shooting ranges and construction sites,
Process Monitoring of coffeebeans cracking during roasting,
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

Task formulations
- Audio Classification
- Sound Event Detection
- Anomaly Detection

Continious monitoring challenges
- Class imbalance
- Interpretable models
- Privacy
- Edge processing

Audio ML
- Spectrograms
- Time-windows
- Convolutional Neural Networks

