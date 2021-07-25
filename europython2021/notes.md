
# Disposition

- Introduction. 5 mins
- Application. 5 mins
- Data. 5 mins
- SED model. 5 mins
- SED system. 5 mins
- Outro. 2 minutes
- Questions. 5 minutes
- Bonus. 5 minutes

Approx 40 minutes scheduled

# TODO

- Transfer over the presentation from Geekle
- Review presentation

Planned adjustments
- Expand on model building
MFCC+LogisticRegression
RNN+mel-spec
CNN+mel-spec
- Expand a bit on evaluation
Window-wise versus event-wise
Precision/recall-tradeoff
Higher-level, BPM accuracy

- Add in call for data?

- Improve CTAs for Soundsensing at end.
Add product pictures
Add team pictures?

- Add EuroPython logo to first/last slide

- Do a full run-through of presentation
- Record a video. With OBS

- Update bio and picture on webpage
- Book and do a tech check "speaker training"



# Format

45 minute slot.
5-10 minutes Q&A.

35 minutes presentation

Live presentation preferred
Recording as backup. Deadline 21 July

# Planning

## What people need to understand

- Audio events
What is an audio event.
Onset/offset
Definition of AED task. Input/outputs

- Typical audio ML pipeline
Analysis windows
Features over time
Spectrogram

- Post-processing.
Counting. Threshold above X
Event-rate

- How to evaluate performance
Window-wise vs event-wise
sed_eval: https://tut-arg.github.io/sed_eval/
tolerances

## Assumptions
What we will (mostly) assume that people know

- Basic digital audio
- Basic Machine Learning. Supervised classification
- Typical Neural Networks. CNN/RNN ?

## Out of scope

What people do not need to understand

- ? Weakly labeled data 
- Making efficient networks

Tips & tricks

- Error analysis
Manually examining mistakes that your algorithm is making

- Labeling strategies
Semi-supervised
Alignment tools

- Pretrained model
OpenL3 / YAMNET / PANN

Challenges

- Out-of-distribution data
Device. Environment. 
Data augmentation

