
# Edge AI track



## Title
Machine Health Monitoring using acoustic sensing at the edge

## Abstract
Machines are a key part of the infrastructure that powers modern life.
From the pumps that gives us fresh water in the tap,
to transformers that distributes electricity,
and the ventilation systems that keeps our buildings airy and cool.
Millions of such machines exist, and they should all operate consistently without faults.
Monitoring the health of the machines continiously can be done using sensors,
detecting anomalies and triggering alarms - preferably before downtime occurs.
Soundsensing has developed sound and vibration sensors that use Machine Learning to perform this task.
Edge processing enables this to be done while maintaining privacy,
and keeping the amount of data transfer and storage down.
In this talk we will share some of the problems we are working on,
challenges we face and solutions that we came up with. 

## Format

11:35 - 12:10
30 minutes + Q&A

## Goals

Attract customers/partners outside of Nordics.

## Call to action


## Outline

Introduction
- Who we are
- What we do

- Challenges
- System architecture


## 

## What we solve for Commercial Real estate

Preventive maintenance is costly
Issues may go undetected for long time, if no tenants

##



## Machine Failure types


## Time variations

Building usage, weather, building operations

Daily       Workday start - end
Weekly      Workday vs weekend
Yearly      Weather

Building operations is becoming increasingly more dynamic
Driven primarily by energy optimization 

## System Architecture

db20
- Sensor with 4G built-in
- Powered by 12/24V
-  

- Wireless sensors with BLE/LoRa
- Gateway with Ethernet/4G


## Lack of ground thruth

## Anomaly Detection
How it differs from (binary) classification

## Training pipeline

For Anomaly Detection

Run on a fixed interval. Ex: 1 per day

Take historical data. Ex: 30 days
Excluding time-period marked as anomalous. Incidents, maintenance et.c
Train on this as normal data
Any deviations from it consider anomalous

Store this model.
Use to make predictions until next model is built.



## Monitoring: input statistics


## Monitoring: output statistics


## Monitoring: shadow-models



## Only send data when device is on

Ventilation systems are often turned off at night, and in weekends
Up to 50% saving possible

Some pumps only run for a few minutes now and then
Up to 99% saving possible 

High-state / low-state

Threshold enter / leave
Soundlevel
Minimum time in state
Maximum time in state

Different sampling/processing configuration per state


## Edge preprocessing for order tracking

Rotation frequency finding

Peak finding in spectrum
For vibration monitoring
1x, 2x

## 

## Edge Learning Anomaly Detection

Representation learning using Convolutional Neural Network
Generic for all devices

Needs to be efficient and robust
kNN
ESP32 modules exist with 8MB PSRAM


Spectrogram 128ms 30b with compression around 3000 bytes
>>> 43200*3000/1e6
129.6 MB


8e6/(43200)
185 bytes per 1 minute


Can be read in around 1 second.
Up to 16 MB/sec EasyDMA read rate
https://infocenter.nordicsemi.com/index.jsp?topic=%2Fps_nrf52840%2Fqspi.html
Up to 20 MB/s sustained
https://www.esp32.com/viewtopic.php?t=16131

Maximal standby current of ESP-PSRAM32 is 50 uA

D-cell, or 2x C cell
18-20Ah

>>> 19000/(365*24*5)
0.45662100456621

400 uA total budget
100 uA radio
200 uA microphone
100 uA processing <- too little

100% does not seem feasible right now
10% duty cycle however should be well within 

BLE NRF51
advertizing interval 1000ms 	27.5uA 

Low-power MEMS microphone 185 uA
Continious sampling not really possible with 5+ years of battery life



TDK T5828, 95uA
ST IMP23ABSU, 150 uA 

https://devzone.nordicsemi.com/f/nordic-q-a/19208/nrf52-microphone-saadc-pdm-or-i2s
700 uA to 1400 uA for analog/PDM

1-10 second per 1 minute
1.6%-16% duty cycle
2-20 MB per month, compressed

5 second window, 5*8 frames
40 messages per 1 minute, 30 bytes each
< 1 message per 1 second
Around 50 uA average expected

Might hit 100 uA total, and 5 years


BLE 4.0-4.2 advertizing package. Limited to 37-8= 29 bytes
Scan response would have extra 31 data bytes available.
BLE 5.0. Enables 255 bytes for single packet
A chain can hold a maximum of 1650 bytes

Because older devices that don’t support Bluetooth 5 will not be able to discover extended advertisements,
an advertising set with legacy advertising PDUs for older scanning devices should also be used,
at least until Bluetooth 5 supported hardware is commonplace in the market.


about iBeacons only using advertisements
The reason connections are not allowed is that if the Beacons were to establish a connection,
advertisements would have to stop, so no other device could find the beacon.

## Challenges

### Input is high frequency, underlying conditions slow

Must aggregate data in time to features of relevance to machine condition
From 1-100 kHz to 0.01 Hz (minutes).
Want to detect issues well within the hour.
Ensure no impact on tenants.
For gradual changes, wear and tear, talking about months.

Natural seasonalities across day and week and year.

Responses

- On-edge processing
Spectrogram computing
- Learned downsampling using time-series models
Representation learning
- Statistical aggregation methods

### Anomalies are rare

Each piece of equipment may only fail every few years.
Sometimes at end of life or in start, can have higher rates.
Failures are often novel in nature.
Severe class imbalance.
Lack of labeled data for supervised learning.
False Positives must be very seldom

Responses

- Synthetic introduction of anomalies
- Real physical mock systems, introducing
- Composing recorded anomaly events into real data-streams

### Normal data is highly variable and complex
Operating condition variations.
Timers. Regulation loops. Bang-bang and gradual.
Based on environmental conditons, weather outdoors.
Based on building usage. Use of meeting rooms. Doors open. Use of water.
CO2 monitoring.
Pressure monitoring.
Airflow monitoring.

Getting increasingly more complex! Why? Energy savings.
Old-school buildings

Responses

- Sensor data collection from real-world buildings and tech-rooms 
Already have 100'000 hours
- Using related information
Data about the equipment types, operating schedules
Data from machine control system
Using during Exploratory Data Analysis, and Error Analysis.
Using as labels for supervised learning tasks.

### Decisions are not always clear cut


Responses

- Cost-sensitive learning
-  


## Edge AI in wireless network architectures

### Edge constraints

Unit costs.
- Hardware. Little compute
- Installation. Wireless. Battery-powered
- 

Running costs.
- Data transfer. Little data as possible
- Maintenance. No movable parts.

Aspects
- Data transport
- Energy usage
- Storage capacity
- Memory capacity
- Processing capacity
- Updateability

### Edge processing

Preprocessing
Machine Learning in the cloud.
Inference in the cloud.

A must have to support.

### Edge inference

Model learned in the cloud, and then pushed to device.
For example at a daily rate.
Can be general, or device-specific.

### Device-specific

Challenge: Training needs the input data, must be sent to cloud. 
Need to subsample a lot for device-specific learning,
tradeoff between edge processing gains and training accuracy.
But sometimes the data-stream has a lot of repetition.

Can use a local novelty estimator.
Send novel data-samples primarily.
Otherwise just some random/periodically subsampled.
Introduces bias, needs to be managed carefully.

Dynamic transmit amounts. Harder to estimate battery life.
Can have a fixed budget, use novelty as a prioritization scheme.

### Generic

Learned feature transformations.
Embeddings. Compact vector representations

Representation learning.
Model trained and shared across all devices for example.
Or even "all" data for a given sensor modality.
Ie model pretrained on AudioSet for audio 



### Edge learning

Single unit. Online learning.
Need to ensure robustness.
Solid feature pre-processing pipeline.
Down to a few well-known metrics.
Using simple,robust learners.


Jointly. Federated learning.


### Edge storage

Store collected (raw) data distributed at the edge.

Characteristics:

- Only sends the most important events/metadata 
- Raw/richer data stored on disk on edge
- Rolling buffer, keeping the last N days or last M GB of data.
- Raw/rich data can be fetched/uploaded on-demand

Advantages:

- Storage grows automatically with number of sensor nodes in system
- Allows access to raw data when needed
- Do not have to pay for data transfer for raw data "just in case"

Challenges:

- Limited lifetime of affordable storage 
- Storage also takes considerable energy
Though normally considerably less than transmit?
- Connectivity of edge device may be intermittent

Opportunities:

- Indexing the edge data using neural network representation learning
Allow querying the edge data using Approximate Nearest Neighbours / Locality Sensitive Hashing
Could optionally send the index information across to server. Allows querying without needing edge device in the loop. Can fetch more information on-demand 


## Requirements for Edge AI

- ML model monitoring.
Models are now training themselves, automatically.
Need to automate the quality control.
Tracking input/output statistics. 

- Automated device updates.
Model or firmware. Firmware-over-the-air (FOTA)
For cloud models especially.



## Digital tranformation of machine maintenance in commercial real-estate

Introducing reliability engineering to technical maintenance of buildings
This is a transformation of a whole industry.
Success requires a whole industry to complete it.

Condition Based Maintenance
Condition Monitoring
Preventive Maintenance
Usage-based Maintenance
Preventive Maintenance

Requires not just tools, but also improved processes, skills

Success requires organization wide effort.

- Making reliability as priority. Organizational, leadership
- Defining and monitoring KPIs.
- Processes and tools for measuring KPI and related indicators
    Condition Monitoring of machines
    Monitoring of conditions in building
    Taking input from tenants
- Processes for driving improvements. Quality Management
- Hiring people with right skills, aptitudes and attitudes
- Up-skilling existing people
- Documenting Quality. Standards and certifications, marketing


Educational. Universities. Vocationary training.
Consultancies. Organizational transformation. 
Equipment manufacturers.
Proptech vendors.
Certification. ISO9000, BREAM

What other actors are pulling in this direction now?

How can existin actors be activated to facilitate the transformation?

How can Soundsensing be a key player, and driver in this transformation?


People to talk to

- Kuben yrkesfag lærere. James,Torbjorn
- ESSO Slagentangen. Via Eli
- SINTEF. Intro via akustikk
- NTNU. Intro via Trym?
- Org transformation companies. Intro via TRK?

## Reliability Engineering

Mean Time Before Failure (MTBF)
Mean Time Between Failures (MTBF) 
Mean time between system aborts (MTBSA)
Mean time between critical failures (MTBCF)
Mean time between unscheduled removal (MTBUR)

MTBF isn't meant to predict the behavior of a single component; it predicts the behavior of a group of components


ANSI centrifugal pump
The average ANSI pump MTBF is 2.5 years,
with a realistic average target of 3.75 years, and excellent target of 4.5 years.
A MTBF of 1.5 to 2.0 years would be considered poor performance.

https://www.efficientplantmag.com/2008/10/pump-statistics-should-shape-strategies/


Failure rate.
Order of magnitude.
1000 tech rooms, 1 per day.
0.001 per day per room
Annualized failure rate – Probability that a device or component will fail during a year of use

Bathtub curve
https://en.wikipedia.org/wiki/Bathtub_curve
Early-failure. Decrease over time.
Random failure. Constant over time.
Wear-out failure. Increase over time.
Weibull chart analysis

Downtime
Mean Time To Repair (MTTR)

Iterative process

- Detect issue
- Diagnose issue
- Plan fix
- Order. Parts and personell
- Repair

Back into monitoring again.


## Relevant tracks

https://appliedmldays.org/events/amld-epfl-2022/tracks/edge-ai
https://appliedmldays.org/events/amld-epfl-2022/tracks/ai-engineering
https://appliedmldays.org/events/amld-epfl-2022/tracks/ai-physics
https://appliedmldays.org/events/amld-epfl-2022/tracks/ai-manufacturing
https://appliedmldays.org/events/amld-epfl-2022/tracks/ai-industry
https://appliedmldays.org/events/amld-epfl-2022/tracks/methods-for-generating-realistic-synthetic-data
https://appliedmldays.org/events/amld-epfl-2022/tracks/the-data-ai-maturity-journey

## Interesting workshops

https://appliedmldays.org/events/amld-epfl-2022/workshops/designing-effective-visualisations-to-communicate-data-stories
https://appliedmldays.org/events/amld-epfl-2022/workshops/unpacking-the-black-box-how-to-interpret-your-machine-learning-model

## Previous talks

AMLD2018 - Christopher Bishop, Microsoft Research: Model Based Machine Learning
https://www.youtube.com/watch?v=7T2_hkKaB5I

Derive the appropriate AI algorithm
by making modelling assumptions explicit

https://www.mbmlbook.com/toc.html
