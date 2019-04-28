
# Task 1 
Hosted on Kaggle
https://www.kaggle.com/c/freesound-audio-tagging-2019

### Baselines
https://github.com/DCASE-REPO/dcase2019_task2_baseline
LB 0.537

* TensorFlow
* MobileNetV1 type model
* Online mel-spectrogram conversion (using GPU)
* label smoothening
* 96 mels, 0.5 sec windows
* pretrain on noisy set, warmstart and train on curated set
* Fast, 2 minute inference on GPU
* ! no data augmentation


https://www.kaggle.com/mhiro2/simple-2d-cnn-classifier-with-pytorch

LB 0.611

* PyTorch
* Basic 2D CNN model.
* LeakyReLU/PReLU in output
* Preprocessed log-melspec
* 128 mels, 2 sec windows, 128 frames (2*347 samples hop at 44.1kHz)
* ! Test Time Augmentation (TTA). 5x
* ?? Horizontal flip data augmentation

## Ideas

### Preprocessing

- Mean-subtract. Minmax scaling

### Data Augmentation

- time-stretch
- frequency-shift
- Mixup/between-class
- Cutout/random-erase 
- Noise addition

SpecAugment.
Showing that data augmentation on log mel-spectrograms (not audio waveform) performs well
https://ai.googleblog.com/2019/04/specaugment-new-data-augmentation.html
Used TensorFlow `sparse_image_warp`

### Combining results

- Test-time-Augmentation
- GBT over frame-wise embeddings?
GlobalMean might not be the best
