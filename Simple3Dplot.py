#can get fig. to open, but has nothing on it.

import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
print("Please be patient while I do importing and plotting")
delta = 0.1
x = p.arange(-3., 3., delta)
y = p.arange(-3., 3., delta)
X, Y = p.meshgrid(x, y)
Z = p.sin(X) * p.cos(Y)

fig = p.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=5, cstride=3, linewidth=1)
ax.plot_wireframe(X, Y, Z, color='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
p.show()  