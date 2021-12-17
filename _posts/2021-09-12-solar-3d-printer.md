---
published: true
title: "Solar 3D Printer: my take on Markus Kayser's Solar Sinter"
layout: post
categories: [solar, printer, sustainable, solarpunk, vitrifier]
permalink: solar-3d-printer
---

Following up on [this hastily edited post](https://fenollp.github.io/concentrated-solar-for-infrastructure-and-fuel) about using the Sun to extract some form of hydrogen and to decarbonate part of the construction industry, I present this *Solar Desert Sand Vitrifier* I have been working on.

![MuJoCo simulation](./assets/sha256/6cfb26c4ab7dd416e081ab41745524a28ecf219222d4b57b2e8903f277a859f5.png)
[Link to simulation code](./assets/simulation_v0.zip) and [to the simulator: MuJoCo](https://mujoco.org/).


## Briefly

My goal is for this machine to be able to print house walls by melting desert sand with focused sunlight. Requiring only highly available and renewable energy and material.

Building on [Markus Kayser's Solar Sinter](https://kayserworks.com/798817030644) I designed and sized a prototype which *should*...
1. use a Fresnel lens `≥1.5m2` area (Markus Kayser's lens that we know can melt desert sand)
1. translate and rotate the lens within a *print volume* `100x` larger than Solar Sinter's 40cmx40cmx40cm
1. achieve mean *print speed* `≥1cm/min` which seems slower than Kayser's machine (from the video)
1. calibrate extra easily, with positioning `tolerances in cm`
1. cost `≤1000€`. Much cheaper than [`$28k` QT10-15](https://french.alibaba.com/product-detail/QT10-15-fully-automatic-block-making-machine-62335577166.html), [`$39k` BigRep-ONE](https://www.theverge.com/2014/2/19/5425278/bigrep-3d-printer-will-print-furniture-at-home#:~:text=BigRep%20One%20might%20be%20capable,for%20a%20lot%20less%20cash.) or [`>$1.5M` VX4000](https://amfg.ai/2018/09/18/top-10-large-scale-industrial-3d-printers/#:~:text=One%20thing%20to%20keep%20in,take%20advantage%20of%20its%20technology.) as well as orders of magnitude worse precision and speed.

## Lens

Finding a large circular Fresnel lens was tough!

First I looked for cheap Fresnel lenses from (broken) [80s-90s-00s Rear-projection TVs](https://en.wikipedia.org/wiki/Rear-projection_television) on my local equivalent to Craig's List. The few I could find ended up not large enough.

Here's the result of around a minute of summer sunlight exposition around midday at Paris latitude with a [AA67-00115B (Samsung SP43T8HPX/BOB)](https://manualzz.com/doc/1117713/samsung-sp-43t8hp-specifications) 43" (=0.63m2) lens: ![almost sintering](./assets/sha256/5d601c06df4a014a2e69b651e6715df3bbbb67c42d0b879159e2aa1083369b78.png)

Then I went for the modern 65" (=1.2m2) flatscreen TVs but these turned out to only sport linear Fresnel lenses! Meaning they focus light into a line and not a single spot.
*Also, you wouldn't believe how much money some people ask for a **once expensive** but utterly smashed screen...*

On AliExpress I could only find lenses in the meter square area. To melt sand we must achieve temperatures ranging from 1000 to 1500 degrees Celsius and talking with different sellers (as well as a French one selling the cheapest lenses I found) all were confident temperatures upwards of 800-900C weren't achievable...

In the future I'd like to come back to these cheap-ish Chinese lenses ($200-$700) and get a deal as there are *a lot* of competition there. Also, see [these exhorbitant shipping fees](https://www.aliexpress.com/item/32819940513.html) lately ($600 for a 1.2m2 lens priced $250)?
But first I need to replicate results!

I ended up finding [CF1200-B2](https://www.ntkj-japan.com/products/solar-concentrator-fresnel-lens/), a 1.5m2 PMMA rectangular spot lens with a smallish focal distance of 1.2m.
Note that acrylic (PMMA) is as good as glass for lenses and is usually lighter (3.5kg here).
This turned out pretty expensive: 250EUR/piece, 500EUR shipping to EU, 120EUR customs.

Again, bulk pricing is required here if I ever want to achieve less-than-a-thousand euros per machine...


## Large print volume


co2 emitted per kg of plastic vs aluminum
lifetime of plastic vs aluminum
strength of 3d printed screws
	hollow screws are possible


ask asca films for enough samples to cover outside cube frame with such that there is enough power outputed to not require non-organic ones


make parts of the corner pieces removeable so some can be replaced and even upgraded or help grow larger scale iteration


in the end the printer may look like a plastic kleenex
	use thermoplasticity to create a Fresnles lens + stand that follows the Sun (Tournesol) faster than the print head has to move


the more shippable the printer the better chance it has of selling kits


open cable robot project
	https://hackaday.io/project/166527/components


# motors
https://reprap.org/wiki/NEMA_17_Stepper_motor

https://makersportal.com/blog/raspberry-pi-stepper-motor-control-with-nema-17
	Raspberry Pi pins
		V    https://pinout.xyz/pinout/5v_power
		G    https://pinout.xyz/pinout/ground
		DIR  https://pinout.xyz/pinout/pin15_gpio22
		STEP https://pinout.xyz/pinout/pin16_gpio23
		EN   https://pinout.xyz/pinout/pin18_gpio24
	Python
		https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11DRV8825.md
		https://github.com/gavinlyonsrepo/RpiMotorLib/blob/fd166f1c6501d9c8ee18f57fa81329445ce244c8/test/MultiMotorThreading_DRV8825.py
=> enough pins in just one RPi?

https://www.omc-stepperonline.com/sale.html/clearance-sale-nema-17-stepper-motor-bipolar-l-48mm-w-gear-ratio-27-1-planetary-gearbox.html
	https://www.omc-stepperonline.com/download/17HS19-1684S-PG27.pdf
	17HS19-1684S-PG27
	Motor Type: Bipolar Stepper
	Holding Torque without Gearbox: 52Ncm(73.6oz.in)
	Planetary Gear Ratio: 26.85: 1
	$24
	=> `52*26.85/100 N.m`
		=> `~1.4kg` max hold per motor
	https://m.media-amazon.com/images/I/31cKfwDcIqL._AC_.jpg
		A BLK A+ 1B
		C GRN A- 1A
		B RED B+ 2B
		D BLU B- 2A
2b 2a 1a 1b
red blu grn blk


https://www.amazon.fr/drv8825-Module-dissipateur-thermique-exemple-Imprimante/dp/B01JIW13RY
	DRV8825 / A4988 motor driver
	~ 4EUR per motor

https://www.amazon.fr/Jeanoko-Control-Shield-DRV8825-imprimante/dp/B08VVZZB81
	support for DRV8825 / A4988
	~ 6EUR per motor

https://www.amazon.fr/CQRobot-Pieces-JST-PH-Connector-Female/dp/B0731MZCGF
	JST 2mm 4p connector
		stepper motor -to-> DRV8825 support card

--->>> >>> https://www.adafruit.com/product/2348
	RPi HAT
	USD23 / each adds 2 steppers
	https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi
	1.2-3A
	4.5-13.5VDC
	stacking header
		https://www.adafruit.com/product/2223
		USD3

*spring+cable system x4 to hold lens down*
* 3d print circular spring
* Auto-Rewind Spool Holder mechanism
* spiral spring
* vacuum cleaner power cable mechanism
* 3d print cord rewind
* [MARBLE THROWER 3D print model](https://www.cgtrader.com/3d-print-models/games-toys/board-games/marble-thrower)
* EUR10 [Vicloon Porte-clés Yoyo,Enrouleur Rétractable Longueur 70 cm avec Ressort Renforcé et Cordon Résistant,pour des Cartes d'identité avec Porte-clés Clip de Ceinture et le Crochet de Serrage](https://www.amazon.fr/Vicloon-Porte-cl%C3%A9s-Enrouleur-R%C3%A9tractable-R%C3%A9sistant/dp/B08HQFHB4Y/)
* Enrouleur Rétractable
* EUR10 [Enrouleur retractable avec clip ceinture et crochet. Réenroule jusqu'à 180g](https://www.actset.eu/fr/home/834-enrouleur-retractable-.html)
* EUR37 [Longe porte-outils anti-chute ceinture rétractable à enrouleur automatique ERGODYNE 3010 122cm 2.2kg](https://echaf-equipement.com/longe-porte-outils-anti-chute-ceinture-retractable-a-enrouleur-automatique-ergodyne-3010.html)
* EUR10 [Deolven Porte-Clés à Ressorts à Spirale,7 Pack Extensible Porte-clés en Plastique Coloré Cordons de Pêche Rétractable Sangle en Spirale d'attache pour Clés Torch Pinces École 7 Couleurs](https://www.amazon.fr/MUCHEN-SHOP-Porte-Cl%C3%A9s-Extensible-R%C3%A9tractable/dp/B07X2CV5MT)
* EUR9 [Porte-clés rétractable robuste Kuuqa - Enrouleur avec 100 cm de fil d’acier, noir](https://www.amazon.fr/Kuuqa-Porte-cl%C3%A9s-r%C3%A9tractable-haute-capacit%C3%A9/dp/B06XWVLJMY/)
* EUR11 [Ferplast Flippy Small Deluxe Laisse à enrouleur pour petits et moyen chiens Violet](https://www.amazon.fr/Ferplast-Flippy-Deluxe-Laisse-enrouleur/dp/B00DHCYW7A/)
* EUR65 [Enrouleur mural encastrable avec sangle rétractable Fix](https://www.usinenouvelle.com/expo/enrouleur-mural-encastrable-avec-sangle-p373764555.html)
* 1kg 1.2m [RETRACTABLE TOOL LANYARD REFERENCE : TS9000108](https://kratossafety.com/en/tool-lanyards/563-retractable-tool-lanyard.html)
* EUR290 [Barrière de sécurité à enrouleur rétractable - Barrière à sangle robuste avec crochet (15-25 m)](https://flexibarrier.com/fr/barriere-de-securite-a-enrouleur-ak-barriere-a-sangle-a-montage-mural-avec-crochet-15-25-m)
* EUR9 [Fil Linge Retractable, Corde À Linge Rétractable, Bobine De 12 M, Enrouleur De Corde À Linge Extensible, Économise De L'espace (gris Argenté)](https://www.amazon.fr/Retractable-R%C3%A9tractable-Enrouleur-Extensible-%C3%89conomise/dp/B092691YCQ/)




[![cubic frame 4 motors](./assets/sha256/64899490b39155fb4d22f15f5c6dfb38e5bebfbf8d6c1686fe4bf7b122b9d784.png)](https://sci-hub.ru/10.1109/ICCRE.2019.8724123)

[![cubic frame 8 motors](assets/sha256/dfea93be35bdb3ec636af2b91c307c944e8d3ca69d12e094548b21aeb26486fa.png)](https://www.youtube.com/watch?v=YAYxv8pr6Zo)

[![cubic frame 8 motors identical mounts](./assets/sha256/f0d56ae6506a6519ac54ff06d1bcb79197051757e67f8f69f39d364866b488a0.png)](https://sci-hub.ru/10.1109/IROS.2015.7353818)


## Change powder delivery system
Improve on *Markus Kayser’s Solar Sinter* by replacing ③ & ⑤ with a powder deposition system inspired from FDM: [Fused Deposition Modeling](https://en.wikipedia.org/wiki/Fused_filament_fabrication).

[![a sintering printer](./assets/sha256/7959b85bd8a8afaa6bec593fe98bcb5aea4732d2a0902ab407fea2c4b1f8986e.png)](https://formlabs.com/blog/what-is-selective-laser-sintering/)

**vibrating tube**
* inject powder through a tube


## Cubic frame material
Curtain pole (interior diameters)
	•	28mm 2.5m wood(ash) 11€/m
	•	16mm 2.5m metal(brass) 5€/m
	•	19mm 2.5m metal(white|black) 7€/m
	•	19mm 2.5m metal(brass) 8€/m
	•	28mm 2.5m metal(brass) 13€/m
	•	28mm 2.5mm metal(nickel) 12€/m
See also: elbow connector 10-13€/p, bracket 11-15€/p.
At Castorama.


TODL https://sci-hub.ru/https://www.osapublishing.org/ao/abstract.cfm?uri=ao-59-18-5358 20, Indoor daylighting using Fresnel lens solar-concentrator-based hybrid cylindrical luminaire for illumination and water heating


## European Standard Rail Aluminum Extrusion Profile
EUR7 per meter https://www.aliexpress.com/item/1005002453943888.html



EUR53 [Infrared Thermometer,High Temp Thermometer Pyrometer -58℉- 2732℉ (-50℃ to 1500℃),30:1 Distance Spot Ratio,AP-2732 Non-Contact Digital Dual Laser Pointers Flashlight IR Temperature Gun【NOT for Human】](https://www.amazon.com/Infrared-Thermometer-58%E2%84%89-2732%E2%84%89-1500%E2%84%83/dp/B07PHQ9YG9/)

## Photocatalytic water splitting

[10, Efficient Solar Hydrogen Production by Photocatalytic Water Splitting: From Fundamental Study to Pilot Demonstration](https://sci-hub.ru/10.1016/j.ijhydene.2010.01.030)
* > The object of our work is to explore the possibility of mass solar hydrogen production by coupling photocatalytic reactors with solar light concentrators
* > a hydrogen production rate of 0.164 L/h per unit volume
* > this technology to be economic[ally] viable in the near future
* it is necessary to narrow the band gap of photocatalysts to harvest visible-light

[13, Metal sulphide semiconductors for photocatalytic hydrogen production](https://sci-hub.ru/10.1039/c3cy00018d)
* > sulphide semiconductor photocatalysts have excellent solar spectrum responses and high photocatalytic activities
* > we highlight the crucial issues in the development of highly efficient sulphide photocatalysts without noble metal cocatalysts
* > These studies show not only the possibility of utilizing low cost carbon materials as a substitute for noble metals (such as Pt) in the photocatalytic H2-production but also a significant enhancement in the H2-production activity using metal-free carbon materials as effective co-catalysts.

[20, Ultrafine nano 1T-MoS2 monolayers with NiOx as dual co-catalysts over TiO2 photoharvester for efficient photocatalytic hydrogen evolution](https://sci-hub.ru/10.1016/j.apcatb.2020.119387)

[20, Recent progress on ammonia fuel cells and their potential applications](https://sci-hub.ru/10.1039/d0ta08810b)
* > ammonia fuel cells offer a clean and reliable energy source, which can mitigate many of the limitations associated with hydrogen economy and contribute to a more nearby sustainable future

https://www.nature.com/articles/s41586-021-03907-3	21, Photocatalytic solar hydrogen production from water on a 100 m2-scale


[](https://3dsolved.com/is-pla-heat-resistant-abs-asa-petg-and-more/)
* *PC: Polycarbonate (resists 150°C) but is on the expensive side & often blended for those of us without an industrial-grade 3d printer*
* *ABS (resists 105°C) cheap, tough but careful with the toxic fumes*


https://ropebot.eu/
https://www.researchgate.net/publication/352014468_Motor_Current_Based_Force_Control_of_Simple_Cable-Driven_Parallel_Robots
https://ropebot.eu/wp-content/uploads/2021/08/cropped-WauBie3-scaled-1.jpg
https://www.youtube.com/watch?v=PBNUb04DoZs
PaperCableCon21.pdf


https://discourse.odriverobotics.com/t/nema-enclosures-for-d5065-and-d6374-motors/830/8


https://webcamtests.com/
15EUR [TAKRINK Webcam 1080P Webcaméra Cybercaméra Ordinateur Microphone Intégré Port USB avec Couvercle de Webcam Trépied pour Chat Vidéo et Enregistrement](https://www.amazon.fr/TAKRINK-Cybercam%C3%A9ra-Ordinateur-Microphone-Enregistrement/dp/B08NX3MVBQ)
30EUR grand angle=>all feets in picture [Webcam PC 1080p HD - eMeet Nova Webcam Streaming Mise au Point Automatique avec Double Microphone, Web caméra USB pour Ordinateur Portable, Grand Angle 96°, Plug & Play, pour Linux, Win10, Mac](https://www.amazon.fr/Webcam-1080p-Automatique-Microphone-Ordinateur/dp/B09B6SYG1M)


https://en.sandhelden.de/about-sustainibility


lzyiec7qh0s71 Toghrol Tower

 I'm also looking at strings for my CDPR. I just bought https://www.decathlon.fr/p/tresse-de-peche-aux-leurres-tx12-grise-130-m/_/R-p-306977
Dyneema braided x12, 0.18mm diameter, 16.22kg, 130m for 30EUR => 0,24€/m
Should hold my <5kg loads but can't test right now. Maybe I should've gone for a thicker string?
Anyway that is 5x cheaper than the 1EUR/meter string that was mentioned.

[VGEBY Pêche Split Rings, 200 Pcs 5Tailles Heavy Duty Acier Inoxydable Split Anneaux Solide Connecteurs De Pêche Attirail De Pêche](https://www.amazon.fr/VGEBY-5Tailles-Inoxydable-Connecteurs-Attirail/dp/B07TVT8YSH/)
[Dovesun Fishing Rod Repair Kit Fishing Rod Guide Repair Kit Rod Ceramic Guides Ring 12 Sizes 0.15in to 1.18in](https://www.amazon.com/Dovesun-Fishing-Repair-Kit-Rod-Ceramic/dp/B08RNMSBN5/)
Tobben from Hangprinter: "used in v4 = ceramic ring from sewing machines"
EUR14 [MaoXinTek Guides pour Canne à Pêche, 80 pièces Kit de Réparation Anneau Guide de Pêche Céramique en Acier Inoxydable et Carbone pour Canne à pêche télescopique](https://www.amazon.fr/MaoXinTek-R%C3%A9paration-C%C3%A9ramique-Inoxydable-t%C3%A9lescopique/dp/B08NJMP3DX/)

EUR20 [32 Channel Digital Expansion HAT for Raspberry Pi](https://www.robotshop.com/eu/en/32-channel-digital-expansion-hat-raspberry-pi.html)

[CDPR video playlist](https://www.youtube.com/playlist?list=PLwDcOJWL58gYBzDNXOi2dURGvxXAQk3oq)

[Company Makes Bikes With Strings Instead Of Chains](https://www.youtube.com/watch?v=6NVRd8B-VmU)

https://hackaday.com/2017/10/12/this-3d-cable-printer-remixes-the-delta/

Arcus 3D C1 - Leveling the end effector. https://www.youtube.com/watch?v=ul78heZUyfM tripod

[20, A new control scheme of cable-driven parallel robot balancing between sliding mode and linear feedback](https://hal.archives-ouvertes.fr/hal-02515924/document)
Screenshot from 2021-10-12 00-29-38.png


cable robot camera stand
future: CDPR
	stackable
	can climb up/down
	can extend frame
	cable holders can move/rotate/slide on the inner frame so multiple CDPRs can work in a tight volume simultaneously

# Name?
not: Shai-Hulud https://dune.fandom.com/wiki/Shai-Hulud


https://www.amazon.com/MegaCast-Graphite-Crucibles-Refining-Aluminum/dp/B075CT9FLX/
EUR11 [Moule De Fonderie De Fonte De Coulée De Graphite De Grande Pureté De Werse Pour L'Or Et L'Argent - 750G](https://www.amazon.fr/Fonderie-Coul%C3%A9e-Graphite-Werse-LArgent/dp/B07HG5Z62M)

https://www.amazon.fr/Pomcat-r%C3%A9sistant-chaleur-s%C3%A9curit%C3%A9-Demeurant/dp/B077NGWXKX/

EUR9 [300m Dyneema Spectra Extreame Braided Fishing Line Super Strong Multifilament 4 Stands Fishing Wire](https://www.joom.com/en/products/1512468169939706457-112-1-26193-1551209324)
EUR45 [Kanirope® Corde dyneema PRO 1mm 100m noir 12x tressée SK78 pré-étirée enrobée](https://www.amazon.fr/Corde-Cordage-Dyneema-100m-tress%C3%A9/dp/B00NHQC1FQ)

https://www.trinamic.com/products/integrated-circuits/


https://www.thingiverse.com/thing:2932583
thread spool guide
	thread groove
	https://www.thingiverse.com/thing:3184816
		wear_groove_NB.stl
joints
	tetra angle joinery
	https://www.thingiverse.com/thing:996842
https://github.com/SolidCode/SolidPython
https://github.com/openscad/openscad
held tightly to the motor shaft with a set screw in an inserted nut
	https://www.goilacog.com/index.php?main_page=product_info&products_id=148603
	lead screw
	https://www.thingiverse.com/thing:40642/files
		AJGW-GearsHering_Small.stl



EUR10 [Salzmann 3M Diamond Grade Autocollants réfléchissants imperméables | Équipée de 3M Scotchlite | Autocollants pour les voitures, les motos, les bicyclettes - 4pcs](https://www.amazon.fr/Salzmann-Autocollants-r%C3%A9fl%C3%A9chissants-imperm%C3%A9ables-bicyclettes/dp/B00QX39BVM/)
EUR9 [24 Pcs Autocollants Réfléchissants d'Avertissement Stickers Réfléchissants de Sécurité Stickers de Visibilité Nocturne Autocollants de Bande Imperméables pour Véhicule, 1,18 x 3,25 Pouces](https://www.amazon.fr/Autocollants-R%C3%A9fl%C3%A9chissants-dAvertissement-Visibilit%C3%A9-Imperm%C3%A9ables/dp/B08QZ2FQ34)
EUR5 [Wowow 3M Bande réfléchissante - Ruban adhésif - Reflective tape - Blanc](https://www.amazon.fr/Wowow-3M-Bande-r%C3%A9fl%C3%A9chissante-Blanc/dp/B000Z2ITVU)
EUR12 [10M Ruban D'avertissement Réfléchissant, ONTWIE Sécurité Réfléchissant Avertissement éclairage Autocollant Ruban Adhésif Rouleau Bande, Couleurs Blanches pour Beautify Vélo Moto Décoration - 2.5cm](https://www.amazon.fr/Davertissement-R%C3%A9fl%C3%A9chissant-ONTWIE-Avertissement-Autocollant/dp/B07PN8QTPZ)
EUR15 [ONTWIE Ruban Réfléchissant étanche Haute Visibilité Marquage Industriel Danger Heavy Duty Attention Attention Ruban Auto-adhésif de Sécurité Extérieur - Rouge 10M](https://www.amazon.fr/ONTWIE-R%C3%A9fl%C3%A9chissant-Visibilit%C3%A9-Industriel-Auto-adh%C3%A9sif/dp/B08QMKC551)


https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/



https://www.youtube.com/watch?v=WWrb1iyCLlI


printer-types.png
[Low cost metal 3D printing! Electrochemical additive manufacturing](https://www.youtube.com/watch?v=B-UbDk7LrvU)

Jonas & Konrad from ropebot.eu
https://openmv.io/collections/cams/products/openmv-cam-h7-plus
https://www.bloft.fi/
https://www.robotmuralist.com/albert


model sun > 8 ropes & lens > light cones > ellipsys on sandbed
	bonus points when normal to Sun
learn ellipsys -> motor speeds (+/-/0)
	state0 -to-> stateN via speed chunks
		may assume only one (2) speed setting(s)
genetic?


So for my solar printer project I need to come up with the reverse kinematics so as to trace a light path on the sand surface
You sent
Meaning: I have to trace this path on the ground with sunlight, how do I move each of the 8 cables to achieve this path?
You sent
I'd like to learn that task instead of coming up with the maths. I have a camera looking at the ground + 3-4 reference points to correct the trapeze of the camera (since the webcam is a bit above the ground)
You sent
I found https://deepmind.com/blog/announcements/mujoco which I believe can help with data generation. I plan to simulate 8 rigid cables, one at each corner of a cube. Each cable is attached to a square plane in the middle of the cube (2 cables per corner of the plane, one coming for above one from below). Then I have two cones coming out of that square (ie. my lens). The cones connect at the lens' focal length. Then, from moving each cable I can look at the intersection of these cones with the ground (an ellipsis).
Now my learning task is to control how to move the cables so that the intersection is close to being a dot. Others have solved the maths before so I guess this should be learnable...
My question then: what kind of AI model should I be training on this synthetic data (8 motor input speeds [-1;1] + ellipsis shape and position relative to the center of the ground) ? An LSTM?
*cdpr inverse kinematics*
Jean-Pierre Merlet
	https://www-sop.inria.fr/members/Jean-Pierre.Merlet/merlet_eng.html
	https://scholar.google.com/citations?hl=en&user=3EsGMmwAAAAJ&view_op=list_works&sortby=pubdate
21, Mixing neural networks and the Newton method for the kinematics of simple cable-driven parallel robots with sagging cables
15, Kinematics and statics of cable-driven parallel robot by interval-analysis-based methods
[21, Efficient Kinematics of a 2-1 and 3-1 CDPR with Non-elastic Sagging Cables](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3EsGMmwAAAAJ&sortby=pubdate&citation_for_view=3EsGMmwAAAAJ:zGdJYJv2LkUC)
[20, The Prince’s tears, a large cable-driven parallel robot for an artistic exhibition](https://sci-hub.ru/10.1109/ICRA40945.2020.9197011)
[04, Multi-criteria optimal design of parallel manipulators based on interval analysis](https://www-sop.inria.fr/teams/hephaistos/PDF/fang_merlet_mmt_2005.pdf)
[04, Interval method for calibration of parallel robots: Vision-based experiments](https://sci-hub.ru/10.1016/j.mechmachtheory.2006.03.014)

https://docs.lyceum.ml/dev/lyceumai/algorithms/naturalpolicygradient/

[19, Control of a Cable-Driven Parallel Robot via Deep Reinforcement Learning](https://sci-hub.ru/downloads/2020-06-01/19/ma2019.pdf?rand=618b670bb68cd)

https://github.com/RobotLocomotion/drake/tree/99e87e7a94158a591c9b1cdd6255109f3dd3a723/examples/multibody/strandbeest/model

https://github.com/bencbartlett/3D-printed-mirror-array

crazy art with CDPRs
https://www.arn.land/
