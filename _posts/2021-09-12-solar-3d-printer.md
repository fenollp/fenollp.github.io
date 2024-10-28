---
wip: true
title: "Solar 3D Printer: my take on Markus Kayser's Solar Sinter"
layout: post
categories: [solar, printer, sustainable, solarpunk, vitrifier]
permalink: solar-3d-printer
---

Following up on [this hastily edited post](https://fenollp.github.io/concentrated-solar-for-infrastructure-and-fuel) about using the Sun to extract some form of hydrogen and to decarbonate part of the construction industry, I present this *Solar Desert Sand Vitrifier* I have been working on.

![MuJoCo simulation](./assets/sha256/6cfb26c4ab7dd416e081ab41745524a28ecf219222d4b57b2e8903f277a859f5.png)
[Link to simulation code](https://github.com/fenollp/solar-desert-sand-vitrifier/tree/61219d88fccb471e1ac77019ed788ead39c79db9) and [to the simulator: MuJoCo](https://mujoco.org/).


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

### Imaging lens
Let's engineer a brick-printing lens: a Fresnel lens that produces a rectangular image so that the lens needn't be moved on x-y (it only needs to be normal to the Sun).
* *Blender: simulate parametric fresnel lens to produce a specific image* (instead of point-focus or linear)
* [github.com/rafael-fuente/diffractsim](https://github.com/rafael-fuente/diffractsim)

### ultra thin lenses
* [https://youtu.be/CT_9EyOCivU?t=23](https://youtu.be/CT_9EyOCivU?t=23)
* [https://www.solarbrother.com/en/buy/fresnel-lens-xl/](https://www.solarbrother.com/en/buy/fresnel-lens-xl/)
* [https://heliac.dk/](https://heliac.dk/)
	* *Unfortunately, we will not be able to support you as we have decided to no longer sell lenses but only focus on our large-scale, integrated solar fields for industries and district heating.*
	* *For the same reason we will not be able to develop a custom lens mold.*
	* [Heliac's 2018 Solar Cooker](https://static.wikia.nocookie.net/solarcooking/images/7/71/L15_Heliac_Solar_Cooker_Presentation.pdf/revision/latest?cb=20180315185906#page=8)
		* | Focal length (cm) | Spot size (cm) | Length (cm) | Width (cm) | Weight (g) | Cost (€) |
		|---|---|---|---|---|---|
		| 200 | 8 | 140 | 109 | 300 | 10 |
		| 73 | 1 | 82 | 48 | 70 | 5 |

---
..WIP..

---


## Large print volume

* `co2 emitted per kg of plastic vs aluminum`
* `lifetime of plastic vs aluminum`
* `strength of 3d printed screws`
	* `hollow screws are possible`


* `ask asca films for enough samples to cover outside cube frame with such that there is enough power outputed to not require non-organic ones`


* `make parts of the corner pieces removeable so some can be replaced and even upgraded or help grow larger scale iteration`


* `in the end the printer may look like a plastic kleenex`
	* `use thermoplasticity to create a Fresnles lens + stand that follows the Sun (Tournesol) faster than the print head has to move`


* `the more shippable the printer the better chance it has of selling kits`


* `open cable robot project`
	* [https://hackaday.io/project/166527/components](https://hackaday.io/project/166527/components)


# motors
* [https://reprap.org/wiki/NEMA_17_Stepper_motor](https://reprap.org/wiki/NEMA_17_Stepper_motor)

* [https://makersportal.com/blog/raspberry-pi-stepper-motor-control-with-nema-17](https://makersportal.com/blog/raspberry-pi-stepper-motor-control-with-nema-17)
	* Raspberry Pi pins
		* V    [https://pinout.xyz/pinout/5v_power](https://pinout.xyz/pinout/5v_power)
		* G    [https://pinout.xyz/pinout/ground](https://pinout.xyz/pinout/ground)
		* DIR  [https://pinout.xyz/pinout/pin15_gpio22](https://pinout.xyz/pinout/pin15_gpio22)
		* STEP [https://pinout.xyz/pinout/pin16_gpio23](https://pinout.xyz/pinout/pin16_gpio23)
		* EN   [https://pinout.xyz/pinout/pin18_gpio24](https://pinout.xyz/pinout/pin18_gpio24)
	* Python
		* [https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11DRV8825.md](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11DRV8825.md)
		* [https://github.com/gavinlyonsrepo/RpiMotorLib/blob/fd166f1c6501d9c8ee18f57fa81329445ce244c8/test/MultiMotorThreading_DRV8825.py](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/fd166f1c6501d9c8ee18f57fa81329445ce244c8/test/MultiMotorThreading_DRV8825.py)
* `=> enough pins in just one RPi?`

* [https://www.omc-stepperonline.com/sale.html/clearance-sale-nema-17-stepper-motor-bipolar-l-48mm-w-gear-ratio-27-1-planetary-gearbox.html](https://www.omc-stepperonline.com/sale.html/clearance-sale-nema-17-stepper-motor-bipolar-l-48mm-w-gear-ratio-27-1-planetary-gearbox.html)
	* [https://www.omc-stepperonline.com/download/17HS19-1684S-PG27.pdf](https://www.omc-stepperonline.com/download/17HS19-1684S-PG27.pdf)
	* 17HS19-1684S-PG27
	* Motor Type: Bipolar Stepper
	* Holding Torque without Gearbox: 52Ncm(73.6oz.in)
	* Planetary Gear Ratio: 26.85: 1
	* $24
	* => `52*26.85/100 N.m`
		* => `~1.4kg` max hold per motor
	* <img src="https://m.media-amazon.com/images/I/31cKfwDcIqL._AC_.jpg"/>
		* A BLK A+ 1B
		* C GRN A- 1A
		* B RED B+ 2B
		* D BLU B- 2A
* 2b 2a 1a 1b
* red blu grn blk


* [https://www.amazon.fr/drv8825-Module-dissipateur-thermique-exemple-Imprimante/dp/B01JIW13RY](https://www.amazon.fr/drv8825-Module-dissipateur-thermique-exemple-Imprimante/dp/B01JIW13RY)
	* DRV8825 / A4988 motor driver
	* ~ 4EUR per motor

* [https://www.amazon.fr/Jeanoko-Control-Shield-DRV8825-imprimante/dp/B08VVZZB81](https://www.amazon.fr/Jeanoko-Control-Shield-DRV8825-imprimante/dp/B08VVZZB81)
	* support for DRV8825 / A4988
	* ~ 6EUR per motor

* [https://www.amazon.fr/CQRobot-Pieces-JST-PH-Connector-Female/dp/B0731MZCGF](https://www.amazon.fr/CQRobot-Pieces-JST-PH-Connector-Female/dp/B0731MZCGF)
	* JST 2mm 4p connector
		* stepper motor -to-> DRV8825 support card

* [https://www.adafruit.com/product/2348](https://www.adafruit.com/product/2348)
	* RPi HAT
	* USD23 / each adds 2 steppers
	* [https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
	* 1.2-3A
	* 4.5-13.5VDC
	* stacking header
		* [https://www.adafruit.com/product/2223](https://www.adafruit.com/product/2223)
		* USD3

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
Curtain pole (interior diameters) (Castorama)
* 28mm 2.5m wood(ash) 11€/m
* 16mm 2.5m metal(brass) 5€/m
* 19mm 2.5m metal(white|black) 7€/m
* 19mm 2.5m metal(brass) 8€/m
* 28mm 2.5m metal(brass) 13€/m
* 28mm 2.5mm metal(nickel) 12€/m
* See also: elbow connector 10-13€/p, bracket 11-15€/p.


<img src="https://www.researchgate.net/publication/320437261/figure/fig2/AS:550578309025792@1508279506553/The-collector-is-designed-using-two-linear-Fresnel-lenses-which-are-perpendicular-to.png"/>
* [(2020) Indoor daylighting using Fresnel lens solar-concentrator-based hybrid cylindrical luminaire for illumination and water heating](https://opg.optica.org/ao/abstract.cfm?uri=ao-59-18-5358)

## European Standard Rail Aluminum Extrusion Profile
* EUR7 per meter
	* [https://www.aliexpress.com/item/1005002453943888.html](https://www.aliexpress.com/item/1005002453943888.html)
* EUR53 [Infrared Thermometer,High Temp Thermometer Pyrometer -58℉- 2732℉ (-50℃ to 1500℃),30:1 Distance Spot Ratio,AP-2732 Non-Contact Digital Dual Laser Pointers Flashlight IR Temperature Gun【NOT for Human】](https://www.amazon.com/Infrared-Thermometer-58%E2%84%89-2732%E2%84%89-1500%E2%84%83/dp/B07PHQ9YG9/)

## Photocatalytic water splitting

* [(2010), Efficient Solar Hydrogen Production by Photocatalytic Water Splitting: From Fundamental Study to Pilot Demonstration](https://sci-hub.ru/10.1016/j.ijhydene.2010.01.030)
	* *The object of our work is to explore the possibility of mass solar hydrogen production by coupling photocatalytic reactors with solar light concentrators*
	* *a hydrogen production rate of 0.164 L/h per unit volume*
	* *this technology to be economic[ally] viable in the near future*
	* it is necessary to narrow the band gap of photocatalysts to harvest visible-light*
* [(2013), Metal sulphide semiconductors for photocatalytic hydrogen production](https://sci-hub.ru/10.1039/c3cy00018d)
	* *sulphide semiconductor photocatalysts have excellent solar spectrum responses and high photocatalytic activities*
	* *we highlight the crucial issues in the development of highly efficient sulphide photocatalysts without noble metal cocatalysts*
	* *These studies show not only the possibility of utilizing low cost carbon materials as a substitute for noble metals (such as Pt) in the photocatalytic H2-production but also a significant enhancement in the H2-production activity using metal-free carbon materials as effective co-catalysts.*
* [(2020), Ultrafine nano 1T-MoS2 monolayers with NiOx as dual co-catalysts over TiO2 photoharvester for efficient photocatalytic hydrogen evolution](https://sci-hub.ru/10.1016/j.apcatb.2020.119387)
* [(2020), Recent progress on ammonia fuel cells and their potential applications](https://sci-hub.ru/10.1039/d0ta08810b)
	* *ammonia fuel cells offer a clean and reliable energy source, which can mitigate many of the limitations associated with hydrogen economy and contribute to a more nearby sustainable future*
* [(2021) Photocatalytic solar hydrogen production from water on a 100-m2 scale](https://www.nature.com/articles/s41586-021-03907-3)
	* *we here report safe operation of a 100-m2 array of panel reactors over several months with autonomous recovery of hydrogen from the moist gas product mixture using a commercial polyimide membrane*
	* *While the hydrogen production is inefficient and energy negative overall, our findings demonstrate that safe, large-scale photocatalytic water splitting, and gas collection and separation are possible.*

* [Is PLA heat resistant? ABS, ASA, PETG and more](https://3dsolved.com/is-pla-heat-resistant-abs-asa-petg-and-more/)
	* *PC: Polycarbonate (resists 150°C) but is on the expensive side & often blended for those of us without an industrial-grade 3d printer*
	* *ABS (resists 105°C) cheap, tough but careful with the toxic fumes*

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PBNUb04DoZs?si=CaSbKr7T6ZTjzvwG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
* [(2021) Motor Current Based Force Control of Simple Cable-Driven Parallel Robots](https://link.springer.com/chapter/10.1007/978-3-030-75789-2_22)
* [https://ropebot.eu](https://ropebot.eu)
	* **Jonas & Konrad** from ropebot.eu
* <!-- PaperCableCon21.pdf -->
<img src="https://ropebot.eu/wp-content/uploads/2021/08/cropped-WauBie3-scaled-1.jpg"/>

## Motors
* [https://discourse.odriverobotics.com/t/nema-enclosures-for-d5065-and-d6374-motors/830/8](https://discourse.odriverobotics.com/t/nema-enclosures-for-d5065-and-d6374-motors/830/8)

## Cameras
* [https://webcamtests.com/](https://webcamtests.com/)
* 15EUR [TAKRINK Webcam 1080P Webcaméra Cybercaméra Ordinateur Microphone Intégré Port USB avec Couvercle de Webcam Trépied pour Chat Vidéo et Enregistrement](https://www.amazon.fr/TAKRINK-Cybercam%C3%A9ra-Ordinateur-Microphone-Enregistrement/dp/B08NX3MVBQ)
* 30EUR grand angle=>all feets in picture [Webcam PC 1080p HD - eMeet Nova Webcam Streaming Mise au Point Automatique avec Double Microphone, Web caméra USB pour Ordinateur Portable, Grand Angle 96°, Plug & Play, pour Linux, Win10, Mac](https://www.amazon.fr/Webcam-1080p-Automatique-Microphone-Ordinateur/dp/B09B6SYG1M)
* ["Run openpilot with webcam on PC"](https://github.com/commaai/openpilot/tree/31228ce5605b6ba231ac09e22fd41946bf80ab36/tools/webcam#run-openpilot-with-webcam-on-pc)
	* *at least 720p and 78 degrees FOV (e.g. Logitech C920/C615)*
* [https://openmv.io/collections/cams/products/openmv-cam-h7-plus](https://openmv.io/collections/cams/products/openmv-cam-h7-plus)

## Vision things
* `reflective film`
	* EUR10 [Salzmann 3M Diamond Grade Autocollants réfléchissants imperméables Équipée de 3M Scotchlite Autocollants pour les voitures, les motos, les bicyclettes - 4pcs](https://www.amazon.fr/Salzmann-Autocollants-r%C3%A9fl%C3%A9chissants-imperm%C3%A9ables-bicyclettes/dp/B00QX39BVM/)
	* EUR9 [24 Pcs Autocollants Réfléchissants d'Avertissement Stickers Réfléchissants de Sécurité Stickers de Visibilité Nocturne Autocollants de Bande Imperméables pour Véhicule, 1,18 x 3,25 Pouces](https://www.amazon.fr/Autocollants-R%C3%A9fl%C3%A9chissants-dAvertissement-Visibilit%C3%A9-Imperm%C3%A9ables/dp/B08QZ2FQ34)
	* EUR5 [Wowow 3M Bande réfléchissante - Ruban adhésif - Reflective tape - Blanc](https://www.amazon.fr/Wowow-3M-Bande-r%C3%A9fl%C3%A9chissante-Blanc/dp/B000Z2ITVU)
	* EUR12 [10M Ruban D'avertissement Réfléchissant, ONTWIE Sécurité Réfléchissant Avertissement éclairage Autocollant Ruban Adhésif Rouleau Bande, Couleurs Blanches pour Beautify Vélo Moto Décoration - 2.5cm](https://www.amazon.fr/Davertissement-R%C3%A9fl%C3%A9chissant-ONTWIE-Avertissement-Autocollant/dp/B07PN8QTPZ)
	* EUR15 [ONTWIE Ruban Réfléchissant étanche Haute Visibilité Marquage Industriel Danger Heavy Duty Attention Attention Ruban Auto-adhésif de Sécurité Extérieur - Rouge 10M](https://www.amazon.fr/ONTWIE-R%C3%A9fl%C3%A9chissant-Visibilit%C3%A9-Industriel-Auto-adh%C3%A9sif/dp/B08QMKC551)
* [4 Point OpenCV getPerspective Transform Example](https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/)

## Fibers
* [Dyneema braided x12, 0.18mm diameter, 16.22kg, 130m for 30EUR](https://www.decathlon.fr/p/tresse-de-peche-aux-leurres-tx12-grise-130-m/_/R-p-306977)
	* `=> 0,24€/m`
	* Should hold my <5kg loads. Maybe I should've gone for a thicker string?
	* Anyway that is 5x cheaper than the 1EUR/meter string that was mentioned.
* [VGEBY Pêche Split Rings, 200 Pcs 5Tailles Heavy Duty Acier Inoxydable Split Anneaux Solide Connecteurs De Pêche Attirail De Pêche](https://www.amazon.fr/VGEBY-5Tailles-Inoxydable-Connecteurs-Attirail/dp/B07TVT8YSH/)
* [Dovesun Fishing Rod Repair Kit Fishing Rod Guide Repair Kit Rod Ceramic Guides Ring 12 Sizes 0.15in to 1.18in](https://www.amazon.com/Dovesun-Fishing-Repair-Kit-Rod-Ceramic/dp/B08RNMSBN5/)
* **Tobben from Hangprinter**
	* *used in v4 = ceramic ring from sewing machines*
* EUR14 [MaoXinTek Guides pour Canne à Pêche, 80 pièces Kit de Réparation Anneau Guide de Pêche Céramique en Acier Inoxydable et Carbone pour Canne à pêche télescopique](https://www.amazon.fr/MaoXinTek-R%C3%A9paration-C%C3%A9ramique-Inoxydable-t%C3%A9lescopique/dp/B08NJMP3DX/)
* [Company Makes Bikes With Strings Instead Of Chains](https://www.youtube.com/watch?v=6NVRd8B-VmU)
* EUR9 [300m Dyneema Spectra Extreame Braided Fishing Line Super Strong Multifilament 4 Stands Fishing Wire](https://www.joom.com/en/products/1512468169939706457-112-1-26193-1551209324)
* EUR45 [Kanirope® Corde dyneema PRO 1mm 100m noir 12x tressée SK78 pré-étirée enrobée](https://www.amazon.fr/Corde-Cordage-Dyneema-100m-tress%C3%A9/dp/B00NHQC1FQ)

* EUR20 [32 Channel Digital Expansion HAT for Raspberry Pi](https://www.robotshop.com/eu/en/32-channel-digital-expansion-hat-raspberry-pi.html)

* [**Cable robots videos**](https://www.youtube.com/playlist?list=PLwDcOJWL58gYBzDNXOi2dURGvxXAQk3oq)

* [https://hackaday.com/2017/10/12/this-3d-cable-printer-remixes-the-delta/](https://hackaday.com/2017/10/12/this-3d-cable-printer-remixes-the-delta/)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ul78heZUyfM?si=UaPGFOXV6ecvBT6q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

* [(2020) A new control scheme of cable-driven parallel robot balancing between sliding mode and linear feedback](https://hal.archives-ouvertes.fr/hal-02515924/document)
<!-- Screenshot from 2021-10-12 00-29-38.png -->


* `cable robot camera stand`
* `future: CDPR`
	* `stackable`
	* `can climb up/down`
	* `can extend frame`
	* `cable holders can move/rotate/slide on the inner frame so multiple CDPRs can work in a tight volume simultaneously`

## Name?
* not: `Shai-Hulud` [https://dune.fandom.com/wiki/Shai-Hulud](https://dune.fandom.com/wiki/Shai-Hulud)
* not: the `drej`
* le peuple des dunes en breton: `erin` [https://geriafurch.bzh/fr/brfr/erin](https://geriafurch.bzh/fr/brfr/erin)
	* dune de sable / dune sablonneuse : `erin`
	* sable fin : `traezh munut`
	* sable / sable maritime / sable de mer : `traezh`
	* dune : `tevenn`
* `Voir le monde dans un grain de sable` ~ William Blake

## Crucibles
* EUR16 [Foundry Clay Graphite Crucibles Black Cup Furnace Torch Melting Casting Refining Gold Silver Copper Brass Aluminum](https://www.amazon.com/MegaCast-Graphite-Crucibles-Refining-Aluminum/dp/B075CT9FLX/)
* EUR11 [Moule De Fonderie De Fonte De Coulée De Graphite De Grande Pureté De Werse Pour L'Or Et L'Argent - 750G](https://www.amazon.fr/Fonderie-Coul%C3%A9e-Graphite-Werse-LArgent/dp/B07HG5Z62M)
* EUR18 [Pomcat Gants résistants à la chaleur d’un fourneau pour le raffinage des métaux précieux 33 cm](https://www.amazon.fr/Pomcat-r%C3%A9sistant-chaleur-s%C3%A9curit%C3%A9-Demeurant/dp/B077NGWXKX/)


<img alt="Toghrol Tower" src="https://i.pinimg.com/originals/c5/cc/a1/c5cca19e4c24dfb2d273d62cbc4f5e52.jpg"/>

* [https://www.sandhelden.de/about-us](https://www.sandhelden.de/about-us)

* [https://www.trinamic.com/products/integrated-circuits/](https://www.trinamic.com/products/integrated-circuits/)

* [https://www.thingiverse.com/thing:2932583](https://www.thingiverse.com/thing:2932583)
* `thread spool guide`
	* `thread groove`
	* [https://www.thingiverse.com/thing:3184816](https://www.thingiverse.com/thing:3184816)
		* `wear_groove_NB.stl`
* `joints`
	* `tetra angle joinery`
	* [https://www.thingiverse.com/thing:996842](https://www.thingiverse.com/thing:996842)
* [https://github.com/SolidCode/SolidPython](https://github.com/SolidCode/SolidPython)
* [https://github.com/openscad/openscad](https://github.com/openscad/openscad)
* `held tightly to the motor shaft with a set screw in an inserted nut`
	* [https://www.goilacog.com/index.php?main_page=product_info&products_id=148603](https://www.goilacog.com/index.php?main_page=product_info&products_id=148603)
	* `lead screw`
	* [https://www.thingiverse.com/thing:40642/files](https://www.thingiverse.com/thing:40642/files)
		* `AJGW-GearsHering_Small.stl`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WWrb1iyCLlI?si=8p-dwL_Nte3BBlwz&amp;start=152" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!-- printer-types.png -->
* [Low cost metal 3D printing! Electrochemical additive manufacturing](https://www.youtube.com/watch?v=B-UbDk7LrvU)
* <img src="https://static.wixstatic.com/media/71b5b3_149ccc51b79949b7af398395f6b92f0f~mv2.jpg/v1/fill/w_1269,h_1269,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/71b5b3_149ccc51b79949b7af398395f6b92f0f~mv2.jpg"/>
	* [https://www.bloft.fi/](https://www.bloft.fi/)


* `model sun` > `8 ropes & lens` > `light cones` > `ellipsys on sandbed`
	* `bonus points when normal to Sun`
* `learn ellipsys` -> `motor speeds (+/-/0)`
	* `state0` -to-> `stateN` via speed chunks
		* `may assume only one (2) speed setting(s)`
* `genetic?`


```
So for my solar printer project I need to come up with the reverse kinematics so as to trace a light path on the sand surface
Meaning: I have to trace this path on the ground with sunlight, how do I move each of the 8 cables to achieve this path?
I'd like to learn that task instead of coming up with the maths. I have a camera looking at the ground + 3-4 reference points to correct the trapeze of the camera (since the webcam is a bit above the ground)
I found https://deepmind.com/blog/announcements/mujoco which I believe can help with data generation. I plan to simulate 8 rigid cables, one at each corner of a cube. Each cable is attached to a square plane in the middle of the cube (2 cables per corner of the plane, one coming for above one from below). Then I have two cones coming out of that square (ie. my lens). The cones connect at the lens' focal length. Then, from moving each cable I can look at the intersection of these cones with the ground (an ellipsis).
Now my learning task is to control how to move the cables so that the intersection is close to being a dot. Others have solved the maths before so I guess this should be learnable...
My question then: what kind of AI model should I be training on this synthetic data (8 motor input speeds [-1;1] + ellipsis shape and position relative to the center of the ground) ? An LSTM?
```
## cdpr inverse kinematics
* Jean-Pierre Merlet
	* [https://www-sop.inria.fr/members/Jean-Pierre.Merlet/merlet_eng.html](https://www-sop.inria.fr/members/Jean-Pierre.Merlet/merlet_eng.html)
	* [https://scholar.google.com/citations?hl=en&user=3EsGMmwAAAAJ&view_op=list_works&sortby=pubdate](https://scholar.google.com/citations?hl=en&user=3EsGMmwAAAAJ&view_op=list_works&sortby=pubdate)
* [(2021) Mixing neural networks and the Newton method for the kinematics of simple cable-driven parallel robots with sagging cables](https://doi.org/10.1109/ICAR53236.2021.9659400)
* [(2015) Kinematics and statics of cable-driven parallel robot by interval-analysis-based methods](https://theses.hal.science/tel-01516606/document)
* [(2021) Efficient Kinematics of a 2-1 and 3-1 CDPR with Non-elastic Sagging Cables](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3EsGMmwAAAAJ&sortby=pubdate&citation_for_view=3EsGMmwAAAAJ:zGdJYJv2LkUC)
* [(2020) The Prince’s tears, a large cable-driven parallel robot for an artistic exhibition](https://sci-hub.ru/10.1109/ICRA40945.2020.9197011)
* [(2004) Multi-criteria optimal design of parallel manipulators based on interval analysis](https://www-sop.inria.fr/teams/hephaistos/PDF/fang_merlet_mmt_2005.pdf)
* [(2004) Interval method for calibration of parallel robots: Vision-based experiments](https://sci-hub.ru/10.1016/j.mechmachtheory.2006.03.014)

* [https://docs.lyceum.ml/dev/lyceumai/algorithms/naturalpolicygradient/](https://docs.lyceum.ml/dev/lyceumai/algorithms/naturalpolicygradient/)

* [(2019) Control of a Cable-Driven Parallel Robot via Deep Reinforcement Learning](https://sci-hub.ru/downloads/2020-06-01/19/ma2019.pdf?rand=618b670bb68cd)
* [rlcoach](https://github.com/IntelLabs/coach)
* [https://www.gshi.me/blog/NeuralControl/](https://www.gshi.me/blog/NeuralControl/)
* [https://github.com/RobotLocomotion/drake/tree/99e87e7a94158a591c9b1cdd6255109f3dd3a723/examples/multibody/strandbeest/model](https://github.com/RobotLocomotion/drake/tree/99e87e7a94158a591c9b1cdd6255109f3dd3a723/examples/multibody/strandbeest/model)

* [https://github.com/bencbartlett/3D-printed-mirror-array](https://github.com/bencbartlett/3D-printed-mirror-array)

## crazy art with CDPRs
* [https://www.arn.land/](https://www.arn.land/)

<blockquote class="twitter-tweet" data-theme="dark"><p lang="en" dir="ltr">Caption this <a href="https://t.co/5E0HmXfLWy">pic.twitter.com/5E0HmXfLWy</a></p>&mdash; Amazing Physics (@amazing_physics) <a href="https://twitter.com/amazing_physics/status/1477505125006680064?ref_src=twsrc%5Etfw">January 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## large-scale seawater desalination plant

* [https://github.com/aidanscannell/pilco-tensorflow](https://github.com/aidanscannell/pilco-tensorflow)
* [https://github.com/deepmind/dm_control/blob/master/dm_control/mjcf/README.md](https://github.com/deepmind/dm_control/blob/master/dm_control/mjcf/README.md)
* [https://github.com/openai/mujoco-py/blob/master/examples/markers_demo.py](https://github.com/openai/mujoco-py/blob/master/examples/markers_demo.py)
* [https://github.com/deepmind/acme](https://github.com/deepmind/acme)

<img src="https://i.redd.it/cnu760qb2hc81.jpg"/>

## helical piling
* [https://en.wikipedia.org/wiki/Screw_piles](https://en.wikipedia.org/wiki/Screw_piles)

* [https://www.designboom.com/architecture/magnus-larsson-sculpts-the-saharan-desert-with-bacteria/](https://www.designboom.com/architecture/magnus-larsson-sculpts-the-saharan-desert-with-bacteria/)

* [https://urbanutopias.net/2019/09/01/arcosanti/](https://urbanutopias.net/2019/09/01/arcosanti/)
* [https://en.wikipedia.org/wiki/Arcosanti](https://en.wikipedia.org/wiki/Arcosanti)
* [https://www.archdaily.com/517456/inside-masdar-city](https://www.archdaily.com/517456/inside-masdar-city)

## dunes divert wind patterns
* [https://en.wikipedia.org/wiki/Sand_dune_stabilization](https://en.wikipedia.org/wiki/Sand_dune_stabilization)
* [(2014) Echo Dune](https://link.springer.com/referenceworkentry/10.1007/978-1-4614-9213-9_134-1)
	* *An echo dune is a topographically anchored (static) high-order bedform with a single crescentic slip face parallel to a topographic obstruction (e.g., cliff, rock) ≥60° in slope.*
* **artificial ocean dune**
	* [(2019) Remobilizing stabilized island dunes for keeping up with sea level rise?](https://link.springer.com/article/10.1007/s11852-019-00697-9)
	* [(2005) Artificial Construction of Dunes in the South of Portugal](https://www.jstor.org/stable/4299434)
	* [(2023) Dune construction and strengthening](https://climate-adapt.eea.europa.eu/metadata/adaptation-options/dune-construction-and-strengthening)
	* [(2010) Dune construction and stabilisation](https://www.ctc-n.org/technology-library/protection-hard-engineering/dune-construction-and-stabilisation)
* [**compound dunes**](https://www.britannica.com/science/compound-dune)
* **mega-dunes, or draa**
	* [https://www.britannica.com/science/barchan](https://www.britannica.com/science/barchan)
	* [https://en.wikipedia.org/wiki/Iva_(plant)](https://en.wikipedia.org/wiki/Iva_(plant))
	* [https://en.wikipedia.org/wiki/Spartina_patens](https://en.wikipedia.org/wiki/Spartina_patens)
	* [https://en.wikipedia.org/wiki/Hudsonia](https://en.wikipedia.org/wiki/Hudsonia)
	* [https://en.wikipedia.org/wiki/Spartina](https://en.wikipedia.org/wiki/Spartina)
	* [https://en.wikipedia.org/wiki/Cakile_maritima](https://en.wikipedia.org/wiki/Cakile_maritima)
	* [https://en.wikipedia.org/wiki/Honckenya](https://en.wikipedia.org/wiki/Honckenya)
	* [https://en.wikipedia.org/wiki/Ammophila_arenaria](https://en.wikipedia.org/wiki/Ammophila_arenaria)
* [(2008) Chapter Three: Topography of the Great Sand Sea](https://www.sciencedirect.com/science/article/abs/pii/S0070457107100042)
* [(2013) Suitability of Recycled Glass Cullet as Artificial Dune Fill along Coastal Environments](https://www.researchgate.net/publication/236962695_Suitability_of_Recycled_Glass_Cullet_as_Artificial_Dune_Fill_along_Coastal_Environments)

<!-- 
https://www.3fstudio.de/news
	https://www.mae.ed.tum.de/en/cbm/about-us/staff-a-z/matthaeus-carla/
		>>> when prototype is ready, to iterate
		also: Julian +49 177 4838602 from TU Munich, works on clay+timber slabs
 -->

## lens support structure
* [Profilé de carrelage intérieur Diall rond PVC noir lisse 23mmx250cm](https://www.castorama.fr/profile-de-carrelage-interieur-diall-rond-pvc-noir-lisse-23mmx250cm/3663602911838_CAFR.prd?storeId=1420)
* [GAH PROFILÉ D'ARRÊT À CARRELAGE](https://www.manomano.fr/p/gah-profile-darret-a-carrelage-3343681)
* [Profilé de finition aluminium L.2,50m H.6mm](https://www.google.com/shopping/product/4333842615611326270?q=PROFIL%C3%89+D%27ARR%C3%8AT+CARRELAGE&sxsrf=APq-WBtoxXcoxCZIXeepiX_AwJIZUi71UQ:1648063369914&biw=1536&bih=754&dpr=1.25&prds=eto:11807279368339208278_0,rsk:PC_12485619535725637494&sa=X&ved=0ahUKEwiZ6u2--tz2AhXMxoUKHQFHCToQ8gIIjgsoAA)
* [Profilés de finition chrome pour panneau mural - 2 profilés de 10x5x2100 mm – FINISH MURAL CHROME](https://www.manomano.fr/p/profiles-de-finition-chrome-pour-panneau-mural-2-profiles-de-10x5x2100-mm-finish-mural-chrome-40984012)

## building strong is the backbone of society
* **frame**
* `Truffaut support bâton 180cm 16mm 12x3.99€`
* `70EUR Tonnelle pliante 3 x 3 M - Tecto Bleu - tente de jardin Pop UP, Pergola pliable, Barnum`
	* [Google Shopping](https://www.google.com/shopping/product/11279253279860043085?q=tente+barnum+pliable&hl=en&sxsrf=APq-WBs44_rrZxhErKQ3jyugey8dOzr8Vw:1648650231975&uact=5&oq=tente+barnum+pliable&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgYIABAWEB4yCAgAEBYQHhAYMggIABAWEB4QGDIICAAQFhAeEBgyCAgAEBYQHhAYMggIABAWEB4QGDIICAAQFhAeEBgyCAgAEBYQHhAYMggIABAWEB4QGDoECAAQQzoFCAAQgAQ6BAgAEBg6BAgAEBM6CAgAEBYQHhATOgoIABAWEB4QExAYSgQIQRgBUPUEWLkjYNAkaANwAHgAgAGCAYgBvAqSAQQxOC4xmAEAoAEBwAEB&sclient=products-cc&prds=eto:12845507702489222954_0,rsk:PC_9907812213786617354&sa=X&ved=0ahUKEwjN2cHjhO72AhWD4YUKHfGZDK4Q8gIIjAooAA)
	* [Leroy Merlin](https://www.leroymerlin.fr/produits/terrasse-jardin/parasol-tonnelle-et-store/tonnelle-pergola/tonnelle-et-pergola-autoportante/tonnelle-pliante-3-x-3-m-tecto-bleu-tente-de-jardin-pop-up-pergola-pliable-barnum-9m2-82931846.html?Megaboost)
* **parasol deporte**
	* [Darty](https://www.darty.com/nav/achat/maison_jardin/mobilier_de_jardin/parasol/alice_s_garden_parasol_deporte_carre_3x3m_hardelot_3x3m_rouge_manivelle_anti_retour_toile_deperlante_facile_a_utiliser__MK1220476904.html)
	* [Darty](https://www.darty.com/nav/achat/maison_jardin/mobilier_de_jardin/parasol/alice_s_garden_parasol_deporte_350cm_hardelot_coloris_gris_structure_anthracite_manivelle_anti_retour___MK974705071.html)
	* [Darty](https://www.darty.com/nav/achat/maison_jardin/mobilier_de_jardin/parasol/outsunny_parasol_rectangulaire_inclinable_bois_polyester_haute_densite_2l_x_1_5l_x_2_3h_m_gris_clair__MK399747197.html)
* **pieu vissé**
* **Manivelle anti-retour**
	* **Anti-reverse crank**

<!-- My testing spot https://goo.gl/maps/hqaNupDDLT3Fbqx77 -->

## regolight
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/jVCiPTXYYu8?si=xeqFLw1XipPV5dem" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!-- 
https://github.com/jim-fx/plantarium
* toprint/
 -->


## emergency shutdown
`lens top protection`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/DBbG_yhcP9Q?si=3oyU3dPeHLGkTabU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Another, [bulkier one here](https://www.youtube.com/watch?v=dwY8cJhAhgI)

## numbers
* [Heat production of magnifying glass](https://physics.stackexchange.com/a/103039/267116)
	* **solarbrother**'s lens:
		* `f=200cm` => image radius is `200cm*10e-3 = 2cm` => 4cm2 (ideal) spot size (spec says 8cm)
		* => `(1.05*1.41)/((2 * 10e-3)**2) * 1000` = `3.7MW/m2` ??
	* **NTKJ**'s 120cm focal lens:
		* => `1.44cm2` spot size
* [Calculation of Solar Insolation](https://www.pveducation.org/pvcdrom/properties-of-sunlight/calculation-of-solar-insolation)

## moving frame
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/SjRwflxpEEg?si=GQsIgEbS4bsMs-YP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Making our own Fresnel lenses
* it's not easy...
* [How to Make a Lens Through Silicone Molding](https://www.youtube.com/watch?v=As20UPia718)
* [Make Your Own Optical Lenses](https://www.youtube.com/watch?v=mfAGivG9Koc)
* ...but at scale?
* [**Jelle Seegers**'s Solar Metal Smelter](https://jelleseegers.com/Solar-Metal-Smelter)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WYjmkhCwiA4?si=SjVGoWaNRur-16YQ&amp;start=130" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

> the lens is a fresnel lens machined with a hand made jig from polycarbonate, and afterwards polished with methylene chloride.

<img src="https://freight.cargo.site/w/2000/i/eae693f736437685162f699878c3bdc758e1f2d1f8dae6a7be12bda891d746d1/Totaalbeeld-Solar-Metal-Smelter-2.jpg"/>

## pulleys
* [WINSINN GT2 Pulley 20 Teeth 8mm bore 6mm Width 20T Timing Belt Pulley Wheel Aluminum for 3D Printer (Pack of 5Pcs)](https://www.amazon.com/WINSINN-Aluminum-Synchronous-Timing-Printer/dp/B077GMKW1C/ref=pd_bxgy_sccl_1/131-0002034-1252970)

## powering steppers off
* **stepper enable toggle fast**
* [https://forum.arduino.cc/t/stepper-control-with-multiple-momentary-toggles/555587/4](https://forum.arduino.cc/t/stepper-control-with-multiple-momentary-toggles/555587/4)
* **stepper complete shutdown**
	* [https://electronics.stackexchange.com/questions/418686/power-down-sequencing-with-a-hard-power-switch-stepper-driver](https://electronics.stackexchange.com/questions/418686/power-down-sequencing-with-a-hard-power-switch-stepper-driver)
* [https://marlinfw.org/docs/gcode/M018.html](https://marlinfw.org/docs/gcode/M018.html)
* **stepper disable shutdown**
	* [https://github.com/Klipper3d/klipper/issues/906](https://github.com/Klipper3d/klipper/issues/906)
* [https://forum.arduino.cc/t/turning-off-a-stepper-motor-with-code-not-hardware/354506](https://forum.arduino.cc/t/turning-off-a-stepper-motor-with-code-not-hardware/354506)

## rpi4 auto-join wifi list
* [https://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/](https://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/)

## heat reflector + windscreen
* [ASR Outdoor 10 Panel Wind Shield Heat Reflector Compact Collapsible Aluminum Panels](https://www.amazon.com/ASR-Outdoor-Reflector-Collapsible-Removable/dp/B07CPGFN9F)
* [https://www.screwfix.com/p/radiator-reflector-foil-470mm-x-4m-1-88m/88629](https://www.screwfix.com/p/radiator-reflector-foil-470mm-x-4m-1-88m/88629)
* [https://www.wildernessshop.com.au/products/msr-heat-reflector-windscreen-all-models](https://www.wildernessshop.com.au/products/msr-heat-reflector-windscreen-all-models)
* **reflecteur mirolege**

## xy cable system
* **synchromesh drive system**
* [Positron V3.2 BOM V5](https://docs.google.com/spreadsheets/d/1M--jvOxUEVNc-NtEsor3uPZQsdXsPD1CKWxmc8fwLWI/edit#gid=1902140897)
* [Synchromesh Drive Systems](https://www.sdp-si.com/products/Timing-Belts-and-Cables/Synchromesh-Drive-Systems.php)
	* <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0GMzYMI6rf8?si=xJ2mr9cOlJsJU8HK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
* [Very Large Cable Driven CoreXY Mechanism](https://reprap.org/forum/read.php?397,830177)
	* [cables](https://vimeo.com/282957836) [belts](https://vimeo.com/286113087)
	* [CoreXY Mechanism Layout and Belt Tensioning](https://drmrehorst.blogspot.com/2018/08/corexy-mechanism-layout-and-belt.html)

* fresnel lens on a roll + engineer lens so projected image is a slice of silhouette + only moving part is lens rolling and sand layer deposition
