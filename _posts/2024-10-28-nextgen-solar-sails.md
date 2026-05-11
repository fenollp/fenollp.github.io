---
title: nextgen solar sails
layout: post
categories: [projects]
permalink: nextgen-solar-sails
---


<!--![Not a solar sail but an amazing Space shiny nonetheless](https://upload.wikimedia.org/wikipedia/commons/7/74/Inflatable_Antenna_Experiment.jpg)-->
![Artist concept of a solar sail in space NASA](https://planetary.s3.amazonaws.com/web/assets/pictures/_2400x1587_crop_center-center_82_line/20130604_Earth_Sail_3023x2006.jpg.webp)


# Let's craft Solar Sails (cheaply & at home)

Rockets are fast but solar sails are faster! Also, we can't really (shouldn't) play with rockets (nor nuclear ones) in our kitchen…

*So, how about projecting Humanity through the stars using some fishing line, a pack of chips and some ducktape?*

Seriously, [solar sail](https://en.wikipedia.org/wiki/Solar_sail)ing is extremely promising. [Chemical rockets max out at](https://space.stackexchange.com/a/17130/33749) ~500 [Isp](https://en.wikipedia.org/wiki/Specific_impulse) while solar sails [could achieve a tenth of the speed of light](http://ffden-2.phys.uaf.edu/webproj/212_spring_2015/robert_miller/physics.html). They take a long time to accelerate but do so without requiring fuel. They are made of a large reflective surface & a payload: steering, comms and what have you. In other words solar sails are mostly defined by their mass-to-area ratio.

I propose you invent a new sail that beats the mark of **<10g/m²** (or `>100m²/kg`) for less than 30€, with your hands and some ✨SCIENCE✨.


## Bill of Materials

### Space blankets [~3€](https://www.decathlon.fr/p/couverture-de-survie/_/R-p-12837)

Emergency thermal blankets [aka. Mylar (aka. BoPET)](https://en.wikipedia.org/wiki/Mylar) sport an amazing `~98%` reflectivity. Meaning most of the energy hitting it transforms to momentum and not heat. They only deform at `>200°C` plus they don't [outgas](https://en.wikipedia.org/wiki/Outgassing).


### Fishing line [~5€](https://www.leroymerlin.fr/produits/fil-nylon-filete-standers-diam-0-4-mm-x-l-100-m-70626640.html)

Nylon thread can be twisted to act as Nylon Linear Material Actuators aka NLMAs, *pulling with great force* compared to its weight **when heated to ~120°C**. Per this 2016 paper: [New twist on artificial muscles](https://www.pnas.org/doi/full/10.1073/pnas.1605273113).

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Za0VeU9Ov7A?si=8DWeNUu-us_nyCkA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

See also this cute Instructables: [Fabricating Fishing Line Artificial Muscle at Home](https://www.instructables.com/Fabricating-Fishing-Line-Artificial-Muscle-at-Home/).

>>> Note however that Nylon should be replaced with Polyester (Dacron) thread or Kevlar/Aramid which [contain much less water](https://en.wikipedia.org/wiki/Hygroscopy), before circumnavigating the planet.


### Ducktape [~20€](https://www.shop-sks.com/fr/3M-ruban-adhesif-de-transfert-966-transparent-9-mm-x-55-m-0-05-mm)

Space-grade [3M™ Adhesive Transfer Tape 966](https://www.3mfrance.fr/3M/fr_FR/p/d/v000090242/) is specifically tested to meet NASA & ESA standard [ASTM E595](https://store.astm.org/e0595-15r21.html): `<1.0%` mass outgassed. It **handles 120°C with ease** and will not produce fumes that kill you.


## DIY

Temperatures in [Low Earth Orbit](https://en.wikipedia.org/wiki/Low_Earth_orbit) range [from –170°C to **123°C**](https://www.oreilly.com/library/view/diy-satellite-platforms/9781449312756/ch01s05.html). There, *sunlit Nylon muscles tense*. 
Set your kitchen oven to [thermostat](https://fr.wikipedia.org/wiki/Thermostat_(four)) 4 ([gas mark](https://en.wikipedia.org/wiki/Gas_mark) ½) to reproduce this `120°C` cooking orbit.

Now it is up to you to find a way to combine the above materials (and/or more) into a tightly-packed *structure that unfolds* once in LEO and takes a *flat enough shape* to reflect Sun rays.

In short:
* Overall weight must be minimized and then so should initial volume (deployed within a Space launch vehicule)
* Structure must not outgas: materials should not sublimate nor exert gas (attitude would change, lifespan would shorten)
* LEO insolation temperatures should be utilized as deployment energy

This challenge is proposed to University (or High School) students to devise a way to fit the largest & lighest (& mightiest) Solar Sail
they can in the cheapest Cubesat possible, aiming for a total mass below 10g/m², all hardware included.


## See also
* **Electric sails** à la [flying spiders](https://en.wikipedia.org/wiki/Ballooning_(spider))
  * [**Extreme Metamaterial Solar Sails for Breakthrough Space Exploration**: NASA Innovative Advanced Concepts (NIAC) Phase II Final Report](https://ntrs.nasa.gov/citations/20250008150)
* **Laser sails**
  * [Philip Lubin: Breakthrough Discuss 2017](https://www.youtube.com/watch?v=7UVgMCVFCe0)
  * [Photonic Propulsion for Relativistic Flight Enabling the First Interstellar Missions Philip Lubin](https://www.youtube.com/watch?v=hWZCCjV29ig)
* [**Alpha CubeSat** University project](https://alphacubesat.cornell.edu/lightsail.html)
* **Using inflatable booms**
  * [Ultra-Thin Solar Sails for Interstellar Travel](https://www.niac.usra.edu/files/studies/final_report/333Christensen.pdf)
* **Shaping sail surface**
  * [Zac Manchester: Breakthrough Discuss 2017](https://www.youtube.com/watch?v=HKT_OSLF-YA)
* **ToughSF's blog**: [Riding Sunbeams with Solar Sails](https://toughsf.blogspot.com/2023/05/riding-sunbeams-with-solar-sails.html)


---

## Some of my own explorations

### Tumbleweed-like structure + insolated Nylon muscles to open up parabolic surface
Light but solid "articulations" keep the shape in extension, once Nylon muscles extend it

<center>
    <img alt="The dancefloor cover grid model" src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Dancepol_net.jpg"/>
</center>

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/pNxY0e3Ng_M?si=65CVQWg0wCvxUiLY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

### [Tensegrity](https://en.wikipedia.org/wiki/Tensegrity)
[BEST (Berkeley Emergent Space Tensegrities) Robotics](https://best.berkeley.edu/best-research/best-berkeley-emergent-space-tensegrities-robotics/) lab.

### Knitting configurations
Cool [videos](https://www.youtube.com/results?search_query=muscle+knitting+machine).

The [Ripstop](https://en.wikipedia.org/wiki/Ripstop) pattern.

[Circular](https://en.wikipedia.org/wiki/Circular_knitting) techniques.


<center>
<img alt="knitted nylon muscles" src="https://www.pnas.org/cms/10.1073/pnas.1605273113/asset/7720899e-df03-4c14-b90e-e6357f3d6efe/assets/graphic/pnas.1605273113fig04.jpeg"/>
</center>

### [Auxetic](https://en.wikipedia.org/wiki/Auxetics) dome
Nylon muscles pull on the many centroids such that the plane expends into a dome that then stays as such

[(2021) Bistable Auxetic Surface Structures](https://sci-hub.ru/https://doi.org/10.1145/3450626.3459940)

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vrOjy-v5JgQ?si=uk-dXg-4SKGmNmjF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2tKj7wQtXxY?si=YWlIK4o0VsvaMhXJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

Check out [github.com/UH-AIM/bistable-auxetic-surface-structures](https://github.com/UH-AIM/bistable-auxetic-surface-structures) by [The Architected Intelligent Matter (AIM) lab](https://aim.me.uh.edu).

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/-9mXmNcvbBg?si=fZMvAwF5KsXcYXJO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UL-OQYvQPO8?si=OX5Ft6j30zZdFlMw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
