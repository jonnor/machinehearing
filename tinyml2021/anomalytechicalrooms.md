# Acoustic Condition Monitoring using Anomaly Detection on microcontroller

## Talk proposal

The operation of practically any facility relies heavily on correctly functioning technical equipment.
In any office building, machines are running continiously to ensure that occupants have what they need:
electricity, water, air circulation, cooling and heating.
The goal of a facility manager is to ensure that occupants never experience disruption in these services,
which means being able to detect and mitigate potential issues before they become a problem.

Using sound-based sensors for monitoring such systems is attractive because they are
non-invasive, can be retrofitted easily, and can monitor multiple co-located machines.
Depending on the machinery in question they can be an alternative or compliment to
built-in machine monitoring, or other monitoring systems based on image, vibration, power or air quality analysis. 

In this presentation we will report on a case-study and proof-of-concept
that Soundsensing has performed together with a real-estate and facility management company.
Audio data was collected from an equipment room over a few weeks,
and an Anomaly Detection model developed that could fit on our microcontroller based hardware.
Then the system was tested by injecting anomalous sounds.
We will cover the results of the study and future plans for larger-scale testing and rollout.

Soundsensing is a leader in acoustic monitoring using Machine Learning.
Their IoT sensors are used to monitor noise levels in workplaces and cities,
and to monitor the condition of machines and processes in manufacturing and real-estate.

## Call-to-Action

Working in real-estate or other industry with noisy machinery such as pumps, fans, transformers etc?
Join our list of companies interested in pilot-testing Soundsensing for condition monitoring!

## Notes

If an issue is detected too late,
it can often take a lot of time to fix, be costly
- and negatively affect customer relationship with occupant.

While such system increasingly has built-in monitoring
a lot of monitoring is done by human inspection.
Costing a lot.
But also missing problems due to inspections not being regular enough, or issues overlooked

Based on baseline method from DCASE2020 challenge
Also used in TinyMLPerf benchmark
https://github.com/mlperf/tiny/
https://github.com/cskiraly/dcase2020_task2_baseline

Collected sound from technical room over a few days.
Synthetically injected anomalous sounds at different signal-to-noise ratios.
Able to detect

