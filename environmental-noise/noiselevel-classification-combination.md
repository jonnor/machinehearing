



## Notes

Noise source analysis
Combining audio classification with soundlevel
to explain the contributions in

Max-levels versus average levels

Max levels, noise events.
Want to count how many occur, during night etc
T-1442
Want to know the source for each event


Loud event detection. Based on thresholds LAF
Classify event.


Time-series segmentation

Consider


Source separation.
Spectrogram based. 

Binary masks. Assign each TF bin to one source  
Soft/Ratio Masks. Estimate
https://source-separation.github.io/tutorial/basics/tf_and_masking.html

Challenge: uncertainty


# Background

## Typical scenarios for automated noise analysis
Representative use-cases. Especially receiver positions. And also noise sources.
Something where acousticians, muncipality or affected residents are interested in the results

Challenges: Multiple source co-occurring. Especially when overlapping in time.

Cases at different ends of spectrums

- Sparse. Receiver in quiet residential areas. Explosions as main source.
- Dense. Receiver in apartment in busy urban area. Sources: Social noise, construction noise, traffic noise
- Dense. Receiver in busy office. Sources: Office noise, construction noise, traffic noise

Intuitions

- The louder the sound, the more likely it is to be dominant
- The more sparse the events are, the more likely loud sounds are to be dominant - low co-occurence of noises
- The lower the background noise, the easier for event noises to be (relatively) loud

Models are relevant where the noise sources are far from constant.
High degree of temporal variability.
If the noise is near-continious, less suited?

## Interesting datasets.
- PNB.
- Traffic.
- Startuplab office.

# Research agenda

- Task formulation.
The tasks of combining noise levels and audio classification does not yet seem to be defined or established
in relevant communities? Acoustics, Machine Learning
- Real-world evaluations of data wrt different task formulations / approaches
- Results of using the methods in practice, performance

Could have publications at multiple stages of this.
Can split out investigations into domains/usecases.
Want to demonstrate the soundness of using proposed strategy.

## Hypothesis
1. Events regulated by maximum soundlevel
can be solved in straightforward manner using Sound Event Detection

2. Most practical environmental noise mixtures can be well approximated by
a single dominant noise source at a time
(ie source separation is rarely needed)

# Dominant Noise Source Classification

Noise Classification using the single-dominant-source method/assumption

## Task formulation

### Input

Stream of audio. Consisting of multiple noise sources.
Noise sources are typically time-varying.

### Output

Discrete class labels in `{class0,class1....classN}`

Might also allow for added pseudo-classes {unknown,mixture}
`unknown` means the model cannot reliably detect the class.
can be result of. insufficient classifier confidence, out-of-distribution outlier detector 

`mixture` means that the dominant-source assumption is violated,
there are multiple sources that meaningfully contribute to the overall noise level.
Result of dominant-source classification


## How often is the single-dominant-source-at-a-time a reasonable assumption?
Or v.v., how often is the single-dominant-source-at-a-time assumption broken?
If B is -5dB of A, then B contribution to sum is 1.2 dB
If B is -10dB of A, then B contribution to sum is 0.4 dB
How often does two (or more) noise sources appear concurrently, where B is within 10 dB of A
Time resolution ~1 second

If one had captured a mixture of these things, how would one analyse the data to answer this question?

Could maybe select some time-periods
Say 10-30 seconds long
that are representative of whole dataset
analyze these manually
mark periods of single dominant, multiple contributions

statistical analysis
each source modelled as a soundlevel generating process
characterized by
a. sound level distribution
LAFeq for each time-step
b. emission probabilities

Time-steps in order of 0.1 to 1 seconds.
Maybe 0.125 to match LAF?
Assumes that one can classify to precicely, which might be a stretch.
But that can be considered separate problem

There is considerable temporal dependency between time-frames (for each source)
More like each activation of a source has a short (soundlevel) sequence associated with it

?? Can we ignore this in the statistical analysis?
How to represent in simple but effective way?

Might be possible to have source activity as a binary
Maybe the activation patterns of sources can be Poisson

could we formulate a generative model,
and fit it to real-world mixtures?
could test it on synthetic mixtures first,
to check if model is able to fit properly

could create a models for estimating single-dominant source or not
synthesize mixtures to form dataset
different dB ratios of A,B (might also need to have background noises C,D,E)
train model to predict the ratio
use model to analyze real-world data

Is worthy of a paper of its own?
From product point-of-view. Want to 

## 

two noise sources
active 5 seconds at a time
30 seconds between each activiation
independen from eachother

what is probability of happening at same time?
ie overlapping by more than 1 second



