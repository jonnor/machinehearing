

Combining soundlevels and classifications/detection

# Deadline
December 1

## Theme / T10 S04
T10 S04


## Abstract Format
< 300 words

- Title of the abstract: capitalize all words, for example "NOISE CONTROL OF HYDRAULIC PUMPS".
- Authors' names (Last name first, like "Einstein, Albert")
- The abstract should be presented in one paragraph.
- Do not include references or key words into the abstract.


# Title
Tracking number of gunshot noise events using multiple wireless sensor nodes

ICSV28: ALL CAPS

# Keywords
Shooting range, impulsive noise, Sound Event Detection, wireless sensor network, noise monitoring

# Abstract

Shooting ranges are subject to noise regulations,
which may include a limit on the number of total number of gunshots per year.
This number of noise events is often used to estimate the overall noise contribution,
using ISO 17201-5 or similar.
This makes it desirable to track the number of gunshots fired at the shooting range when in operation.
It allows to to compare the actual numbers to that stipulated in regulations,
to estimate if the facility is operating at, below or above capacity.
We describe a method of tracking the number of noise events using wireless acoustic sensor nodes,
where machine learning is used for sound event detection of the gunshots.
In particular we focus on larger facilities with multiple shooting ranges,
where multiple sensors are required to cover the entire area.
This raises the challenge that some noise events may be picked up by multiple sensors,
neccessitating a strategy for ensuring that such events are not counted multiple times.
As the sensors have separate clocks there may also be time-misaligment to account for.
We compare multiple strategies for estimating a total number of events,
and evaluate their performance using data from a site in Norway.


## InterNoise 2021

Abstract & Registration Open 	1st December 2021
Abstract Submission Deadline 	4 February 2022
Abstract Notification 	4 March 2022
Paper Submission Opens 	4 March 2022
Paper Submission deadline (requiring assessment) 	4 April 2022
Non Assessed Paper Submission deadline 	29 April 2022
Early bird registration deadline for authors 	29 April 2022

200 words max

I intend to attend the conference in person, but will be happy to pre-record and submit my presentation for online transmission should I subsequently be unable to travel.

Environmental Noise
9.13 Smart Cities and Noise Monitoring

## ICSV27

Abstract Deadline: 31 January 2022
Notification of Acceptance of Abstracts: 20 February 2022
Deadline for Full-Length Submission:    31 Mar 2022
Notification of Acceptance of Full-Length Papers: 20 May 2022


https://www.icsv28.org/index.php?va=viewpage&vaid=41&form_macro_id=10#Macro


# Background


ISO 17201 - Acoustics. Noise from shooting ranges
https://doi.org/10.3403/BSENISO17201

Part 1 Acoustics. Noise from shooting ranges. Determination of muzzle blast by measurement
Part 2 Acoustics. Noise from shooting ranges. Estimation of muzzle blast and projectile sound by calculation
Part 3 Acoustics. Noise from shooting ranges. Guidelines for sound propagation calculations
Part 4 Acoustics. Noise from shooting ranges. Prediction of projectile sound
Part 5 Acoustics. Noise from shooting ranges. Noise management

TODO, get these standards, read them through
https://www.standard.no/no/Nettbutikk/produktkatalogen/Produktpresentasjon/?ProductID=248731


### ISO 17201-5

The following management scheme allows the sound impact of a shooting range on a neighbourhood to be estimated.
The usage is expressed by the sum of the number of shots, nk,
of all source combinations, k,
that contribute to immission class i.
The contribution of one shot of source combination, k,
is expressed by its longterm averaged sound exposure level LE,A(k) at the reception point, which is used to assign immission class i to this combination.

Using the number of shots within each immission class, the quota count (QC) for each reception point is calculated.
The QC is directly related to the specified value set by the management, which is the equivalent continuous sound pressure level of all shots.
This value is related to the rating level by possible additions.
From the equivalent continuous sound pressure level the sound emergence can be obtained,
if the background sound pressure levels are known.
If an event index is used, the QC concept can be modified to
take into account only those shots which are above a specified limit. For other evaluation schemes, the QC
concept may not be applicable. 

The background sound pressure level can be evaluated by using a percentile level such as LA,90 or LA,95 for an appropriate time period.
The time period should be specified and should not be less than half an hour.
The value obtained shall be representative for the evaluation period of the shooting range and shall not contain unusual events. 

>  It is assumed that the management knows the usage of the range in form of all nk shooting numbers

###  The Swiss shooting sound calculation model sonARMS
2011

https://www.academia.edu/16963094/The_Swiss_shooting_sound_calculation_model_sonARMS

Sound propagation wrt meterological effects inheritet from sonRAIL
Designed for medium to long distances. 1 km

Estimates short-time time series

