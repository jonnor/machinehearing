
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


## What we solve for Commercial Real estate

Preventive maintenance is costly
Issues may go undetected for long time, if no tenants


## Challenges


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


### Input is high frequency, underlying conditions slow

Must aggregate data in time to features of relevance to machine condition
From 1-100 kHz to 0.01 Hz (minutes).
Want to detect issues well within the hour.
Ensure no impact on tenants.
For gradual changes, wear and tear, talking about months.

Responses

- On-edge processing
Spectrogram computing
- Learned downsampling using time-series models
Representation learning
- Statistical aggregation methods

### Decisions are rarely clear cut

Responses

- Cost-sensitive 


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

## Edge AI in wireless network architectures


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

### Edge inference

- Embeddings. Vector representations
Base for further logics

### Edge learning

Single unit. Online learning.
Jointly. Federated learning.


### Edge processing
Preprocessing
Machine Learning in the cloud.
Inference in the cloud.


### Edge constraints
Unit costs.
- Hardware. Little compute
- Installation. Wireless. Battery-powered
- 
Running costs.
- Data transfer. Little data as possible
- Maintenance. No movable parts.

- Data transport
- Energy usage
- Storage capacity
- Memory capacity
- Processing capacity
- Updateability


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
