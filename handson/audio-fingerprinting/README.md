
# Audio identification using fingerprinting

Stack Overflow questions

- https://stackoverflow.com/questions/75490868/how-to-get-mel-spectagram-peaks-array-in-python

## Educational resources

### Fundamentals of Music Processing
https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S1_AudioIdentification.html
Describes the classic audio fingerprinting using spectral landmarks.
With implementations in Python.

## Software

### Adblockradio
Used a Shazam-like audio fingerprinting technique using spectrogram peaks.
Implemented in Node.js
https://github.com/adblockradio/stream-audio-fingerprint

### Dejavu
Audio fingerprinting.
Using spectrogram peaks.
Implemented in Python.
Uses a database. Binary hashing of fingerprints.
https://github.com/worldveil/dejavu

Process described in
https://willdrevo.com/fingerprinting-and-audio-recognition-with-python/

### spectromap
https://github.com/Aaron-AALG/spectromap
Python library for getting spectrogram constellation map (or audio fingerprint).

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


