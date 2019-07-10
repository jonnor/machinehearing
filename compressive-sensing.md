
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


