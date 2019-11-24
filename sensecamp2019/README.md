
# Context

https://forcetechnology.com/en/events/2019/sensecamp-2019
"Opportunities with Machine Learning in audio”


09.45 - 10.25 	Deep audio - data, representations and interactivity
Lars Kai Hansen, Professor, DTU Compute - Technical University of Denmark
10.25 - 11.05 	On applying AI/ML in Audiology/Hearing aids
Jens Brehm Bagger Nielsen, Architect, Machine Learning & Data Science, Widex
11.05 - 11.45 	Data-driven services in hearing health care
Niels H. Pontoppidan, Research Area Manager, Augmented Hearing Science - Eriksholm Research Center


## Format

30 minutes, 10 minutes QA

# TODO

- Add some Research Projects at the end

Pretty

- Add Soundsensing logo to frontpage
- Add Soundsensing logo to ending page
- Add Soundensing logo at bottom of each page


# Goals

From our POV

1. Attract partners for Soundsensing
Research institutes. Public or private.
Joint technology development?
2. Attract pilot projects for Soundsensing
(3. Attract contacts for consulting on ML+audio+embedded )

From audience POV

> you as audio proffesionals, understand:
>
> possibilities of on-sensor ML
> 
> how Soundsensing applies this to Noise Monitoring

> basics of machine learning for audio
 


## Partnerships

Research

What do we want to get out of a partnership?
How can someone be of benefit to us?

- Provide funding from their existing R&D project budgets
- Provide resources (students etc) to work on our challenges
- Help secure funding in joint project



## Calls to action

1-2 Data Science students in Spring 2020.

Looking for pilot projects for Autumn 2020 (or maybe spring).

Interested in machine learning (for audio) on embedded devices?
Come talk to me!
Send email. <jon@soundsensing.no>


## Title
Classification of environmental sound using IoT sensors


## Audience

Audio practitioners. Many technical, some management.

- Familiar with Sound.
Audio aquisition, Sampling rate, Frequency spectrum, Spectrograms
- Not familiar with Machine Learning
Supervised learning. Convolutional Neural Networks.
- Not familiar with Internet of THings

## Scope

Style.
Less training/tutorial/howto compared to EuroPython/PyCode
More Research&Development oriented.
More Soundsensing focused.



# Outline

Introduction

- About me
- About Soundsensing
- Noise Monitoring
- Thesis

- Environmental Sound Classification
- Wireless sensor network contraints. IoT
- On-edge classification
- Future sneakpeak: Neural accelerators for HW


- Existing ESC work
- SB-CNN model
- Typical Audio classification pipeline
- Performance vs compute landscape


- How to get this to fit on a small device?
Limiting input size
Depthwise Convolutions

Tricks

- Unknown class
- Merging to more high-level classes
- Mapping over longer times

## Out of scope

On-edge challenges

## Q

Availability of

- Low-power microcontroller. ARM Cortex M4F
- FPGA.
- ASIC.

ST Orlando

Cortex-M4 microcontroller (MCU) and 128 KB of memory
6.2 mm x 5.5 mm die
200 Mhz
41 mWatt
2.9 TOPS/W
AlexNet at 10 FPS. 


Microphone becomes the bottleneck.

Vesper VM1010
Wake on Sound
18 uWatt

PUI Audio PMM-3738-VM1010
Wake on Sound
9 μW of power

https://www.digikey.com/en/product-highlight/p/pui-audio/wake-on-sound-piezoelectric-mems-microphone


https://blog.st.com/orlando-neural-network-iot/


What is the TOPS/watt for current Cortex M4F?
How does it compare with proposed milli-watt scale accelerators


Lattice sensAI stack
FPGA
1 mW-1W

https://www.latticesemi.com/Blog/2019/05/17/18/25/sensAI

Human presence detection. 5 FPS 64x64x3. 7 mW
VGG8. 8 layer CNN.

Lattice ICE40 UltraPlus CNN accelerator IP
http://www.latticesemi.com/Products/DesignSoftwareAndIP/IntellectualProperty/IPCore/IPCores04/compactcnn

TensorFlow Lite for microcontrollers
https://www.tensorflow.org/lite/microcontrollers

STM32Cube.AI
STM32 X-CUBE-AI
https://www.st.com/en/embedded-software/x-cube-ai.html


emlearn





## Takeaways
Or talking points...

- ML on audio close to human-level performance on some tasks
(when not compute constrainted)

- On-edge inference is desirable to keep data traffic down.
Enable battery power / energy harvesting - cheaper installation costs - denser networks.
Lower data traffic - cheaper wireless costs.

- ML-accelerators for low-power sensor units are expected in 2020

- Soundsensing has developed a low-power sensor unit for Noise Monitoring.
- We are running pilot projects now.

- Strong cross pollination from bigger ML domains.
Image and Natural Language Processing pushes Audio forward
CNNs. Sequence modelling (RNNs).
