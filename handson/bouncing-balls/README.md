
# Detecting time differences of sound events

Temporal distances

## Time difference of a bouncing ball


Max Clark asked on Stack Overflow
Conversational Neural Network for Peak Detection and time difference of a bouncing ball
https://stackoverflow.com/questions/69426301/conversational-neural-network-for-peak-detection-and-time-difference-of-a-bounci

Target here is actually to get the heigth of the ball bounce.
There is information in that in the time difference between first and second bounce,
but also in the distance between second and third, etc.
So the neural network should maybe just

The bounceback amount (ratio?) is a way to measure how springy the ball and surface (combined) are.

https://demonstrations.wolfram.com/BounceTimeForABouncingBall/

The coefficient of restitution is
the velocity of the ball after the bounce,
divided by the velocity before the bounce

One can estimate COR using the time differences of the bounces.
dt1/dt2
https://iopscience.iop.org/article/10.1088/1361-6552/aa71ea

One can also estimate COR using the height difference of the bounces.
If one has the drop height, one only needs one time-difference.

Coefficient Of Restitution (COR) is mostly constant,
but some indications that it can change by up to 10% when height is increased 10x.

Sports balls have standardized COR values
Table tennis ball. Shall bounce up 24–26 cm when dropped from 30.5 cm on to a standard steel block. COR of 0.887 to 0.923.
Basketball. Shall rebound to between 960 and 1160 mm when dropped from a height of 1800 mm. COR between 0.53–0.64.
Tennis ball. ATP regulations. Bounce to a height of 135 cm and 147 cm when dropped from 254 cm on a hard surface. COR of between 0.728 and 0.759.
Golf ball. Roughly 0.70
Baseball prewar construction is about 0.45.


For drop from rest, ignoring air friction
    C_R = \sqrt{\frac{h}{H}}, where
    h {\displaystyle h} h is the bounce height
    H {\displaystyle H} H is the drop height


https://www.millersville.edu/physics/experiments/045/
Bounce-to-bounce time is proportional to the square root of the bounce height.
Only dependent on the COR?

Log flight time is linear in bounce number
https://www.researchgate.net/publication/228575622_Aerodynamic_Effects_in_a_Dropped_Ping-Pong_Ball_Experiment/figures?lo=1

## Triggering

A practical solution running on a device would need to "trigger" the model somehow.
One could have an "armed" state which means the model is ready.
And then trigger on the first bounce. With some pre-buffer time.

One could also try continious triggering, and hiding results without detection.
Need model to then also output the probability of a ball bounce having happened. 

## Model

Under simple conditions with a clear signal
and little background noise the amplitude is probably a good-enough feature.

## Outputs

How well can one get the Coefficient of Restitution?

How well can one classify the type of ball?
On a known/fixed surface / environment.
With an unknown surface.

How well can humans do it?
If only doing one bounce, vs two bounces vs full sequence.

How well can one classify the type of surface?
With a known ball type, with unknown ball type

What kind of model would it take to generate bounces that are indistinguishable from real ones?
With human evaluation.

## Conditions

Things that influence the height of the ball bounce.

- Ball initial state
Height
X and Y velocity. Simplified: only consider 0,0
- Ball.
Type of ball. Inflated, solid
Coefficient Of Restitution
Common. Golfball,basketball,tabletennis,tennis
Inflation level.
Diameter.
Weight.
- Surface
Hardness. Asphalt
- Recording environment
Inside, outside
Reverberation,background noises
- Recording device

## Simulation

Impact sound.
How to get a realistic emission?

How does the emission change with different ball properties?
Impact speed.

Soundlevel/energy should change with impact speed.

General expectation.
velocity up by sqrt(2) doubles kinetic energy, doubles sound power, up 3 dB 
assumes a constant ratio of conversion from kinetic to acoustic energy
this process might change a bit based on velocity
maybe also shifts frequency content?

https://metinmediamath.wordpress.com/2013/11/30/home-experiment-impact-speed-and-sound-level/
db = 29 * v**0.43
doubling velocity gave approx 10 dB increase

Hardness of ball and surface.
Harder means more high frequency content.
Harder means a shorter impact, shorter time. Reverberation might mask some of this though.

Listening to tennis ball impact.
Velocity decrease seems to decrease in high frequency content?


## Data collection

Shot video with camera held vertically.
Have visible measuring reference for the height.
Drop the different balls from different heights onto different surfaces.

Can then use the video footage and the meter stick as reference.

Test the bounciest and loudest combinations first to ensure everything is in range.

## Reference data

"bouncing ball reference"

https://www.youtube.com/watch?v=5rYrQHqoCHI
10 or so balls. Concrete floor. Drop height around 1 m. Moving around 3 m.

https://www.youtube.com/watch?v=pZlYl0l2lFs&list=PLybgRIq62sCyNUN6wHk5goAlVkMNOBWN_&index=1
23 different balls

