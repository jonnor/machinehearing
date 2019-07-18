
# Collecting datasets for Machine Learning

Most tutorials, workshops and presentations on Machine Learning start with
a well defined task and pre-existing clean and annotated dataset.
But in order to machine learning on a problem you care about,
you will likely need to create your own datasets.

So in this workshop we will we will create a new dataset,
including the problem formulation, data collection, data cleaning and annotation.
Will then use this dataset with pre-existing machine learning models.

To keep things manageable, we will focus on the task of
machine learning for audio classification.
However most of the practical considerations and techniques
should be applicable to many other domains in machine learning.

Participants should bring:

- Laptop. Windows|MacOS|Linux
- Smartphone with working microphone. Android|iOS

Beneficial to have basic understanding of machine learning.

## Goal

Learn to 

## Learning objectives


## Topics

Structure of a machine learning dataset.
Training/validation/test splits.
Steps of building a dataset.


How much data do we need?
Statistical validity.
100x of each.
Depends on problem difficulty.
Number of classes.
Intra-class variation.
Inter-class variation.
Deep learning. Can be 100k samples needed.

Tricks for dealing with low amounts of data.
Estimating using a learning curve.

Problem definition.
Single-label versus multi-label
Closed set classification versus open-ended
Taxonomy. How to define the classes.
Coarseness. Hiearchies.
Look at existing taxonomies. In existing datasets.
AudioSet.

What is a reasonable performance target?

Is there actually consensus?
Do multiple experts agree?
Does the same expert agree with him/herself?

Label quality.
Dealing with label noise.
Annotation metadata.
Annotator. When annotated.
Prominence/salience/difficulty background/foreground.

Weak labels.
Strong labels.

Where to get data?

- Collect manually
- Autonomous sensors.
- Online repositories.
APIs. Scraping.
NB: Licensing
- Crowdsourcing. Remote workers.
- Designing into product

Bias
Is the data in training representative of real inputs to system?

Concept drift.
Feedback loops.




## Organization

Brainstorm.
What can, and would we like to classify.

9-15 participants.
2-3 groups a 3-5 people.
Each group decides their own problem to tackle,
and how to collect data.
Need to plan the data collection process.

All participants put raw data into 'data lake' (per group/task).
Should keep some nodes.

Participants load up raw data.
Annotate. Audacity
Split into fixed-size pieces.


## Ideas
- Adversarial testsets.
Have participants from outside the team also collect data to test generalization with.

## TODO
- Test Audacity on Windows
- Test Audacity on MacOS
- Test audio recording on Android phone
- Test audio recording on iOS phone
- Decide data lake transfer

## Challenge
Internet/network connectivity for collaboration on data.
Needs to be good.
What are the fallbacks?

Time required to actually collect and prepare.
