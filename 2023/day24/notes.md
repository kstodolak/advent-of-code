# Part1

Line equation: ax + by = c

Any point:

P<sub>h</sub> = (x, y) + t * (V<sub>x</sub>, V<sub>y</sub>)

t = (P<sub>x</sub> - x) / V<sub>x</sub> = (P<sub>y</sub> - y) / V<sub>y</sub>

Without t:

(P<sub>x</sub> - x) / V<sub>x</sub> = (P<sub>y</sub> - y) / V<sub>y</sub>

V<sub>y</sub>(P<sub>x</sub> - x) = V<sub>x</sub>(P<sub>y</sub> - y)

V<sub>y</sub>P<sub>x</sub> - V<sub>x</sub>P<sub>y</sub> = V<sub>y</sub>x - V<sub>x</sub>y

So:

**a = V<sub>y</sub>**

**b = -V<sub>x</sub>**

**c = V<sub>y</sub>x - V<sub>x</sub>y**


To find intersection we have to solve system of 2 linear equations

a1x + b1y = c1

a2x + b2y = c2

finding x and y:

**x = (b2c1 - b1c2) - (a1b2 - a2b1)**

**y = (c2a1 - c1a2) / (a1b2 - a2b1)**


# Part 2

To find common point with rock and hailstone it must be true for some t:

x<sub>r</sub> + Vx<sub>r</sub> * t = x<sub>p</sub> + Vx<sub>p</sub> * t

Then:

Vx<sub>r</sub> * t - Vx<sub>p</sub> * t = x<sub>p</sub> - x<sub>r</sub>

t = (x<sub>p</sub> - x<sub>r</sub>) / (Vx<sub>r</sub> - Vx<sub>p</sub>)

It is true for all coords:

t = (x<sub>p</sub> - x<sub>r</sub>) / (Vx<sub>r</sub> - Vx<sub>p</sub>) = (y<sub>p</sub> - y<sub>r</sub>) / (Vy<sub>r</sub> - Vy<sub>p</sub>) = (z<sub>p</sub> - z<sub>r</sub>) / (Vz<sub>r</sub> - Vz<sub>p</sub>)

so we can remove t and find just: 

(x<sub>p</sub> - x<sub>r</sub>) / (Vx<sub>r</sub> - Vx<sub>p</sub>) = (y<sub>p</sub> - y<sub>r</sub>) / (Vy<sub>r</sub> - Vy<sub>p</sub>) = (z<sub>p</sub> - z<sub>r</sub>) / (Vz<sub>r</sub> - Vz<sub>p</sub>)

By splitting it into min 2 equations. For example with x and y coord and for x and z coord

