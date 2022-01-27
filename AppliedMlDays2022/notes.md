
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
