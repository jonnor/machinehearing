
## Advertisement detection

## SO question

https://stackoverflow.com/questions/75961430/how-to-find-out-how-many-times-a-specific-audio-repeats-in-another-longer-audio

Other questions about the same

- https://stackoverflow.com/questions/70076172/find-number-of-times-recognized-audio-repeat-in-the-source
- https://stackoverflow.com/questions/62086171/compare-a-fragment-of-an-audio-file-to-a-long-audio-file
- https://softwarerecs.stackexchange.com/questions/77290/finding-audio-clips-within-audio-files


https://stackoverflow.com/questions/75653582/check-if-a-small-audio-clip-is-part-of-another-audio-file
https://dsp.stackexchange.com/questions/36136/how-many-times-does-a-certain-sound-appear-in-an-audio-clip


## Problem formulation

- With a single query example.
One-shot detection. Audio matching.
- With 2-10 examples.
Few-shot detection.
- Without any query example.
Zero-shot detection.
Generic Audio Classification / Sound Event Detection / Audio Segmentation.

## Feature representation

Audio fingerprinting. Spectrogram landmarks. 

## Background

## Length of an advertisement

Ad spots are often in 15, 30, 45 or 60-second chunks.
Recommended to keep ads short.
15-30 seconds may be typical.

## Existing works

Advertisement detection and replacement using acoustic and visual repetition
https://research.google/pubs/pub55.pdf
M Covell et. al, 2006. Google Research.
Over 100 citations.

Adblock Radio. An adblocker for live radio streams and podcasts. Machine learning meets Shazam.
https://github.com/adblockradio/adblockradio
Project archived in 2021.
Had a web player for ad-free radio between 2015 and 2019.
https://www.adblockradio.com/en/

## Audio identification using fingerprinting

Used a Shazam-like audio fingerprinting technique using spectrogram peaks.
Implemented in Node.js
https://github.com/adblockradio/stream-audio-fingerprint

Audio fingerprinting.
Using spectrogram peaks.
Implemented in Python.
Uses a database. Binary hashing of fingerprints.
https://github.com/worldveil/dejavu

Process described in
https://willdrevo.com/fingerprinting-and-audio-recognition-with-python/

An Industrial-Strength Audio Search Algorithm
A Wang, 2013
Seminal paper from Shazam.
Over 1k citations.
Introduced the concept of peak-pairs.
As a core feature uses a triplet of `f0, f1, t1-t0`.
Has drastically increaed specificity.

https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S1_AudioIdentification.html
Describes the classic audio fingerprinting using spectral landmarks.
With implementations in Python.


A Highly Robust Audio Fingerprinting System
https://ismir2002.ismir.net/proceedings/02-FP04-2.pdf
2002
Jaap Haitsma, Ton Kalker
Philips Research


https://github.com/Aaron-AALG/spectromap
Python library for getting spectrogram constellation map (or audio fingerprint).



## Audio matching


https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_AudioMatching.html
Using subsequence Dynamic Time Warping, and Diagonal Matching.

https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_DiagonalMatching.html


https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_SubsequenceDTW.html
Explains DTW when applied to subsequence alignment / local alignment, for audio matching.
Compares implementations using `librosa` and `libfmp`.
https://librosa.org/doc/latest/generated/librosa.sequence.dtw.html

https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_DiagonalMatching.html


