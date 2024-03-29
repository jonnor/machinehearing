

# Image

## Datasets

More interested in a detection case. Either pet, or background

# Scenario analysis

Barks are rather impulsive. Quite loud.
Meows rather tonal. Not neccesarily so loud.

Domestic environment.
Say in living room.

Possible confusing sound events

Speech. Shouting.
Kids crying.
Music.
Kitchen cutlery etc. Bangs etc.

Should include confuser events in dataset.
In addition to silence/background.

What is a likely SNR range for meow?

Evaluation references
Strong unconstrained baseline as top reference. Ex: YAMNet/PANN based. 128 mels
Strong microcontroller baseline. Ex: SB-CNN. 64 mels?

# Data


## Background data, domestic soundscapes

#### Real-Life Indoor Sound Event Dataset (ReaLISED) for Sound Event Classification (SEC)
https://zenodo.org/records/6488321

#### DASEE-dataset
Domestic Acoustic Sounds and Events in the Environment of dementia patients
https://www.kaggle.com/datasets/abigailcopiaco/daseedataset
11-class database containing excerpts of clean and noisy signals at 5-seconds duration each, uniformly sampled at 16 kHz. 
Has cat and dog classes, along with other events, also silence
Is synthetical mixes
80 GB total.
Maybe a decent test set?

Mix of recorded and synthetic data (used in DCASE task 4 since 2019).

#### DESED
https://github.com/turpaultn/DESED
Has a mix of realistic soundscapes (recording), and a soundbank
Using Scaper for mixing
Dedicated evaluation set. Mixed?

Weakly labeled training set. 1578 clips (2244 class occurrences).
Synthetic strongly labeled set.
https://dcase.community/challenge2022/task-sound-event-detection-in-domestic-environments

## Event Data, pet vocalization

Kaggle Cats and Dogs Dataset
https://www.microsoft.com/en-us/download/details.aspx?id=54765


#### BarkMeowDB - WAV Files of Dogs and Cats
https://zenodo.org/records/3563990

#### haydenroche5/meow_dataset
https://github.com/haydenroche5/meow_dataset
has youtube data and a cat named newton

#### Cat Meow (Kaggle)
https://www.kaggle.com/datasets/andrewmvd/cat-meow-classification

#### CatMeows: A Publicly-Available Dataset of Cat Vocalizations
https://zenodo.org/records/4008297

#### AE-Dataset: Acoustic Event Dataset
https://data.vision.ee.ethz.ch/cvl/ae_dataset/
28 class acoustic event sounds.

#### Audio Cats and Dogs (Kaggle)
https://www.kaggle.com/datasets/mmoreaux/audio-cats-and-dogs/code
Comes from AE-Dataset.

YAMnet baseline
https://www.kaggle.com/code/alperkaraca1/audio-classification-using-yamnet



# Models

## Models for ESP32 grade microcontroller

How well can microcontroller scale models run?

- CNN with 3 channels. At 64x64 or 32x32 ?
- CNN with 1 channel / greyscale
- MLP
- MLP with DCT preprocessing
- RF with DCT preprocessing
- HAR??

FOMO
80 Mhz CPU able to process 64x64 pixels (B&W) in 1 second
256 KB RAM
https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices

EdgeImpulse MobileNet V1 and α=0.10 (around 53.2K RAM and 101K ROM).
takes 96x96 px images

