// openscad - -o - --export-format binstl <_/light.scad >_/lightcone.stl

cylinder(h=1.2, d1=0, d2=1.05, center=false, $fn=500);
// translate([0,0,-1.2])
//     cylinder(h=1.2, d1=0.5, d2=0, center=false, $fn=500);
translate([0,0,1.2])
    cylinder(h=1.2, d=1.05, center=false, $fn=500);
