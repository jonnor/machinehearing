
Notes on some of the submission for DCASE 2022 challenge.

# Task 2

Official score Ω is given by the harmonic mean of the AUC and pAUC scores over all the machine types, sections, and domains.

## ROBUST ANOMALY SOUND DETECTION FRAMEWORK FOR MACHINE CONDITION MONITORING

Ranked 1.

Used CNN based on MobileFaceNet.
Tried Inception and Xception, no improvement.

Tried different anomaly scores

- Model output probability (DCASE Baseline)
- Mahalanobis distance
- Cosine similarity

Found that the features of some machine types are mainly concentrated in high frequencies.
Pass the audio through a high-pass filter before passing through the Mel filter.

Self-supervised learning using machine as the label.
Found that this easily overfits after few epochs.
Chose models at different epochs using pAUC.
Save the average embedding and covariance matrix of each machine ID to
calculate the Mahalanobis distance and cosine distance.

Pre-trained on all machines. Then fine-tune on each machine.

## AITHU SYSTEM FOR UNSUPERVISED ANOMALOUS DETECTION OF MACHINE WORKING STATUS VIA SOUNDING
Liu et al.

Six subsystems, including three self-supervised classification methods,
two probabilistic methods and one generative adversarial network (GAN) based method.
Final submission are four ensemble systems, which are different combinations of the six subsystems.
The best official score of the ensemble systems can achieve 86.81% on the development dataset,
whereas the corresponding Autoencoder-based baseline and the MobileNetV2-based baseline are with scores of 52.61% and 56.01%, respectively.

Probabalistic models called WSP-NFCDEE and IMDN (Interpolation Mixture Density Network)
WSP-NFCDEE is built on  (NFCDEE)
WSP-NFCDEE is that we add a Weighted Statistic Pooling before the normalizing flows.

IMDN, we adopt three network structures mainly based on CNN and GRU,
and a special density estimation loss function that combines the IDNN structure and Gaussian Mixture Model.
We employ three networks name IGNN, LRCGNN, and a simplified DeepFilterNet.
LRCGNN additionally add a Conv1d layer after the first fully connected layer of IGNN.

AEGAN-AD. Based on a DCGAN-like autoencoder,
with the discriminator being our encoder and the generator being our decoder.


## COMPARATIVE EXPERIMENTS ON SPECTROGRAM REPRESENTATION FOR ANOMALOUS SOUND DETECTION
Kazuki Morita

Per-Channel Energy Normalization (PCEN)
Harmonic-Percussive Source Separation (HPSS)

Using MobileFaceNet
Additive Angular Margin Loss as a loss function.
128d output dimensionality.
Used LOF, GMM, kNN to compute anomaly score.
PCEN/HPSS did not really make any considerable improvements.


## THE DCASE2022 CHALLENGE TASK 2 SYSTEM: ANOMALOUS SOUND DETECTION WITH SELF-SUPERVISED ATTRIBUTE CLASSIFICATION AND GMM-BASED CLUSTERING
Xiao et al.

Integrates two domain generalization methods:
a self-supervised attribute classification and a GMM-based clustering for unsupervised ASD.
The results show that our ensemble system can achieve 88.5% in average AUC under the source domain,
78.5% in average AUC under the target domain, and 68.8% in average pAUC.

Model 1. STgram-MFN
STgram as the input feature and
MobileFaceNet (MFN) as the self-supervised classifier.

Model 2. gwrp-GMM
GMM-based clustering using global weighted rank pooling (GWRP) on log-Mel spectrogram.
Using a per-machine regularization value r.
85.4% average score. Really good for such a simple model.
Also tried using SMOTE with GMM to. Improved performance by 2% points in the target domain.

! not clear how the GMM and GWRP are done exactly

Seed, expand and constrain: Three principles for weakly-supervised image segmentation.
Kolesnikov, Lampert, 2016
Introduced Global Weighted Rank Pooling (GWRP) for images.

Can be seen as a generalization of GMP (global max-pooling) and GAP (global mean pooling)
GWRP computes a weighted average score for each class,
where weights are higher for more promising locations.
Uses a decay parameter, which at the extremes gives GMP and GAP.

## TWO-STAGE ANOMALOUS SOUND DETECTION SYSTEMS USING DOMAIN GENERALIZATION AND SPECIALIZATION TECHNIQUES

81.15 % for omega on the development set.

Two-stage ASD systems consisting of an
outlier exposure-based feature extractor and
an inlier modeling-based anomalous detector in serial.
Final systems are obtained by ensembling several systems with several hyperparameters for each approach.


# Task 1. Low-Complexity Acoustic Scene Classification
https://dcase.community/challenge2022/task-low-complexity-acoustic-scene-classification-results

## CP-JKU SUBMISSION TO DCASE22: DISTILLING KNOWLEDGE FOR LOW-COMPLEXITY CONVOLUTIONAL NEURAL NETWORKS FROM A PATCHOUT AUDIO TRANSFORME
Schmid et al
Team ranked 1. 59.6 % accuracy

Teacher, Patchout faSt Spectrogram Transformer (PaSST)
Student, Receptive Field Regularized Convolutional Neural Network (RFR-CNN).


## HYU SUBMISSION FOR THE DCASE 2022: FINE-TUNING METHOD USING DEVICE-AWARE DATA-RANDOM-DROP FOR DEVICE-IMBALANCED ACOUSTIC SCENE CLASSIFICATION
Lee et al
Team ranked 2. 

4 layer convolutional neural network
Used Multi-scale frequency channel attention (MFA) and BC-Res2Net
Used Feature pyramid module (FPM) as the aggregation after convolutional layers
Knowledge Distillation increased accuracy by 9 percentage points.


## RECEPTIVE FIELD REGULARIZED CNNS WITH TRADITIONAL AUDIO AUGMENTATIONS
Morocutti, Shalaby

A 4 layer CNN, with 6 conv blocks total.
Knowledge Distillation from a large teacher CNN.

Team ranked nr 3. 54.5 % accuracy
Only used 1/3 of possible budget (21,930 parameters / 9.775 MMACs)


