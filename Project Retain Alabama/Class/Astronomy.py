
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

x_range = y_range = np.arange(-20,20,5)

xval, yval = np.meshgrid(x_range, y_range)

G = 6.67408E-11    # gravitation constant
m1 = 597000     # Mass of obj 1 in kg
m2 = 59700    # Mass of obj 2 in kg          feel free to change these
r = 37900.35  ** 2 # distance b/n masses
    

xdot = yval
ydot = G * (m1*m2/r)        # Newtons law of Grav

Q = plt.quiver(xval, yval, xdot, ydot, pivot="middle")
plt.quiverkey(Q,1,1,1, "=Planet")

plt.title("Planet Phase Space Thingy")
plt.axis("scaled")
plt.show()
