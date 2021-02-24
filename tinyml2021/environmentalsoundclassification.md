
# Environmental Noise Classification on microcontrollers

## Proposal abstract

Noise is a growing problem in urban areas, and according to the WHO is the second environmental cause of health problems in Europe.
Noise monitoring using Wireless Sensor Networks are being applied in order to understand and help mitigate these noise problems.
It is desirable that these sensor systems, in addition to logging the sound level, can indicate what the likely sound source is.
Performing such Environmental Noise Classification directly in the sensor is desirable in order to
avoid sending audio data to the cloud, which may have negative impacts on data transfer amounts, battery lifetime and privacy.
 
In this talk we will explain how we tested several different
Convolutional Neural Networks for this task on the STM32L476 low-power microcontroller,
and the results we were able to achieve on the Urbansound8k dataset.
Several techniques such Depthwise-Separable convolutions, striding for downsampling, reducing input dimensionality was
tested in order to make the CNN models as efficient as possible,
and these will likely be useful also for other audio or image tasks.

The research was initially carried out as part of a master thesis at the Norwegian University of Life Sciences (NMBU).
Since then we have continued to work on this topic at Soundsensing,
and we will share some of the progress and challenges in bringing this kind of research to market.

## Call-to-Action

Want to test out Machine Learning for Noise Monitoring?
Be it in cities, residential areas, offices, or factory floors.
Order the Soundsensing dB20 devkit,
and join our pilot program for Noise Classification.


## Has talk been given before
Kind-of yes, kind of no. EuroPython 2019. But very little focus on optimization/microcontroller
https://www.youtube.com/watch?v=uCGROOUO_wY
