
#doesnt work, "pos needs to be vector" -> poss wrong/older library
from visual_graph import *
posy = 100; Lcord = 250
Hweight = 50; W = 10

#scene = DisplayStyle(height=600, width=600, range=380)
alt = curve(pos=[(-300, posy, 0), (300, posy, 0)])
divi = curve(pos=[(0, -150, 0), (0, posy, 0)])
kilogr = cylinder(pos=vector((0, posy-Lcord, 0), radius=20, axis=(0, Hweight, 0), color=color.red))
cord1 = cylinder(pos=(0, posy, 0), axis=(0, -Lcord, 0), color=color.yellow, radius=2)
cord2 = cylinder(pos=(0, posy,0), axis=(0, -Lcord, 0), color=color.yellow, radius=2)

arrow1 = arrow(pos=(0, posy, 0), color=color.orange)
arrow2 = arrow(pos=(0, posy, 0), color=color.orange)

magF=W/2.0
v = 2.0
x1 = 0.0
anglabel = label(pos=(0, 240, 0), text='angle (deg)', box=0)
angultext = label(pos=(20, 210, 0), box=0)
Flabel1 = label(pos=(200, 240, 0), text='Force', box=0)
Ftext1 = label(pos=(200, 210, 0), box=0)
Flabel2 = label(pos=(-200, 240, 0), text='Force', box=0)
Ftext2 = label(pos=(-200, 210, 0), box=0)
local_light(pos=(-10, 0, 20), color=color.yellow)

for t in arange(0., 100.0, 0.2):
    rate(50)
    x1 = v*t
    theta = asin(x1/Lcord)
    poscil = posy-Lcord * cos(theta)
    kilogr.pos = (0, poscil, 0)
    magF = W/(2.*cos(theta))
    angle = 180.*theta/pi
    cord1.pos = (x1, posy, 0)
    cord1.axis = (-Lcord*sin(theta), -Lcord*cos(theta), 0)
    cord2.pos = (-x1, posy, 0)
    cord2.axis = (Lcord*sin(theta), -Lcord*cos(theta), 0)
    arrow1.pos = cord1.pos
    arrow1.axis = (8*magF*sin(theta), 8*magF*cos(theta), 0)
    arrow2.pos = cord2.pos
    arrow2.axis = (-8*magF*sin(theta), 8*magF*cos(theta), 0)
    angultext.text = '%4.2f'%angle
    force = magF
    Ftext1.text = '%8.2f'%force
    Ftext2.text = '%8.2f'%force