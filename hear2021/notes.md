
HEAR 2021: Holistic Evaluation of Audio Representations + Q&A
Breakout: HEAR 2021: Holistic Evaluation of Audio Representations 
https://neurips.cc/virtual/2021/competition/21954

# TODO

# Follow up research
Why does OpenL3 do so well?

Why does YAMNet do so poorly?
Exceptions need fixing

What improvements can be done to perform better?
Influence on music|env for OpenL3
Influence of input representation size. M128

Could we make OpenL3 more efficient, using tech from YAMNet?
SeparableConvs, smaller input feature size

# Result analysis

## Overall

What is the single best model?
Dominates the others most often

## YAMNet and OpenL3

What are the expecations going in?
That performance would be quite similar
Use published results. AudioSet ?

Which one is better, OpenL3 or YAMNet?

References.
- Best in task
- Best all-around
- Median performance

Maybe boxplot / stripplot as ref.
Colorize ours. Gray/opacit the refs?


# Ideas


## Holistic emsembles
Ensemble all of the vectors together. How well does combined system perform?

Can one learn a holistic model, using the best performers as teachers?

Can a holistic model trained on N tasks, perform well on unseen tasks?
For which train/test combinations?


## YAMNet results

A. Jansen, J. F. Gemmeke, D. P. W. Ellis, X. Liu, W. Lawrence, and D. Freedman,
“Large-scale audio event discovery in one million youtube videos,” in IEEE ICASSP, 2017, pp. 786–790

On the 20,366-segment AudioSet eval set, over the 521 included classes,
the balanced average d-prime is 2.318, balanced mAP is 0.306, and the balanced average lwlrap is 0.393.


Why so poor?
Is only a linear layer after during train. Yes

Is it due to the padding


https://www.tensorflow.org/tutorials/audio/transfer_learning_audio ?
Transfer learnuing tutorial on ESC-50
Gets 81% accuracy ?

HEAR 2021 result
Soundsensing 	yamnet_hear 	0.838
Matches


https://paperswithcode.com/paper/wav2clip-learning-robust-audio/review/
Results for OpenL3, YAMNet, Wav2Clip, 
On Urbansound8k, ESC-50, FSC50k, 	VGGSound	TAU Audio Only	DESED (AR)	VGGSound (CMR)

Yamnet,ESC-50
0.8505
Yamnet,FSD50k
0.5039

MARL + Soundsensing 	openl3_hear 	0.447 	2.117

matches

https://github.com/tensorflow/models/blob/master/research/audioset/yamnet/yamnet.py

64 mel bins not enough?

https://github.com/tensorflow/models/blob/master/research/audioset/vggish/README.md


YAMNet better than OpenL3 on ESC-50
Matching on GZTAN
Matching on libricount
Matching on vocal imitation (both quite bad)




## Conclusion

OpenL3

YAMNet. No, it does not look like. Good performance on ESC-50, otherwise mediocre or bad

Suprising given the pretty good performance on AudioSet
Highlights the importance of broad evaluation?

Why the large difference in performance?

## Pres


4 blocks of convolutional, max pooling layers
flattened
dense layer
L3 has dim 6144

mel

Used AudioSet [7] to train the L3-Net audio embedding models.
10 second videos
∼2M videos

Two subsets

Music 296K
Environmental 195K videos

Mel128, Mel256

Data augmentation:
random 

224x224 image patches and 1 s audio clips

512 d vector

    embedding_size = 512

    openl3_model = openl3.models.load_audio_embedding_model(
            input_repr="mel256",
            content_type="music",

AUDIO_POOLING_SIZES = {
    'linear': {
        6144: (8, 8),
        512: (32, 24),
    },
    'mel128': {
        6144: (4, 8),
        512: (16, 24),
    },
    'mel256': {
        6144: (8, 8),
        512: (32, 24),
    }
}

    pool_size = AUDIO_POOLING_SIZES[input_repr][embedding_size]
    y_a = MaxPooling2D(pool_size=pool_size, padding='same')(m.output)
    y_a = Flatten()(y_a)


Perhaps more importantly,
when a sound is pitch-shifted the pattern created by its harmonic partials change when using a linear frequency scale,
whereas with a (quasi) logarithmic frequency scale such as the Mel scale, pitch shifts result in a vertical translation of the same harmonic pattern, meaning that convolutional filters should generalize better when using the latter

# OpenL3

input_1 (InputLayer)         [(None, 1, 48000)]        0         
_________________________________________________________________
melspectrogram (Sequential)  (None, 256, 199, 1)       0         
_________________________________________________________________
conv2d (Conv2D)              (None, 256, 199, 64)      640       


...

audio_embedding_layer (Conv2 (None, 32, 24, 512)       2359808   
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 1, 1, 512)         0         
_________________________________________________________________
flatten (Flatten)            (None, 512)               0         

Max pooling. Huge downsample. 32, 24
High time-frequency resolution until the end

# YAMNet

reshape (Reshape)            (None, 96, 64, 1)         0         
_________________________________________________________________
layer1/conv (Conv2D)         (None, 48, 32, 32)        288       

....

layer14/pointwise_conv/relu  (None, 3, 2, 1024)        0         
_________________________________________________________________
global_average_pooling2d (Gl (None, 1024)              0         


Lower temporal resolution
Lower frequency resolution
/2 stride in first conv layer

3,2 time/freq at end
global mean pooling


What would happen if
- swapping max for global avg pool (and v.v.)?
- Removing last N layers in YAMNet case, then maxpool

Could maxpool be beneficial base when scene embedding using mean?
Different time-segments pick out slightly different pattern
Increased variance?


OpenL3 frame embedding improvement

Could avoid maxpool for time, to get better time-frame embedding.
Have 24 steps per 1 second => 40 ms
32 freq bands, and 512 channels
dimensionality 16384 if flattened
maybe acceptable as is

OpenL3 scene improvement
Use the 

