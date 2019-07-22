
# EuroPython 2019

[Presentation video (YouTube)](https://www.youtube.com/watch?v=uCGROOUO_wY) |
[Slides](https://jonnor.github.io/machinehearing/europython2019/slides.html)

# Transcript

Welcome to the session Jon Nordby is a maker and full-stack IOT developer.
He successfully defended his master's thesis in data science two weeks ago and he's now embarked on an IOT startup called sound sensing.
Today he'll talk to us about a topic related to his thesis: Audio classification with machine learning.

Hi thank you. So, audio classification is not such a popular topic as for instance image classification or a natural language processing so I'm happy to see that there's still people in the room and interested in this topic.


So first a little about me. I'm an Internet of Things specialist have background in electronics from nine years ago worked a lot as a software engineer, because electronics is mostly software these days or a lot of software.
And then I went to do a master's in data science because IoT to me is the combination of electronics (sensors especially), software: you need to process the data, and data itself in some transform sensor data into information that is useful. Now I'm consulting on IoT and machine learning and I'm also CTO of Soundsensing.
We deliver sensor units for noise monitoring.

In this talk my goal (we'll see if we get there) is that you as a machine learning practitioner without necessarily prior experience in sound processing can solve a basic idea classification problem.
We'll have an introduction about digital sound very briefly. And then we'll go through a basic audio classification pipeline. And then some tips and tricks for how to kind of go little bit beyond that basic.
And then I'll give some pointers to more information.
The slides and a lot of my notes and machine in general little bit broader than audio classification is on this github.

So applications. There are some very well recognized subfields of audio, speech recognition is one of them.
And for instance there you have as a classification task you have keyword spotting, so hey Siri or hey hey Google.
As a task in music analysis you also have many tasks, genre classification for instance can be seen answer a simple audio classification task.
We're gonna keep it mostly on the general levels we're not gonna use like a lot of speech or music specific domain knowledge. We still have examples in across a wide range of things, I mean anything you can do with hearing as a human you we can get close to or many [tasks] at least and classification tasks with with machines today

In ecoacoustics you might wanna analyze bird migrations using sensor data to see their patterns, you might want to detect poachers in protected areas to make sure that no one actually is going around shooting were there should be no gunshots. 
It's using quality control in manufacturing, especially because you can you don't have to go into the equipment or the product under test, you can listen it to it from the outside.
For instance used for testing your electrical car seats they say that all motors run.
In security it's used to help monitor large grounds of CCTVs and by also analyzing audio.
And in medical for instance you could detect heart murmurs which is a could be indicative of a heart condition.
So these are some motivating examples.
And so in digital sound I'll just go very briefly through this.
First thing to that is important is that sound is almost always, or basically always, a mixture.
Because sound I mean it it will move around the corner unlike image for instance
and you will always have sound coming for 12 C also transport in in the ground and they reflected by a wall.
And all these things makes it so you always have multiple sound sources or the source of interest
and then always other sound sources.

In audio acquisition okay we have for a sound is a it's air pressure we need to go have a microphone converted to electrical voltage, an ADC and then we have a digital waveform which is what we will deal with.
Then it's quantized in time for instance with the sampling rate and amplitude.
And we usually deal with mono primarily with one now when we do order classification still there is some methods around stereo but not widely adopted and also more channels.
We typically use uncompressed formats, it's just the safest.
Although you in real life situation you might also have compressed data which can have artifacts and so on that might influence your model.
So after we have a waveform we can convert it in a spectrogram and this in practice is very useful representation, both for as a human for understanding (what is this sound) and for the machines.
To use this one example, is a frog croaking like / r / r / r. very periodically you see a little gap.
And then it's hard to see but in top in a higher level there is some cicadas that are going as well seen and this allows us to both see the few frequency representation and the patterns across time and together you can often this this allows you to separate as different sound sources from your mixture.


So we'll go through a practical example just to keep it kind of hands-on.
Environmental Sound Classification so giving out a signal of my mental sounds so these are everyday sounds that are around in the environment for instance it can be out outdoors: Cars, children and so on.
It's very widely researched we have several open data sets that are yeah quite good.
AudioSet is is several I think tens of thousands or even hundreds of thousands of samples.
And in 2017 we've reached roughly human level performance (only one of these data sets has an estimate for what is human level performance) but we seem to have surpassed enough.

And one nice data set is the Urbansound8k which has ten classes of 8k samples.
They're roughly four seconds long and nine hours total and state of the art here is around 80 percents of (79 to 82) accuracy.
Here we have some spectrograms and these are the easy samples, this data set has many challenging samples where the sound of interest is very far away and hard to detect, and these ones are easy.
So you see the siren goes like very up and down and jackhammers and drilling have very periodic patterns.
So how can we detect this using a machine learning algorithm in order to output these classes?
I will go through a basic audio pipeline, and skipping around like 30 to 100 years of history of audio processing kind of going straight to what is now the typical way of doing things.
And it looks something like this.
So first in the input we have our we have our audio stream.
It's important to realize that of course audio has time related to it so it's more like a video than to an image.
And in practical case scenario might you do real-time classification so this might be a infinite stream that just goes on and on.
So it's important for that reason and for also the Machine Learning to divide the stream into small or relatively small analysis windows that you will actually process.
However you often have the mismatch between how often you have labels for your data versus how often you actually want a prediction ,it's known as weak labeling.
I won't go much into it but so in the urban sound it's for sound 4 seconds sound snippet so that's what kind of are we're given and this curated data set.
However it's usually beneficial to use smaller analysis windows to reduce the dimensionality of the machine learning algorithm.
So the process goes that we will divide the audio into these segments, it will often use overlap.
And then we'll convert it into a spectrogram and we'll use a particular type of spectrogram called a Mel-spectrogram which been shown to work well.
And then we'll pass that frame or features from the spectrogram into our classifier and it will output the classification for that small time window.
And then because we have labels per 4 seconds we'll need to do an aggregation in order to come up with the final prediction for these four seconds, not just for this one little window.
Yeah we'll go through these steps now.
So first analysis we notice I mention we often use overlap so this is somewhat specified in two different ways: one is an overlap percentage, here we have 50% overlap, so that means that we're essentially classifying parts of the or we're classifying every piece of the other stream twice.
So we could have even more overlap people maybe a 90 percent overlap then we're classifying it 10 times and that gives the algorithm a kind of multiple viewpoints on this audio stream, and makes it easier to catch the sounds of interest.
Because the model might in training might have been kind of prefer a certain sound to appear in a certain position inside this analysis window, so overlap is a good way of of working with that.
so a mission we used a specific type of spectrogram. So the spectrogram is usually processed with those called Mel-scale filters these are inspired by the human hearing. Our ability to differentiate sounds of different frequencies reduce is reduced as frequencies to get higher. So low sounds were able to detect small frequency of variations however high pitched sounds we need large frequency variations towards.
And by using this kind of filters on the spectrogram we obtain the representation is some more similar to our ears but more importantly it's a smaller representation for a machine learning model, and also you'll be able to merge kind of related data in in two consecutive bins for instance.
So when you've done that it looks something like this.
On the top is a normal spectrogram and you see kind of a lot of small details.
The bottom one we've we started the Mel filters at 1000 Hertz.
This is bird audios which is quite high pitched, a lot of chirps up and down. And in the third one we've with normalized the earth.
We usually use log-scale compression because sound has a very large dynamic range so sounds that are faint versus sounds that are very loud for the human ear is a factor of 1000 or a factor of 10,000 in energy difference.
So when you've normalized log-scaled applied the spectrum and normalized you look at something like the image below.

So in Python code this picture shows the processing. I'm not gonna go through all this in detail, we have an excellent library called librosa which is great for just loading and loading the data and doing basic feature pre-processing.
Also some of the deep learning frameworks have their own Mel-spectrogram implementations that you may also.
But this is a general thing in streaming so when people analyze audio they often apply normalization learned from the mean for instance across their whole samples for four seconds in this case, or from their whole data set.
That can be hard to to apply when you have a continuous audio stream which has for instance changing volume and so on so so what we usually do is to normalized per frame so the hope is that you have enough information in our roughly one second of the data in order to do a this normalization.
And doing normalization like this has some interesting consequences when when when there is no input because what happens is if you have no input to your system.
Probably you're gonna blow up all the noise. So your sometimes need to exclude very low energy signals from being classified. Just like little practical tip. 

So conclusion neural networks they're hot. Who here has basic familiarity, at least gone through a tutorial or read a blog post about image classification and CNN's? Yeah that's quite a few. 
So CNN's are the best in class for image classifications. Spectrograms are image-like audio representation, they have some differences, so a question is (or maybe it was): will CNN's work well on spectrograms?
Because that would be interesting and the answer is yes.
This been researched quite quite a lot and this is great because there is a lot of tools, knowledge, experience and pre-trained models for image classification.
So being able to reuse those in the audio domain, which is not such a big field, is a major major win.
So you'll see a lot of the research lately is, it can be a little bit boring in audio classification research, because a lot of it is like taking one year ago image classifying tools and applying them, and seeing whether it works.
It is however a little bit surprising that this actually works because the spectrogram has a frequency on the y-axis typically it's shown that way and time on the other axis. So a movement or a scaling in this space doesn't mean the same as in an image. You know an image if I have my face inside an image doesn't matter where my face appears.
If you have a spectrogram and you have certain sound it's like a chirp up and down, if you move that up in frequency or down ,at least if you move it a lot, it's probably not the same sound anymore.
It might go from a human talking to a bird, the shape is might be similar but the position matters.
So it's a little bit surprising that this works, but it does seem to do really well in practice.

So this is one model that's does well on Urbansound.
And one thing you'll note compared to a lot of image models is that it's quite simple, I mean relatively few layers this is smaller than or the same kinda size as LeNet5.
And there are three convolutional blocks followed by Mike and with max pooling between the two first bucks.
And that's, you know, the standard kind of architecture.
This one using five by five instead of two or three kernels, doesn't make much of a difference you could stack another layer and do the same thing. And we flatten and then we use a fully connected.
From 2016 and still is one is like close to state-of-the-art on this dataset Urbansound.
Okay so if you are training CNN from scratch on audio data, start with a simple model. I mean there's no usually no reason to start with say VGG16 with 16 layers and millions of parameters, or even MobileNet or something like that. You can usually go quite far with with this kind of simple architecture, a couple of convolutional layers

So in case for example this could look something like this.
Where we have our individual kind of blocks convolution max pooling really non-linearity same for the second one and our full classification at the end the full connected layers. so yes and then like so this is our classifier will pass the classification through this and it will give us a prediction for which class it was certain classes in the urban zone. And then for each window and then we need to aggregate these individual windows and there are multiple ways of doing this you could do simplest kind of thing to think about is to do majority voting so if we have ten windows over for second spectrum we could do the prediction so eh and then just say okay the majority class wins that works rather well it's not differentiable and so it can either do this processing so on and you're kind of you're you're making very rough predictions on each on a step so mean mean pooling or global average pooling across those analysis windows usually does a little bit better and it's nice with deep learning frameworks is that you can also have this as a layer so for instance in Keras you have the time distributed layer

which is there's sadly extremely a few examples of our lines it took me a like it's not that hard to use but to mail it to to figure out how they do it and so we apply a base model which is in this case the input to this function we pass it to the time distributed layer and which essentially it will it will use a single instance of your model so we'll share the weights for all these steps in the or all the analysis windows and and then if so we'll just run in multiple times when you do the prediction step and then it will global average pooling over these predictions so here we're averaging predictions you can also you can also do more advanced things where you would for instance average your feature representation and then do a more advanced classifier on top of this but this called probabilistic voting quite often and all literature when you do this mean mean pooling yes that allows us so this will give us a new model which is what will tend take not single in analysis windows which will take a set of analysis windows typically an error corresponding to our four seconds with for example 10 windows so if you do this and a couple more tricks from my thesis you can have a system working like this so this has in addition to building model and so on which I've gone through we're also deploying to a small microcontroller using the when they're provided tools that converts to Karis model and so on so that's kind of roughly standard things anyone I go into it here so little demo video if we have sound so here are 10 classes children playing think it's basically what we do also here is we threshold the prediction so if no prediction is good we'll consider it unknown and this is also important in practice because sometimes you have out of class data is drilling or this actually the the sample I found said jackhammer jackhammer is also a path and really they are to my ear hard to distinguish sometimes and the model can also struggle with there's a dog barking and so in this case all the classification happens on the small sensor unit which is what I focus on in life in my thesis [Music] it actually it didn't get the first part of this iron this dude only this undulating sound later so this and but actually these samples are from are not from the urban sound dataset which I've trained out so they're out of the main samples which is generally a much more challenging yeah challenging task yes that's it for demo.

If you want to know more about doing sound classifications on this sensory units very small you can get my full thesis. Both the report and the code is here. It's also linked from the Machine hearing repository.
yes so I won't go much details there
Some tips and tricks. So we've covered the basic audio processing pipeline, the modern one, and that will give you results and generally quite good results with the modern CNN architecture.
And there are some tips and tricks especially in practice where when you are having a new problem.
You're not researching an existing data set, your data sets are usually much smaller and it's quite costly and tedious to annotate all the data, and so on so there are some tricks for that.
First one is data augmentation. This is well known from from other deep learning applications, especially image processing. And the augmentation can be done on audio can be done either in the time domain orin the spectrogram domain, and in practice it both seem to work work fine.
So here are some examples of common common augmentations.
The most common and possibly most important is to do time shifting.
So remember that I said that in the when you classify an analysis window we may one second you know the sounds of interest there or and what the individual convolution kernel sees what might be very short if you have bird chirps they're like and those are you know maybe 100 milliseconds max or maybe in 10 milliseconds so they they occupy very little space in that image that the classifier sees.
But it's important that it's able to classify it no matter, or it's desirable, that it's able to classify it no matter where inside this analysis window it appears.
So time shifting simply means that you shift your samples in time forward and backward (left and right) and that gives them you know that I would have seen that okay bird chirps can appear you know many places in time at any place in time and it doesn't make a difference to the classification. So this is by far the most important one and you can usually go for quite far with just time shifting.
If you do want precise location of your event, so you want to have a classifier that can tell *when* did chirps appear, not just in the 100 millisecond range instead of just that there was birds in this 4-10 seconds audio then you might not want to do time shifting.
Because you might want to have kind of that the sound always occurs in the middle window but then you need to your labeling needs to to respect that.

Time stretching. So many sounds you know if I speak slowly or I speak very fast its it's the same, you know it's the same meaning, it's the same certainly the same class it's both speech. So time stretching is also very very efficient to capture such variations and
also pitch shifting so if if I'm speaking with low voice or a high-pitched voice you know, it's still the same kind of information. And the same carries in in you know for general sounds, at least a little bit, so a little bit of time shift you a pitch shift you can accept, but a lot of big shift might kind of bring you into new clas. For instance the difference between human speech and and bird chirps it might that might be a big pitch shift so so you might want to limit how much your pitch shift. Typical augmentation settings here is like maybe 10 to 20 percent on time shift and pitch.
You can also add noise this is also quite efficient especially if you if you do know that you have variable amount of noise. Random noise works okay you can also sample there's like lot of repositories of basically noise well you'll mix in noise with your signal and classify that.

Mix-up is an interesting data augmentation strategy that makes these two samples like by a linear combination of the two and actually adjusts the labels accordingly and that has been shown to work really well also in combination with other augmentation techniques on the audio so um yes we can basically apply CNN's and with the standard kind of image type architecture this means that we can do transfer learning from image data.
So of course image data has, I mean is, significantly different from from spectrograms I mentioned the frequency axis and so on however the some of the base operations that are needed you need to detect edges you need to detect diagonals you need to detect patterns of edges and diagonals you need to detect kind of a blob of area those are common kind of functionality needed by both.
So if you do want to use a bigger model, definitely try to use the pre-trained model and finds unit and for instance most people and frameworks including Keras have retail models written on ImageNet.
The thing is that most of these models they apply take RGB color images as data. And it can work to just like use one of those channels and zero fill the other ones. But you can also use just copy the data and cross the three. There's also some paper showing that you can do multi-scale, so for instance one has a spectrogram with very fine time resolution and one has a one with a very coarse time resolution, and they put them in different channels and this can be beneficial. But because image data and some that are quite different you usually do need to fine-tune so it's usually not enough to just apply a pre-trained model and then just tune the classifier at the end.
You do need to do a couple of layers at the end and typically also the first layer at least sometimes you fine-tune the whole thing but it is generally very beneficial so definitely if you have a smaller data set and you need that high performance and you can't get it with a small model go with the pretrained model for instance MobileNet or something like that.

Audio embeddings is another is another strategy, inspired by text embeddings where you create a for instance 128 dimensional vector from from your text data, you can do the same with sound.
So with Look Listen Learn L3 you can convert one second audio spectrogram into 512 dimensional vector which has been trained on millions of YouTube videos, so it has seen a very large amount of different sounds and that uses a CNN under the hood. And basically gives you that that very compressed vector classification. I didn't finish any code sample here but there is a very nice latest work is OpenL3. Look Listen Learn More is the paper, and they have a Python package which makes it super simple. Just import, it is one function to pre-process and then you can classify audio basically just with a linear classifier from scikit-learn.
So if you don't have any deep learning experience and you want it you want to try a order classification problem definitely go this route first. Because this will basically handle the audio part for you and you'll just you can apply a simple simple classifier after that.
One little tip I mean you might want to do your own dataset right.
Audacity is a nice editor for for audio and it has a nice support for annotating by adding a label tracking.
There's like keyboard shortcuts for for all the functions that you need, so it's quite quick to use.
So here I'm annotating some custom audio where we did event recognition and the nice thing is that the format that they have is basically a CSV file. It has no header and so on but but this pandas line will basically give you a nice data frame with all your annotations from the sound.


Yes so it's time to summarize. Oops, I have a FIXME in my slides.
Okay so we went through the basic audio pipeline we split the audio into fixed length analysis windows we used log melt spectrogram as a speech representation because it's shown to work very well we then applied a machine learning model typically a convolutional neural network and then we aggregated the predictions from each individual window and we merge them together using global mean pooling and models that I would recommend trying first if you trying some new data try audio embeddings with open l3 and a simple model likely notice fire or or random forest for instance try convolutional neural network using transfer learning it's quite powerful and are usually examples that will get you pretty far if you do for instance preprocessor spectrograms and save them as PNG files basically you can kind of take any image classification Python that you have already or if you're willing to kind of ignore this merging of different analysis windows and use that data mutation is very effective time shift time stretch which shift noise add or basically recommended to use sadly there is not such nice like or like go-to implementations of these in infants and carers generators but it's not not that hard to do I just yes some more learning resources for you the slides and also a lot of my notes in general are on this github if you do wanting a hands-on experience tensorflow has a pretty nice tutorial called simple audio recognition and it's it's about recognizing speech commands which could be interesting in general but it's taking a general approach it's not speech specific so you can use it for other things also there's one book recommendation computational analysis of sounds in advance it's quite thorough when it comes to general audio classification a very modern book from 2018 so that's a nice one not so so I think we have [Applause] we have 10 minutes for questions so please go to the microphones and the aisles to ask them I think our first is there Hey yeah thanks Joan a very interesting application of machine learning I have two questions more questions so there's obviously a like a time series component to your data I'm not so familiar with this audio classification problem but alright can you tell us a bit about time series methods maybe lsdm and so on how successful they are yes yeah time series is intuitively one would really want to apply that because there is definitely time component so conditional recurrent neural networks do quite well when you're looking at longer time scales for instance there's a classification task called audio Scene Recognition for instance right I have a 10 or maybe 30-second clip is this from a restaurant or from a city and so on and there you see that the recurrent networks that do have a most much stronger time modelling they do better but for small short tasks who CNN's do just fine surprisingly okay and the other small question I had was just to understand your label the target that it's it's learning you said that this is all very mixed the sound is a very very mixed data set so are the labels just like one category of sound when you're learning or would it be beneficial to have you know maybe a weighted set of two categories when doing learning yep so in order classification tasks the typical style or kind of by definition is to have a single label on a some sort of window of time you can have multi-label datasets of course and in practice that's a more realistic modeling of the world because you basically always have multiple sounds so I think Auto set has multi labeling and there's a new urban sound data set now that also has multiple labels and then you apply like kind of more tagging approaches and but classic you're using classification as a base with tagging is you can either use separate classifier per track or sound of interest or you can have a joint model which has multi-label classification so definitely this is something that you would want to do but it does complicate the problem we have over there when we put a mic and you mentioned about data argumentation that we can also mix up to separate our cases and mix them and then the label of that mix up should be like weighted also because it kind of concludes with previous question usually like 0.5 and 0.5 for the other and yes so a mix up is it was proposed things like 2-3 years ago there's a general method so you basically take your sound with your target class and you say okay let's take 80% of that not 100 and then take 20% of some other sound which is a non target class mix it together and then update the labels accordingly so it's kind of just telling you hey there is we're basically creating a lot of there is this predominant sound but there's also this sound in the background okay thank you yes you mentioned about the main frequency ranges but usually when you record audio microphones you get up to 220 thousand Hertz yes so they have you any experience or I could comment on when you have added information of the higher frequency ranges does that affect the machine learning algorithm or yeah so typically recordings are done at forty four kilohertz or 48 kilohertz for general audio often machine learning is applied at lower frequency so with the 22 kilohertz or something is in just 16 in the rare case is also 8 so it gives it depends on the sounds of interest if you're doing birds definitely you want to keep that those high-frequency things if you're doing speech you can do just fine on 8 kilohertz usually another thing is that noise tends to be in the lower areas of the spectrum there's more energy in the lower end of the spectrum so if you are doing birds you might want to just ignore everything below 1 kilohertz for instance and that definitely simplifies your model especially if you have a small data set yes we have more questions you need to go to the mic either here there quick question you mentioned the editor that has support for annotating audio could you please repeat the name yes audacity oh that's ok yes and and and my general question do having tips if for example you don't have an existing data setting just starting with a bunch of audio that you want to annotate first do do you have any advice for strategies like some maybe semi-supervised to this yeah semi-supervised it's very interesting there's a lot of papers but I haven't seen like very good like practical methodology for it and I think in general annotating a data set is it like a whole other talk here but I'm very interested to come to chat about this this later and thanks to you and I didn't never done very nice talk my question would be do you have to deal with any pre-processing or like white noise filtering you mean to remove white noise it's exactly just you just said like removing or ignoring certain amount yes you can I mean scoping your frequency range definitely it's very easy so just like just do it if you if you know where your things of interests are denoising you can apply a separate denoising step beforehand and then do machine learning if you don't have a lot of data that can be very beneficial for instantly maybe you can use a standard denoising algorithm trained on like thousands of our stuff or just a general DSP method if you have a lot of data then in practice the machine learning algorithm itself learns to suppress the noise but but it only works if you have a lot of data so thank you for a talk is it possible to train a deep convolutional neural net directly on the time domain data using a 1d convolutions and delete deleted convolution yes this is possible and it is very actively researched so it's only but it's only within the last like year or two that they're getting to the same level of performance a spectrogram based models but some models now are showing actually better performance with the end-to-end trained model so this I expect that you know in a couple of years maybe that will be the kind of go-to for a practical application can I do a speech recognition with this this is only like six classes like and I think you have much more classes yes if you want to do automatic speech recognition so the complete vocabulary of English for instance then you you you can theoretically but there are specific models for all automatic speech recognition that will in general do do better so so if you want full speech recognition you should look at speech specific methods and there are many available so but if you're doing a simple task like commands like yes/no up down one two three four five you can limit your vocabulary to say maybe under the hundred classes or something then it gets much more realistic to apply a kind of speech unaware model like this okay thanks for an interesting presentation I was just wondering from the teases it looks like you applied this model to a microprocessor can you tell a little bit about the framework you use where you transfer it from a Python yes so we we use the vendor provided library from as micro electronics for the stm32 and it's called x-cube AI you'll find links in the in the github it's a proprietary solution only works on that microcontroller but it's it you just it's very simple you plug in your you you throw in the carrots model it will give you a c model out and the have examples about the pre-processing yeah with some bugs but but there it does work and the firmware code is also in the github repository not just the model so you can basically download that and and start going okay yeah do join me here if you want to talk more about some specifics thing about auto classification also be around listen this thing thank you thank you Jon Nordby [Applause]

## Speed
6700 words. 45 minutes. 150 words per minute.

# Proposal

45 minute session

## Audio Classification with Machine Learning
Learn how to classify sound using Convolutional Neural Networks

### Short abstract
Sound is a rich source of information about the world around us with many applications within music and speech domains, as well as specific tasks in industry and science.

This talk will show you how to build practical models for sound classification, using Convolutional Neural Networks on audio spectrograms.
Tricks for dealing with small amounts of data will also be covered, including transfer learning, audio embeddings and data augmentation.

### Long abstract
Sound is a rich source of information about the world around us.
Modern deep learning approaches can give human-like performance on a range of sound classifiction tasks.
This makes it possible to build systems that use sound to for example:
understand speech, to analyze music, to assist in medical diagnostics, detect quality problems in manufacturing, and to study the behavior of animals.

This talk will show you how to build practical machine learning models that can classify sound.
We will convert sound into spectrograms, a visual representation of sound over time,
and apply machine learning models similar to what is used to for image classification.
The focus will be on Convolutional Neural Networks, which have been shown to work very well for this task.
The Keras and Tensorflow deep learning frameworks will be used.
Some tricks for getting usable results with small amounts of data will be covered,
including transfer learning, audio embeddings and data augmentation.

A basic understanding of machine learning is recommended.
Familiarity with digital sound is a bonus.

## Bio
Engineer with several years of experience as a Software Developer within Embedded Systems and Digital Signal Processing.
These days focusing on Machine Learning for Internet of Things, and recently completed a Master in Data Science.

Jon loves making things and teaching others to do the same, and is very active in the maker scene in Oslo, Norway.

### Tags
Data Science
Machine Learning
Deep Learning


# Presentation

## Format

- 30 minutes.
30 slides
- 10 minutes. Q/A 


## Outline

Introduction

- About me
- Talk outline
- Example applications
- Digital audio

Audio Classification pipeline

- Analysis-windows
- mel-spectrogram
- CNN for audio

Better models

- Audio Embeddings
- Transfer Learning
- Data Augmentation

Outro

- Summary
- More info

BONUS

- Own dataset
- Streaming
- Audio Event Detection
- Weakly labeled data
- Tagging
- Segmentation

Out-of-scope

- CNN details
- Fourier Transform


## Notes

Example applications

Know your problem.
How often do you want outputs
Classification vs Event/onset detection
(weakly labeled, multi-instance)

Streaming.
Listening continiously
Word-error-rate, false-predictions per hour

Tasks that build upon classification
Segmentation.
Novelty/anomaly detection
(not: search/fingerprinting, )

DO:
Use (log-mel) spectrograms
Divide into analysis windows. Overlap optional
Use AudioSet audio-embeddings, with RF/SVM
https://github.com/marl/openl3

Use CNN, transfer learning from ImageNet

Use basic data augmentation. Time-shift! Time-stretch, pitch-shift. Try Mixup!
(but careful about time-shift for AED)
