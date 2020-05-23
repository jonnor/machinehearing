## Anomaly Detection for IoT sensor data

## Brief
Anomaly Detection (AD) is the task of automatically identifying data that deviates from the normal,
so called abnormal or anomalous datapoints.
This talk will show how you can build Anomaly Detection system for time-series data
using Python and standard open-source machine learning libraries.

## Description
With Internet-of-Things (IoT) enabled sensors, data is continiously streaming in
and in many organizations the amount of data collected is increasing every year.
The data varies across the day, week and year, as well as due to fluctuations
in the environment and business practices.
Most of the time the data reflects that things are operating as normal.
However once in a while deviations occur that may be indicative of serious issues:
faulty equipment, unintended changes in business processes, tampering with sensors,
or intrusions in the network.
Anomaly Detection allows to automatically flag such cases for further investigation.

In this talk we will go through several different approaches,
from simple methods for small number of features,
to more powerful multi-variate methods.
Will also cover some practical considerations,
such as how to tune a system to minimize the impact of false positives.

We will focus on applications to sensor data and IoT systems,
but the techniques and approaches discussed can be applied generally
to any other kind of time-series data.

Practical demonstrations on open datasets will be shown,
with code examples in Python.
We will be using the common machine learning libraries
scikit-learn, Keras and TensorFlow.
