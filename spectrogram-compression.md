
# Spectrogram data compression 

What is a good compression scheme for spectrogram/time-frequency data?
What kind of lossy compressions can be tolerated, if any?
The process should probably be easily reversible.

## Image compression on spectograms

First tests in Compression.ipynb in jonnor/birddetect

    birdsong in noisy environment
    10 sec, 64 mels, 12ms frameshift (800 frames)
    8bit log melspec. 55k original

    with PNG
    30k, approx 50% of original
    8bit log melspec, with JPEG
    70% quality. => 8k, approx 15% of original.
    10% quality. => 2k, 4% of original.
    Visibly very degraded, but seems to have preserved the bird calls OK

Looks like 1/10th the size _might_ be realistic!

TODO: test classification with compressed spectograms
Both mismatched (train on originals, test on compressed)
and reduced (train+test on compressed)

## Usage as raw data
Can spectrograms be used as 'raw' data format, intead of the audio waveform?

Requirements: 

- Learn-able. Can be used to train strong methods.
- **Annotate-able**. Can be labeled by humans to establish ground truth.
Transform back to audio for listening? Is the phase information neccesary?
Can one use DCT compression and skill preserve intelligibility?
- Adaptable, can be used for other purposes than originally intended.
Ex. From birdsong presence detection to bird species classification
Can be used to develop stronger systems as state of art improves, or constraints are relaxed.
- General-purpose. Can be used across a wide range of problems.
Bioacoustics, ecoacoustics, industrial monitoring, security

### Implementation on sensor

OpenMV has an MIT licensed software JPEG encoder, optimized for microcontrollers.
Mostly integer math, using precomputed DCT etc.
https://github.com/openmv/openmv/blob/master/src/omv/img/jpeg.c

"have tried running a JPEG encoder on ESP32, and got about 20 fps at 320×240 when compiling with -Os"
https://hackaday.com/2016/10/31/whats-new-esp-32-testing-the-arduino-esp32-library/#comment-3250015


Refs

[Survey of image compression algorithms in wireless sensor networks](https://ieeexplore.ieee.org/abstract/document/4631875/). 2008.
A review on eight popular image compression algorithms.
Found that Set-Partitioning in Hierarchical Trees (SPIHT) wavelet-based image compression best.
High compression efficiency and its simplicity in coding

## Normalization

Should they be recorded/transmitted raw, or after applying normalization?
Maybe store RMS and median/mean alongside?

## Amplitude non-linearity
log is the standard. Compresses the range of numbers a bit. Has also been shown to be beneficial to classification:
A COMPARISON OF AUDIO SIGNAL PREPROCESSING METHODS FOR DEEP NEURAL NETWORKS ON MUSIC TAGGING

`TODO: consider other scaling methods. sqrt/cubic`
https://www.researchgate.net/publication/269097301_Comparing_Time-Frequency_Representations_for_Directional_Derivative_Features
Found cube-root compression to be good, both on Gammatone and Mels.

Human and Machine Hearing book:
Ch3.1. Page51. Great diagram of relationship between log,exp,pow(...) as expanding or contracting non-linear functions.
Ch5.5. Page 98. Power-law compression of mel-spectrogram with exponents 0.25-0.67 can be better than log or lin.

### Refs

[Very low bitrate spatial audio coding with dimensionality reduction](https://ieeexplore.ieee.org/document/7952254). 2017.
Using tensor compression based on randomization and partial observations.
A common strategy is to transmit only the downmix of the objects along some small information permitting reconstruction at the decoder. In practice, this is done by transmitting compressed versions of the objects spectrograms and separating the mix with Wiener filters.
Previous research used nonnegative tensor factorizations in this context, with bitrates as low as 1 kbps per object.
Building on recent advances on tensor compression, we show that the computation time for encoding can be extremely reduced. Then, we demonstrate how the mixture can be exploited at the decoder to avoid the transmission of many parameters, permitting bitrates as low as 0.1 kbps per object.

[Reduced dimension image compression and its applications](https://ieeexplore.ieee.org/document/537681).
Reduced dimension image compression (ReDIC) algorithm.
Discuss its application to sonar spectrograms for low-latency, low-cost transmission.
Compare original and reconstructed spectrograms derived from real data at a 52:1 compression ratio.

[Speech reconstruction for MFCC-based low bit-rate speech coding](https://ieeexplore.ieee.org/abstract/document/6890586). 2014.
Speech reconstruction is a key issue in speech coding.
(LSE-ISTFTM) speech reconstruction algorithm for MFCC-based low bit-rate speech coding.
