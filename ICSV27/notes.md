
# Title
Automatic Detection Of Noise Events at Shooting Range Using Machine Learning

# Abstract

Outdoor shooting ranges are subject to noise regulations from local and national authorities.
Restric-tions found in these regulations may include limits on times of activities, the overall number of noise events,
as well as limits on number of events depending on the class of noise or activity. 
A noise monitoring system may be used to track overall sound levels,  but rarely provide the ability to de-tect activity or count the number of events, required to compare directly with such regulations.
This work investigates the feasibility and performance of an automatic detection system to count noiseevents. 
An empirical evaluation was done by collecting data at a newly constructed shooting rangeand training facility.
The data includes tests of multiple weapon configurations from small firearmsto high caliber rifles and explosives, at multiple source positions, and collected on multiple differentdays.
Several alternative machine learning models are tested, using as inputs time-series of standardacoustic indicators such as A-weighted sound levels and 1/3 octave spectrogram, and classifiers suchas Logistic Regression and Convolutional Neural Networks. Performance for the various alternativesare reported in terms of the False Positive Rate and False Negative Rate. The detection performancewas found to be satisfactory for use in automatic logging of time-periods with training activity.

## Format

Maximum 12 minutes
Approx 10-12 slides

## Outline

- Introduction
Name, position
Co-authors.
Fabian Nemazi
Dag Rieber

Soundsensing collaboration with Politiets Nasjonale Beredskapsenter (PNB)

- Acknowledgements

Work has been funded though a collaboration between Soundsensing AS and Politiets Nasjonale Beredskapsenter construction project,
led by Paul Torgersen at Marstrand.
In the first months of the project,
Soundsensing received funding from the Research Council of Norway as part of the program STUD-ENT.

Organization of acoustical tests was lead by Lars R. Nordin at Brekke & Strand AS.
Data collection for Soundsensing AS was performed by
Erik Sjølund and Ole Johan Aspestrand Bjerke. 


- Background
Soundsensing, Noise Monitoring
PNB. Training facility. 1 km to neighbours
Police National Emergency Response Center

PICTURE. PNB

- Data collection

PICTURE. Recording locations

Testing whether one central sensor would be enough,
or whether need to have one sensor per area

- Synthetization of dataset

Salamon, et.al
Scaper: A library for soundscapesynthesis and augmentation,
IEEE Workshop on Applications of Signal Processing to Audioand Acoustics (WASPAA), 2017

Gontier et.al
An efficient audio coding schemefor quantitative and qualitative large scale acoustic monitoring using the sensor grid approach
MDPI Sensors, 2017

- RandomForest model

Split into short time-frames

PICTURE. Audio curve with annotated areas

- CNN model

- Results

It obtained an event-wise F1 score of 80.5%,
with a precision of 95.5% and recall of 69.6% (insertion error rate of 4.5% anddeletion error rate of 30.4%).



PICTURE. Precision-Recall curve, table

- Outcomes

PICTURE. Logbook

- Further work

Label noise

Determining the origin of impulsive noise events
using wireless sound sensors
Fabian Nemazi, 2021
