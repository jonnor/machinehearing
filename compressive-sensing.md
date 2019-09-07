
# Compressed sensing
Aka compressive sensing.

Family of signal processing methods that allow efficient aquisition and reconstruction of sparse signals.

Avoids having to sample at very high frequencies when the information of interest is

This is of special interest to battery-powered continious-monitoring systems,
where aquisition can be a bottleneck in power consumption.

## Introduction

[Compressed Sensing: The big picture](https://sites.google.com/site/igorcarron2/cs).
Acquiring and recovering a sparse signal in the most efficient way possible (subsampling) with the help of an incoherent projecting basis.
Buildling sensing hardware that can directly produced such compressed signals.
Sparse means signal of interest is compressible. Challenge: Need to know with which family of functions it is sparse.
Fourier,polynomials,wavelets.
Many approaches to finding sparse representations/sparse dictionaries. Page lists 11.
Donoho-Tanner phase transition diagram, tool for evaluating whether a signal is compressible with an L1 solver.
Lists a set of 10 different conditions needed to enable sparse recovery.
Lists some 40 different solvers, until 2013.

[Introduction to Compressed Sensing](http://www.dfg-spp1324.de/download/preprints/preprint093.pdf). `TODO: review and make notes`

[Compressive Sensing](https://link.springer.com/referenceworkentry/10.1007%2F978-0-387-92920-0_6). 2011.
Introduction and overview on both theoretical and numerical aspects of compressive sensing

[Compressive Sensing by Random Convolution](https://epubs.siam.org/doi/abs/10.1137/08072975X). 2009. `TODO: review`
Demonstrates that convolution with random waveform followed by random time-domain subsampling is a universally efficient compressive sensing strategy. 

Practical Compressed Sensing: modern data acquisition and signal processing. 2011. Becker.

## Review papers

[A Systematic Review of Compressive Sensing: Concepts, Implementations and Applications](). 2018, IEEE Access. MEENU RANI.
Accessible intro, good diagrams. Table over Number of Required Compressive Measurements with different random methods.
Including structured random and determenistic, which does not have to be sent along with signal.
Acquisition strategies: RANDOM DEMODULATOR, MODULATED WIDEBAND CONVERTER (MWC), RANDOM MODULATION PRE-INTEGRATOR (RMPI), RANDOM FILTERING,
COMPRESSIVE MULTIPLEXER, RANDOM EQUIVALENT SAMPLING (RES), RANDOM CONVOLUTION, QUADRATURE ANALOG-TO-INFORMATION
CONVERTER (QAIC), RANDOM TRIGGERING-BASED MODULATED WIDEBAND COMPRESSIVE SAMPLING (RT-MWCS).
! Random Filtering seems easy and applicable to streaming data.
Recovery methods.
Basis Pursuit, Basis Pursuit Denoising (BPDN), Dantzig Selector, Total Variation Denoising (TV).
Convex optimization: BP simplex, BP interior...
Greedy algorithms. Faster but requires knowledge of signal sparsity.
Matching Pursiot, Orthongonal Matching Pursuit.
Compressive sampling matching pursuit (CoSaMP) and subspace pursuit (SP).
Iterative hard thresholding (IHT), Iterative soft thresholding (IST), approximate message passing (AMP).
Fourier sampling, heavy hitters on steroids (HHS), chaining pursuits and sparse sequential matching pursuit. 


[Convolutional Dictionary Learning: A Comparative Review and New Algorithms](https://arxiv.org/abs/1709.02893). 2018.

[Sparse Representations, Compressive Sensing and dictionaries for pattern recognition](https://ieeexplore.ieee.org/abstract/document/6166711/).
2011, Vishal M. Patel. `TODO: review`
Compressive Sensing (CS), Sparse Representation (SR) and Dictionary Learning (DL). 
Recent works in SR and CS have shown that if sparsity in the recognition problem is properly harnessed then the choice of features is less critical.
What becomes critical, however, is the number of features and the sparsity of representation.


## Applications

Applications in MRI, 3d-imaging, hyperspectral imaging, ultrasound imaging.

DiffuserCam, [Lensless single exposure 3d-imager](http://nuit-blanche.blogspot.com/2017/10/diffusercam-lensless-single-exposure-3d.html).
[3d-ultrasound with single sensor](http://nuit-blanche.blogspot.com/2017/12/compressive-3d-ultrasound-imaging-using.html)


One of the world’s first compressed sensing hardware devices, the random modulation pre-integrator (RMPI). The RMPI


## Applied to sound


[Single-sensor multispeaker listening with acoustic metamaterials](http://people.duke.edu/~yx35/reprints/Cocktail_party_listener_PNAS2015.pdf)
Hardware approach to multi-source separation. Using 3d-printed waveguides, single sensor.


[COMPRESSED SENSING OF AUDIO SIGNALS USING MULTIPLE SENSORS](https://www.researchgate.net/publication/257304755_Compressed_sensing_of_audio_signals_using_multiple_sensors). 2008. Anthony Griffin and Panagiotis Tsakalides.
Compares Signal Distortion Ratio (SDR) of Speech,Music,Birdcall,Impulsive type audio with DCT/DWT and basis/orthononal matching pursuit.
! Birdcall shows very high SDR, when using DCT. Good for denoising? 

[Effect of downsampling and compressive sensing on audio-based continuous cough monitoring](https://ieeexplore.ieee.org/abstract/document/7319816/). 2015.
98% at full rate. Undersampling to 400Hz 90%.
Sampling with compressive sensing at 100Hz also 90%.

[A compressive beamforming method](https://ieeexplore.ieee.org/abstract/document/4518185/). Direction of Arrival estimation.

[A Comparative Study of Audio Compression Based on Compressed Sensing and Sparse Fast Fourier Transform (SFFT): Performance and Challenges](https://arxiv.org/abs/1403.3061).
References two other papers about compressed sensing in audio compression.
To obtain exact recovery, the rule of thumb is to apply incoherent sampling and taking measurements 4 times the sparsity level of the signal.
Orthogonal Matching Pursuit one algorithm for doing recovery.
Sparse Fast Fourier Transform can transform in sub-linear time.
Binning Fourier coefficients into a small number of buckets.
The recovery process reduces to extracting the location of the non-zero (index) elements in the matrix A and use them to order the sparse K signal, embed zeros in the other locations and perform inverse FFT.
Considerably simpler than the general compressed sensing case.
Propose an innovative way to embed the indices in the extracted largest frequency bins to relax the need for extra coded values.
! Only tested on a single, unspecified audio file, 15 seconds long.

## Other papers

[Distributed Compressive Sensing](https://arxiv.org/abs/0901.3403). 2009.



# Compressed sensing (CS) and its relation to neural networks and deep learning
Notes from presentation given at meetup.
https://www.meetup.com/Under-the-hood-Explaining-what-goes-on-inside-DNN-AI/events/263780245/

By Dr. Anders Hansen.
Head of research group Applied Functional and Harmonic Analysis
at the Cambridge Centre of Analysis at DAMTP.

Secure and Safe AI. Want them to be probably so.

## Safe AI.
Humans make mistakes.
If replacing humans with AI must allow AI to do the same.
But placing restrictions of what kinds of mistakes being made

## Secure.

Secure to adversarities

Would like to use AI to

- Replace humans in problem solving.
/ Replace established algoritms in sciences **focus today**

## compressed Sensing

Typically used for inverse problem.
MRI is the flagship usecase.
In 2017 CS is approved for use in MRI machines by FDA.

- Single pixel camera
- Lessless camera
- Compresive video

### Inverse problems. Related to "integraral transform"

- Electron microscopy
- Xray, tomography
- Radio inferiometry

Sensor gives a Fourier sequence.
Need to decode this integral to get the signal of interest.

MRI imaging takes a long time. Expensive, annoying. Desirable to reduce this.
High resolution traditionally takes multiple hours.
Subsample measurements.

CS uses randomness in the sampling.

How many samples needed in order to recover the signal of interest?
Dependent on sparsity.

## Sparsity
Extra assumption that Compressed Sensing makes.


Wavelets can be used to represent images.
Weighted sum of wavelets.
Can use very few non-zero coefficients in order to represent the image.
Well known for modern compression techniques. 

CS idea. WHy don't we exploit sparsity *when we sample*


Many possible solutions.
Sparsity constraint.
L0 formulation requires Non-convex optimization.
Basis pursuit problem.

Linear system.

There is a theorem for deciding `m`, number of samples.
incoherence parameters U.

Can be very hard to get the best performance.
Sampling strategy is one critical parameter.

- Uniform random.
- Full sampling center + uniform random elsewhere
- Gaussian distribution


FDA has approved Deep Learning for diagnostics.
Under what kind of restrictions?


## AI replacing (standard) algorithms

ReLu popular also for inverse problems.


Instability issue.
AutoMAP network.
Image reconstruction.

CS on the other hand is stable against perturpations.


Want to use neural network for inverse problems.

Image denoising with NN has been very successful.
Learn the noise, and then subtract it from the image.
Need to know the noise model.
Could the same technique be used for inverse problem?

First idea: Use denoising algorithm on the filtered back projection.
Shown to be working in 2016.

## Instability test
How does NN perform with perturbated inputs

"in instabilities of deep learning in image reconstruction"

Obvious mistakes might be OK. Have to redo the experiment
Subtle mistakes are worse. Not detected, can cause (serious) mistakes.
Tumor detected where none, or tumor missed where present.

Can easily synthesize examples which fails. 
Does it happen in practice? We don't know yet!


## A reason for instability

Recovering the null space.
null space. Domain where the function takes a non-zero input and maps it to zero.
When trying to interpolate (as is the nature of the DL training processs),
this will happen. 

"kernel awareness".
We need information about the null space.
Compressed sensing is stable *on some specified domain*.
Robust nullspace property.

'need to figure out what areas we can do things. Which inputs (domain) are valid'.
There is a limitation between how we sample and how well we can do (in a stable fashion).
Especially how sparse our input are, and the size of our reduced sparse space.

For fixed M1, an A. - can find an optimality constant
If we can reach the optimality constant, call this an optimal map.
May not be able to. Have a family of 


Mathematically there is basically a guarantee that DL training will not reach an optimal map.


### Are there stable NNs for inverse problem that performs well 

Lasso problem. Very similar to Basis Pursuit problem.
Lasso is common in image recovery.
ISTA. Solver algorithm for Lasso problem.
If writing out N steps of ISTA, it forms a neural network!

This allows to construct NNs that.

### Instability in classification

Instability guarantees given are for inverse problems.
For classification dont have the same limits/theorems.

Preventing for instability in classification:
State of the Art. Adversarial training.


## Questions
How would one start with compressed sensing to an IoT sampling problem?
Want to sample as seldomly as possible, for energy efficiency. 





