from pylab import *

xval, yval, = meshgrid(arange(-20, 20, 5), arange(-20, 20, 5))


G = 9.8     # gravity
m1 = 1900000000000000000000000000     # Mass of obj 1 (jupiter) in kg
m2 = 5970000000000000000000000    # Mass of obj 2 (Earth) in kg          feel free to change these
r = 379.38   # distance b/n masses
r = r*r     

xdot = yval
ydot = G * (m1*m2/r)        # Newtons law of Grav

streamplot(xval, yval, xdot, ydot)

show()
