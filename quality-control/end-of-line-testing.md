
# End of line testing

Sound can be used to check whether produced mechanical units operate as they should.
This is a type of quality control method, and might be deployed as part of end-of-line test.

## Question
These questions was originally posed on the Sound of AI Slack.
I have tried to synthesize the key part of the questions and some answers here.

#### Questions

1.
Is it "easy" to implement the project into a computer that then only evaluates the devices?
Since it would need to stand like at the end of the production line and analyze many devices.
How do I do that?
How do I get it to that point where I can use the project that it runs automatically and that it can just be used like an autonomous device tester should?

3. 
I‘m currently recording my own machines sound to put it as a dataset into the dcase project!
I‘m not exactly what to be careful about though.
Like should I keep it at the same place as long as most of the sound comes from that place?
I could later arrange the microphone to be stated in the same way after
I finished the project and the Machines need to be tested, so that’s not a problem for me at all,
I was just curious whether it would be more efficient to train the model somehow when I place the mic in other places as well.

4.
Should I train the model with different kind of speeds of the machine?
I mean I can turn the motor on different levels and stuff?
From how I see the other data files from the datasets that are provided within the dcase project,
it seems that they named the files „something_vel_4_loc_A“ for example in which they rotate through all (locations?) A to H and all (Velocities?) 4 -> 8 -> 12 -> 16

5.
They also differ normal sounds and anomalous sounds, but I actually wanted to create a model which would be trained upon mostly normal sounds, since I don’t have an anomalous device :/ Is it not possible to do that without having anomalous sounds?


These are pretty large questions. I will try to address them briefly.

#### Labeled abnormal cases are critical for quantifying performance

5. The DCASE baseline models are trained only on normal sounds.
BUT - in order to measure performance (evaluate your model) you will need at least some data that is labeled.
Otherwise, it is impossible to quantify how well your method works!
So you really should make sure to get some known cases of abnormal vs normal samples.
Preferably realistic ones. Or synthesized in a realistic/representative way, if this is not feasible. As low as 10 or 100 samples will be useful.
If this is a collaboration project - tell those responsible for the data that you NEED this.


#### Planning an end-of-line acoustic quality testing project

1. "easy"? No. That is not a word I would use. Doable, yes - given sufficient time.
Making a useful model for anomaly detection for a real-world problem is alone quite challenging. Especially considering you have to capture your own data.
Deploying a model that has been shown to work on collected into production is also challenging.
This holds in general for ML works - dealing with hardware is an added complexity in this project - as is the possible contamination of data from the acoustic environment that the system is deployed in.

If you are to plan such a project.
Then I would allocate 40% of the resources to building good datasets (incl procedures and tooling for this).
10% to the model development.
And 50% to deploying.
Plan for at least 3 complete iterations of this entire loop.

#### Data collection strategy
3/4 this would require a few chapters of a few different books to fully answer... And I unfortunately do not have any good references at hand.
The fundamental principle however, is that your data used for training/validation/test must be representative of your deployment scenario.
This implies A) ensuring that all the natural variability of the data is in the dataset, and B) that there are no kinds of variability in the dataset.
Important activities to do early is to map out what "axes of variability" exists. What things can vary (and not) in your case - and what is the range. You can get a good start by doing a brainstorming exercise. But very quickly you should capture a little bit of data and do some Exploratory Data Analysis to really start fleshing it out

To ensure feasibility, you want to eliminate as many factors of unnecessary variability as possible. In acoustics, this primarily means doing a very controlled recording setup, trying to eliminate ambient noise as much as possible

And to maximize the system ability to detect problems, you would maximize the variability along the axes of interest. If the unit-under-test has multiple possible configurations, then do those in a controlled/repeatable fashion.

#### Variabilty in acoustic data
Some inspiration for the variability brainstorming for acoustical problems.
You should consider each of these major areas and dig all the way into the nitty gritty of your exact problems.

```
## Source factors.
What is the span of normal sounds from the unit-under-test.
What are the possible failure modes, and how do they manifest in terms of sound.
## Ambient noise factors
What other sources of sound exist in the measurement environment, and what kind of sounds do they make?
## Recording factors.
Microphone used.
ADC/recorder used, incl settings.
Position relative to source of interest and to ambient noise sources.
## Environmental factors
How would these things play in? On either source, ambient or recording. Temperature. Humidity, etc
```

