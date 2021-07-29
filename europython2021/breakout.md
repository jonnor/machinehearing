
Notes from breakout sessions.
Questions/answers after the talk.

olle nordesjo
Hi Jon Nordby, awesome talk! I'm very interested in the semi-automatic labelling/annotation for this type of data. Have you tried any other methods than the GMMHMM method you showed?Jon Nordby
When we capture datasets ourselves, we try to "Design for Labeling". For example we will put one sensor right next on known sound sources, and then transfer the labels from that onto the sensor positions we are actually interested in. But this is only feasible when controlling the data capture part
For annotating existing audio one can use a general clustering model, like DBSCAN. This could use as input some audio embedding vectors, extracted with pretrained neural nets like OpenL3 / YAMNet etc. These have rather large windows though, 1 seconds typical. So one might want to do a post-processing pass to better time-align the labels.
Few-shot event detection can be used to build a custom classifier, which can be done interactively. Justin Salamon has done some work on this at Adobe
https://www.youtube.com/watch?v=ebAlnW3Xs2k&t=1s
https://www.justinsalamon.com/news/few-shot-sound-event-detection
Before you continue to YouTube
Sign in a Google company Before you continue to YouTube Google uses cookies and data to: Deliver and maintain services, like tracking outages and protecting against spam, fraud, and abuse Measure audience engagement and site statistics to understand how our services are used
Few-Shot Sound Event Detection
 - Justin Salamon
Machine listening research, code, data & hacks!
*custom classifier that one uses for labeling
Jon Nordby
And also from a practical perspective, the use of Weak labeling (not precise in number of events or timestamps), is a major reduction in label annotation requirements.
The best starting point for that right now is probably Qiuqiang Kong PhD thesis and related publications
https://openresearch.surrey.ac.uk/esploro/outputs/doctoral/Sound-event-detection-with-weakly-labelled-data/99514413602346
olle nordesjo: see above for some approaches!olle nordesjo
Jon Nordby: That is super handy! Thanks, I'll look through those resources. Have you used things like pigeon/pigeonXT for polishing the uncertain classes at all? Or any other method of taking action on weird annotations?Jon Nordby
Have not seen pigeon before, looks like a neat tool! Integrating into Jupyter is nice. We have some internal tools that we use for labeling, but not a lot of smarts there yet. It is web based though, which makes it super quick to bring up without any installation. I am looking at something like Dash to try to merge the Jupyter world and enabling some smarts, while keeping the web accessibility  
olle nordesjo
Ah yes, that sounds like a solid idea. For 1d data I've been having some success with "ruptures" (on pypi), followed by pigeon to manually group the things I need, but I'm not sure it would work that easily on spectrograms
Jon Nordby
Yeah change point detection usually work mostly with very low dimensionality data. But time-series / temporal segmentation models are often multi-variate, and can be used similarly. There are actually some in librosa, but I have not yet had time to try them, or have seen much other uses of it. Practical ML labeling is unfortunately understudied, or at least underpublished, compared to ML models
Using UMAP on an audio embedding one can often get things down into 2-10 dimensions though, which may work well with change point detection.
olle nordesjo
Yes! I've noticed the same thing. Would be very glad to see someone giving similar amount of effort to audio labelling as people have done for image labelling. Again, thanks for great talk!

