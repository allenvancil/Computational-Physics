from vpython import *
string="blue: sin^2(x), black = cos^2(x), cyan: sin(x)*cos(x)" 
graph1=graph(title=string, xtitle='x', ytitle='y', background=color.white, foreground=color.black) #properties of plot 

y1 = gcurve(color=color.blue) #solid line curve, color blue
y2 = gcurve(color=color.black) #solid bars, color black
y3 = gdots(color=color.cyan) #dots, color cyan
for x in arange(-5,5,0.1):
    y1.plot(pos=(x, sin(x)**2))
    y2.plot(pos=(x, 2*sin(x)*cos(x)))
    y3.plot(pos=(x, 2*(cos(x)**2-sin(x)**2)))

    #y2.plot(pos=(x, cos(x)*cos(x)/3.))
    #y3.plot(pos=(x, sin(x)*cos(x)))