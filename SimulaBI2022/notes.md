
# Goals

- Recruit students
State in the introduction, and in outro

# Format

Rundt 30 min.
Høres det bra ut? Det er litt vanskelig å si hvor aktiv klassen kommer til å være, men forhåpentligvis blir det en bra diskusjon.

Spørsmål jeg tenker er er viktige går i retning av hva slags beslutninger man må ta fra både
businessperspektiv
og AI-perspektiv
når man skal løse utfordringen man står overfor.

Jeg tenkte også at jeg kunne stille noen spørsmål etter du presentere for å kanskje innlede en liten diskusjon.

# Audience

Studentene er ikke veldig tekniske.
Kanskje litt fokus på usecase er bra,
og også litt om hvordan å ta i bruk AI/maskinlæring i en startup.


# TODO

- Finish disposition of slides

*** Time-series of real rooms
Soundlevels. Pumps, ventilation


# Main takeaways

- Technical maintenance in commercial buildings still done in a very
on-site, labor-intensive, ad-hoc way

- Soundsensing is delivering Conditioning Modern to use IoT to modernize technical maintenance of machines
Plan to reach millions of buildings world-wide

- We are working in practice now.
Developing together with our customer in pilot projects
Decided to go for this market segment in October.
Have installed sensors since November.
Have 5 paying customers

- We need skilled and motivated people to join us


# Disposition

30 minutes total
20 minutes slides.
10 minutes questions.

20-30 slides

The company

The usecase
    Commercial buildings. What is that?
    Maintenance in CB today
Condition Monitoring
    How can Machine Learning help?


- Commercial Buildings
What are they
The different actors. Owner, building manager, facility manager, tenant
What is important
- Technical Maintenance (of buildings)
Driftsansvarlig bygg. Vaktmestere. Teknikere.
- Maintenance strategies
Breakdown maintenance
Preventive maintenance.
Time-based maintenance (TbM)
Usage-based Maintenance (UbM)
Predictive Maintenance
- Condition-Based Maintenance (CbM)
Temperature,Sound,vibration
Examples
- Machine Learning for CBM
Supervised learning approach
Lack of labeled data
Unsupervised Anomaly Detection
Labeled validation/test sets

** Machine State Estimation. On/off, level
** Contextual Anomalies. Time schedule


Maybe

- Remote monitoring
SD systems

Failure Finding Maintenance (FFM)
Risk Based Maintenance (RBM)



## Talking points

- Even for a technology-driven data-intelligence provider,
majority of time is spent outside the ML analytics/modelling.
Primarily to get the *right* data in place.

Rely on IoT sensors for data gathering.
A lot of the data that would be valuable is currently unstructured, spread everywhere.
Failure modes, frequency, costs. Time to repair. Downtime consequences.
Emails, SMS/phonecalls
Invoices
Hard to get statistical significance

- Machines and operations are getting more complex
Energy recycling
Demand regulation instead of static schedules
Driven by stricter requirements on energy efficiency (and high costs of energy)
High expectations on quality and reliability

- Still long ways to go for "digitalization", "data driven" in operations of commercial real-estate
Use of "IoT", "Machine Learning" still quite early
"Proptech"
Buildings may be 10,30,50 years old. Maybe last major overhaul 20 years ago.
Myriad of different systems, vendors, protocols
Organizations may not even track their maintenance costs systematically.
Downtime, cost of repair/replacement


- Taking well-established practices from heavy-asset and high-reliability industries,
adapting it for use in commercial buildings


# Engagement

## Questions to audience

- Has anyone here experienced being at school and some part of the building did not work?
Maybe the heating was broken, and it was too cold? 
Or the air ventilation broke, and you got really tired?
How quickly was it fixed?

- Why do they put all the equipment into these small rooms?


Re ventilation system
- What are some things that could go wrong here?
Failure Mode Effect Analysis (FMEA) 


- Re breakdown maintenance.
Does this seem like a good strategy? What are the consequences?
What could be a better way to decide when to do maintenance?


- What are the problems with doing maintance not often enough?


- What are the problem with doing maintenance too often?


- Supervised vs unsupervised learning?
Labeled data versus non-labeled data. "ground truth"



## Where we are going

10 years
10 million buildings
Year 1.

Company like AirThings
Worth over 1 billion NOK

Be in "every" commercial building on the planet, in target segments.
Size, usage type

Transform the maintenance of commercial real-estate industry
Become data-driven organizations
Higher quality of service at the same costs
Lower environmental impact

## What we can offer

Interesting technical and practical challenges
Working directly with the use-cases at hand
Working in small team, were you will have large influence
Good opportunities 

## What we are looking for 

Machine Learning / Data Science.
Likes working practical and hands-on
Happy to occationally wander outside pre-defined roles
" do things you dont know "
Interest in mechanical machines and physical processes,
or the organizational side of operating buildings

Paid internships summer 2022
Master/bachelor thesis spring 2023
Full-time Data Scientist



# Background


## Commercial building stakeholders

- Property Owner
- Building Operations Manager
- Janitors
- Service technicians
- Tenants

## CB facilities

Lighting
Ventilation
Heating/cooling
Drinking water
Hot water
Plumbing
Electricity
Internet

## Soundsensing intersects

- IoT. Electronics Engineering / Embedded Devices.
- Data Science. Machine Learning
- Maintenance. Reliability Engineering
- Commercial Building Management. Business transformation.



# Replacement problem

In Sudden Failure case
Wear-out: Progressive Failure

Operations Research
18:3. REPLACEMENT OF EQUIPMENT THAT FAILS SUDDENLY

Individual Replacement Policy.
Under this policy, an item is replaced immediately after its of replacement failure.

Group Replacement Policy.
Under this policy, we take decisions as to when all the items must be replaced,
irrespective of the fact that items have failed or have not failed, with a provision that if any item fails before the optimal time,
it may be individually replaced.


https://www.reliasoft.com/resources/resource-center/optimum-preventive-maintenance-replacement-time
https://www.weibull.com/hotwire/issue156/hottopics156.htm

# Open source reliability software

http://www.openreliability.org/projects/
Fault Tree Analysis on R
EventTree
Weibull Analysis on R

Stochastic Modelling for RAM Analysis - Reliability, Availabiilty and Maintainability

https://reliability.readthedocs.io/en/latest/
https://github.com/MatthewReid854/reliability
Accelerated Life Testing Models
Reliability growth, optimal replacement time, sequential sampling charts, similar distributions, reliability test planners
Fitting Weibull mixture models
Fitting probability distributions to data including right censored data

http://reliawiki.org/index.php/Accelerated_Life_Testing_Data_Analysis_Reference

First, preventive maintenance makes sense when the component gets worse with time. In other words, as the component ages, it becomes more susceptible to failure or is subject to wearout. In reliability terms, this means that the component has an increasing failure rate. The second requirement is that the cost of preventive maintenance must be less than the cost of corrective maintenance. If both of these requirements are met, then preventive maintenance is appropriate and an optimum time (minimum cost) at which the preventive replacement should take place can be computed


# Cost-sensitive learning

Risk Based Maintenance (RBM) is when you use a risk assessment methodology
to assign your scarce maintenance resources to those assets that

(remembering that risk = likelihood x consequence).
likelihod

Failure case

Failure is guaranteed at some point in time
Likelihood = 1.0
Do not know exactly when, just have to put a time for it.

Failure rate increases at the end
Useful-life period, where the failure rate is constant and the distribution of times to failure (or between failures) is exponential.

To model the reliability across entire bathtub curve need to use the
Weibull distribution.

https://www.weibull.com/hotwire/issue21/hottopics21.htm


Cost of failure
Reduced Quality of service on tenant
Emergency fixing.
Risk of 

Cost of replacing equipment

## Risk Based Maintenance (RBM)

Risk Based Maintenance (RBM) is when you use a risk assessment methodology
to assign your scarce maintenance resources to those assets that
carry the most risk in case of a failure (remembering that risk = likelihood x consequence).


