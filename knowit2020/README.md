
# Context


## Format

35 minutes, 10 minutes QA

## Title
Classification of environmental sound using IoT sensors


## Audience

Developers

- Most are not familiar with sound
Samplerate, spectrograms etc
- Maybe familiar with Machine Learning
Supervised learning. Convolutional Neural Networks.
- Not familiar with Internet of Things

## Scope

Focused on **Audio**
Especially Continious Monitoring scenarios
with applications in Industrial IoT
But techniques described here are
applicable to Music
and somewhat applicable to Speech

Focused on **Classification**
but tasks like
Audio Event Detection
Anomaly Detection
builds on the same basic foundation

Take people (quickly) through the entire process
From problem identification
data collection
model building
system deployment

Style.

Less code/model details than EuroPython/PyCode
A bit higher level.
Showcase more Soundsensing offering,
how it helps


If you have an application for audio ML,
you should now have a good understanding of the overall process
of designing a solution for this

If you have a continious monitoring scenario,
consider using Soundsensing sensor and data platform



# Goals

From Soundsensing POV

1. Attract partners
Customization/**integration** providers
2. Attract potential employees
2 full stack developers. 1 frontend-lead
3. Attract investors
Raising money now. Opportunities for angels.
4. Attracting pilot customers
Usecases that can be done based on existing/planned offering

From audience POV

> you as developers, understand:
>
> possibilities and applications of Audio ML
> 
> how the overall workflow of creating an Audio ML solution is
>
> what Soundsensing provides to make this easier

## Takeaways

- Machine Learning on Audio is now very powerful, with many interesting applications
Expected to become more efficient and affordable in the

- If you have an Audio ML task
identify what information is needed. Time resolution etc.
choose task formulation AC, AED, AD
collect audio data. Can use standard recorders. Mobile phone, AudioMoth
Annotating tool. Audacity, AudioAnnotator 
start with (log mel) spectrogram
Convolutional Neural Network as a base

Tricks. Data Augmentation. Self-supervised.


- Soundsensing has a sensor and data platform
Install the sensors, turn them on, and data is available in an API.
Customers or **Partners** can then build ML solutions on top of this. 
Can also put ML models on device

- Running pilots now, open for more in the fall
If you have an application of the technology, come talk to us

- Interesting place to work.
Cutting edge development
Fast growing field. ML+IoT
Have internships available now
Hiring two developers in 2019

 
## Talking points

- ML on audio close to human-level performance on some tasks
(when not compute constrainted)

- On-edge inference is desirable to keep data traffic down.
Enable battery power / energy harvesting - cheaper installation costs - denser networks.
Lower data traffic - cheaper wireless costs.

- ML-accelerators for low-power sensor units are expected in 2020

- Soundsensing has developed a low-power sensor unit and data platform for.

First application is Noise Monitoring, Acousticians as customer group

Running pilot projects with customers now.

- Strong cross pollination from bigger ML domains.
Image and Natural Language Processing pushes Audio forward
CNNs. Sequence modelling (RNNs).

## Calls to action

- Come talk to us about applications of Audio ML



## Offering

Can use Soundsensing as:
- infrastructure provider
- end2end user solution 

ML solution/infrastructure.
What Soundsensing provides, integration points for customer/partner
Layer cake

Infrastructure

- Data aquisition
- Data transport
- Data storage
- Sensor fleet management

DB-10 as one of many sensor possibilities


Models

- Audio Classification
- Audio Event Detection
- Anomaly Detection

Interfaces

- HTTP API
- User interface
Integration with 3rd party systems

Application

- Noise Monitoring
- Condition Monitoring

Target Markets

- Acousticians
- Construction
- Office
- 

- Manufacturing
- Real-estate
- 



# Outline


Introduction

- About me
- About Soundsensing

Scope
- 

## More

Check http://github.com/jonnor/machinehearing
How to make a small model for on-edge usage. SenseCamp2019
More in-depth on model building, training setup. EuroPython2019

