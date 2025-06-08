
## Others that want to do this

Constrains inside the EM loop

- https://github.com/jmschrei/pomegranate/issues/9

# Anomaly Detection for cyclic behavior

In manufacturing and automation, cycling behavior is common in several processes.
For example in assembly, a machine might first do A, then B, then C,
and correct outcome depends on the correct order of operations, as well as correct operation inside each.

In such a system, one want to be able to detect anomalies, such as:

- Incorrect order of operations/states (in a cycle)
- Cycles that do not complex / are aborted prematurely
- Cycles that take abnormally long (or short) time
- States (in a cycle) that are abnormally short or long
- Anomalous data inside a particular stage

Thesis. A typical automation loop is be well approximated with a HMM, using a `linear` topology.
This, along with some preprocessing, should enable detecting all these kinds of anomalies.

A constrained HMM approach is particularly attractive when
different stages in cycle have different lengths (possibly also varying in length).


## Datasets

#### Genesis Demonstrator
https://www.kaggle.com/datasets/inIT-OWL/genesis-demonstrator-data-for-machine-learning

- Machine is ortable pick-and-place, with air powered gripper
- Sorts different two different materials (wood and metal) into their corresponding target locations
- Materials can come from 
- 8 states in the State Machine of the program.
- 3 kinds of anomalies introduced in different sub-datasets: linear drive jam, linear drive gradual impairment, air pressure gradual drop
- Rrecords 5(+4) continuous signals, 13 discrete signals

#### Bosch Research CNC Machining Data
https://github.com/boschresearch/CNC_Machining

- Tri-axial accelerometer (Bosch CISS Sensor) mounted inside the machine.
- Sampling rate equal to 2 kHz.
- Thereby normal as well as anomoulous data have been collected for 6 different timeframes, each lasting 6 months from October 2018 until August 2021 and labelled accordingly.
- Data from three different CNC milling machines each executing 15 processes.

#### CNC turning: roughness, forces and tool wear
https://www.kaggle.com/datasets/adorigueto/cnc-turning-roughness-forces-and-tool-wear?select=Prep.csv

Surface roughness was measured on six different spots after each machining run

? might all be normal. Not sure if there are outliers/anomaly conditions present.

#### CNC Mill Tool Wear
https://www.kaggle.com/datasets/shasun/tool-wear-detection-in-cnc-mill

Machining data was collected from a CNC machine for variations of tool condition, feed rate, and clamping pressure.
Each experiment produced a finished wax part with an "S" shape.
Run on 2" x 2" x 1.5" wax blocks.

- 18 experiments, each giving one time-series
- Sampled at 10 Hz
- Multiple active machining operations, labeled as "Layer 1 Up", "Layer 1 Down", "Layer 2 Up", "Layer 2 Down", "Layer 3 Up", and "Layer 3 Down". 
- Experiments were run with different feed rates,
- Experiments were run with different clamping pressures, of 2.5, 3.0, and 4.0 bar
- visual flaws indicated with a passed_visual_inspection column
- Some experiments were aborted for safety concerns, see machining_completed column
- Eight experiments were run with an unworn tool while ten were run with a worn tool (see tool_condition column for indication).

! Simple experiments.
Would be quite doable to replicate locally. If one has a CNC mill capable of reporting actual positions, as well as motor voltage/amp/power.

WARN: some dirty data:

    Note that some variables will not accurately reflect the operation of the CNC machine.
    This can usually be detected by when M1_CURRENT_FEEDRATE reads 50,
    when X1 ActualPosition reads 198, or when M1_CURRENT_PROGRAM_NUMBER does not read 0.
    The source of these errors has not been identified.

This notebook has some reasonable basic EDA on the dataset,
https://www.kaggle.com/code/paulsatyajit/cnc-milling-machine-tool-wear-detection

    Experiments are up to 2000 seconds long.

This one has some focused EDA on Spindle output power vs Machining process
https://www.kaggle.com/code/jiprud/cnc-data-analysis

    Hypothesis: Output power of the tool (S1_OutputPower) is bigger for "Milling" points than in "Preparation" ones. Let's see if we can prove this.
    Conclusion: hypothesis was proven correct. Average spindle power for Milling steps is two times bigger than for non Milling steps

Notebook explored Mahalanobis for unsupervised anomaly detection for tool wear
https://www.kaggle.com/code/clashofphish/attempt-mahalanobis-distance-for-outlier-detection

    Had problems with bad readings.
    Was not successful.


Questions:

- Can we reliably find the machining states, with unsupervised method? Segmentation
- Do we need special features/preprocessing to be able to do the segmentation?
- Can one detect the "jog" between each active operation?
- What changes/differences are there in the signal between toolwear/not, degraded/not and aborted/not ?
Powers, regulation delays (diff in Position/Velocity/Acceleration).
- Can the condition leading to aborted operation be detected, with unsupervised method?
So not using position, which is consequence of an actual abort.
- Is a stage-aware or per-stage analysis helpful in predicting toolwear/visual degradation?

#### Turning Dataset for Chatter Diagnosis Using Machine Learning
Dataset: https://data.mendeley.com/datasets/hvm4wh3jzx/1
Paper: https://arxiv.org/abs/1905.08671

- Two perpendicular single axis accelerometers, a tri-axial accelerometer, a microphone, and a laser tachometer.
- no-chatter, intermediate chatter, chatter, and unknown.
- The cutting test is performed by turning an Aluminum 6061 workpiece on a Clasuing-Gamet 33 cm (13 inch) engine lathe
- four different cutting configurations were collected where each cutting configuration depends on the stickout distance
- For each stickout distance, we collect data for several combinations of the rotational speed and depth of cut

800 MB compressed, 6 GB uncompressed.

### Custom data collection / demonstration
Can maybe be done with a 3d printer, CNC machine.
Making the same part repeatedly.
Ideally a part that is simple to make, such that one can collect many times.
Need a way to introduce realistic/plausible anomalies, in a safe manner.


### Manufacturing process as repeated-cycle

In CNC mills or lathes, making a part is often a series of cuts.
Combined this makes one very long cycle - unique to a part.
One can of course model this particular part/program as a long sequence of states, one state per unique cut.

But one can maybe also model individual cuts as repeated instances of the same cycles (enter, cut, leave),
without modelling each cut as a separate state?
Perhaps they can be similar enough that anomalies can be detected.


## VAD

Hidden-Markov-model-based voice activity detector with high speech detection rate for speech enhancement
https://digital-library.theiet.org/content/journals/10.1049/iet-spr.2010.0282
2012

An improved noise-robust voice activity detector based on hidden semi-Markov models
https://www.sciencedirect.com/science/article/abs/pii/S0167865511000584
2011

A semi-continuous state transition probability HMM-based voice activity detection
https://www.researchgate.net/publication/224751061_A_semi-continuous_state_transition_probability_HMM-based_voice_activity_detection
June 2004

## AD

Anomaly Detection with HMM Gauge Likelihood Analysis
https://arxiv.org/abs/1906.06134
2019

Efficient Modeling of Discrete Events for Anomaly Detection Using Hidden Markov Models
https://link.springer.com/chapter/10.1007/11556992_38
2005

Hidden Markov Model-based Tool Wear Monitoring in Turning
https://www.researchgate.net/publication/245368193_Hidden_Markov_Model-based_Tool_Wear_Monitoring_in_Turning
2002

Online milling tool condition monitoring with a single continuous hidden Markov models approach
2014
https://www.extrica.com/article/15019
Using a left-right HMM-GMM. 3 states.
CNC cutting operation. Cut entry, cutting, cut exit.
Used to generate a tool health condition using the log-likelyhood of the model.
Used both Vibration and AE signals.
Preprocessed with wavelet transform.
