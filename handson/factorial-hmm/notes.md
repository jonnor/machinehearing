
## Factorial Hidden Markov Model

Also called a Fractorial HMM or FHMM.

An FHMM has M independent Markov chains of latent variables,
each of which can be in K states.
In general the time and space complexity for a HMM is quadratic in the number of states.
For a factorial HMM, the number of states is exponential in the number of latent Markov chains.
A naive implementation of exact Factorial HMM has computational complexity $𝑂({TK^{2M}})$ .
But using the independence of the hidden chains in the factorial HMM reduce complexity to $𝑂({TMK^{M+1}})$
(Ghahramani and Jordan, 1997).
However this is still exponential in the number of chains, which may limit it to low numbers.
For higher number of chains, approximate or variational approaches may be needed.

### Energy load disaggregation

Also known as Electricity disaggregation, or Non-Intrusive Load Monitoring (NILM). 

Is frequently done using a Additive Factorial Hidden Markov Model.
In each state, the appliance consumes a power which can be modeled by a normal distribution with mean μ and small variance σ.
The number of states is often just 2, ON or OFF.

- [NILMTK: Non-Intrusive Load Monitoring Toolkit](https://github.com/nilmtk/nilmtk).
Contains dataset parsers, evaluation tools and baseline models with a standardized API. 
! not installable from PyPi
! setup.py has very specific dependencies on matplotlib,pandas,networkx etc
- [Torch-NILM](https://github.com/Virtsionis/torch-nilm).
Contains tools to evaluate neural NILMs in PyTorch. Also contains a set of strong baseline models.
Compatible with NILMTK.
! not installable from PyPi 
! no setup.py file available
- [Tutorial on implementing Additive Factorial HMM in Python](https://nbviewer.org/github/nilmtk/nilmtk/blob/v0.1.0/notebooks/fhmm.ipynb). By Nipun Batra, part of nimlmtk.
- [Python implementation by Nelli Gofman](https://github.com/pipette/Electricity-load-disaggregation).
Has its own implementation of the Fractorial HMM, using a naive strategy.
Testing on UK-DALE dataset.
- [nilm-eval FHMM](https://github.com/beckel/nilm-eval/blob/master/Python/fhmm.py).
Based on tutorial by Nipun Batra.
! not updated since 2015. Uses sklearn.hmm, which was made into hmmlearn a log time ago
- [wikienergy tutorial on FHMM in Python](https://github.com/dssg/wikienergy/blob/master/docs/tutorials/FHMM_Tutorial.ipynb)
!not updated since 2016


https://github.com/nilmtk/nilmtk-contrib/blob/master/nilmtk_contrib/disaggregate/


##

Trying out disaggregators from nilmtk

pip install git+https://github.com/nilmtk/nilm_metadata
pip install git+https://github.com/jonnor/nilmtk
pip install git+https://github.com/jonnor/nilmtk-contrib


