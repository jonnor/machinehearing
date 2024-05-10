
## Acoustics

#### The sound of two hands clapping
1987
Bruno Repp,

He distinguished 8 hand clap positions:

Hands parallel and flat

- P1: palm-to-palm
- P2: halfway between P1 and P3
- P3: fingers-to-palm

Hands held at an angle

- A1: palm-to-palm
- A2: halfway between P1 and P3
- A3: fingers-to-palm
- A1+: A1 with hands very cupped
- A1-: A1 with hands fully flat

Pictures of these in
https://intelligentsoundengineering.wordpress.com/2017/06/26/applause-applause-thank-you-thank-you-youre-too-kind/

Individual claps varied widely, but there was no evidence of inﬂuence of sex or hand size on the clap spectrum.
He also measured his own clapping with the eight modes above.
If the palms struck each other (P1, A1) there was a narrow frequency peak below 1 kHz together with a notch around 2.5 kHz.
If the ﬁngers of one hand struck the palm of the other hand (P3, A3) there was a broad spectral peak near 2 kHz.

#### The sound of many hands clapping
https://www.nature.com/articles/35002660
Neda et al
2000

Observed that the applause begins with incoherent random clapping, but then synchronization and periodic behaviour develops after a few seconds. This transition can be quite sudden and very strong, and is an unusual example of self-organization in a large coupled system.

Synthesis of clapping and applause sounds was covered in detail, and to great effect, by Peltola and co-authors.
They presented physics-based analysis, synthesis, and control systems
capable of both producing individual hand-claps, or mimicking the applause of a group of clappers.

## Data

https://bigsoundbank.com/search?q=applause
https://freesound.org/search/?q=applause&f=&w=&tm=0&s=Date+added+%28newest+first%29&advanced=0&g=1&only_p=1&cm=0&page=2#sound
Youtube


## Feature-extraction for


#### Characteristics-based effective applause detection for meeting speech
https://www.researchgate.net/publication/220226738_Characteristics-based_effective_applause_detection_for_meeting_speech
August 2009, Signal Processing

First study the characteristic differences between applause and speech, such as duration, pitch, spectrogram and occurrence locations.
Then, an effective algorithm based on these characteristics is proposed for detecting applause in meeting speech stream.
In the algorithm, the non-silence signal segments are first extracted by using voice activity detection.
Afterward, applause segments are detected from the non-silence signal segments based on the characteristic differences between applause and speech

Reports F1 scores of 96.15%.
Uses a Voice Activity Detection to get non-silence segments.
Uses minimum time threshold on applause.
Uses F0 from VAD.


#### Applause Sound Detection

https://www.aes.org/e-lib/browse.cfm?elib=15926
2011. AES
Uhle, Christian

A combination of mel-frequency cepstral coefficients and low-level descriptors yielded the best classification performance.
Low-pass filtering of the feature time series leads to the concept of sigma features.


#### TOWARDS RELIABLE REAL-TIME OPERA TRACKING: COMBINING ALIGNMENT WITH AUDIO EVENT DETECTORS TO INCREASE ROBUSTNESS

Attempt live tracking of full operas
First apply a state-of-the-art audio alignment method based on online Dynamic Time-Warping (OLTW).
Analyzing the tracker’s most severe errors, identify three common sources of problems specific to the opera scenario.
To address these, we propose a combination of a DTW-based music tracker with specialized audio event detectors -
for applause, silence/noise, music, and speech.
Also combines with MFCC.


https://www.researchgate.net/publication/321363547_On_Similarity_and_Density_of_Applause_Sounds

Applause ranges from very sparse sounds with well-distinguishable individual claps for small crowds to extremely dense and almost noise-like sounds for very large crowds.
While commonly used perceptual attributes like loudness, pitch, and timbre seem insufficient to characterize different types of applause,
"density" was recently introduced and found to be an important perceptual attribute for characterizing applause sounds. 


Very few people clapping, it consists of very sparse and well-organized isolated claps, 
ranging up to extremely dense and completely noise-like signals with no identifiable structure
when a huge crowd is applauding.
The mixture of noise-like signal components (with large entropy),
and individually perceivable and temporally fine-granular impulses provides only very little
redundancy or irrelevancy that could be used for bit rate reduction in perceptual audio coding.


A novel semantic applause decomposition method into
foreground claps and noise-like background is introduced
and shown to be beneficial in several applications

#### Video Temporal Segmentation using Applause Sound and End-of-Act Detection for a Circus Performance Video Archive

13 pages of literature review on Applause Sound detection



#### Perception and Processing of Applause-Like Sounds
Alexander Adami


For instance, the amount of reverberation has an effect on how strongly individual claps are
temporally smeared and blended resulting in an increased noise floor and consequently, rendering
the applause more noise-like. Furthermore, room acoustics imposes a certain venue-dependent
spectral envelope on the resulting applause sound given by the room’s impulse response. There

Also spatial dependencies on the perceived characteristics of applause, e. g., applause listened
to from inside a crowd sounds much more inhomogeneous than from outside a crowd. Whereas
the former scenario results in more individual and prominent near-by foreground claps dominating
the background component, with increasing distance to the crowd in the latter scenario, the
ratio of both shifts towards the relatively equal-leveled background component. This effect is
dependent on the size of the crowd, as well, and more prominent for a large crowd.

Synthesis approach using layering.
Hidden reference test using webMUSHRA.

Defined applayse density indicator.
Foreground vs background applause events.
Model to decompose foreground to background applause/clapping events.


# Exploratory Data Analysis

Applause is mostly in the form of clapping.

Co-occurences in addition to clapping.
There can be voice/speech overlapped. From presenter or host.
There can be yeeps and other calls. Engaged audience.

In spectrogram view, clapping looks pretty "dense" (as opposed to sparse). Especially compared to speech.
Both broad-band in terms of frequency content. And no tonal components.
And also dense in time. Onsets are close enough that room reverberation never lets the levels drop all the way down.

In published conference talk recordings, the clapping is relatively low in volume relative to the person(s) speaking.
This is usually the desired for playback, and levels are probably set to make it so, either live or in post-production.
Means that it is not entirely representative of the sound in the room in terms of sound level.
I would think that applause would generally be as loud as person speaking, or maybe a bit louder even?
!1 file had room mic in separate channel from speaker microphones.


