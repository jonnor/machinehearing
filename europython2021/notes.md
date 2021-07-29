
# Disposition

- Introduction. 5 mins
- Application. 5 mins
- Data. 5 mins
- SED model. 5 mins
- SED system. 5 mins
- Outro. 2 minutes
- Questions. 5 minutes

Approx 40 minutes
5 minutes of Q&A.

https://ep2021.europython.eu/talks/9cE22Ve-sound-event-detection-with-machine-learning/

Previous talk spent 30 minutes before model/system.
Should be more like 20.

# TODO

- Do a full run-through of presentation

- Upload/link slides on webpage
- Update bio and picture on webpage


## Done

Moved to Bonus
- Semi-automatic labeling
- Streaming inference
- Youtube data collection
- Less weakly labeled data
- Analysis window details

- Do a techcheck on Streamyard
https://support.streamyard.com/hc/en-us/articles/360043726731-Screen-Sharing
https://support.streamyard.com/hc/en-us/articles/360043291612-Guest-instructions
- Review speaker documentation
Check speaker video, https://www.youtube.com/watch?v=UgQFlw66O4o



## Action

- 15 minutes before, join Matrix backstage
- Post link to Github project and slides in Matrix
- Tech will give Streamyard invite link
- !! USE CHROME
- Display Name. Jon
- Start your webcam and audio
!! Use share Chrome tab. Include "share audio"
Screen sharing a video with audio

- Tell your session chair that you are ready in StreamYard’s Private Chat

- The session chair introduces you and your talk
- !!! The session chair will ask a few questions,
and then let you start the presentation

## Backup video settings

MP4 container
AAC-LC, stereo, 48kHz
H.264, progressive, high profile, variable bitrate
5-8 Mbps bitrate
24, 25 or 30 frames per second; higher rates are also acceptable as long as the file size remains reasonable
720p or 1080p (non-interlaced)



## Nope

- Add in call for data

- Expand a bit on evaluation
Window-wise versus event-wise
Precision/recall-tradeoff
Higher-level, BPM accuracy

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

