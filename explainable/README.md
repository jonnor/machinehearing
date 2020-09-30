
## Expainable Audio ML
In many domains and tasks it is highly desirable
that predictive models can be explainable somehow,
and audio is no different.
Aka Interpretable models.

Being able to explain model behavior in general,
or for subsets, or for a particular input instance can be be useful for
checking robustness, debugging models, ensuring compliance et.c

Some techniques that are being explored:

* Local Interpretable Model-agnostic Explanations (LIME)
* Layer-wise relevance propagation (LRP) 
* SHapley Additive exPlanations (SHAP)
* DeepLIFT (Deep Learning Important FeaTures)

Quite often this is done on spectrogram (time-frequency) representation of audio.
The spectrograms themselves might have a degree of intepretability.
But as a 2d representation, it allows to use image-based explanations.

In audio we might want to:

- See strength of feature contributions wrt time
- See contributions in time-frequency (spectrogram) space
- Listen to only the contributing parts of the sound (source-separation)

Different approaches can be to

- create a model which is interpretable/explainable by construction
- generate explainer models on top of a black-box model

## Papers

### audioLIME: Listenable Explanations Using Source Separation
[https://arxiv.org/abs/2008.00582](Paper link).
By Verena Haunschmid, Ethan Manilow, Gerhard Widmer.

Use LIME on spectrograms to decompose into multiple sources.
Then constructs audio for each of these sources, that can be listened to independently.

### Towards explainable Music Emotion Recognition: The route via mid-level features
[Paper link](http://archives.ismir.net/ismir2019/paper/000027.pdf).
By Shreyan Chowdhury, Andreu Vall, Verena Haunschmid, Gerhard Widmer.
From Institute of Computational Perception, Johannes Kepler University Linz, Austria.
Published at ISMIR 2019.

Proposal for a way to make an *explainable* model for music emotion.
Model output: Emotion estimation along 8 dimensions. Valence, Energy, Tension, Anger, Fear, Happy, Sad, Tender.
Defined 7 perceptual features, and asked human evaluators to evaluate music clips in terms of these.
Melodiousness, Articulation, Rhythmic Stability, Rhythmic Complexity, Dissonance, Tonal Stability, Modality/Minorness

Used a deep neural network to estimate these perceptual features.
Then used a linear model on top of these features to obtain output emotions.
Compare to a standard neural network model (not inherently explainable).

Results:
When trained separately, performance dropped a bit.
When trained jointly, perfomance of explainable model matched

Very simple idea. Easy to adopt to other tasks **if mid-level evaluations are available**.

Weakness. No baseline "explainer" model included?
Like using SHAP on the baseline neural network.


### Interpreting and Explaining Deep Neural Networks for Classification of Audio Signals
[Paper link](https://arxiv.org/abs/1807.03418). [.
By Sören Becker, Marcel Ackermann, Sebastian Lapuschkin, Klaus-Robert Müller, Wojciech Samek.
From Fraunhofer and TU Berlin, 

Uses layer-wise relevance propagation (LRP), previously proposed by same authors.

Tested speech classification. Gender classification. 
Evaluated both a spectrogram-based model and a raw-waveform audio model. Very similar performance.

Shows relevance maps on the spectrograms.

#### [audioMNIST](https://github.com/soerenab/AudioMNIST)
30000 audio recordings (ca. 9.5 hours) of spoken digits (0-9) in English.
50 repetitions per digit for each of the 60 different speakers.
Controlled conditions. Quiet offices with a RØDE NT-USB microphone mono channel at 48kHz, 16bit.
Meta information including age (22-61 years), gender (12 female/48 male), origin and accent of all speakers.

### Understanding the Importance of Heart Sound Segmentation for Heart Anomaly Detection
[Paper link](https://arxiv.org/abs/2005.10480).
By Theekshana Dissanayake, Tharindu Fernando, Simon Denman, Sridha Sridharan, Houman Ghaemmaghami, Clinton Fookes.

Heart sound segmentation, as preprocessing step before classifcation.
To detect abnormal heart sounds.

Used SHAP to see whether the model uses the segmentation part of the model or local features the most.
Also to indicate whether the S1 or the S2 heart sounds are getting focused on.
Used SHAP to compute feature contributions at different points in time.

Combined SHAP with Occlusion Maps to find the importance of a feature region.
Plotted on the time axis.

Annoying: Probability scores not shown on normal/abnormal examples.

### PhysioNet heart abnormality dataset
[Challenge](https://physionet.org/content/challenge-2016/1.0.0/)
[Dataset](https://archive.physionet.org/physiobank/database/challenge/2016/)
Heart sound recordings were sourced from several contributors around the world.
Either a clinical or nonclinical environment, from both healthy subjects and pathological patients.
The Challenge training set consists of five databases (A through E) containing a total of 3,126 heart sound recordings,
lasting from 5 seconds to just over 120 seconds. Entire training set is 169 MB.

The heart sound recordings were collected from different locations on the body.
Four locations are aortic area, pulmonic area, tricuspid area and mitral area,
but could be one of nine different locations.

Please note that due to the uncontrolled environment of the recordings,
many recordings are corrupted by various noise sources, such as talking, stethoscope motion, breathing and intestinal sounds. Some recordings were difficult or even impossible to classify as normal or abnormal.


## Tools

## [tf-explain](https://github.com/sicara/tf-explain#available-methods)
Can visualize Activations, Gradient sensitivity on input, Occlusion Sensitivity, GRAD-CAM, etc. Layer-Wise Relevance Propagation is on the roadmap.
Callback-based for Keras. Takes validation data as input.
Integration with Tensorboard, results can be seen live there.

The resolution of Grad-CAM is the spatial resolution of the last convolutional feature map,
this can cause it to miss details. 
For occlusion sensitivity, one must choose the right values for mask size and stride.
 



