
# Title
Automatic Detection Of Noise Events at Shooting Range Using Machine Learning

# Abstract

Outdoor shooting ranges are subject to noise regulations from local and national authorities.
Restric-tions found in these regulations may include limits on times of activities, the overall number of noise events,
as well as limits on number of events depending on the class of noise or activity. 
A noise monitoring system may be used to track overall sound levels,  but rarely provide the ability to de-tect activity or count the number of events, required to compare directly with such regulations.
This work investigates the feasibility and performance of an automatic detection system to count noiseevents. 
An empirical evaluation was done by collecting data at a newly constructed shooting rangeand training facility.
The data includes tests of multiple weapon configurations from small firearmsto high caliber rifles and explosives, at multiple source positions, and collected on multiple differentdays.
Several alternative machine learning models are tested, using as inputs time-series of standardacoustic indicators such as A-weighted sound levels and 1/3 octave spectrogram, and classifiers suchas Logistic Regression and Convolutional Neural Networks. Performance for the various alternativesare reported in terms of the False Positive Rate and False Negative Rate. The detection performancewas found to be satisfactory for use in automatic logging of time-periods with training activity.

## Format

Maximum 12 minutes
Approx 10-12 slides

## Outline

- Introduction

Welcome to this presentation
of our paper
Automatic Detection Of Noise Events at Shooting Range Using Machine Learning

My name is Jon Nordby
and I am presenting on behalf of my co-authors
Fabian Nemazi
Dag Rieber

This work was in a collaboration between
Soundsensing and Politiets Nasjonale Beredskapsenter
PNB for short

- PNB

PNB is a combined training facility and operative base for the police special forces in Norway
It is located in close proximity to Oslo center and the surrounding urban area, to ensure quick response times

Outdoor shooting ranges for firearm training
Training facility for explosives

The nearest residential area is around 1.2 kilometers away from the site,
both to the west and to the north

A large amount of resources and effort has been put to ensuring that noise impact is minimal
including allowed firing directions at shooting range,
the construction of large earthwalls and noise barriers,

The facility also has a helicopter landing pad,
but helicopted noise was not included in our project
as it was considered well monitored through the aviation logbooks

## Regulations


## Project goals



## Data collection

Data was collected while the site was still being constructed

Testing of noisemap calculation
Following protocol from Norwegian guidelines M-128
1 event per 30 seconds, with series of 10 events
In worst case weather-conditions for noise propagation,
and the most noisy weapon configurations, locations, directions

Placed one recording unit at central location,
and one per training area

Recordings showed that the central unit picked up
all events with good clarity
So all analysis was done with data only from that device

## Synthetization of dataset

To make the dataset more realistic,
including higher density of , occational overlapping events,
a dataset was synthesized by
mixing the original noise events
with different backgrounds

We set the loudness of the noise events
to be same or lower as the originals,
to ensure the task was hard enough to reflect challenging conditions

Salamon, et.al
Scaper: A library for soundscapesynthesis and augmentation,
IEEE Workshop on Applications of Signal Processing to Audioand Acoustics (WASPAA), 2017

Gontier et.al
An efficient audio coding schemefor quantitative and qualitative large scale acoustic monitoring using the sensor grid approach
MDPI Sensors, 2017

## RandomForest model

Our simple baseline model was a Random Forest on hand-engineered features from soundlevels

## CNN model


## Results


- Outcomes

PICTURE. Logbook

- Further work

Label noise

Determining the origin of impulsive noise events
using wireless sound sensors
Fabian Nemazi, 2021


## Blaa


- Acknowledgements

Work has been funded though a collaboration between Soundsensing AS and Politiets Nasjonale Beredskapsenter construction project,
led by Paul Torgersen at Marstrand.
In the first months of the project,
Soundsensing received funding from the Research Council of Norway as part of the program STUD-ENT.

Organization of acoustical tests was lead by Lars R. Nordin at Brekke & Strand AS.
Data collection for Soundsensing AS was performed by
Erik Sjølund and Ole Johan Aspestrand Bjerke. 


- Background
Soundsensing, Noise Monitoring
PNB. Training facility. 1 km to neighbours
Police National Emergency Response Center
