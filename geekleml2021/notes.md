

# Style

Show the output/demo first.
Then walk through how to make it
Complete code in a Github, ideally


# Outline


- Introduction
- About Soundsensing
- Audio Event Detection. Task definition
- Application example. Tracking Beer Fermentation
- Data gathering. Hunting Youtube. youtube-dl
- Exploratory Data Analysis. Spectrograms. Audacity, librosa
- Labeling data. Audacity
- Audio ML pipeline. System diagram
- Pre-processing? Analysis windows. (spectrograms, already covered)
- Training & evaluation. CNN, RNN. Keras
- Post-processing?
- Results
- Streaming inference. Running in real-time 


# Planning

## What people need to understand

- Audio events
What is an audio event.
Onset/offset
Definition of AED task. Input/outputs

- Typical audio ML pipeline
Analysis windows
Features over time
Spectrogram

- Post-processing.
Counting. Threshold above X
Event-rate

- How to evaluate performance
Window-wise vs event-wise
sed_eval: https://tut-arg.github.io/sed_eval/
tolerances

## Assumptions
What we will (mostly) assume that people know

- Basic digital audio
- Basic Machine Learning. Supervised classification
- Typical Neural Networks. CNN/RNN ?


## Out of scope
What people do not need to understand

- ? Weakly labeled data 
- Making efficient networks

Tips & tricks

- Error analysis
Manually examining mistakes that your algorithm is making

- Labeling strategies
Semi-supervised
Alignment tools

- Pretrained model
OpenL3 / YAMNET / PANN

Challenges

- Out-of-distribution data
Device. Environment. 
Data augmentation


# Misc

### Error analysis

False Negatives / False Positives.
Rank by probability. Inspect

Can be generalized to multi-class.
For example using pairwise-confusions. Expected-Actual


### Bias/variance diagnostics

High Variance problem: Training error much lower than test error
High Bias problem: Both training and test error high
Different strategies to fix the two cases

Diagnostic
Convergence failure.
Optimizing wrong loss function. 

Lecture 11.2 — Machine Learning System Design | Error Analysis — [ Machine Learning | Andrew Ng ]
https://www.youtube.com/watch?v=k1JGvqr56Yk

DeepLearningAI: Carrying Out Error Analysis (C3W2L01)
https://www.youtube.com/watch?v=JoAxZsdw_3w

Debugging ML Models and Error Analysis | Stanford CS229 | Andrew Ng
https://www.youtube.com/watch?v=ORrStCArmP4

Machine Learning System Design | Error Analysis
https://www.coursera.org/lecture/machine-learning/error-analysis-x62iE

Microsoft Error Analysis toolkit.
https://erroranalysis.ai/


# Resources

https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection
Using PANNsCNN14Att
Shows training with weak supervision
Part of Cornell Birdcall Identification challenge
https://www.kaggle.com/c/birdsong-recognition

Was used as inspiration for the winning entry
https://www.kaggle.com/c/birdsong-recognition/discussion/183208
DenseNet with focal/BCELoss
SpecAugment, Mixup
Ensemble of 4 models

Attention based pooling
https://www.kaggle.com/hidehisaarai1213/introduction-to-sound-event-detection/comments#962915
tahn instead of softmax

Attention-based Deep Multiple Instance Learning
https://arxiv.org/abs/1802.04712
Maximilian Ilse
ICML 2018



