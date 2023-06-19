
# Wind noise detection

Audio recordings made outdoors can often be contaminated by wind induced microphone noise.


## Papers

## Automatic detection of microphone wind noise :Maximising accuracy of amplitude modulation ratings
https://core.ac.uk/reader/74220300
Sabine von Hünerbein, Trevor Cox, Paul Kendrick
Acoustic Research Centre, University of Salford

Decision trees
Classified into multiple wind noise level classes / SNR classes.

Used a time-series method, and a modulation frequency method
Used 23 ms frames, and 1 second aggregation

https://www.researchgate.net/publication/265394962_Perception_and_automatic_detection_of_wind-induced_microphone_noise

### Automatic classification and reduction of wind noise in spectral data
https://pubs.aip.org/asa/jel/article/1/6/063602/219610/Automatic-classification-and-reduction-of-wind
2021.

The method uses the characteristic spectral slope of wind noise to classify individual spectral frequencies as either contaminated or uncontaminated.

When several short-timescale measurements (e.g., several two-second spectra) are available,
a decontaminated long-timescale average spectrum can be calculated (e.g., a spectrum composed of one-hour median spectral levels at each frequency, also known as an L50⁠)


he frequency spectrum of atmospheric turbulent pressure fluctuations can be grouped into three frequency ranges:
the energy-containing range, the inertial subrange, and the dissipation range.
The energy-containing range occurs at low infrasonic frequencies (often less than a few Hz),
which are below the frequencies of interest for the outdoor acoustic measurements considered in this paper.
In the dissipation range, turbulent fluctuations rapidly dissipate into heat,
so wind noise is typically negligible compared with the acoustic sources or instrumentation noise.
The frequency of the dissipation range increases with wind speed and typically occurs above 100–1000 Hz.


For most outdoor acoustic measurements, contaminating wind noise in the inertial subrange is of primary importance.
The inertial subrange lies between the energy-containing range and the dissipation range and can occur between high infrasonic and mid-range audible frequencies.
In the inertial subrange, the stagnation pressure fluctuations caused by atmospheric turbulence interacting with the microphone diaphragm or windscreen are proportional to f−5/3
⁠, where f is the frequency. Turbulent-turbulent pressure fluctuations, which are proportional to f−7/3⁠, are negligible compared with the stagnation pressure fluctuations.3
Thus, the magnitude frequency spectrum of wind noise varies linearly with logarithmic frequency, i.e., SPL∝log(f)⁠, where SPL is the sound pressure level created by wind noise.

Identifying contamination in screened microphone data processed using one-third-octave bands is accomplished by finding data which approximates the characteristic wind noise slope of −26.7 dB per decade.

### Wind-induced microphone noise detection - Automatically monitoring the audio quality of field recordings
https://www.researchgate.net/publication/261204456_Wind-induced_microphone_noise_detection_-_Automatically_monitoring_the_audio_quality_of_field_recordings
2013

A large training database is formed from a wind noise simulator which generates an audio stream based on time histories of real wind velocities. A Support Vector Machine detects and classifies according to wind noise level in 25 ms frames which may contain other sounds. Statistical and temporal data from the detector over a sequence of frames is then used to provide estimates for the average wind noise level.


### Wind-robust sound event detection and denoising for bioacoustics
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13928
2022

Uses wavelet spectrogram

### Characterizing and detecting wind noise in audio recordings
Honkakunnas, Aapo (2021)

Four audio signal features were used in modeling the characteristics of wind noise:

- zero-crossing rate,
- root mean square energy,
- sub-band spectral centroid,
- magnitude squared coherence

Logistic regression, Gaussian Mixture Model, and Hidden Markov model

Got precision 90% at recall 80%.
### A review of wind-noise reduction methodologies.
2009

### Wind-induced microphone noise detection - automatically monitoring the audio quality of field recordings
https://ieeexplore.ieee.org/document/6607519
Kenrick, Cox

This paper presents a single channel algorithm which, within the presence of other sounds, detects and classifies wind noise according to level.
A large training database is formed from a wind noise simulator which generates an audio stream based on time histories of real wind velocities.
A Support Vector Machine detects and classifies according to wind noise level in 25 ms frames which may contain other sounds.
Statistical and temporal data from the detector over a sequence of frames is then used to provide estimates for the average wind noise level

### Sub-Band Detector for Wind-Induced Noise
Sapozhnykov, V. V, 2019

TODO

### Robust Wind Noise Detection and Suppression for Wearable Glass with Multi-Microphone Array
Anthony D. Rhodes, Intel Corporation

Wind Detection Methods (5):

- (WD1) Short-Term Mean (STM) Method
- (WD2) Signal Sub-Band Centroids (SSC) Method
- (WD3) Negative Slope Fit (NSF) Method
- (WD4) Coherence-Based Methods
- (WD5) Neural Network with Context-Framing

the spectral energy distribution for very low frequencies (< 10 Hz) for
wind is discernable from that of speech.

#### Short-Term Mean (STM) Method
I_STM(λ) using short-term mean features for time frame λ.
The mean value of short segments can be used to detect low frequency parts in a signal.

C. Nelke. “Wind noise short term power spectrum estimation using pitch adaptive inverse binary
masks”, in Proc. of IEEE Intern. Conference on Acoustics, Speech and Signal Processing, 2015.

#### Signal Sub-Band Centroids (SSC) Method

Signal sub-band centroids (SSC) as a discriminative feature
Consider the sub-band range: [0, 10]
Apply a smoothing procedure (500ms windows), following by a Gaussian fit

#### Negative Slope Fit (NSF) Method
NSF (negative slope fit) approach to wind noise classification
magnitude of the spectrum of wind noise can be roughly approximated
by a linear decay over the frequency

#### Neural Network with Context-Framing
Feed-forward NN for wind noise detection
log-power spectra. Frame length??
Using N=3 context frames
Using noise-aware training
50 hidden nodes
Using 1 minute of training data
200 ms frame smoothing

### 

## Data

### Wind Noise Database
https://www.iks.rwth-aachen.de/forschung/tools-downloads/databases/wind-noise-database/
Indoor and outdoor samples.
MATLAB code for a generative wind noise model.

### Test dataset for separation of speech, traffic sounds, wind noise, and general sounds
https://zenodo.org/record/4279220

Contains various sounds from the Audio Set and spoken utterances from VCTK and DNS datasets.
