
# Dominant Sound Classification and Dominant Sound Event Detection

An approach to classification of sounds for noise monitoring,
under the assumption of single-dominant-source.

# Task formulations

## Dominant Sound Classification

TLDR: Modification on (closed-set) Audio Classification,
where the output class shall be the one that contributes the most to the soundlevel.

Input

> Stream of audio. Consisting of sound events from multiple different sound sources.

Output

> Single class label. Being the class that contributed the most to the soundlevel.

## Dominant Sound Event Detection

TLDR: Modification on (monophonic) Sound Event Detection,
where the output class shall be the one that contributes the most to the soundlevel.

Input

> Stream of audio. Consisting of sound events from multiple different sound sources.

Output

> A stream of class activations over time one per point in time.
> The active class shall be the one that made the most contribution to the soundlevel.
> High resolution at output, corresponding with soundlevel measurement. For example LA_fast (125 ms) or LA_slow (1000 ms).

## Common
In addition to `{class0,class1....classN}`, also allow for two pseudo-classes: {unknown,mixture}

- `unknown` means the model cannot reliably detect the class.
- `mixture` means that the dominant-source assumption is violated,
there are multiple sources that meaningfully contribute to the overall noise level.


# Research questions

- How often is the single-dominant-source-at-a-time a reasonable assumption?
- How well can we attribute soundlevels to their class?

# Hypothesis

The big stuff

- The Dominant Sound assumption holds a lot of times in real Noise Monitoring usecases
- Using the Dominand Sound assumption simplifies analysis, and enables useful Noise Monitoring metrics
- Dominant Sound Classification can be done with standard Audio Classification methods,
given an appropriately labeled dataset.
- Dominant Sound Event Detection can be done with standard Sound Event Detection methods,
given an appropriately labeled dataset.

Small things that would be good to figure out

- Applying the same frequency weighting curve used for soundlevel to the spectrogram used for classification,
makes it easier for models to solve the Dominant Sound Classification / Sound Event Detection task.
At least with limited data and/or model capacity.

# Research methods

## How often is the single-dominant-source-at-a-time a reasonable assumption?

Or v.v., how often is the single-dominant-source-at-a-time assumption broken?
How often does two (or more) noise sources appear concurrently, where B is within 10 dB of A
Time resolution either 125ms (LAF) or 1 second (LAS).

#### Possible ways of answering

- Analysis of selected recordings in representative scenarios. Qualitative
- Statistical analysis of co-occurence, given simple models
- Analysis of real-world dataset covering many cases. Primarily quantitative

#### Simplified statistical analysis of co-occurrence

For example:
Given two noise sources, each active for 5 seconds at a time.
Say 30 seconds between each activiation.
Assume that they are independent from eachother.
What is probability of happening at same time?
ie overlapping by 1 second or more.
Model emission with Poisson?

Two variables: duration and .
Can compute probabilities of co-occurence as a table.

#### Small scale analysis

Pre-requisites: Identify some appropriate scenarios.

Could maybe select some time-periods
Say 10-30 seconds long
that are representative of whole dataset
analyze these manually
mark periods of single dominant, multiple contributions

#### Large scale analysis

If one had captured a mixture of these things, how would one analyse the data to answer this question?

statistical analysis
each source modelled as a soundlevel generating process
characterized by
a. sound level distribution
LAFeq for each time-step
b. emission probabilities


## How well can we attribute soundlevels to their class?

Measure in terms of dB. Ground truth computed from labels.
Requires a labeled dataset with suitable labels.



# Open questions
Things that need to be resolved to answer hypothesis or parts thereof.

## Noise Monitoring scenario/usecase
Which usecase are a good fit of the proposed method?

Method benefits scenarios where there are multiple noise sources,
and where discriminating between them is of interest,
particularly were it is useful to be able to "assign" each noise to a class.

In general, for measurement of human-created noise, we would like to separate out
Biophony and Geophony from Anthrophony.
Ref Soundscape Ecology.

Noise regulations tend to regulate based on noise sources.
In a mixed-environment, such as residential, multiple.
Road Noise vs Air Traffic vs Rail Noise vs Industrial vs Community vs Other.

Two types of uses:

A) Being able to do overall analysis of a soundscape/situation.
Over longer periods of time, say 1 week or more.
Need method to be unbiased.
Primarily on an aggegated/statistical level, not necessarily every single minute.

Compare per-class event counts, in aggregate
Compare per-class LAeq contribution, in aggregate

B) Being able to attribute particular (periods of) noise events to a source/class.
Need to have high precision for such events. And sufficient recall to actually be able to attribute, not just have "unknown".


## Choice of classes
Find and use established taxonomies/ontologies.
Preferably from the noise/acoustics area.
Or if not found, from audio machine learning area.

## Choice of datasets
Assuming that large-scale analysis is done.
Do appropriate datasets exist at all?

# Limitations

#### Ignoring of short-time temporal characteristics 
Each activation of a source has a short (soundlevel) sequence associated with it.
Assuming that LAF/LAS captures well enough.



# Ideas

## Synthetic datasets

Can synthesize mixtures to form a dataset.
Different dB ratios of A,B (might also need to have background noises C,D,E)
Train model to recover the dominant event. Or maybe to predict the dB ratio.
Should be powerful as a pre-training concept, to get large training sets, which should enable strong models.
Possible target for a follow-up paper.

## TinyML classification

The Dominant Sound Event Detection task should be solvable using SED systems that
can run on contemporary IoT Noise Monitoring devices.
Target for a follow-up paper.

## Generative modelling

Might be possible to have source activity as a binary
Maybe the activation patterns of sources can be Poisson

Could we formulate a generative model,
and fit it to real-world mixtures?
could test it on synthetic mixtures first,
to check if model is able to fit properly



# Paper

## Target publication

#### InterNoise

https://internoise2024.org

Deadlines

- Abstract deadline 09.02.2024
- Abstract notification 01.03.2024

Relevant session

- 2.5. Measurement Methods for Smart Cities and Noise Monitoring

#### ICSV

https://icsv30.org/index.php?va=viewpage&vaid=223

Non Peer-Reviewed Papers

- Abstract Deadline: 31 December 2023
- Notification of Acceptance of Abstracts: 15 January 2024
- Deadline for Full-Length Submission: 31 March 2024

Peer reviewed Paper

- Abstract Deadline: 31 December 2023
- Notification of Acceptance of Abstracts: 5 January 2024
- Deadline for Full-Length Submission: 31 March 2024
- Deadline for Full-Length Submission: 15 February 2024


# Related work


### Road Traffic Noise vs Anomalous Noise Event
Being able to separate Road Traffic Noise from other noise events has been studied,
and methods for this proposed and discussed in:

Development of an anomalous noise event detection algorithm for dynamic road traffic noise mapping
https://www.researchgate.net/publication/272784654_Development_of_an_anomalous_noise_event_detection_algorithm_for_dynamic_road_traffic_noise_mapping
ICSV22, 2015
Road Traffic Noise (RTN) versus other, Anomalous Noise Event (ANE)
! almost only self-citations.

Methods for Noise Event Detection and Assessment of the Sonic Environment by the Harmonica Index 
https://www.mdpi.com/2076-3417/11/17/8031 
2021
Discusses different noise event indicators.

> 2.2.2. Recognition of the Noise Event Source
> ANED algorithm was trained using more than 150 h of expert-manually labeled data,
> coming from the 24 sensors, deployed by the DYNAMAP project in Milan, with around 8% of anomalous noise events
> (e.g., bird singing, sirens, dogs barking, horns, trams)

Development and validation of an anomalous noise events detector focused on salient events through an urban and suburban WASN adapted to real-operation
https://merit.url.edu/ca/publications/development-and-validation-of-an-anomalous-noise-events-detector--4
ICSV 2021
Road Traffic Noise RTN vs Anomalous Noise Event (ANE).

> The algorithm detected — for the events catalogued as high-salience:
> — all of the present airplane noise
> - more than 90% of works, and people talking
> 
> For the mid-high salience
> - more than 84% of airplane noise
> - nearly 80% of works
> - and more than 60% of people talking


# Resources

## Datasets

#### DCASE2017 - Sound event detection in real life audio
https://dcase.community/challenge2017/task-sound-event-detection-in-real-life-audio
Captured on city streets in Finland. Recordings are 3-5 minutes long.
Labeled with events.
Classes: brakes squeaking, car, children, large vehicle, people speaking, people walking
2 GB total.

Could be used to study how often sounds co-occur?

#### DCASE2023 - Sound Event Detection with Soft Labels
https://dcase.community/challenge2023/task-sound-event-detection-with-soft-labels#baseline-system
MAESTRO dataset.
Real outdoors, multi-minute
2.6 GB total.

Birds singing, Car, People talking, Footsteps, Children voices, Wind blowing, Brakes squeaking,
Large vehicle, Cutlery and dishes, Metro approaching, Metro leaving.
Contains labels for both road noise, rail noise, community noise.
Also contains labels for geophony and biophony.

Could be used to study how often sounds co-occur?

#### SONYC-UST v2
https://zenodo.org/record/3966543
10 second clips. Tagged with the classes.
Has good class taxonomy - designed for (urban) noise monitoring.
8 high-level classes. 23 fine-grained.

Could be possible to re-annotate with the dominant class?
Could be used to study how often sounds co-occur?

#### Other
https://dcase.community/challenge2022/task-sound-event-detection-in-domestic-environments
https://dcase.community/challenge2023/task-sound-event-detection-with-weak-labels-and-synthetic-soundscapes 


# Theory

## Single dominant source

Given a mixture of two sound sources, A and B, where A is the louder of the two.
If B is -5dB of A, then B contribution to sum is 1.2 dB
If B is -10dB of A, then B contribution to sum is 0.4 dB
This means that when A is +10 dB of B, its contribution to the sum is neglible.

## Thresholds for becoming noticable noise

TITLE 7 NATURAL RESOURCES & ENVIRONMENTAL CONTROL DELAWARE ADMINISTRATIVE CODE, 1149 Regulations Governing the Control of Noise. USA

> Intrusive noise means unwanted sound which intrudes over and above the existing noise at a given location.
> The relative intrusiveness of the sound depends upon its
> amplitude, duration, frequency, time of occurrence and tonal or informational content as well as the prevailing ambient noise level.
> A sound pressure level of 3 dB(A) above the ambient level is normally just discernable,
> with levels of 5 dB(A) to 10 dB(A) the lower level region for complaints.

Noise Guide for Local Government Part 2 Noise assessment, Australia

> The NSW Industrial Noise Policy (EPA 2000),
> which is specifically aimed at large and complex industrial activities,
> defines intrusive noise as 5 decibels above the background noise level
> 
> The background level is the LA90 measurement of all noise in the area of the complaint
> without the subject noise operating or affecting the measurement results.
> 
> The Interim Construction Noise Guideline (DECC 2009) notes there may be
> some community reaction to noise from major construction projects where this is more than 10 decibels
> above the background noise level for work during the daytime.
> This recognises that construction noise is generally temporary
> with the community having a slightly higher tolerance for it.

BS4142:2014 states

> The significance of sound of an industrial and/or commercial nature depends
> upon both the margin by which the rating level of the specific sound source exceeds the background
> sound level and the context in which the sound occurs
> ...
> A difference of around +10dB or more is likely to be an indication of a significant adverse impact,
depending on the context.”
> A difference of around +5dB is likely to be an indication of an adverse impact,
depending on the context.”

