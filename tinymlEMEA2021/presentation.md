
---
author: Jon Nordby <jon@soundsensing.no>
date: June 07, 2021
css: style.css
width: 1920
height: 1080
margin: 0
pagetitle: 'TinyML EMEA 2021: Perfect coffee roasting with TinyML sound sensing'
---

<section class="titleslide level1" data-background-image="./img/roest-soundsensing-cover.svg.jpg" style="background: rgba(255, 255, 255, 0.75); padding-top: 1.7em;" >

<h1 style="">Perfect coffee roasting</br> with TinyML sound sensing</h1>

<p>
<b>Jon Nordby</br>
jon&#64;soundsensing.no</br>
tinyML EMEA 2021</br>
</b>
</p>

</section>


<aside class="notes">

A project that Soundsensing did for the company Roest.
</aside>

## Roest

![](./img/roest-sample-roaster-2x-tightcrop.jpg){width=75%}

::: notes

Roest is a Norwegian company producing machines for roasting coffee

Their s100 sample roaster is the most modern sample roaster on the market, and has won several design awards

A sample roaster is used for sampling and testing coffee,

which professionals in the coffee business do continiously in order to bring you great coffee

:::


## {data-background="./img/soundsensing-technology.jpg" style="background: rgba(255, 255, 255, 0.0);"}

::: notes

Soundsensing is a leading provider of sensor solutions that combine audio and machine Learning

Our technology is a combination of machine learning models, hardware and a cloud-based data platform 

From this technology we build solutions for

Noise Monitoring for construction, office and industrial use

Condition Monitoring, of technical equipment and processes

We are experts in using sound to understand the world.

And also for coffee, sound is important

:::

## Roasting coffee

![](./img/roasting-curve-annotated.png){width=70%}

::: notes

Coffee roasting is the process of taking green and raw beans

and heating them up over time to develop the proper coffee aroma

After roasting the beans can be ground, and used to make coffee

The key to a good roast is to stop the process at the right time

The method used by the very best roasters is to listen for the 1st crack

This is when the water in the beans turn to steam and the beans pop like popcorn

making an audible sound

:::

## Doing it manually

![](./img/roest-2-prøvebrenner-kaffegeek.jpg){width=75%}

::: notes

Listening to the 1st crack is done by many professional roasters

It requires constant attention over a 3 minute period

This makes it quite tedious to do

Different operators may also mark the 1st crack time a bit differently,

leading to inconsistencies

With Soundsensing we can automate this machine listening task

:::

## Automatic First Crack Detection

![](./img/firstcrack-tech.jpg){width=85%}

::: notes

For the Roest machine we developed a on-edge solution running on a board inside the machine

It using a MEMS microphone and an ST microcontroller, and Soundsensing firmware

We trained a Sound Event Detection to recognize the "cracks" of the coffee beans

We used Tensorflow to train

and converted it to run on the microcontroller using ST X-CUBE-AI 

Let us see how it works in practice!

:::

## Demo video

<video controls class="r-stretch" data-autoplay src="./img/soundsensing-roest-simple-scappy1.mp4"></video>

::: notes

The operator starts the automated roasting process by adding beans

After around 5 minutes the beans start cracking

The cracking is detected and a counted shown at the bottom of the screen

The count of cracks is logged over time in the dashboard

After a preset time from the detected 1st crack start

the machine automatically stops the process

and the beans are ready

:::

## Summary

Benefits of fully automated roasting

* Operator can do other things while machine runs
* Improved consistency over time and operators
* Works well regardless of operator skill level

Summary

* Acoustic detection of first crack
* Shipping on Roest coffee roasters since 2020
* Using TinyML solution developed by Soundsensing

::: notes

:::


## {data-background="./img/roest-soundsensing-cover.svg.jpg" style="background: rgba(255, 255, 255, 0.75);"}


<h2>Want to sense activities or monitor machinery</br>
using sound and machine learning?</h2>

<b>
</br>
<a href = "mailto:contact@soundsensing.no">contact@soundsensing.no</a>
</br>
</br>

<em>TinyML EMEA 2021: Perfect coffee roasting with TinyML sound sensing</em>

<p>
Jon Nordby
</br>jon&#64;soundsensing.no
</p>
</b>

::: notes

This is only one example of what one can do with
sound, machine learning and TinyML

Do you have an sensing/monitoring problem that can be approached with sound?
In process-, manufacturing or other industries.
Get in touch with Soundsensing!

:::


# Bonus

Bonus slides after this point


## More resources

Machine Hearing. ML on Audio

- [github.com/jonnor/machinehearing](https://github.com/jonnor/machinehearing)

Machine Learning for Embedded / IoT

- [github.com/jonnor/embeddedml](https://github.com/jonnor/embeddedml)

Thesis Report & Code

- [github.com/jonnor/ESC-CNN-microcontroller](https://github.com/jonnor/ESC-CNN-microcontroller)



## {data-background="./img/roest-soundsensing-cover.svg.jpg" style="background: rgba(255, 255, 255, 0.75);"}


<h2>Want the worlds best coffee roaster?</h2>

<b>
</br>
<a href = "mailto:sales@roestcoffee.com">sales@roestcoffee.com</a>
</br>
</br>
</b>

::: notes

For your office, home, or local cafe

If you want the worlds most advanced coffe-roaster,
Contact Roest!

![](./img/roest-2-prøvebrenner-kaffegeek.jpg)

:::

