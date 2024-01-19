import numpy as np
from surf2stl import surf2stl
import numpy.matlib

def pol2cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return(x, y)

radius = 1.0
height = 20.0
number_z = 50
nodes = 50

r = radius * np.ones(nodes)
th = np.linspace(0, 2 * np.pi, nodes)
z = np.linspace(0, height, number_z)

x, y = pol2cart(r, th)

X = np.tile(x, (number_z, 1))
Y = np.tile(y, (number_z, 1))
Z = np.tile(z, (nodes, 1)).T

x_c = np.zeros(nodes)
y_c = np.zeros(nodes)
z_c = np.tile(height, nodes)

X = np.vstack([X, x_c])
Y = np.vstack([Y, y_c])
Z = np.vstack([Z, z_c])

surf2stl('cylinder.stl', X, Y, Z, 'ascii')