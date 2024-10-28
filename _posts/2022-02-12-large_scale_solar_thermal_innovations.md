---
wip: true
title: 'Large scale solar thermal innovations, curated(ish)'
layout: post
categories: [solar, power, sustainable, solarpunk, post-scarcity, veille]
permalink: large-scale-solar-thermal-innovations
---

<p align="center">
<video controls autoplay muted loop>
	<source src="./assets/sha256/25ec8351b740f8964bee7ae38123dea013c7e5fbf3abb4d5f876c021305666fb.mp4" type="video/mp4">
	Have a looksee <a href="https://www.reddit.com/r/BeAmazed/comments/q22gja/thats_an_amazing_visual_illusion/">here</a>!
</video>
</p>


## optimization on heliostats

* `metalized BoPET instead of glass mirror`
* `single (DC) motor for dual axis tracking`
	* `shape support so that circular rotation turns into elliptical movement (in a plane) with constant offset in the third dimension`

* [13, Monolithic 2 DOF fully compliant space pointing mechanism](https://ui.adsabs.harvard.edu/link_gateway/2013MecSc...4..381M/doi:10.5194/ms-4-381-2013)
* [same same but different](https://www.thingiverse.com/thing:3612786)
<img src="https://cdn.thingiverse.com/renders/bd/a1/cd/52/2e/fe287cfa9e72c7efc5451c5175c8c5a5_display_large.jpg"/>

* `mylar film mirror roll`
	* `heliostat = streched Mylar between 2 rolls`
		* `washing = roll enough new film such that clean new area replaces dusty old area`
			* `periodically replace rolls (tweak periodicity for economics)`
			* `wash dusty rolls in dedicated plant w/ closed loop water system`
	* [(2011) Novel solar cogeneration trough system based on stretched microstructured Mylar film](http://dx.doi.org/10.1117/12.896197)


## robot peeling plastic film

* `save millions of cubic meters of desalinated water a year`
	* `insert water usage numbers from Ouarzzazzate and others`
	* `closed loop water use`

* `solve PV dust deposition issue on other celestial bodies as well`
	* `links/images to Mars rovers`
	* `and NASA's attempts at circumventing this issue`
		* `too harsh weigth constraints for blower, broom, film rolls`
		* `dust devils help`
		* `larger dust grains help`

* `stack 25 years worth of transparent PET/PMMA/... film stacks on top each PV panel`
	* `so dust off happens through peeling one film`
		* `save on desalinated water`
		* `25 years meaning as many as times PVs are water washed`

* `not this`: [13, Automated Removal of Prepreg Backing Paper - A Sticky Problem](https://www.diva-portal.org/smash/get/diva2:656534/FULLTEXT01.pdf)

* `no pneumatics, no general problem solving`
* `but instead a 1-servo peelable design. Made especially for this purpose.`
* `at scale replace servos by something a single machine or human can peel off at walking speed`

* `peeling thin transparent film`
* `surface protection tape`


## alternative concentrators

[19, A Review on Solar Concentrators with Multi-surface and Multi-element Combinations](https://doi.org/10.15627/jd.2019.9)
<img src="https://solarlits.com/jd/figures/6-80-7.jpg"/>


## alternative plants ~ fewer moving parts

`Cassegrain -type reflector & concentrator systems`

* [https://en.wikipedia.org/wiki/Cassegrain_reflector](https://en.wikipedia.org/wiki/Cassegrain_reflector)
	* > a combination of a primary concave mirror and a secondary convex mirror

<p align="center"><img width=560 height=315 src="./assets/sha256/1a8ba7c26a83d10ce53cb93d34d9572565b14e12a884cdc88ddc966e7b41b1b3.png"></p>
*from the **amazing** [Why is this Space Telescope so Tiny?](https://www.youtube.com/watch?v=HxwhCmO90UQ)*

### TransAstra Corporation's Optical Mining Technology
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/X5GKz9XLh70?si=lgF3zGDw4naePkoB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Beam-down solar thermal power plant

<p align="center"><img src="./assets/sha256/c0e475e7c9fe229eabbf180ed115507103cfa8e349a8b349fcbf29d688e742da.png"></p>

The [Yumen Xinneng CSP Plant](https://www.google.com/maps/place/Yumen+Xinneng+CSP+Plant/@40.3294927,97.2700596,1130m/data=!3m1!1e3!4m6!3m5!1s0x37c7b33e18f6d759:0x6162019542e51786!8m2!3d40.3326771!4d97.2732976!16s%2Fg%2F11hzwxmcgz?entry=ttu) and [NREL's listing](https://solarpaces.nrel.gov/project/yumen-xinneng-xinchen-50mw-beam-down).

<p align="center">
<a href="https://www.energy.gov/sites/prod/files/2019/04/f61/CSP%20Summit%202019%20Panel%203%20%E2%80%93%20CAS%20Wang.pdf#page=12">
<img src="./assets/sha256/f6ea0ceb68a210a5ffbe0cab6cfc85b95cf76b74418535e7724d06b2a77121aa.png"/>
</a>
</p>

* [(2014) Issues with beam-down concepts](https://doi.org/10.1016/j.egypro.2014.03.028)
	* > Most beam-down central receiver systems replace the usual central tower, receiver, and heat transfer vertical piping and pump
		with a hyperbolic reflector located below the aim point of the field.
		This reflects the impinging light toward the ground. It is shown that this also expands the image which would have been produced
		at the initial aim point by several fold, to the extent that an array of CPC's is required to restore some of the concentration.
		It is suggested that the costs of the towers to support the secondary reflector assembly, the reflector and its strong-back,
		and the CPC's may well equal or exceed that of the elements eliminated. The requirement that secondary size and cost be constrained
		also limits the boundary of the heliostat field to the extent that, for a given aim point height,
		typically half or less of the optimum power to the tower top receiver can be achieved in the beam-down configuration.
* [(2015) Modeling of Beam Down Solar Concentrator and Final Optical Element Design](https://vikasmech.github.io/Master-s-Thesis/Master%27s%20Thesis_Vikas.pdf)
* [(2015) Preliminary Optical, Thermal and Structural Design of a 100 kWth CSPonD Beam-down On-sun Demonstration Plant](https://doi.org/10.1016/j.egypro.2015.07.359)
* [(2016) Validation of an optical model applied to the beam down CSP facility at the Masdar Institute Solar Platform](https://doi.org/10.1063/1.4949031)
* [(2017) An Origami-Inspired Design of a Thermal Mixing Element Within a Concentrated Solar Power System](https://doi.org/10.1115/DETC2017-68360)
* [(2023) A Novel Dual Receiver–Storage Design for Concentrating Solar Thermal Plants Using Beam-Down Optics](https://www.mdpi.com/1996-1073/16/10/4157)
	* <img src="https://www.mdpi.com/energies/energies-16-04157/article_deploy/html/images/energies-16-04157-g001.png"/>
* [(2023) Progress in beam-down solar concentrating systems](http://dx.doi.org/10.1016/j.pecs.2023.101085)
* [(2023) A Novel Dual Receiver–Storage Design for Concentrating Solar Thermal Plants Using Beam-Down Optics](https://www.mdpi.com/1996-1073/16/10/4157)
* [(2011) Concentrated solar power on demand](https://www.solarpaces.org/wp-content/uploads/Concentrated-solar-power-on-demand.pdf)

Notable authors:
* [Dr. Nicolas Calvet](https://www.ku.ac.ae/academics/college-of-engineering/department/department-of-mechanical-engineering/people/dr-nicolas-calvet)
* [Evangelos Bellos](https://scholar.google.com/scholar?oi=bibs&hl=fr&cites=11266656088223967158&as_sdt=5&pli=1)

### MOSAIC
Spherical `cassegrain-schmidt solar concentrator` with mobile receiver on a [Cable-Driven Parallel Robot](./solar-3d-printer)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Wo55_kVMGNM?si=KBgWtpf5RUi0meHu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Part of [EU's H2020 Research program](https://mosaic-h2020.eu/scientific-publications).

<img src="https://www.mdpi.com/energies/energies-13-01816/article_deploy/html/images/energies-13-01816-g002.png"/>
<img src="https://www.mdpi.com/energies/energies-13-01816/article_deploy/html/images/energies-13-01816-g009.png"/>

* [(2020) Low-Cost Solar Electricity Using Stationary Solar Fields; Technology Potential and Practical Implementation Challenges to Be Overcome. Outcomes from H2020 MOSAIC Project](https://doi.org/10.3390/en13071816)
	* > At any time of the day, a spherical mirror reflects the rays coming from the sun along a line that points to the sun through the center of the sphere.

* *A funky paper*: [1975, Stationary concentrating reflector cum tracking absorber solar energy collector: optical design characteristics](https://doi.org/10.1364/AO.14.001509)

* [(2012) Cassegrain Solar Concentrator System for ISRU Material Processing](https://ntrs.nasa.gov/citations/20120004046)
<img src="https://d3i71xaburhd42.cloudfront.net/0491dbb9c4a6f461fd45333d46d471abf4803a07/5-Figure4-1.png"/>

* [(2008) Innovative design of cassegrain solar concentrator system for indoor illumination utilizing chromatic aberration to filter out ultraviolet and infrared in sunlight](https://sci-hub.ru/10.1016/j.solener.2008.12.013)
	* <img src="https://ars.els-cdn.com/content/image/1-s2.0-S0038092X08003502-gr7.jpg"/>

* `companies + links`
	* [https://www.linkedin.com/groups/13519618/](https://www.linkedin.com/groups/13519618/)
		* [https://mosaic-h2020.eu/contact-us/](https://mosaic-h2020.eu/contact-us/)
	* [https://www.cener.com/en/areas/solar-thermal-energy-department/](https://www.cener.com/en/areas/solar-thermal-energy-department/)
	* [https://www.tekniker.es/en/renewable-energy](https://www.tekniker.es/en/renewable-energy)
	* [https://cordis.europa.eu/project/id/727402](https://cordis.europa.eu/project/id/727402)
	* [https://sfera3.sollab.eu/2021/11/05/launch-of-the-4th-sfera-iii-transnational-access-campaign/](https://sfera3.sollab.eu/2021/11/05/launch-of-the-4th-sfera-iii-transnational-access-campaign/)
	* [https://sfera3.sollab.eu/about-us/#partners](https://sfera3.sollab.eu/about-us/#partners)


### synthese
* `reduce cost`
	* `minimize moving parts / motor count`
	* `maximize concentration factor (>9000 Suns! .webm)`

* `Beam-down has sub-ideal concentration:`
	* `final image is enlarged by hyperbolic secondary concentrator.`
	* `low aperture = smaller heliostat field (than towers)`
	* `... but beaming directly to TES (thermal energy storage) skips pumping, pipes and cycling day-night`

* `MOSAIC has`
	* `fixed heliostats (yay)`
	* pumps, pipes and oven (nay) mounted on a [cable-driven parallel robot](https://en.wikipedia.org/wiki/Cable_robots)

*I feel there's something to be found at the intersection of this Venn diagram!*

=> given a large static spherical heliostat field, is there a possible secondary concentrator that would focus this linear light?
