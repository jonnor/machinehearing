
12 minutes speaking time.
TED style

1. Main point
TinyML is challenging but worth it
We solve Noise Monitoring using TinyML

Around 12-24 slides.


# TODO

- Tune

# PDF exporting

With reveal.js, can add  ?print-pdf to URL
Note: must go before the #part

Using Chromium print, system dialog
With custom paper format, set to 13.34 × 7.5 inches

Here are some examples from the Urbansound8k dataset.


Ask


# Outline

### Intro
Hi

My name is Jon Nordby.

I am Head of Data Science and Machine Learning
at Soundsensing
We are an IoT sensor company focused on sound and Machine Learning.

Today I will talk to you about
clasifying Environment Sounds on microcontroller

### Environmental Noise

Environmental Sounds are sounds that we have around us in our environment,
especially outdoors.

It can be cars honking, music played from a club, speech from 

When environmental sounds are unwanted we call it environmental noise.


Environmental Noise pollution is a big, and growing problem.
More and more we live in urban environments, with many noise sources around us.

WHO estimates that in Europe alone 13 million suffer from sleep distubance due to noise.
Such noise causes the body to be stressed, and in constant alert mode.
This increases risk of cardiovascuar disease, obesity etc.

And almost 1 million disability adjusted life years are lost due to noise.
This makes noise the environmental pollution that affects the most people in Europe.

## Occupational Noise

Another serious problem is hearing loss.

It is estimated that 40 million people are affected by hearing loss from work.

Affects workers across many industries,
including construction, manufacturing and shipping.


### Noise Monitoring

Soundsensing helps to address these issues by providing better tools
for monitoring noise, understanding the underlying causes, and what is needed to make improvements.

We provide easy-to-use IoT sensors that can continiously measure the noise-level,
as well as classify the dominant noise-source over time.

This is presented in our online dashboard,
and is also available in an API for integrating with other systems.


### Wireless Sensor Network

When providing a Noise Monitoring sensor system there are multiple systems architectures one can consider.

Alternative A
would be to record audio in the sensor and transmit to the cloud.
This is a conceptually very simple solution,
and one could use a standard neural network in the cloud to do audio classification
without much computational constraints on the model.

However this would require a lot of data transfer,
which is costly in terms of energy and data traffic in a cellular 4G system.

It also would be very poor for privacy,
as potentially sensitive audio such as speech
would have to be transported through the network
and could potentially be stored in a server.

Alternative B would be to preprocess the data in the sensor, and classify this in the cloud.
Would have to reducing the data enough to be privacy friendly and save considerable data traffic,
but not so much as to reduce classification performance,
which can be a difficult trade-off.

But the best solution both for Privacy and Data Traffic would be the TinyML solution.
To do all the processing on the sensor, and only transmit data about the classes to server.

However this means the entire model needs to fit the constraints of the sensor device.


## Device constraints

If we consider a typical low-power microcontroller such as an ARM Cortex M4F,
and we dedicate 50% of the resources to the machine learning, that means
- 64 kB RAM



## Small models

In work that we did in 2019, we found that existing models
were at 1-3 orders of magnitude too large to fit on device.

And we showed that one can reach about
10 percentage points from the unconstrainted State-of-the-Art models
when running on such a device.

We have since made several improvements to close the gap further,
but these are not published.

As far as I known this still is the best published performance on Urbansound8k

... how did we do it

TODO: link thesis

### Audio Classification

Here is a typical audio classification pipeline.
The input audio is on the top.
It is chopped into fixed-length windows.
Then each audio window is converted to a spectrogram representation, usually Mel-spectrogram.
Each spectrogram window is fed to a classifier, typically a Convolutional Neural Network.
And if the sounds classes of interest is longer than the window length, one does some aggregation
to combine predictions for multiple windows into prediction for a single clip.

### Reduce input dimensionality

The first optimizalization one can do is in preprocessing.
The key is to use a small input to the model as possible.
So if one reduces the sample rate, the range and resolution of frequencies bands,
the time duration and resolution of the window, one can make large gains.

Also makes it easier to learn with for small datasets!

TODO: note easier to learn

### 

The windows 
This gives the model a couple of different view of the same sound, which increases performance.
Typical SOTA models use maximum overlap, over repeating over 20x times on same audio section.

The performance benefit can however be quite minor. Try 1x, 2x, 4x first

Not that this increases detection latency and resolution.
Might not be limiting in some cases, like keyword spotting or event detection.


## Use a small model

For many audio tasks one can get really far with a small model.
For example 2-4 convolutional layers followed by 2 dense layers
does well on a range of tasks.

One can start with a large model and then prune it,
but our experience start with small model is easier and works well.

TODO: reference Salamon Bello

## Depthwise-separable Convolution

The convolutions in the network take up most of the CPU budget,
especially the early ones with large.

A Conv2d with multiple channels actually does convolution
over 3 dimensions. Width, height and channel.

This can be separated into two operations,
first convolution over spatial dimensions,
then convolve over the channel dimensions. 

5-10x speedups with very little performance impact.


## Downscaling

In a Convolutional Neural Network one downsamples the data as one gets deeper in layers,
to operate on progressively higher level features.
This is usually done by doing max pooling after each convolution,
which means to pick the highest value within the input.
However this is quite wasteful, as is disregards a lot of data computed by previous layer.

An alternative is to drop the max pooling, and instead use a stride higher than one in the convolution.
This reduces the amount of times the convolution is run.

Can sometimes perform better than max-pooling, since the downsampling is included in the learned function! 

TODO: merge into one slide

## Quantization

Quantizing down to 8 bit integers can be done almost without loss in performance.
4x improvement in FLASH and RAM

On Cortex M4F one can get around 4x improvement in CPU performance as well

## Latest development

This area is very actively researched.
Many of these you will find dedicated talks about here at TinyML Summit.


## Noise Monitoring

Automatically creating a logbook of noisy training activities.

One of our customers operate a training facility for police special forces,
where they fire guns and conduct explosives training.
They use our system to have documentation that they follow the regulations,
and to verify any noise complains that come in.

We are now expanding this solution to other applications,
such as Construction, Industry and Transportation.

If you are working in these areas and interested in testing it out,
let us know.


## Condition Monitoring

We have also used the same techniques
to develop an Anomaly Detection system using sound,
which has been tested out on pumps.

This means that the condition of technical equipment
can be continiously monitored,
freeing up time for the janitors and providing better detection of issues.

We are currently looking to test this in larger
scale and on more types of machinery.



## Conclusions

1. Can classify Environmental Sounds directly on sensor
2. Made possible using efficient CNN techniques
3. Integrated into Soundsensing IoT sensors
4. Used for Noise Monitoring and Condition Monitoring

## Questions

Thank you!

Are there any questions? 


# Misc

Outputs
Audio Classification as first piece of bigger systems
Bringing to market
Deployments
Challenges

