

# TODO
- Pick up poster
- Pick up roll-up and sensors
Maybe tablet
Tablet stand?
- Make presentation
- Make demo slides


## Audience
Likely mostly researchers and students
within Machine Learning an Artificial Intelligence

Expecting a pretty technical audience.
Interested in methods, development, challenges
Some also in the practical aspects of applying ML

## Goals

* Attract skilled team members.
* Attract research partners. Softfunding opportunities 
* Attract pilot project partners.

Focus more on Condition Monitoring compared to Noise Monitoring.

## Interactions

Have something for people to remember you by.

Business cards.
Should be same for everyone in company

Flyers.
Company information. "work with Soundsensing"
Product information. "buy Soundsensing"

## Presentation

### Schedule
1700-1830

### Format
15 minutes, including 5 minutes Q&A
10 slides

Repeat the same at both Nordic AI Meet (Oslo) and NORA Annual Conference (Bergen)

## Story-arc
Soundsensing
- audio machine learning
- from monitoring of noise to condition monitoring of machines and processes


## Call to Action

- Do pilot project together with us!
Primarily targetting technical rooms in commercial real-estate.
Owners, facility managers

Open for other possibilities.
Manufacturing, process industry, heavy machinery etc

Link to signup. Send email if interested

- Come work with us
Research collaborations, master thesis, internships
May be looking for 1 Machine Learning Engineer for 2022


10 slides

- About Soundsensing
- Noise Monitoring
- Roest project

- CTAs

## Poster

Focused on what we have achieved.
Quite high technical level.

Is now at
https://nordicaimeet.virtualpostersession.org/

### Printing


https://www.copycat.no/produktkategorier/ekspress/
A1 ekspress 560 NOK

Rådhusgata 17
Tlf. 22 33 77 00
sentrum@copycat.no
Man-fre 8-16*


## Demo

Presentation?
Stand?

1700-1900

Show data.
Show outputs.
Show usecases.

Should be rich in information, showing details etc.
Does not need to be interactive

Materials

- Demo video master thesis


- Audio classification web interface.
Prepare various audio clips

- Noise activity detection
Noise activity report.
Using PNB as a case
Illustrated using construction work as a case?

- Fabian thesis.
Presentation has some OK images

- Web application / grafana
Can make some screenshots from there

- Hardware
Also deserves a few slides


Could maybe be autorotating slides?

https://pointerclicker.com/how-to-make-slides-transition-automatically-in-google-slides/
https://ask.libreoffice.org/t/loop-an-impress-presentation/66

Need a projector or TV screen

portable projector
https://www.komplett.no/product/1130220/tv-lyd-bilde/projektorer/projektorer/asus-projektor-zenbeam-s2#


# NORA Annual Conference

The NORA.startup segment will be divided into two sessions.


## Stand
All the startups who have signed up for a presentation will be given a dedicated space in a function room to set up a stand.
The stands will be open the entire second day of the conference.

https://www.nora.ai/nora-annual-conference/Nora.startup%20introductions/

## Presentation
At 15:00, members of NORA.startup will be invited to present their startups to the conference participants.
We will set aside 15 minutes for each startup, followed by a 5 min Q&A.

15:25-15:40
Soundsensing
Ole Johan Aspestrand Bjerke



# Proposal

Abstract document, from template
https://docs.google.com/document/d/1PXDzPa-HfgZg_G4xIYXhMsK-8L-Yq8AvHgk57uVYj0Q/edit?usp=sharing

Abstracts.
< 500 words including references

Was accepted as a poster.

# Categories.

- [X] Oral presentation 
- [ ] Full paper (additionally)
- X Poster / demo 

# Meta
The abstract may
introduce the research area,
objective of your research,
contribution you that look to make,
any results / findings that you may have,
and how you see the future work from this research work to evolve.

All add references in the style indicated below. 

# 

Title,
Authors,
Affiliations,
Abstract,
Keywords,
Main text (including figures and tables),
Acknowledgements,
References.


# Keywords
Acoustics, Audio Classification, Environmental Noise, Sound Event Detection, Noise Monitoring

# Title
Combining Machine Learning and Acoustics for Noise Monitoring

# Text

Noise is a large problem on a socital level.
In Europe alone ---, 
which leads to sleep distrurbances and increased risk of cardiovascular disease. cite WHO 
Improvements in the capabilities and cost of embedded systems and Internet of Things
has made it easier to measure noise in terms of soundlevel over longer periods of time and at more locations.
However the sound level alone tells us very little about the causes of noise,
which must be understood in order to plan and validate remedies. 

The use of Machine Learning is starting to make it possible to automatically classify and detect events in audio,
and there is a growing body of existing research in relevant topics such as
Sound Event Detection, Environmental Sound Classification, and Acoustic Scene Classification. cite DCASE
However we find that most existing work does
not consider the relationship between the noise magnitude/severity (soundlevel)
with noise sources (classification).

Our ongoing research aims to find practical solutions for
automatically determining the source of measured noise,
by combining sound detection and classifaction techniques with
with soundlevel measurements according to current noise regulations and acoustical engineering practice.

Our contributions so far have shown that 
it is feasible to do on-sensor classification of environmental sound on low-cost microcontrollers, cite thesis
that Sound Event Detection (SED) at a known source can be used to create logbooks of noisy activity, cite ICSV27
and that doing SED at both source and receiver allows to determine the source of noise experienced at receiver. cite Brage/EuroNoise2021 

Current work focuses new task formulations for Machine Learning
that incorporate the requirements of acoustic modelling and noise regulations.
We hope that the formalization of these tasks will enable more research and increased relevance for
understanding acoustical noise using Machine Learning.

Our primary method of research involves case-studies and demonstrator projects in the real-world,
and we invite parties interested in noise, acoustics and machine learning to collaborate with us. 

# Acknowledgements
Research in 2019 has received financial support from Research Council of Norway, prosjekt STUD-ENT.
One project in 2020-2021 was done in collaboration with Politiets Nasjonale Beredskapsenter. 

# Notes

Introduction

Noise impact on society
Modern technology improvements. MEMS microphones, IoT, Machine Learning
Lower costs for data collection. Lower cost for data analysis. 
Areas. Environmental noise. Leisure. Industrial. Transportation. HMS

Objective

Come up with practical solutions for monitoring noise at a location over time,
that can automatically attributes the correct noise source.
To gain a better understanding of causes and characteristics of noise at the location,
to document adherence to regulations and best-practices,
and form basis for corrective and preventive measures when issues are found.

Sub-Challenges

- Combining classification with soundlevels
- Selecting appropriate classes for acoustics.
Variations in regulations
Case-specific variations
- Privacy requirements for continious monitoring

Technical challenges

- Number of measurement points usually << number of noise source(s) and locations
- Noise sources may be unknown in number, location, and characteristics
- Highly diverse environments. Source characteristics, propagation, combinations

Findings

- Sound Event Detection can be used at known noise sources to log periods of noisy activity (PNB/ICSV27)
- SED can be used at both source and receiver,
in order to attribute noise at receiver to a known source, or other sources (PNB/EuroNoise2021)
- Environmental Sound Classification can be done on low-power microcontrollers (Master)
- Need for specialized task formulations that combine Acoustics and Machine Learning 
 
Call to Actions

Call for Research Partners.
Joint applications for research funding.
Partners in case studies.
Academic research collaborations
Master thesis supervision

# Privacy

Privacy in Wireless Acoustics Sensor Networks
non-privacy invasive acoustic indicators.
Spectrogram, resolutions
Limitations on classification performance
Limitations on due-dilligence
on-edge inference
Limitations on 
(federated learning)


