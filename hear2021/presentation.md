
Key points

# Cover
Hi everyone.

My name is Jon Nordby.
Presenting on behalf of team MARL + Soundsensing.
The team at MARL - Music and Audio Research Laboratory at New York University
has consisted of 

Aurora Cramer
Ho-Hsiang Wu
and Bea Steers.

and myself from Soundsensing

# Motivation. 

Our goal was not to develop a new architecture or get SOTA performance,
but to see how existing, well-established, open models do.

At Soundsensing we often use models like these as baselines
on new custom datasets.
To judge how the feasibility of a task,
before starting to build custom, optimized models.

So as a team we are interested in seeing how they do on a wide range of tasks.

Made two submissions based on

OpenL3, developed by MARL
YAMNet, developed by Google

Both models use 1 second windows and have been trained on AudioSet.
For HEAR, both submissions used the same overall approach.
For timeframe embeddings, models are ran with 50 ms hop (95% overlap).
And for scene embeddings, models are ran with 0.5 s hop (50% overlap).


We were also in correspondence with the authors of PANNs,
who we are happy to see have also submitted for the challenge. 

# YAMNet 1/2

I will talk briefly about each model,
highlighting some aspects that may be interest. 
Since these are existing models,
we will not go into details,
as these are generally well described in the corresponding papers
and code repositories,
which are linked below.

...... training

Weakly supervised learning
Using the multiple instance learning
A bag of 1 second long windows from the same 10 second audio clip,
are compared with ground truth from tags on the 10 second clip

# YAMNet 2/2

The input representation for YAMNet is a log mel spectrogram
With 64 mel filters between 125 to 7500 Hz
This does not cover the entire hearable range and is low compared to many other models

The model is designed for computational efficiency
Using Depthwise Seperable convolutions everywhere except for last layer

Additionally the first layer uses 2x downsampling using striding
So this is relatively low input resolution

One special feature is that there are 5 conv layers after eachother.
which seems somewhat redundant?

# OpenL3 1/2

OpenL3 was also trained on AudioSet data
But in a self-supervised way

And the model is asked whether the audio and video inputs come
from the same clip at the same time,
or not

OpenL3 builds upon the L3 model from the Look, Listen and Learn
using mel spectrograms instead of linear STFT

In our submission only the audio subnetwork is used

Several data subsets were tested for training
We used the model trained on the music subset,
as the OpenL3 paper showed that this worked well both on music and environmental tasks (ESC-50) 

# OpenL3 2/2

Input representation
Covers the entire hearable frequency range

Also has a quite high temporal resolution, with 5 ms hop and 10 ms FFT window

The model is a quite standard VGG style Convolutional Neural Network, with 2 conv layers and Max
One unconventional part is the large 


## Conclusions

Happy to discuss in the Q&A
We hope to investigate this and shed some light on this in a paper in the upcoming PMLR issue 



