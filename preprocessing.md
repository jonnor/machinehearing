
### Preprocessing

* A-weighting
* Log transform
* Harmonic-percussive-residual source separation. Especially for music.
* Per-channel energy normalization (PCEN).
Static version exists as [librosa.pen](https://librosa.github.io/librosa/generated/librosa.core.pcen.html).
Can also be learned as a neural network layer, see arXiv:1607.05666v1
[Per-Channel Energy Normalization: Why and How](www.justinsalamon.com/uploads/4/3/9/4/4394963/lostanlen_pcen_spl2018.pdf).

* Whitening. Eg PCA.
Removes redundancies in spectrogram. For each frame in spectogram

Normalization

* Cepstral Mean Normalisation (CMN): subtract the average feature value from each feature, so each feature has a mean value of 0.
makes features robust to some linear filtering of the signal (channel variation).
* Cepstral Variance Normalisation (CVN): Divide feature vector by standard deviation of feature vectors, so each feature vector element has a variance of 1.
* For real-time, need to compute a moving average.
* RMS normalization
* Gaussianization, mapping to Gaussian distribution

