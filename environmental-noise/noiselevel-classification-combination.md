
# Combining soundlevel and classification 

When doing Noise Monitoring, we the severity of noise is typically measured using sound level.
There are international standards that define how this is done,
and noise regulations across the world build on these standards. 

When using Machine Learning for Noise Monitoring it is possible to classify the sound
based on its characteristics, enabling to determine what type of sound - or sometimes the source of the sound is.
This has been extensively researched,
for example under the umbrella of Environmental Sound Classification.

However, methods and practices for combining soundlevel and classification seem to be lacking.
This severely limits the usefulness of machine learning for Noise Monitoring.

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

### Dominant Sound simplification

Most practical environmental noise mixtures can be well approximated by
a single dominant noise source at a time.
This means that it can also be solved using Sound Event Detection.
Related claim: Full source separation, is rarely needed.

Work in progress: [Dominant Sound Classification & Dominant Sound Event Detection](./dominant-sound.md).

### Max noise for noise events

Noise types that are regulated by maximum soundlevel tends to be sound events,
and should be solveable in straightforward manner using Sound Event Detection.



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


# Notes

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


