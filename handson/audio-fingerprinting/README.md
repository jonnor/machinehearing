
# Audio identification using fingerprinting

## Notebooks

- [Constellation map](./Constellation.ipynb).
Example of computing Shazam-style constellations using peak-finding on a spectrogram.


## Educational resources

### Fundamentals of Music Processing
https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S1_AudioIdentification.html
Describes the classic audio fingerprinting using spectral landmarks.
With implementations in Python.

### Wolfram: Audio Fingerprinting
https://www.youtube.com/watch?v=oCHeGesfJe8
By Carlo Giacometti.
Implemented in the Wolfram language.
Describes in step-by-step fashion several fingerprinting techniques.
This includes the ChromaPrint method (used by AcoustId), and the "constellation" method (used by Shazam).
Describes fingerprint construction, hashing, matching process.

Can compute just the humber of fingerprint (block) matches.
Or check that the matching blocks are in the correct time/order.

### How does Shazam work

Blogpost by Cameron MacLeod
https://www.cameronmacleod.com/blog/how-does-shazam-work
Contains a lot of good diagrams

Made an implementation in Python
https://github.com/notexactlyawe/abracadabra

### EuroPython 2016: Implementing a Sound Identifier in Python
Presentation by Cameron MacLeod.
Video: https://av.tib.eu/media/21115

### FOSDEM 2016: Over-the-air Audio Identification
How to build a system for matching a partial audio recording
from noisy environments with an audio track or a real-time stream of audio.
Presentation by	Arda Yalçıner.
Video: https://archive.fosdem.org/2016/schedule/event/audio_identification/

Decribes the architecture of a practical system.
Includes also a discussion of the fingerprinting itself.

### How Shazam Works - An explanation in Python
By Michael Strauss
https://michaelstrauss.dev/shazam-in-python

Contains Python example code along with explanations.
Full code in git repository, https://github.com/MichaelCStrauss/shazam-python

### ChromaPrint: How does it work

Two blog post by the creator of the algorithm
https://oxygene.sk/2010/07/introducing-chromaprint/
https://oxygene.sk/2011/01/how-does-chromaprint-work/

### EmySound: How does Audio Fingerprinting work
https://emysound.com/blog/open-source/2020/06/12/how-audio-fingerprinting-works.html

Describes the approach used in SoundFingerprinting library.

## Software

### Dejavu
Audio fingerprinting.
Using spectrogram peaks.
Implemented in Python.
Uses a database. Binary hashing of fingerprints.
https://github.com/worldveil/dejavu

Process described in
https://willdrevo.com/fingerprinting-and-audio-recognition-with-python/

### SpectroMap
https://github.com/Aaron-AALG/spectromap
Python library for getting spectrogram constellation map (or audio fingerprint).

### ChromaPrint 
Homepage. https://acoustid.org/chromaprint
Code. https://github.com/acoustid/chromaprint

MIT. Includes LGPL code from ffmpeg. 

### pyacoustid
https://github.com/beetbox/pyacoustid
MIT license

### abracadabra
https://github.com/notexactlyawe/abracadabra
Implements the Shazam constellation method

Simple command-line tool that allows to register music,
and then listen to microphone to recognize sounds.
Must be installed from git. Not yet on PyPi
MIT licensed

### soundfingerprinting
https://github.com/AddictedCS/soundfingerprinting

- Implemented in C#
- MIT licensed


### Adblockradio
Used a Shazam-like audio fingerprinting technique using spectrogram peaks.
Implemented in Node.js
https://github.com/adblockradio/stream-audio-fingerprint

### Robust Landmark-Based Audio Fingerprinting
https://www.ee.columbia.edu/~dpwe/resources/matlab/fingerprint/
Dan Ellis, 2012
MATLAB implementation. Also been ported to Octave
Based on the ideas used in the Shazam music matching service

No license mentioned.

## Papers

### An Industrial-Strength Audio Search Algorithm
A Wang, 2013
Seminal paper from Shazam.
Over 1k citations.
Introduced the concept of peak-pairs.
As a core feature uses a triplet of `f0, f1, t1-t0`.
Has drastically increaed specificity.

### A Highly Robust Audio Fingerprinting System
https://ismir2002.ismir.net/proceedings/02-FP04-2.pdf
Jaap Haitsma and Ton Kalker, 2002
Seminal paper from Philips Research.
Over 1k citations.

### Efficient music identification using ORB descriptors of the spectrogram image
https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-017-0114-4
EURASIP Journal on Audio, Speech, and Music Processing volume. 2017 

Compare the ORB based method to Shazam.
Shows much better results for speed (pitch+tempo), pitch, tempo changes in songs.
Slightly worse results for gaussian noise.
Storage space was 10% higher than Shazam.

Stores the ORB spectrograms, and not a hash.
Scales much more poorly with number of songs in database.

Based on work done in ORB: an efficient alternative to SIFT and SURF
ORB is two orders of magnitude faster and more computationally efficiency than SIFT.

ORB descriptors can be more efficiently queried using Locality Sensitive Hashing
combined with Approximate Nearest Neighbors search.
OpenCV has an example using FLANN.
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html#flann-based-matcher

## Services

### AcousticId
https://acoustid.biz/

Uses the ChromaPrint algorithm.

Pricing
- 1 million searches, 50 USD/month
- 15 million searches, 150 USD/month

### EmySound
https://emysound.com

