
# Feature representations

* Energy
* Chroma.
* Spectrograms. Linear/log. Mel, bark, constant-Q.
* MFCC
* modulation spectrogram
* Scattering transform

Summarization, pooling
Typically across a set of frames

* Min/max
* Mean/stdev

Delta-frames, delta-delta frames.
Change and change-rate. Common with MFCC

* Bag of frames

Nice summary of feature calculation in Python 'from scratch'.
http://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html

[](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182309).
Using SIF features, spectrograms downscaled. 720 features per frame.
Used one frame energy summary feature. 
Shows SIF-SVM performing almost as good as SIF-CNN and SIF-DNN, and favorable under high noise.

CARFAC aka CAR-FAC, Cascade of Asymmetric Resonators with Fast-Acting Compression

* [Using a Cascade of Asymmetric Resonators with Fast-Acting Compression as a Cochlear Model for Machine-Hearing Applications](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/37215.pdf). Richard F. Lyon, 2011.
* Coclear model. PZFC. Pole-zero filter cascade.
Non-linearity. Feedback in AGC models saturation.
Computational load, approx that of a second-order filter per output channel.
Typical number of channels = 7?
* Converted to Stablilized Audatory Image (SAI). Using STFT?
* Local multi-scale sparse features.
Using Vector Quantization. Bag of Features representation of a file.
High dimesionality, 100'000 dimensions.
Fast online training using Passive Agressive classifier
* [CARFAC reference implementation in C++](https://github.com/google/carfac)

## Scattering Transform

[YouTube: Scattering Invariants for Audio Classification](https://www.youtube.com/watch?v=W_Wbnp_uw-o).
Associated paper: Deep Scattering Spectrum.
Classic approach: Construct an intermediate representation.
Conservative approach: Remove transformations which dont change the class.
Time-shifting. Want invariant. Want to be stable across time-warping (including dilation).
Can be done with Mels, want constant-Q at high frequencies.
Actually comes from biology/psycoacoustics, but has the good mathematical property of time-shift invariance.
8:55. Alternate way to get equivalent data of Mel spectrogram. Convolve filters, then time average them.
Can be seen as a wavelet transform. Constant-Q 'wavelet' filterbank.
But inveriance depends on frame size, and at large frame sizes loses temporal structure.
Want to relieve the model/classifier of having to learn temporal dynamics (equivalence)
Modulation spectrograms, one approach.
Wavelet Modulus Transform. Scattering Cascade.
Basically a convolutional network. Stages of filters and non-linearity (modulus).
Not learned coefficients, but comes from invariants.
Complimentary, CNN does then need to learn these. 
Typically wavelets per octave. 8,4,2 typical in stage 0,1,2.
Energy decays quickly with stages. Most info in 1-2 stages.
First order: Excitation info, Second order: modulation. 
Typical dimensions. 30-80 wavelet in first order, 100 in second order. 
Transform is O(n log n).
Possible to get a rough inverse of the scattering transform.
Frequency-transposition. Different formants can be seen as frequency warping.
Want to be stable for frequency warping for speech signals, often.
Joint (time-frequency) scattering. With a 2d wavelet.

[FEATURE LEARNING WITH DEEP SCATTERING FOR URBAN SOUND ANALYSIS](https://www.researchgate.net/profile/Justin_Salamon/publication/278019931_Feature_Learning_with_Deep_Scattering_for_Urban_Sound_Analysis/links/5578aec208aeacff200287c5.pdf). 2015.
Evaluate the scattering transform as an alternative signal representation to the mel-spectrogram
in the context of unsupervised feature learning for urban sound classification.
Comparable (or better) performance using the scattering transform whilst reducing
both the amount of training data required for feature learning and the size of the learned codebook by an order of magnitude.
Note that in practice computing the scattering transform will take longer than computing the mel-spectrogram
by a multiplicative factor proportionate to the dimensionality of the scattering output.

### Directional Derivative Features
A generalization of delta-features for arbitrary angles.

Comparing Time-Frequency Representations for Directional Derivative Features
https://www.researchgate.net/publication/269097301_Comparing_Time-Frequency_Representations_for_Directional_Derivative_Features
Found cube-root compression to be good, both on Gammatone and Mels.
Directional Derivative Features computed from a Steerable Pyramid Filter-bank.


# Feature learning

Aka feature construction, representation learning.
Has somewhat taken a back-seat to Deep Learning approaches
which integrates feature/representation learning,
such as Convolutional Neural Networks. 

Types

* Dictionary/codebook learning. Supervised/unsupervised
* Sparse coding. Unsupervised
* Non-negative matrix factorization. Unsupervised
* Convolutions. Clustering-based. Spherical k-means. Unsupervised
* Deep Audio Embeddings
* Random Features

## Random Features

[On Random Weights and Unsupervised Feature Learning](http://www.robotics.stanford.edu/~ang/papers/nipsdlufl10-RandomWeights.pdf).
ICML2011. References works showing that random convolutional kernels can do suprisingly well.
Suggesting that one important baseline should be random + linear classifier.
Uses this for fast CNN architecture search.

[DCASE 2017 TASK 1: Acoustic Scene Classification Using Shift-Invariant Kernels and Random Features](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/challenge_technical_reports/DCASE2017_Jimenez_186.pdf). 6k random features. Performed 4% points better than baseline with Gaussian kernel. Random features can be used as privacy measure, keeping the W,b parameters private.
[Another copy](http://www.cs.tut.fi/sgn/arg/dcase2017/documents/workshop_presentations/DCASE2017Workshop_Jimenez_195_presentation.pdf).
[ACOUSTIC SCENE CLASSIFICATION USING DISCRETE RANDOM HASHING FOR LAPLACIAN KERNEL MACHINES](http://www.mirlab.org/conference_papers/international_conference/ICASSP%202018/pdfs/0000146.pdf). IEEE paper.
Uses a linear SVM with random features to approximate a non-linear kernel SVM. Avoids expensive computation of high-dimensional kernel.
Approximates a shift-invariant kernel, like Gaussian, Laplacian and Cauchy.
Allows XOR Hamming distance based similarity calculation. 
With hashing, can reduce data by 2**6 / 64 with minor loss in performance.

## Dictionary Learning

Papers

* Learning Sparse Adversarial Dictionaries For Multi-Class Audio Classification. 2017.
Uses adverserial and reconstructive learning, and can be directly used as a classifier.
* Dictionary Learning for Bioacoustic monitoring with applications to species classification


### Non Negative Matrix Factorization
Non-negativity constraint of NMF only allows additive combinations (not subtractive),
in contrast to ICA/PCA.
Leads to a parts-based representation.
Recommended to impose constraints like sparseness, orthogonality, or smoothness to get more interesting basis vectors.

Many factorization approaches. Gradient descent. Multiplicative update rules, easy to implement.
Semi-supervised method possible with Schmidt2007 "Wind Noise Reduction using Non-negative
Sparse Coding".

[Non-Negative Matrix Factorization And Its Application to Audio](https://www.cs.cmu.edu/~bhiksha/courses/mlsp.fall2009/class16/nmf.pdf). Tuomas Virtanen.
Easy to follow introduction.
References many works on applying NMF to audio.

### Clustering-based

[Automatic large-scale classification of bird sounds is strongly improved by unsupervised feature learning](https://peerj.com/articles/488/).
D. Stowell, 2014. Classifier got strongest audio-only results in LifeCLEF2014.
Inspired by techniques that have proven useful in other domains.
Compare twelve different feature representations derived from the Mel spectrum, using four large and diverse databases of bird vocalisations. Classified using a random forest classifier.
"in our classification tasks, MFCCs can often lead to worse performance than the raw Mel spectral data from which they are derived"
"unsupervised feature learning provides a substantial boost over MFCCs and Mel spectra without adding computational complexity after the model has been trained"
Using spherical k-means, adapted to run in streaming fashion using online Hartigan k-means. Using two passes, first with reservoir subsampling.
Birdsong often contains rapid temporal modulations, and this information should be useful for identifying species-specific characteristics.
feature learning is that it can be applied not only to single spectral frames, but to short sequences (or “patches”) of a few frames.
Also tested a two-layer version, second layer downsampled projected data by 8 then applying feature learning again. 

Hierarchical representation learning using spherical k-means for segmentation-free word spotting
https://www.sciencedirect.com/science/article/pii/S0167865517304166
For Handwriting recognition.

[Learning Feature Representations with K-means](https://cs.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf). Adam Coates, Andrew Ng. 2012.
Best practices for unsupervised learning of convolutional kernels using K-means.
Contrast/mean normalization. ZCA whitening.
6x6 to 8x8 image patches work well, with 500'000 examples, and 256 size codebook.
Suggest 2x2 or 3x3 average pooling.
Tips for multi-resolution and pooling.
Deep models using a 'receptive field' learning scheme. Tested on CIFAR-10.
! Suggests feature learning in separate image regions where they are expected to differ significantly.
This would be case along frequency axis in spectrograms.

[Multiscale approaches to music audio feature learning](https://biblio.ugent.be/publication/4152117). 2013.
Music audio exhibits structure on multiple timescales, which are relevant for different MIR tasks to varying degrees.
We develop and compare three approaches to multiscale audio feature learning using the spherical K-means algorithm.


[A support vector machine (SVM) classifier was built on the sparse representation for acoustic event detection](https://ieeexplore.ieee.org/abstract/document/6854807). 2014.
Bag of spectral patch exemplars. k-means clustering based vector quantization (VQ) was applied on the whitened spectral patches.
sparse feature representation is extracted based on the similarity measurement to the learned exemplars.
A support vector machine (SVM) classifier was built on the sparse representation for acoustic event detection.

