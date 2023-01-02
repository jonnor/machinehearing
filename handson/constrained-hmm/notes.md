
## Others that want to do this

- https://github.com/jmschrei/pomegranate/issues/9

## Implementation notes

In `pomegranate`, the HMM models have a public callback API.
The callback `on_epoch_end` is called on each iteration.
https://github.com/jmschrei/pomegranate/blob/f115a242a5b50854bbf199d43fe2cfd061e9708a/pomegranate/hmm.pyx#L2715
The callback gets the model instance as self.model before on_training_begin
But there is no way to get or set the transitions during training, as they are C arrays inside Cython
Clean solution would be to expose an optional callback for modifying this.
Otherwise have to stick to the workaround from https://github.com/jmschrei/pomegranate/issues/9

> I am using three vector approach to sparse matrices, but each vector is a private attribute right now
> I'll add in a method which takes in either a dense or sparse matrix and calculates a new internal transition matrix from that.

self.out_transition_log_probabilities
self.in_transition_log_probabilities
? which is the last one?

Can have multiple batches per epoch.
Calls self.summarize for each batch
and then self.from_summaries for each epoch

It is in self.bake that transition_log_probabilities gets created, from the self.graph instance
Could create methods like
def get_transition_matrix()
def set_transition_matrix()
Would also need the state_name to index mapping to do much interesting

However for simple dissallowing of certain edges, one can use.

BUT - this does not implement k-means initialization, which has to be done manually

In `sequentia`, the models just use hmmlearn internally, so one would need to use the hmmlearn approach there.

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
