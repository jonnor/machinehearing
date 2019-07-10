
## Application ideas

Fun stuffs

* Detect clapping and its sound level in a conference


## Research questions

* How can one perform environmental monitoring tasks on audio without invading privacy?
Issues: capturing conversations, identifying/tracking speakers.
Possible mitigations.
Use very short recording windows, and sparse sampling to avoid recording (intelligeble) speech?
Can one detect speech and avoid recording in those cases? / discard sample.
Process classification etc on the fly, and do not store the audio recordings?
Device firmware verifiable.
Indicator light on when recording. Can be hardwired to the microphone subsystem power.
Pause mode? Activate to avoid capture for NN minutes. 
* How can one enable continious environmental monitoring using audio in a Wireless Sensor Network?
What is a realistic power budget?. Outdoor, Indoor. Rural, Urban.
What is the power usage of existing solutions/works? Non-edge ML, deep learning edge ML.
How much can power usage be reduced by machine learning?
How would the sensor network architecture look like?
* Energy efficiency of deep learning
How does end2end learned systems compare in number of instructions
versus standard feature engineering?
Can one adopt feature learnings to hand-coded systems to improve efficiency?

Neural Networks for Machine Hearing

* Can Data Augmentation be applied successfully to (mel)spectrogram representation instead of raw audio?
Mixup/between-class.
See: `SpecAugment`

* How to find the most efficient feature representation for audio classification.
Ex: Time window range, time resolution, frequeny range, frequency resolution.
Answer may be class dependent, but also inter-class. Can one do a per-class search to simplify?
Sparsity constraints on initial filters in end2end model. Grouped.

Keywords

* Energy efficiency, energy budget
* Communication link budget
* Privacy
* Cost


## Book reviews

#### Computational Analysis of Sound Scenes and Events
Notes.

Ch11. Computational Bioacoustic Scene Analysis


Ch12. 24/7 AER systems. Smart home applications.
Ch12.2.1. User concept of "event" may comprise several acoustic events taken together. 
Ch12.2.2. Real life AER as an open-set problem, unbounded number of classes.
"binary 1-vs-set" as extension of standard 1-class classifiers.
24/7 AER exposed to ever growing number of non-target events. Prior probability ->1 for on-target, ->0 for target.
Poses challenge for classic metrics like accuracy,f-score. False alarm rate per unit of time can be used instead.
Detection error trade-off (DET) curve, used in keyword spotting.
Ch12.2.3. Current Far-field technology (microphone arrays etc) geared towards speech. Generalization to AER understudied.
Devices have limited compute and memory capacity. 
Introducing Computational cost into Evaluation. References a comparative study. GMM low-cost baseline. SVM similar accuracy, higher cost.
ReLu activation particularly interesting on devices, cheap to compute.
Ch12.3.1. User experience depends to large extent on reliability. Users will not know/care about which subsystem failed.
AER most interesting for remote monitoring. User would need to double check event in order to evaluate reliability.
Missing detections very hard to verify for user. But can be critical for user experience when event was important (broken window during breakin).
Standard measures may not be good predictors of user experience.
Take the place of user. Encourage academic researchers to build sound recognition systems.
Opinion scoring as method for assessing user experience.
Can be included into design of end-user application, to capture data from production system.
Operating point, threshold for positive detection used to tradeoff FP/FN (false alarm / missed detection).
Discrete Cost Function (CDF) can be used to include relative cost of FA/MD.
Ch12.4.2. Privacy of environmental audio data.
GDPR defines level of data privacy. Personal data, sensitive data, confidential data. Profiling: inferring sensitive data from derived data.
Sensitive and confidential data should not be collected/stored. Personal may, if for a specific usage and given permission, and no profiling is done.

Ch13. 24/7 AER systems. Smart cities. Noise pollution, surveillance.
Urban environments more anthrophony than geophony/biophony.
Voice, traffic, construction, signals, machines, music, etc.
Patterns of activity. Daily,weekly,monthly,yearly.
Microphones less affected than cameras by fog,pollution,rain, daily changes in light conditions.
Less succeptible to occlusion, are capapable of omnidirectional sensing.

Noise pollution. Complaints biased by location, socieconomic status, source type.

Ch13.3 Acoustic Sensor networks
Ch13.3.1 Mobile sound sensing. Using existing smartphones to capture,analyze sound.
Many crowdsourcing efforts exists for SPL measurements, geo-tagged.
Some also include subjective data, allows filing complaints.
OnoM@p atempts cross-calibration to avoid erronous data.
Ch13.3.2 Static sound sensing.
Commercial solutions from 560USD - 10k+ for recording SPL. Some examples down to 150 USD.
Desirable to have low-cost, powerful sensor nodes to support computational sound analysis.
Ch13.3.3 Designing a low-cost acousting sensing device.
SONYC project. Raspberry PI + MEMS microphone with onboard MCU. Dynamic range 30-120dBA.
MEMS board on a flexible gooseneck for positioning.
Sensor cost 83USD EX construction and deployment (Dec 2006).
Node requires continious power supply and WiFi connection.
Ch13.3.4 Network Design.
Mounted at 4 meters above street level, every 150m.
Audio data is captured in 10sec, lossless FLAC compressed and encrypted, interleaved with random durations of time(??).
Transfers to control server, then storage servers, for further analysis.
Sensor node also sends status ping every minute.
VPN network for SSH access.
Future versions will utilize mesh networking and reduce power consumption to enable battery powered, energy harvesting.
Many more deployment possibilities become available.
Ch13.4. Lists some 7 datasets with lots of Urban Soundscape data.
Ch13.4.1. Sound source identification, in urban environment.
Proposed urban sound taxonomy. UrbanSound8k dataset implements this.
Reviews performance. MFCC-SVM baseline, SKM-mel-RF, SKM-scattering-SVM, mel-CNN.
SKM-mel-RF had best results with 370ms,16-frame patches. Dictionary of 2000 words.
Deep learning methods needed data augmentation to perform better than SKM.
Scattering transform. Can be seen as extension of mel-spectrogram, computes modulation spectrum coefficients of multiple orderings
through cascades of vavelet convolutions and modulus operators. Convolving then averaging over time using a low-pass filter.
Phase-invariant convolutional layer, capture amplitude modulations in time-shift invariant manner.
Basically same perf as SKM-mel-RF. But dictionary size of only 200. "finding motivates further exploration using deep convolutional approaches"
mel-CNN used 5x5 perceptive field.

Ch14.2.1. Manually designing audio label/class vocabularies.
Ch14.2.1.2 Mining audio data to build vocabularies. Two step process: generate candidates, then filter.
Can used Verb-Noun pairs and Adjective-Noun pairs as names.
Ch14.2.2.2. Using video with audio as basis for learning.
Ch14.2.3. Active learning. Maxizing human effort
14.2.4 Unsupervised Data. Can be basis for annotation effort via similarity metrics
Weak labelling. Multiple-instance-learning.
14.2.5 Evaluation tasks. AudioSet as a potential standard. 10s exerpts, 100 examples, 500 sound categories.

14.3.2 Future approaches. Mid-sized embedding continious spaces.
Triplet loss. Only needs same/different annotation for pairs instead of class label per instance.
Transfer learning. Can be based on embeddings
Source separation, joint estimation.

#### Human and Machine Hearing

Ch3.1. Page51. Great diagram of relationship between log,exp,pow(...) as expanding or contracting non-linear functions.

Ch5.5. Page 98. Power-law compression of mel-spectrogram with exponents 0.25-0.67 can be better than log or lin.

MFCC sometimes used for pitch tracking, easy to split out fundamental.

Ch7.11. IIR filter standard forms. Direct1, direct2. Second order needs 2 delay elements and 5 multiplications.
Larger filters often a cascade of 2-order, favorable for numerical stability and modularity.

Ch7.13. Shows speech with two spectrograms. One with high frequency resolution, other with high temporal resolution.

Ch9. Gammatone and related filters.
Ch9.4. Real gammatone has impulse response of a gammatone distribution times a sinousoid.
Order N, dampening factor, gammatone phase. Orders 3-5 typical for auditory filters.
Ch9.4. All-pole gammatone filter (APGF). No zeroes. One zero gammatone filter (OZGF). Asymmertric
Gammatone filters are special case of gammachirp. Easier to control asymmetry.

Ch10. Nonlinear sytems. Cannot be fully described by responses to sinewaves.
But often characterised by response to sines at different levels, and pairs of sinewaves.
Ch10.1. Volterra Series. Linear convolution model plus corretion terms. (also Wiener series)
Zero term: constant. First term: Linear response. Second term: Product response. Third order: cubic.
Ch10.3-10.4. Essential nonlinearities (in the ear).
Fig10.2. Measurements on live cochlea demonstrating non-linearity.
Two-tone supression.
Intermodulation distortion.

Ch11. Automatic gain control.

Ch21. Stabilized Audatory Image (SAI)

Ch22. Binaural spatial hearing.

Head-related transfer function. Acoustic reason for differences in sound from different sides.
Neural extraction of interaural differences.

How we can localize sound even in reverberant conditions.
Precedence effect. Law of first waveform. Haas effect. 

Ch23.1. Scene analysis.
CASA: Computational Auditory Scene Analysis.

Ch23.2 Attention and Stream Segregation
Separating pieces of sound into different tracks.
Pay 'attention' to particular streams
Following Gestalt principles: common-fate etc
time-frequency masks. Binary masks.

Ch24. Learning and applications

Application: Hearing aids

Ch25.3 Bandpass power and Quadratic Features
Autocorrelation coefficients, power spectra equivalent.
Direct learning of waveform filters. Filter learning.
RElies on a nonlinearity of some kind, quadratic or other,
to rectify filter output or choose sparsity based on outputs with highest power.

Cascading layers of bandpass quadraticfeature extraction,
using wavelet transforms with power detection: Wavelet modulus operators.

Ch28.5 Medial diagnostics through sound. `auscultation`
Heart murmurs. Lung.
The relevant range of frequencies for hearts is lower than normal human hearing. `<20Hz`.

Fault detection in machinery by technicians often also use sound.
