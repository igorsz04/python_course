import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = plt.axes(projection = '3d')
plt.show()

#data for a 3-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,'gray')

#data for 3-dimensional scattered points
zdata = 15*np.random.random(100)
xdata = np.sin(zdata) + 0.1*np.random.randn(100)
ydata = np.cos(zdata) + 0.1*np.random.randn(100)

ax.scatter3D(xdata,ydata,zdata,c=zdata,cmap='Greens')

def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6,6,30)
X, Y = np.meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X,Y,Z,50,cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

