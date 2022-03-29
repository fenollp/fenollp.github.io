---
wip: true
title: 'Large scale solar thermal innovations, curated'
layout: post
categories: [solar, power, sustainable, solarpunk, post-scarcity, veille]
permalink: large-scale-solar-thermal-innovations
---

## optimization on heliostats

```
metalized BoPET instead of glass mirror

single (DC) motor for dual axis tracking
	shape support so that circular rotation turns into elliptical movement (in a plane) with constant offset in the third dimension
```

<p align="center">
<video controls autoplay muted loop>
	<source src="./assets/sha256/25ec8351b740f8964bee7ae38123dea013c7e5fbf3abb4d5f876c021305666fb.mp4" type="video/mp4">
	Have a looksee <a href="https://www.reddit.com/r/BeAmazed/comments/q22gja/thats_an_amazing_visual_illusion/">here</a>!
</video>
</p>

[13, Monolithic 2 DOF fully compliant space pointing mechanism](https://www.researchgate.net/publication/264382996_Monolithic_2_DOF_fully_compliant_space_pointing_mechanism)
[same same but different](https://www.thingiverse.com/thing:3612786)

```
mylar film mirror roll
	heliostat = streched Mylar between 2 rolls
		washing = roll enough new film such that clean new area replaces dusty old area
				  periodically replace rolls (tweak periodicity for economics)
				  wash dusty rolls in dedicated plant w/ closed loop water system
	https://sci-hub.ru/10.1117/12.896197
		Novel solar cogeneration trough system based on stretched microstructured Mylar film.
```

## robot peeling plastic film

```
save millions of cubic meters of desalinated water
	insert water usage numbers from Ouarzzazzate and others

solve PV dust deposition issue on other celestial bodies as well
	links/images to Mars rovers
	and NASA's attempts at circumventing this issue
		too harsh weigth constraints for blower, broom, film rolls
		dust devils help
		larger dust grains help

stack 25 years worth of transparent PET/PMMA/... film stacks on top each PV panel
	so dust off happens through peeling one film
		save on desalinated water
		25 years meaning as many as times PVs are water washed
```

not this: [13, Automated Removal of Prepreg Backing Paper - A Sticky Problem](https://www.diva-portal.org/smash/get/diva2:656534/FULLTEXT01.pdf)
```
no pneumatics, no general problem solving
but instead a 1-servo peelable design. Made especially for this purpose.
at scale replace servos by something a single machine or human can peel off at walking speed

peeling thin transparent film
surface protection tape
```

## alternative concentrators

[19, A Review on Solar Concentrators with Multi-surface and Multi-element Combinations](https://doi.org/10.15627/jd.2019.9)


## alternative plants ~ fewer moving parts

JWST.gif

https://en.wikipedia.org/wiki/Cassegrain_reflector
> a combination of a primary concave mirror and a secondary convex mirror

<p align="center"><img width=560 height=315 src="./assets/sha256/1a8ba7c26a83d10ce53cb93d34d9572565b14e12a884cdc88ddc966e7b41b1b3.png"></p>
*from the **amazing** [Why is this Space Telescope so Tiny?](https://www.youtube.com/watch?v=HxwhCmO90UQ)*

[TransAstra Corporation's Optical Mining Technology](https://www.youtube.com/watch?v=X5GKz9XLh70)

### beam-down solar thermal power plant

<p align="center"><img width="66%" src="./assets/sha256/c0e475e7c9fe229eabbf180ed115507103cfa8e349a8b349fcbf29d688e742da.png"></p>

*From [energy.gov](https://www.energy.gov/sites/prod/files/2019/04/f61/CSP%20Summit%202019%20Panel%203%20%E2%80%93%20CAS%20Wang.pdf#page=12)*

[13, Issues with beam-down concepts](https://sci-hub.ru/https://doi.org/10.1016/j.egypro.2014.03.028)
> Most beam-down central receiver systems replace the usual central tower, receiver, and heat transfer vertical piping and pump with a hyperbolic reflector located below the aim point of the field. This reflects the impinging light toward the ground. It is shown that this also expands the image which would have been produced at the initial aim point by several fold, to the extent that an array of CPC's is required to restore some of the concentration. It is suggested that the costs of the towers to support the secondary reflector assembly, the reflector and its strong-back, and the CPC's may well equal or exceed that of the elements eliminated. The requirement that secondary size and cost be constrained also limits the boundary of the heliostat field to the extent that, for a given aim point height, typically half or less of the optimum power to the tower top receiver can be achieved in the beam-down configuration.

[15, Modeling of Beam Down Solar Concentrator and Final Optical Element Design](https://vikasmech.github.io/Master-s-Thesis/Master%27s%20Thesis_Vikas.pdf)

[15, Preliminary Optical, Thermal and Structural Design of a 100 kWth CSPonD Beam-down On-sun Demonstration Plant](https://sci-hub.ru/https://doi.org/10.1016/j.egypro.2015.07.359)

[16, Validation of an optical model applied to the beam down CSP facility at the Masdar Institute Solar Platform](https://sci-hub.ru/https://doi.org/10.1063/1.4949031)

[17, An Origami-Inspired Design of a Thermal Mixing Element Within a Concentrated Solar Power System](https://sci-hub.ru/https://doi.org/10.1115/DETC2017-68360)

Notable authors:
* [Dr. Nicolas Calvet](https://www.ku.ac.ae/academics/college-of-engineering/department/department-of-mechanical-engineering/people/dr-nicolas-calvet)

### MOSAIC
cassegrain-schmidt solar concentrator

[20, Low-Cost Solar Electricity Using Stationary Solar Fields; Technology Potential and Practical Implementation Challenges to Be Overcome. Outcomes from H2020 MOSAIC Project](https://sci-hub.ru/https://doi.org/10.3390/en13071816)
> At any time of the day, a spherical mirror reflects the rays coming from the sun along a line that points to the sun through the center of the sphere.

A funky paper: [1975, Stationary concentrating reflector cum tracking absorber solar energy collector: optical design characteristics](https://sci-hub.ru/https://doi.org/10.1364/AO.14.001509)

[12, Cassegrain Solar Concentrator System for ISRU Material Processing](https://ntrs.nasa.gov/citations/20120004046)
[08, Innovative design of cassegrain solar concentrator system for indoor illumination utilizing chromatic aberration to filter out ultraviolet and infrared in sunlight](https://sci-hub.ru/10.1016/j.solener.2008.12.013)
https://www.researchgate.net/figure/Cassegrain-solar-concentrator-for-high-temperature-regolith-processing-for-ISRU-oxygen_fig5_283152715
https://mosaic-h2020.eu/scientific-publications/
	https://www.youtube.com/watch?v=Wo55_kVMGNM
https://www.mdpi.com/1996-1073/13/7/1816

#### MOSAIC companies + links
* https://www.linkedin.com/groups/13519618/
	* https://mosaic-h2020.eu/contact-us/
* https://www.cener.com/en/areas/solar-thermal-energy-department/
* https://www.tekniker.es/en/renewable-energy
* https://cordis.europa.eu/project/id/727402

* https://urlz.fr/heDR
* https://sfera3.sollab.eu/about-us/#partners


### synthese
reduce cost
	minimize moving parts / motor count
	maximize concentration factor (>9000 Suns! .webm)

Beam-down has sub-ideal concentration:
* final image is enlarged by hyperbolic secondary concentrator.
* low aperture = smaller heliostat field (than towers)
... but beaming directly to TES (thermal energy storage) skips pumping, pipes and cycling day-night

MOSAIC has
* fixed heliostats (yay)
* pumps, pipes and oven (nay) mounted on a [cable-driven parallel robot](https://en.wikipedia.org/wiki/Cable_robots)

*I feel there's something to be found at the intersection of this Venn diagram!*

=> given a large static spherical heliostat field, is there a possible secondary concentrator that would focus light this linear light?
