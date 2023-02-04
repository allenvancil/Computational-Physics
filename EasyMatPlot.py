from pylab import *
Xmin = -5; Xmax = 5; Npoints = 500
DelX = (Xmax - Xmin)/Npoints
x = arange(Xmin, Xmax, DelX)
y = sin(x)*sin(x*x)
print('arange => x[0], x[1], x[499]=%8.2f %8.2f %8.2f' %(x[0], x[1], x[499])) #prints begining 
print('arange => y[0], y[1],y[499] = %8.2f %8.2f %8.2f' %(y[0], y[1],y[499]))
print("\n Doing plotting, look at Figure 1")
xlabel('x'); ylabel('f(x)'); title('f(x) vs x')
text(-1.75, 0.75, 'MatPlotLib \n Example')
plot(x, y,'r+', linestyle='-.', lw=.5)
grid(True)
show()