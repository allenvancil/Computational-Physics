import numpy as np, matplotlib.pyplot as plt
N, Npts = 100, 1000000;
analyt = 4.5*np.pi #analyical solution

# formating plot area
x1 = np.arange(0, 2*np.pi+2*np.pi/N, 2*np.pi/N) #(xmin,xmax,xstep)
xi = []; yi = []; xo = []; yo = []
ax = plt.subplot()
y1 = 4.5*np.sin(x1)**2
ax.plot(x1, y1, 'c', linewidth=4)
ax.set_xlim((0, 2*np.pi))
ax.set_ylim((0, 5))
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
ax.set_ylabel('$f(x) = x\, \sin^2 x$')
ax.set_xlabel('x')
#fig.patch.set__visible(False)

def fx(x): return 4.5*np.sin(x)**2

j = 0
xx = 2.*np.pi * np.random.rand(Npts) #x randnumber (0,2*pi)
yy = 5*np.random.rand(Npts) #y random num (0,5)
boxarea = 2. * np.pi * 5. #total area enclosed box (2*pi X 5)
for i in range(1, Npts):
    if (yy[i] <= fx(xx[i])): #if yyi random num  <= f(xxi) at xx rand num, pt (xi, yi)
        xi.append(xx[i])
        yi.append(yy[i])
        j += 1
    else:
        yo.append(yy[i]) #append xxi,yyi that fall above f(x)
        xo.append(xx[i])

    area = boxarea * j/(Npts-1) #TotArea * (sum(pts<=f(x)/Tot pts); The area under curve.
    
ax.plot(xo, yo, 'bo', markersize=1)
ax.plot(xi, yi, 'ro', markersize=1)
ax.set_title('Answers: Analytic = %5.3f, MC = %5.3f'%(analyt, area))
plt.show()