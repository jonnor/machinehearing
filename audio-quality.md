
# Audio quality

Any system that reproduces sound needs to do so with a certain quality.
Many metrics have been defined that can measure various aspects of audio quality.
This is an overview of these.

<!-- TODO: Make a table of all the metrics. Link to relevant section -->

## Taxonomy

- Purpose.
Speech Intelligibility,
Speech Quality,
Audio/music quality
- Input data.
Reference or no.
- System modelling.
Signal-based or 
- Measurement type.
Objective, subjective

Is there an objective way to measure sound quality? RE music
https://www.quora.com/Is-there-an-objective-way-to-measure-sound-quality-Audio-community-often-cite-uneven-frequency-in-highs-mids-and-lows-as-poor-audio-quality-but-how-is-that-perceptually-negative-to-someone-who-listens-to-music


### LLR

Evaluation of Objective Quality Measures for Speech Enhancement
2008.
https://ieeexplore.ieee.org/document/4389058
https://ecs.utdallas.edu/loizou/speech/obj_paper_jan08.pdf

Several objective speech quality measures were evaluated:
segmental SNR (segSNR),
weighted-slope spectral distance (WSS),
PESQ,
LPC (Linear Predictive Coding) based objective measures including the
log-likelihood ratio (LLR),
Itakura-Saito distance measure (IS),
and cepstrum distance measures (CEP),
and frequency-weighted segmental SNR (fwsegSNR)

> Compared to the PESQ measure, the LLR and fwSNRseg
> measures are computationally simpler to implement
> and roughly the same correlation coefficient was obtained

!alternative to PESQ?

### fwSNRSeg


### PSQM

ITU-T Recommendation P.861.
1996.
Superseeded by PESQ.

### PESQ
https://en.wikipedia.org/wiki/PESQ

ITU standard.
2001.
https://www.itu.int/rec/T-REC-P.862

`pesq`. Reference implementation provided in C.

https://github.com/ludlows/python-pesq
Python module. Copied original C code.

https://github.com/vBaiCai/python-pesq
another Python package. Marked as WIP

https://www.researchgate.net/post/Is_PESQ_score_a_good_measurement_for_performance_analysis_of_speech_enhancement_algorithms

    PESQ was not intended to compare speech before and after noise reduction.
    Its stated aims were to quantify degradation due to codecs and transmission channel errors.
    It was originally tested on speech with environmental noise (i.e., clean original vs. noisy signal)
    and was found to correlate well in that case.
    However, PESQ was found not to correlate with subjective MOS on a number of other tasks (see the standard), 
    and thus should not be blindly used unless tested first.

### POLQA
http://www.polqa.info/

Requires a license.
May have usage restrictions?

> The POLQA perceptual measurement algorithm is a joint development of OPTICOM, SwissQual and TNO,
> protected by copyrights and patents and available under license from OPTICOM as software for various platforms.

Latest version is POLQA v3 (2018)

Available as PolqaOem64
Used by WebRTC
https://github.com/webrtc-uwp/webrtc/tree/master/modules/audio_processing/test/py_quality_assessment

### VISQOL
Virtual Speech Quality Objective Listener
Signal-based, full-reference, intrusive metric that models human speech quality perception

Based on similarity of spectrograms
Designed to be particularly sensitive to VoIP degradation
> Using a distance metric called the Neurogram Similarity Index Measure or NSIM
Inspired by Structural Similarity Index (SSIM)
> In this work, spectrograms are treated as images to compare similarity.

ViSQOL: an objective speech quality model
https://ai.google/research/pubs/pub43990/
https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-015-0054-9
EURASIP, 2015
Hines

> Paper compares quality predictions with PESQ and POLQA for common problems in VoIP:
> clock drift, associated time warping, and playout delays.
> The results indicate that ViSQOL and POLQA significantly outperform PESQ,
> with ViSQOL competing well with POLQA.

! nice block diagrams of ViSQOL and PESQ, POLQA

> (On speech enhancement algorithms)
> However, these metrics have difficulty with modern communications networks.
> Modern codecs can produce high-quality speech without preserving the input waveform.
> Quality measures based on waveform similarity do not work for these codecs.
> Comparing signals in the spectral domain avoids this problem
> and can produce results that agree with human judgement

### VISQOLAudio

ViSQOLAudio: An objective audio quality metric for low bitrate codecs
https://asa.scitation.org/doi/full/10.1121/1.4921674?TRACK=RSS
Hines

Moidification of ViSQOL, with Voice Activity Detection removed and wider range of frequency bands.
Bark scale.

- AAC-HE and AAC-LC codecs at four bit rates and examples of MP3 and OPUS codecs
- PEAQ, POLQA, and VISQOLAudio
- compared against the subjective listener test results carried out with headphones
to evaluate their suitability for measuring audio quality for low bit rate codecs

MATLAB implementation of ViSQOLAudio available.
! no license info
! password protected, request via email
http://www.mee.tcd.ie/~sigmedia/Resources/ViSQOLAudio
https://sites.google.com/a/tcd.ie/sigmedia/visqolaudio

### AudioMOS

### SI-SDR
Corrected version of 'SI' method from BSS_eval.

https://ieeexplore.ieee.org/document/8683855


mir_eval implements `bss_eval_sources`
Open issue (since 2014...) to implement more.
https://github.com/craffel/mir_eval/issues/68
Also has critiques of bss_eval

### Speech Intelligibility Index
Only reliable for "simple degradations" (additive noise)

### STOI.
Short-time Objective Intelligibility measure.

> Intelligibility measure which is highly correlated with the intelligibility of degraded speech signals,
> e.g., due to additive noise, single/multi-channel noise reduction, binary masking and vocoded speech as in CI simulations.
> The STOI-measure is intrusive, i.e., a function of the clean and degraded speech signals.
> 
> STOI may be a good alternative to the speech intelligibility index (SII) or the speech transmission index (STI),
> when you are interested in the effect of nonlinear processing to noisy speech,
> e.g., noise reduction, binary masking algorithms, on speech intelligibility.

Paper.
https://ieeexplore.ieee.org/document/5495701

- Method is based on spectrograms.
- 15, 1/3 octave bands. Bands from 150-4500 Hz.
- 25 ms frames.
- 400 ms windows.
- Compares two spectrograms, using correlation cofficient. ? more details
- Outputs a time-frequency score.
- Overall score is then the average of these.

Is an estimation of how humans would evaluate. 

https://github.com/mpariente/pystoi
Pure Python implementation.
Python 3 compatible.
Available on PIP.
Has tests against the MATLAB reference implementation by
authors of the paper proposing the method.
http://www.ceestaal.nl/code/
