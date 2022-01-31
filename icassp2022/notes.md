
https://2022.ieeeicassp.org/call_for_industry_expert_presentations.php

# Format
30 minutes oral presentation time followed by a brief Q&A stage (around 6 minutes)

# Proposal

## Title
Optimizing Convolutional Neural Networks for TinyML audio applications

## Details
Jon Nordby
Head of Machine Learning & Data Science
Soundsensing AS
jon@soundsensing.no

## Biography

Jon Nordby is a Machine Learning Engineer that specializes in audio and IoT applications.
He has a Master in Data Science and a Bachelor in Electronics Engineering,
and has worked as a software engineer in electronics and web projects for 10 years.
Since 2019 he is the Head of Machine Learning and Data Science at Soundsensing,
a provider of audio ML models and IoT sound sensors with built Machine Learning capabilities.
Jon is also a member of IEEE Signal Processing Society (SPS), Audio Engineering Society (AES),
Acoustical Society of America (ASA), and International Institute of Acoustics and Vibration (IIAV).

## What we do
Help companies develop audio ML models for deploying into embedded devices.
Assist in setting up audio data collection pipelines
Build optimized models using our internal Audio ML pipeline
Provide reference firmware and hardware designs
Turn-key solutions for some applications

## Type

- General overview of one technology area; or
- **In-depth treatment of one specific technical issue**; or
- Special focus on standardization and deployment challenge

## Outline

Ref SenseCamp 2019 / TinyML 2021

Scope

- Techniques that can be applied with any execution engine (CPU,FPGA,GPU,)
- Focus on standard CPUs found in embedded/microcontroller. ARM Cortex M/A
- Focus on techniques that have widespread support, demonstrated usefulness
- Some mentions of areas of active research
- Out-of-scope: Binarized neural networks, Neural accelerators, hardware co-design

Hardware devices

- Microcontroller
- SBC
- Phone

Frameworks

- Tensorflow Lite for Microcontrollers (TFLM)
- X-CUBE-AI
- Edge Impulse
- nnom
- ?

Constraints

- FLASH. Program space
- RAM. Peak memory
- CPU. Energy

Workflow

- Model search
- Pareto optimal

Optimizations

- Input representations
- Windowing/overlap
- Conv operators
- Neural Architecture search
- Streaming
- Quantization
- Pruning. Grouped conv
- Kernel clustering
- Knowledge. Teacher/student

Areas of active research

? Temporal Convolutional Networks (TCN) 
? Transformers
- Ultra high quantization
- Hardware accelerators
- Hardware/software co-design


## Key aspects

### Relevance and attractiveness to ICASSP
Consumer electronics. Voice assistants. Mobile phones.
Assistive devices. Hearing aids, hearables
Self-driving cars
Industrial Internet of Things.

- Voice tasks. Keyword spotting
- Environmental sound. Env awareness, 
- Condition Monitoring

### Technical contents

- Convolutional Neural Networks
- TinyML class devices, what are they
- Constraints of TinyML devices
- Overall workflow
- Optimization techniques

### Novelty

TinyML a growing area

- Machine Learning and Deep Neural Networks has been shown to do well on many sensing problems
- Large interest for applications in industry and consumer electronics
- Extend edge computing out to the sensors
- Low-cost and privacy-compatible enables new applications
- Fast growing support in the semiconductor/embedded industry
- Many applications already deployed and in use

## Inspirations and motivations

- Understand what is needed to deploy audio ML CNNs on constrained devices
- Learn the most common and widely applicable model optimizations
- Audio ML with CNNs can run on any new ~1 USD microcontroller, with a ~1 USD microphone
Complete devices from 10-100 USD BOM. Including Internet connectivity
- Deploy your models everywhere


## Summary
300 words

Advances in machine learning from deep neural networks have in the last years
greatly increased performance on many audio analysis tasks, enabling new applications.
Generally the advances have involved large and very compute intensive neural networks,
often running on powerful GPUs.
However for many applications it is neccesary to deploy models on highly constrained devices,
such as IoT sensor nodes.
These devices often use microcontrollers with less than 1 MB of RAM and program space,
running at under 100 Mhz and at power budgets of 100 milliwatt or less.
Targeting such devices (dubbed "TinyML") requiring careful adaptation of the neural networks
in order to keep the compute requirements down, while still maintaining the best possible performance.
In this session we'll go through the work that has been done in this area for audio applications,
including tasks such as Keyword Spotting, Sound Event Detection and Environmental Sound Classificaiton.
Primarily the focus will be on Convolutional Neural Networks,
with some notes on Recurrent Neural Networks and Transformers.
Some of thee techniques to be covered include
use of efficient operators like separable convolutions and strided downsampling,
neural architecture search for model optimization,
hyperparameter optimization of spectrogram pre-processing,
quantization, and streaming inference.
The emphasis will be on established solutions which can be easily applied in practice
using frameworks such as Tensorflow Lite for Microcontrollers and X-CUBE-AI,
but also mention of recent works from the research community and open challenges.
While the primary application area are audio tasks on microcontrollers,
they should be widely applicable to efficient neural networks in other "edge" scenarios
such as larger embedded systems, mobile phone and web-browser applications.


