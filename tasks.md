## Tasks

Established problem formulations

General

* Audio Classification
* Audio Segmentation
* Audio Source Separation
* Audio Fingerprinting
* Audio Retrieval

Music

* Beat Tracking
* Music Recommendation
* Music Retrieval
* Music Transcription
* Automatic Music Tagging

Speech

* Automatic Transcription
* Speaker Recognition
* Diarization

### Blind source separation

* Subspace based approaches. Aims to partition the mixture space into source dominant spaces.
Learns the source specific filters/dictionaries/basis that span those spaces.
Examples.
Principal Component Analysis (PCA),
Independent Component Analysis (ICA),
Subspace analysis
* Decomposing and grouping approaches.
The mixture spectrogram is divided into small time-frequency bins
and individual sources are then recovered using a masking.
Masking is is learned using the acoustic properties of the sources.
Examples:
Adaptive Wiener filtering/rules.
Ideal Binary Masking (IBM),
Computational Auditory Scene Analysis (CASA)
* Model based approaches.
Models of the sources are built/learned.
Examples: Non Negative Matrix Factorization (NMF),
Non Negative Sparse Coding (NNSC)

Singular Value Decomposition (SVD),
Eigen Value Decomposition (EVD)
Spectral decomposition
Factorial HMM

### Generating sound

[Roundtripping data via spectrograms in Python](https://timsainb.github.io/spectrograms-mfccs-and-inversion-in-python.html),
has code for converting (Mel) spectrogram back to audio.


### Temporal coherence

Speech has strong correlation (2nd order dependency) among adjacent Time-Frequency (T-F) slots in both time
and frequency. A T-F slot can be described as a pixel (or a set of adjacent pixels) in a power
spectrogram.

! Want to utilize this to classify, but many algorithms don't natively.




### Source separation

[Vocal source separation using spectrograms and spikes, applied to speech and birdsong](https://www.research-collection.ethz.ch/handle/20.500.11850/175085). PhD thesis, ETH Zurich, 2017.
Audio source separation methods (ASS). Monaural source separation (MSS) special-case of ASS where only a single mixture is observed.
Spectral subtraction, Wiener filtering, and subspaces used in speech enhancement.
Ideal Binary Mask (IBM) used in auditory scene analysis (CASA).
Deep Neural Networks have been used to learn binary and soft masks, with state of art reslults.
This thesis presents novel linear and non-linear methods to address MSS in a supervised scenario

Three linear methods proposed in the thesis are:
1) Eigenmode analysis of covariance difference (EACD).
This method identifies spectro-temporal features associated with large
variance for one source and small variance for the other source.
2) Maximum likelihood demixing (MLD).
In this method, the mixture is modelled as the sum of two Gaussian signals
and maximum likelihood is used to identify the most likely sources.
3) Suppression-regression (SR).
Autoregressive models trained to reproduce one source but suppress the other.
4) A non-linear method called Multi-layered Random Forest (MLRF).
MLRF is an ensemble method that trains decision trees for each frequency band.
Given a mixture spectrogram, these trees classify individual T-F bin as belonging
to one of the speakers thus returning an estimate of the IBM.
An estimated IBM in a given layer is used to train a RF classifier in the next higher layer.
Outperforms a deep learning based method in terms of SNR of reconstructed audio.

[Inverting spectrogram after Binary Masking](https://stackoverflow.com/questions/51655119/how-do-i-apply-a-binary-mask-and-stft-to-produce-an-audio-file/51773435#51773435).

[Birdsong Denoising Using Wavelets](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4728069/).
Using wavelets as alternative to bandpass. Not considering any source separation techniques.
Wavelet avoids the fundamental tradeoff between temporal and frequency resolution in Fourier spectrogram.
Nice background info on birdsong, including typical characteristics.

[Adaptive energy detection for bird sound detection in complex environments](https://www.sciencedirect.com/science/article/pii/S0925231214017068?via%3Dihub). Xiaoxia Zhang, Neurocomputing, 2015.
The noise spectrum of each band was estimated and the existent probability of the foreground bird sound for each band was computed to serve for the adaptive threshold of energy detection.
These foreground bird sound signals were detected and selected via adaptive energy detection from the bird sounds with background noises.
Features of Mel-scaled Wavelet packet decomposition Sub-band Cepstral Coefficient (MWSCC).
Moreover, the differences of recognition performance were implemented on 30 kinds of bird sounds at different Signal-to-Noise Ratios (SNRs)
under different noisy environments, before or after adaptive energy detection.
Classified with Support Vector Machine.

[Blind Source Separation With Non-stationary Mixing Using Wavelets](http://www.robots.ox.ac.uk/~sjrob/Pubs/addison_roberts.pdf)
ICA that uses wavelet representation. Uses a sliding-window ICA, assuming that mixing process changes slowly enough wrt window size.
"however seen that despite the best efforts of our proposed algorithm there are still difficulties with the permutation problem.
The choice of window size is also arbitrary". Proposes a Baysian framework as further work



## Audio Event Recognition

[Audio Event Recognition in the Smart Home](https://link.springer.com/chapter/10.1007/978-3-319-63450-0_12)
Very nice background to the Smart Home topic and role of Audio.
"AI applied in the audio domain has become a key driver of the smart home market",
due to home assistant devices such as Amazon Alexa and Google Home.
Contains a number of example applications.

[Machine learning in low-power devices brings sound recognition to the smart home market](https://community.arm.com/processors/b/blog/posts/machine-learning-in-low-power-devices-brings-sound-recognition-to-the-smart-home-market). Whitepaper. ARM, Audio Analytic. 2017.
"Amazon Echo, Google Home and most mobile phones are using microphone arrays to “target” people’s speech through a technique called beamforming,
the vast majority of Consumer Electronics and Smart Home devices are still natively using mono audio capture"
On-edge Audio Event Detection. A clip of the sound is sent along with event (if 512 KB RAM available).
Can support 3 event profiles on Cortex M4, 6 on Cortex M7.

[Sound Event Recognition in Unstructured Environments using Spectrogram Image Processing](http://www.ntu.edu.sg/home/aseschng/Thesis/JohnDennis_PhDThesis2014.pdf). PhD thesis, Jonathan William Dennis, 2014. 200 pages.

[Spectrogram Image Feature for Sound Event Classification in Mismatched Conditions](https://www.researchgate.net/publication/224206697_Spectrogram_Image_Feature_for_Sound_Event_Classification_in_Mismatched_Conditions). Jonathan Dennis, 2011.
Splits spectrogram into 3 bins. 
Linear spectrogram better than log spectrogram in presence of noise.

## Audio Denoising

Can be applied in different domains

* Time domain
* Frequency domain
* Spectrogram domain
* Cepstrum domain

Techniques

* Spectral median filtering
* RASTA-filtering.

Uses bandpass filtering in the log spectral domain, removes slow channel variations.
It has also been applied to cepstrum feature-based preprocessing with both log spectral and cepstral domain filtering.

[RNNoise](https://people.xiph.org/~jm/demo/rnnoise/).
Using deep learning combined with conventional signal processing.
Tuned for real-time usage, 10ms lookahead.
GRU type of RNN.
Split into 22 filterbanks, roughly following Bark scale.
42 inputs features.
Computes outputs: (1) Voice Activity Detection, (22) gains for filterbanks
Training using synthesized data. Adding noise to speech. Adding filters.
C code available, BSD licensed. 7x realtime on RPi.
Has 'donate your noise' collection for a noise dataset. Is it available anywhere?

### Noise types
Biophony, geophony, and anthrophony

* Biophony refers to any sound produced by biological agents: in the forest major biophonies are birds, insects, frogs/toads, and mammals.
Because we are only interested in acoustic activity of birds, all other biological sounds are categorised as noise
* Geophony refers to all non-biological, natural sounds in the environment such as
wind and its effect on trees, rain, thunder, and running water.
* Anthrophony refers to all sound generated from human-made machines such as
aircraft, vehicles, wind turbines, and the recording device (microphone, recorder hum)

Characterises the noise according to its properties into:

* White noise has equal energy at all frequencies, meaning that the power spectrum is flat.
In practice, noise is only white over a limited range of frequencies.
While not all white noise is Gaussian, natural white noise can often be modelled as such.
* Coloured noise shows a non-uniform power spectrum, with the energy generally decreasing in proportion to the frequency f.
Common types of coloured noise include pink (power ∝1f) and brown (power ∝1f2).
* Impulsive noise refers to sudden click like sounds that last for a very short period of time (milliseconds), such as switching noise.
An ideal impulse generates a horizontal line in the power spectrum because these sharp pulses contain all frequencies equally.
* Narrow-band noise such as microphone hum shows a small range of frequencies.
* Transient noise is a burst of noise that occurs for some time, and then disappears.


## Keyword spotting

[Trainable Frontend For Robust and Far-Field Keyword Spotting](https://arxiv.org/pdf/1607.05666.pdf). Yuxuan Wang, 2016.
Introduces Per-Channel Energy Normalization (PCEN).
Several issues with the log function.
1. First, a log has a singularity at 0.
Common methods to deal with the singularity are to use either
a clipped log (i.e. log(max(offset, x))) or a stabilized log (i.e. log(x+offset)).
However, the choice of the offset in both methods is ad hoc and may have different performance impacts on different signals.
2. Second, the log function uses a lot of its dynamic range on low level, such as silence,
which is likely the least informative part of the signal.
3. Third, the log function is loudness dependent.
With different loudness, the log function can produce different feature values even when the underlying
signal content (e.g. keywords) is the same,
which introduces another factor of variation into training and inference.
Although techniques such as mean–variance normalization and cepstral mean normalization can be used to alleviate this issue
to some extent, it is nontrivial to deal with time-varying loudness in an online fashion.

Simple feed-forward automatic gain control (AGC), which dynamically stabilizes signal levels.
Further propose to implement PCEN as neural network operations/layers and jointly optimize various PCEN.
Operation is causal and is done for each channel independently, making it suitable for real-time implementation.
The AGC emphasizes changes relative to recent spectral history and adapts to channel effects including loudness.
Following the AGC, we perform a stabilized root compression to further reduce the dynamic range using offset δ and exponentr.
We note that the offset δ introduces a flat start to the stabilized root compression curve,
which resembles an optimized spectral subtraction curve.
It is worth noting that the main parameters in PCEN are the AGC strength α and smoothing coefficient s,
whose choices depend on the loudness distribution of data.
In addition, PCEN tends to enhance speech onsets, which are important for noise and reverberation robustness.

To improve noise robustness, we perform multi-condition
training by artificially corrupting each utterance with various interfering
background noises and reverberations, where the noise
sources contain sounds sampled from daily-life environments
and YouTube videos. To further improve loudness robustness,
we also perform multi-loudness training by scaling the loudness
of each training utterance to a randomly selected level ranging
from −45 dBFS to −15 dBFS.


## Smart home assistants

[Whisper to Alexa, and She’ll Whisper Back](https://developer.amazon.com/blogs/alexa/post/c0e7798d-32bc-4549-9c24-97d204a7bf3a/whisper-to-alexa-and-she-ll-whisper-back).
Tech details from researcher on whisper detection, and how model differs from general spoken word.
