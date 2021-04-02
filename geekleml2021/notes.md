
# Meta
30 minute slot.
20-25 minutes presentation
Pre-recorded talk. Live Q&A

12:45 — 13:15 CEST
https://python.geekle.us/agenda#!/tab/292052184-1

Approx half the content of EuroPython

# Abstract

Audio Events, or Acoustic Events, are individual distinct sounds.
Audio Event Detection (AED) is the task of detecting such sounds, returning precise times that each kind (class) of sound occurs.
This can be anything from detecting coffee-beans cracking while roasting, to gunshots on a shooting range, to noise made by construction works - all these are real applications the presenter has developed.
This practical talk will show how you can build such a system in Python, using machine learning models applied to audio.
The general approaches shown can also be applied to other sensor data such as vibrations, pressure etc.

# Extended Abstract

Audio Events, or Acoustic Events, are individual distinct sounds.
This could be the pop of popcorn kernels in a popcorn machine,
the cough of a patient,
a car that is passing by on a road,
or the sound of an alarm in an office building.

Audio Event Detection (AED) is the task of detecting such sounds,
returning precise times that each kind (class) of sound occurs.
It finds uses in music analysis, manufacturing, medicine and building management.

Steps
- Set up the supervised learning task from a collected dataset.
- Extract spectrogram features from audio waveforms.
- Train a Convolutional Neural Network (CNN) and Recurrent Neural Network (RNN).
- Run the trained model on an real-time audio stream.
- Process model output probabilties into discrete events.
- Evaluate the performance of the resulting AED system.

Example code in Python covering these aspects will be provided.
Libraries used with be Keras, TensorFlow and scikit-learn for machine learning,
and pysoundfile, PyAudio and librosa for audio processing,
with some numpy and pandas for general data manipulation.

Some general familiarity with supervised Machine Learning is recommended.
Familiarity with time-series or audio is a bonus, but not a pre-requisite.

# Calls to Action

Interested in working on Audio and ML?
- Apply at Soundsensing

Looking for monitoring solutions using Audio?
Use Soundsensing IoT sensors and Audio ML platform



# Demo

Ideal demo

- Concrete usecase
- Simple phenomenon
- Relatable, familiar
- Can use detected events to illustrate/uncover differences
Different event rates say something about other (potentially hidden) process variables.
Ie popcorn. Different brand of popcorn. Different conditions, ie humidity. Amount of beans
Change in events say when something has started or stopped.
- Can show detecting working in real-time
- Can share the data
- Data is easily accessible
- Labeled data exists already
Bird call?
- Fun and geeky


Tracking beer brewing via sound

Rate of fermentation over time
mol/sec

https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FNadia-Musco%2Fpublication%2F282402373%2Ffigure%2Ffig1%2FAS%3A613907060240428%401523378257552%2FIn-vitro-cumulative-gas-production-Panel-A-and-fermentation-rate-Panel-B-over-time.png&imgrefurl=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FIn-vitro-cumulative-gas-production-Panel-A-and-fermentation-rate-Panel-B-over-time_fig1_282402373&tbnid=Gsp5YMmGHkG1bM&vet=12ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygFegUIARCuAQ..i&docid=WvHXcTxPacLZDM&w=709&h=975&itg=1&q=rate%20of%20fermentation%20over%20time&hl=en&ved=2ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygFegUIARCuAQ

https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FFederico-Infascelli%2Fpublication%2F41394048%2Ffigure%2Ffig1%2FAS%3A669993146519561%401536750222607%2FTrend-of-fermentation-rate-over-time.png&imgrefurl=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FTrend-of-fermentation-rate-over-time_fig1_41394048&tbnid=R7LwBqk0XIpDCM&vet=12ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygAegUIARCkAQ..i&docid=Z_pUBmtVx2iewM&w=850&h=397&q=rate%20of%20fermentation%20over%20time&hl=en&ved=2ahUKEwi2uYb8jdTvAhXGtCoKHeNZDfwQMygAegUIARCkAQ


https://www.google.com/search?q=rate+of+fermentation+over+time&tbm=isch&ved=2ahUKEwjU3r32jdTvAhXSxSoKHaDrCxEQ2-cCegQIABAA&oq=rate+of+fermentation+over+time&gs_lcp=CgNpbWcQAzoCCAA6BAgAEENQkUVYqVFgnlJoAHAAeACAAViIAe8FkgECMTCYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=4QxhYJTqLNKLqwGg16-IAQ&bih=985&biw=1918&hl=en#imgrc=EKf6aNkBtPCGPM

Shaped like a Weibull / gamma / lognormal


Plaato app
Scale goes up to 800-1000 BPM
13 per second
75 ms between each

Typical peak might be at 100-200 BPM

https://www.google.com/search?q=plaato+analytics&tbm=isch&ved=2ahUKEwjOu7S0r9_vAhUEtCoKHVdXD1kQ2-cCegQIABAA&oq=plaato+analytics&gs_lcp=CgNpbWcQAzoCCAA6BAgAEBg6BggAEAoQGFDZ_hBY-pYRYJuYEWgAcAB4AIABVogB_QmSAQIxOZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=Y_RmYI7-BYToqgHXrr3IBQ&bih=988&biw=1918#imgrc=5we7VCNxCQR3JM

https://www.google.com/search?q=plaato+analytics&tbm=isch&ved=2ahUKEwjOu7S0r9_vAhUEtCoKHVdXD1kQ2-cCegQIABAA&oq=plaato+analytics&gs_lcp=CgNpbWcQAzoCCAA6BAgAEBg6BggAEAoQGFDZ_hBY-pYRYJuYEWgAcAB4AIABVogB_QmSAQIxOZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=Y_RmYI7-BYToqgHXrr3IBQ&bih=988&biw=1918#imgrc=4CEvO8RRbM5mhM

https://www.google.com/imgres?imgurl=http%3A%2F%2Fhumebrew.com%2Fcontent%2Fimages%2F2019%2F01%2Fplaato-airlock-fermentation-complete-wide.jpg&imgrefurl=http%3A%2F%2Fhumebrew.com%2Fplaato-digital-airlock-review%2F&tbnid=C7-7ouo_2PyD3M&vet=12ahUKEwjOu7S0r9_vAhUEtCoKHVdXD1kQMygAegUIARCmAQ..i&docid=e0eGkBDjLTLBBM&w=1440&h=720&q=plaato%20plot&ved=2ahUKEwjOu7S0r9_vAhUEtCoKHVdXD1kQMygAegUIARCmAQ#imgrc=C7-7ouo_2PyD3M&imgdii=ceckMDLsUqc0nM

# TODO

- Collect initial audio data
- Run through standard classifiers, see how they do
- Run through spectrogram
- Run through soundlevels
- Label some 10-100 events per track, evaluate performance

Compute spectrograms
Generate labels using clustering.
Using GMM-HMM
Put Youtube files in csv

## Exploratory Data Analysis

Always inspect at the data
Listen to audio, look at spectrogram
Audacity open-source software

Characteristics of the sound
Make notes

Event length.
Distance between events
Variation
Changes over time
Differences between recordings
Background noise
Other events that could be easily confused


### Labeling data
Manually using Audacity


### Synthesize data
Using scaper
Vary SNR

## TODO





# Outline

- Definition
- Motivating applications
- Audio pipeline
- Data and labels
- Training
- Evaluate performance
- Running real-time 

Style.
Show the output/demo first.
Then walk through how to make it?
Complete code in a Github, ideally

# Applications

Aka Sound Event Detection
Present/not.

Similar to.
Audio classification
Keyword spotting

## Data requirements

Go for at least 100 events
1 per second, 2 minutes

Baseline simple. Soundlevel/freq, RF
Baseline advanced. Pretrained audio CNN
Custom. Own CNN/RNN on spectrogram

# Planning
What people need to understand

- Audio events
What is an audio event.
Onset/offset
Definition of AED task. Input/outputs

- Typical audio ML pipeline
Analysis windows
Features over time
Spectrogram

- How to evaluate performance
Window-wise vs event-wise
sed_eval: https://tut-arg.github.io/sed_eval/
tolerances

What we will (mostly) assume that people know

- Basic digital audio
- Basic Machine Learning. Supervised classification
- Typical Neural Networks. CNN/RNN ?

Refer to EuroPython talk.


What people do not need to understand

- ? Weakly labeled data 
- Making efficient networks

Undecided

- Post-processing.
Counting. Threshold above X
Event-rate

Tips & tricks

- Error analysis
Manually examining mistakes that your algorithm is making

- Labeling strategies
Unsupervised learning. HMM GMM
Weakly labeled data
Semi-supervised
Alignment tools

- Pretrained model
OpenL3 / YAMNET / PANN

Challenges

- Out-of-distribution data
Device. Environment. 

## Requirements for AED

- Resolution of output. 
- Detection delay
- False Positive Rate / False Negative Rate
- Precision / recall

Things to consider
- Length of events. Min,max,median. Should fit into one window

## Examples

- Popcorn popping. Or coffeebeans
- Gunshot detection
- Bird call
- Cough
- Umm/aaa speech patterns
- Drum hit
- Alarm goes off
- Car passing
- Plop from alcohol fermentation lock

## Events vs not-events
Need to have a well-defined duration
Start-end. Onset/offset
Or at least a clear start

If events are overlapping a lot, might not make sense as events anymore
One hand clap versus clapping

For events one can count the number of occurrences
Classification might instead count number of seconds instead

## Approach
AED as classification of short independent time-windows
Uniform probability of event occuring.

Not considering sequences, or states, in the detector
Ie in speech recognition certain sequences of phonemes are more probable

Monophonic.
Binary classification

Requires that each event is clearly audible and understandable - without context
Low-to-no overlap

## Characteristics of Audio Events

- Duration
- Tonal/atonal
- Temporal patterns
- Percussive
- Frequency content
- Temporal envelope
- Foreground vs background
- Signal to Noise Ratio

Some events are short
Gunshot
Bark

Some are bit longer
Cat mjau

Some events are percussive / atonal.
Cough,  etc

Some have temporal patterns
Some are more tonal
Alarms

Transitions. Into state. Out of state.


### Popcorn-popping

https://www.youtube.com/watch?v=6aAuwZfJTkc
actually happens so close that might not be well approximated as individual events
Get a "cling" from things hitting

10 hours of popcorn popping
https://www.youtube.com/watch?v=--pvwC3yO3Q
inside a micro
popping in bag.
Thuds

https://www.youtube.com/watch?v=Y0xh95oTjG4
open frying pan
popcorns put in over time
makes cling sound
relatively slow event rate
sounds of kernels hitting eachother
flying out of pan and hitting stove


### 
Fermentation
Brewing
Air lock 

Brewers speak of
bubbles per minute 


Event length around 200 ms

Watch an Airlock Bubbling During Mead Fermentation - Entertainment for Brewers
https://www.youtube.com/watch?v=p0jtxp5nWms
5 minutes
Quite regular events
Not so loud events
Quite high ambient noise


ASMR | Homebrewing Airlock Symphony
https://www.youtube.com/watch?v=MN0Mg1uyznU
16 minutes
3-5 different airlocks. Sound different
One has highest event rate
Low ambient noise

https://www.youtube.com/watch?v=by0e-EkAsOE
60 minutes

https://www.youtube.com/watch?v=q2srYoC3FOo
2 hours 20

Every 20 minutes there is another event

ASMR bubbling airlock
https://www.youtube.com/watch?v=b31j5PvXQhY
7 minutes

multiple bubbles in one go. burping. Plops not so clear

Two minutes of air lock bubbling
https://www.youtube.com/watch?v=3iGoz00AMew

Airlock with glyserine
2 minutes
Not so loud
Compressor noise

Bubbling Airlock
https://www.youtube.com/watch?v=WznxXBRUVb0

Very high rate
30 seconds

Airlock bubbling ASMR
https://www.youtube.com/watch?v=vrM-lZ5H54Y

12 minutes
High rate
Bit of burping. But quite consistent sound

Homebrew Ale Airlock Bubbling. So Satisfying!
https://www.youtube.com/watch?v=j7md-wkL1U0
1 minute
1 per second
Quite clear, glassy sound.
Variation due to camera position

Bubbling airlock on a hefeweizen
https://www.youtube.com/watch?v=aVUnxUfeBMA
10 seconds

Airlock Bubbling
https://www.youtube.com/watch?v=8iuJLfs4uP8
low volume
10 seconds

Bubbling airlock
https://www.youtube.com/watch?v=F8Oq1gyTIRY
bit burpy
lots of camera movement

Airlock Bubbling - Short Mead
https://www.youtube.com/watch?v=-FJ8UWZmwZQ
noise higher than bubble sound
30 seconds

Airlock Bubbling for 9 minutes
https://www.youtube.com/watch?v=7gdJ134JKa4
9 minutes
very burpy

Airlock Bubbling for 5 minutes
https://www.youtube.com/watch?v=rBvycO-O_8s
5 minutes
very burpy

St Peters Air Lock Bubbling
https://www.youtube.com/watch?v=eu6nphXTbTM
Big round type airlock
About 1 per second
quite clear
21 seconds
operator noise

Bubbling airlock
https://www.youtube.com/watch?v=jmR-onzH5tY
noise much higher than bubbling
20 seconds

Airlock bubbles - fermentation
https://www.youtube.com/watch?v=kbxwuXZqTs0
25 seconds
round type
quite clear
some operator noise

Air lock bubbling
https://www.youtube.com/watch?v=UZuC7DwVT8A
much more noise than bubbles
20 seconds

crazy Airlock bubbles
https://www.youtube.com/watch?v=SxwBGPdNSzQ
20 seconds
many per secon
still quite clear

Robust porter airlock bubbling
https://www.youtube.com/watch?v=U8IifcAWvo4
1 per 2 seconds
15 seconds

Bubbling beer fermenter airlock
https://www.youtube.com/watch?v=K0QJJLIBef4
very poor audio quality
static

Airlock Bubbles
https://www.youtube.com/watch?v=e5hFI1Z2gGI
clear bubbles
per 2 seconds
10 seconds

Bubbling airlock
https://www.youtube.com/watch?v=UaUlVaap3dY
16 seconds
1 per 2 second
TV background

Mead airlock bubbles
https://www.youtube.com/watch?v=x7Tmty772FQ
20 seconds
varying noise

Bubbles In the Airlock
https://www.youtube.com/watch?v=xdXpCw9qdDo
20 seconds
quite clear
1 per second

Bubbling Fermenter Airlock
https://www.youtube.com/watch?v=_vi1q6QfkG4
low volume
8 seconds

Yeast FM - 1min of Airlock Bubbles from Mead Making
https://www.youtube.com/watch?v=ZFlMHcYdto4
artifical sound
using gating to remove non-bubble periods

beer bubbling (home brew)
https://www.youtube.com/watch?v=6VQTGuOY4Uk

quite clear
1 per 2 sec
some operator noise

Air lock, red wine
https://www.youtube.com/watch?v=vwLZuKaEAEE
21 seconds

Airlock Bubbles
https://www.youtube.com/watch?v=-E3T2OmjTLs
15 seconds
quite clear

Primary Fermentation Air Lock
https://www.youtube.com/watch?v=ZPmEByu-4xQ
very high rate. 4 per second
very clear
1 minute

Alcoholic Ginger Beer fermentation fourth night - getting bubbles
https://www.youtube.com/watch?v=k9OXne3iGpM

1 hour 30
Almost no plops

Ginger beer fermentation day 6. Finally getting some action
https://www.youtube.com/watch?v=Z7aNQXE0nUo

5 hours
Quite quiet plops
1 plop per 30 seconds

30 seconds of a bubbling airlock
https://www.youtube.com/watch?v=1KIecmSnD5g
30 seconds
quite clear
high rate

First Homebrew Hop Nog 2010 Fermenting Bubbles
https://www.youtube.com/watch?v=AWSX4uQopXA
round type
ok clear
34 seconds
1 per 2 seconds

Fermentation Airlock Bubbling (beer or wine homebrewing)
https://www.youtube.com/watch?v=DV_9tfFyY00
clear. 
rate 1 per 2 sec
misc background noise


The sound of Mead bubbling away
https://www.youtube.com/watch?v=m_Y8-TmyyGg
Two bubblers
Low rate. very similar. 1 per 4 sec
1 minute

Airlock bubbling/Airlock en funcionamiento
https://www.youtube.com/watch?v=mRpjUjNK0z0
quite high rate
very clear
15 seconds

Apfelwein fermentation
https://www.youtube.com/watch?v=AjJC_i3g0Mg
two at same time
clear glass sounds
medium rate. 1 per 2 seconds each
30 seconds

Airlock during fermentation
https://www.youtube.com/watch?v=WHlSNkq29k4
medium activity
clear
1 minute

Brewing alcoholic ginger beer. One week on, live
https://www.youtube.com/watch?v=eKTNsWHXkVU

4 hours
1 plop per second almost
 
https://www.youtube.com/watch?v=f3bLQLT48Yc

57 secodns
2 per second. Quite clear

Demijohn Airlock Bubbles 12 mins
https://www.youtube.com/watch?v=0_wDLNikm2M

12 minutes
1 per second
ok clear
high whitenoise

S-Style Beer/Wine Air Lock Bubbling
https://www.youtube.com/watch?v=po2u_qI7-us
20 seconds

the rate of bubble in the mead
https://www.youtube.com/watch?v=xS35DfrhRG0
One per 5 seconds
40 seconds

Beer fermentation air lock, airlock fermentación de cerveza
https://www.youtube.com/watch?v=CXn5vgiV914
20 secs

First attempt at Moonshine! Fermentation process has begun
https://www.youtube.com/watch?v=LiofYnl4UeI
30 seconds

Carboy airlock grape wine
https://www.youtube.com/watch?v=mFaxJJUHtB8
42 seconds

high event rate
quite clear

Bubble, bubble
https://www.youtube.com/watch?v=t0pOz-gviZs
25 seconds
ok clear
misc environmental noise

https://www.youtube.com/watch?v=mKuWlZwWsDM
30 seconds
pausing then large rush. Burping

Strawberry wine- day 7-secondary ferment begins
https://www.youtube.com/watch?v=Qvyf8h8dr4I
30 seconds
quite clear
quite high event rate

Airlock bubbler
https://www.youtube.com/watch?v=FVAH4w_6RGs
30 seconds
very high event rate
still quite clear
lots of tricky ambient noise

Elderflower Airlock
https://www.youtube.com/watch?v=51ytpDZj8v4
very clear
medium rate
1 minute

Beautiful sound of home brew wine
https://www.youtube.com/watch?v=ewOPI-gpoto
2 bubblers
Right next to eachother
lots of camera motion back and forth

S-Style Beer/Wine Air Lock Bubbling
https://www.youtube.com/watch?v=po2u_qI7-us
low rate
quite clear

Primary fermenter airlock bubbling
https://www.youtube.com/watch?v=G5mAKVP-KX8
30 seconds
some odd noises
ok bubble sound
medium acitvity

Homebrew is bubbling away
https://www.youtube.com/watch?v=IzFpqaElTrg
burping a bit
clear sound
1 minute

Airlock bubbler/Home brewing
https://www.youtube.com/watch?v=gQFo3Lg2MAc
2 minutes
Clear, even
Medium rate
some kitchen noise in background


Bubbling In the Airlock
https://www.youtube.com/watch?v=Y-2R3cRRzTI
20 seconds
high rate
quite clear

1 Piece Airlock bubbling Krausen view through clear window in bucket lid
https://www.youtube.com/watch?v=pUkmG2sPBD4
30 seconds
ok clear
some handling noise

The effect of a light fermentation on an airlock
https://www.youtube.com/watch?v=fufqSDnqFto
gurgling
some handling noise
quite uneven

Mead (Honey Wine) Fermenter Bubbling
https://www.youtube.com/watch?v=pMxXWyKu0HM
2-3 bublers
bit low volume

Home brew airlock
https://www.youtube.com/watch?v=pApS0S2PA9I
2 bubblers
noises in background


Active beer fermentation
https://www.youtube.com/watch?v=tw16K7mNAmE
1 minute
high rate
airlock not visible

Fermenting - Airlock activity
https://www.youtube.com/watch?v=NRXuJqZp61w
very high rate
hard to hear

beer bubbling
https://www.youtube.com/watch?v=dE9FjwMeWLs
high rate
burping

Cherry Fever Stout fermenting
https://www.youtube.com/watch?v=PvBE0mZmBHY
high rate
quite clear

Airlock Rhythm
https://www.youtube.com/watch?v=0DXxOutOilU
3 piece
very clear
steady rythm
1 per second
noise in background

Fermentation Airlock
https://www.youtube.com/watch?v=VQTucCuRfrk
burping

Bubbles
https://www.youtube.com/watch?v=Lqw3VX3FcwI
medium rate
30 seconds

Bubbles
https://www.youtube.com/watch?v=bp6CT68rqoY
high rate
quite clear
20 sec

## Existing approaches

Active Airlock
https://www.youtube.com/watch?v=570zQJRhllI
high rate. burping
ok sound
30 seconds

Professional acoustic monitoring of brewing.
Using piezo element. Tzero
https://www.fierceelectronics.com/sensors/high-tech-meets-taproom-acoustic-fermentation-sensor
https://www.tzerobrew.com/monitor

DIY bubble logger. IR photometer based
https://www.sparkfun.com/tutorials/131

DIY hygrometer
https://www.hackster.io/135387/homebrew-fermentation-monitor-9df83e

Airlock bubble counter with android
Using IP camera and movement detection
https://www.youtube.com/watch?v=4kj9-iAY01k

Bubble detector while fermenting beer
https://www.youtube.com/watch?v=AT7ffcUMcEg
Arduino with IR, using colored fluid in airlock

An attempt at counting bubbles from an airlock with sound
https://www.jimsbeerkit.co.uk/forum/viewtopic.php?t=79000
https://www.anfractuosity.com/projects/bubbleometer/
https://github.com/anfractuosity/bubbleometer
July 2017. No updates since

https://www.brewbubbles.com/
DIY optical kit

Bubble logger
used sound
https://www.homebrewtalk.com/threads/bubbler-logger-a-fermentation-logger-measusing-co2-sound-bubbles-to-calculate-sg.665988/
SBL4TILT - "Sound Bubble Logger and Temperature controller for TILT" (ESP32 - TILT repeater, BPM logger and temperature controller
https://www.homebrewtalk.com/threads/sbl4tilt-sound-bubble-logger-and-temperature-controller-for-tilt-esp32-tilt-repeater-bpm-logger-and-temperature-controller.683670/
https://github.com/kbaggen/Sound-Bubble-Logger-and-Temperature-controller-for-TILT
Based on ESP32
Uses sound level.
Microphone is placed down into airlock
Can send data to Brewfather / Brewersfriend 

BrewFather
popular with hobbyists
supports IoT sensor devices
Can enable custom endpoint in Settings
Get a unique URL
Then can send JSON
JSON payload format documented here
https://docs.brewfather.app/integrations/custom-stream
Bubbles Per Minutes is supported


BrewSpy
https://play.google.com/store/apps/details?id=com.yiannnos.myspindel
BrewSpy receives data from your iSpindel , Tilt Hydrometer , PLAATO airlock and PLAATO
Free
Charges for push notification




## Request for data

1 minute
Metadata
- Number of bubbles counted. BPM
- How clearly can bubbles be heard. 1-5
- Type of airlock. S-curve/2-piece, 3-piece
- Hours since start
- Kind of brew
- Would you be interested in a phone or web app that tracks fermentation rate?
- Why / why not
- Any tips or other inputs
- Do you want to get updates about project by email (max every few months)


Record in the location where you typically have your brew sitting.
Record using phone/tablet or .
Record from a distance between 10 cm to 1 meter from airlock.

Looking for realistic sound from typical brewing conditions,
not hi fidelity audio.

Avoid .
Try to avoid too much handling noise when operating the phone/camera.

Upload video to Youtube. Can be Public or Unlisted
Submit data via Google Form
Need some CAPTA / trolling checking 

Multiple submissions welcomed!
Each submission should be recorded at least 1 hour apart.
Chances of 

Giving away Plaato Airlock.

## Communities

https://www.reddit.com/r/brewing/
20k members

https://www.reddit.com/r/Homebrewing
1M members

https://www.reddit.com/r/TheBrewery/
70k members

## Post-processing

Counting. Threshold above X
Event rate. Count / time


# Other


## Error analysis

False Negatives / False Positives. Rank by probability
Can be generalized to multi-class. For example using pairwise-confusions. Expected-Actual


Bias/variance diagnostics
High Variance problem: Training error much lower than test error
High Bias problem: Both training and test error high
Different strategies to fix the two cases

Diagnostic
Convergence failure.
Optimizing wrong loss function. 

Lecture 11.2 — Machine Learning System Design | Error Analysis — [ Machine Learning | Andrew Ng ]
https://www.youtube.com/watch?v=k1JGvqr56Yk

DeepLearningAI: Carrying Out Error Analysis (C3W2L01)
https://www.youtube.com/watch?v=JoAxZsdw_3w

Debugging ML Models and Error Analysis | Stanford CS229 | Andrew Ng
https://www.youtube.com/watch?v=ORrStCArmP4

Machine Learning System Design | Error Analysis
https://www.coursera.org/lecture/machine-learning/error-analysis-x62iE

Microsoft Error Analysis toolkit.

https://erroranalysis.ai/


# Resources

https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection
Using PANNsCNN14Att
Shows training with weak supervision
Part of Cornell Birdcall Identification challenge
https://www.kaggle.com/c/birdsong-recognition

Was used as inspiration for the winning entry
https://www.kaggle.com/c/birdsong-recognition/discussion/183208
DenseNet with focal/BCELoss
SpecAugment, Mixup
Ensemble of 4 models

Attention based pooling
https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection/comments#962915
tahn instead of softmax

Attention-based Deep Multiple Instance Learning
https://arxiv.org/abs/1802.04712
Maximilian Ilse
ICML 2018



