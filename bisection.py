import numpy as np
from numpy import *
eps = 5e-15; Nmax = 100; a = 0.0; b = (3*np.math.pi)/2
def f(x): return np.math.sin(x)

def Bisection(Xminus, Xplus, Nmax, eps):
    for it in range(0, Nmax):
        x = (Xplus + Xminus)/2
        print(" it = ",it, "x = ", x, "f(x) = ", f(x))
        if(f(Xplus)*f(x)>0):
            Xplus = x
        else:
            Xminus = x
        if(abs(f(x))<eps):
            print("\n Root found with precision eps = ", eps)
            break
        if it == Nmax-1: 
            print("\n No root after N iterations\n")
    return x

root = Bisection(a, b, Nmax, eps)
print(" Root = ", root)