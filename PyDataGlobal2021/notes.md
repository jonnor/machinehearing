
https://pydata.org/global2021/present/

## Meta

Talks are 30-minute sessions including time for Q&A.
A talk proposal is a short description of a talk that is aiming to convince someone to part with 30 minutes of their time, in order to learn about something.
A good proposal should disclose:

    The topic (the WHAT) and WHY it is interesting
    The audience to WHOM the talk is addressed
    The TYPE of talk (lots of maths, hands-on, etc) and possibly the tone (light-hearted, informative etc)
    The TAKEAWAY, a.k.a. what will I learn

There are two parts to a proposal:

Brief Summary
This informs attendees what the talk is about.
Discloses the topic, domain and overall purpose.
This is at most a few lines long, and will be printed in the conference programme.

Description

This is a self-contained statement that summarises the aspects of the talk.
It should be structured and present the objective of the talk, its outline, central thesis and key takeaways.
After reading the description, the audience should have an idea of the overall presentation and know what to expect.
The description should also make clear what background knowledge is expected from the attendees.
Both this and the summary will be included in the talk details online.

Topics

    Data Visualization & Interpretability
    Interpretability 

    Data Science in Production
    Lessons from Industry

    Machine Learning
    Data Engineering or MLOps


# Brief Summary


# Description



# Topics

Similarity/search
Segmentation
Clustering
Anomaly/outlier

unsupervised methods in audio

### Similarity/search

using audio embeddings
simple classifiers on strong embeddings.
one-shot, few-short learning
embedding visualization
dimensinality reduction with PCA/UMAP
Tensorboard Projector. Missing play button :(
https://github.com/tensorflow/tensorboard/issues/38
https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/projector

Fork with Audio file support. Assumes audio files are local
https://github.com/kokimame/tensoba

Distance functions
cosine
normalized euclidean

learning specific similarities.
Siamese on top of audio embeddings
linear layer?

Usecase.

Connections to self-supervised learning
SimSiam etc

query by example. Take input audio

dataset understanding and exploration
(non-automated) Outlier detection

ref blogpost by 

evaluation of similarity metrics. How?

Soundsensing highlights

Demo in Soundsensing platform?

Would need to include an embedding projector,
integrated with our API for playback and getting info
need to store embeddings in database
need to compute embeddings for audio clips

DeviceClassification
    device
    time
    ClassificationResult

AudioClassification
    audio_clip
    ClassificationResult

SpectrogramClassification
    spectrogram
    ClassificationResult


### Segmentation
(semi)automatic labeling of sound events

### Clustering
rather simple on top of an embedding / when similarity is in place?

### Anomaly/outlier detection

Probably punt this to later

