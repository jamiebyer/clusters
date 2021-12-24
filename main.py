#Diffusion Limited Aggregation
#model for growth of clusters

#lattice (grid) simulation: use uniform 2D lattice
#particles: unit mass, at any stage fall into two types
#   1. fixed/frozen at some specific lattice site
#   2. mobile: free to move around lattice
#discrete time steps: t^n

# - 1 free particle at a time
# - particle random walks around lattice until adjacent to fixed particle
# - particle gets fixed at current location
# - new walker launched

#initialization: typically one seed particle, particles launched at random angle at a radius
#extension: "central bias"

#animation example from: https://coderedirect.com/questions/418911/animated-matplotlib-imshow


#try using an increasing radius!

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import sys
import random

length = 30

fig = plt.figure()
ax = plt.axes(xlim=(0, length-1), ylim=(0, length-1))
empty_arr = np.zeros((length, length), dtype = int)
arr = np.copy(empty_arr)

im=plt.imshow(arr, interpolation='nearest', vmin=0, vmax=255, origin='lower', animated=True)


radius = int(np.floor(length/2))

#initial middle point
x = [radius]
y = [radius]


def check_status():
    global x, y
    launch = False
    if (x[-1] == radius) & (y[-1] == radius):
        launch = True
    elif np.sqrt((x[-1]-radius)**2 + (y[-1]-radius)**2) > radius:
        x.pop()
        y.pop()
        launch = True
    else:
        for i in range(len(x)-1):
            if (abs(x[-1]-x[i]) <= 1) & (abs(y[-1]-y[i]) <= 1):
                launch = True
                break
    
    if launch == True:
        #launch point
        theta = np.random.random_sample()*2*np.pi
        x.append(int(np.floor(np.cos(theta)*radius)) + radius)
        y.append(int(np.floor(np.sin(theta)*radius)) + radius)

def walk():
    global x, y
    rand = np.random.random_sample()
    if rand < 0.25 :
        if x[-1] == length - 1:
            x[-1] = 0
        else: x[-1] = x[-1] + 1
    elif rand < 0.5 :
        if x[-1] == 0:
            x[-1] = length - 1
        else: x[-1] = x[-1] - 1
    elif rand < 0.75 :
        if y[-1] == length - 1:
            y[-1] = 0
        else: y[-1] = y[-1] + 1
    else:
        if y[-1] == 0:
            y[-1] = length - 1
        else: y[-1] = y[-1] - 1
    return

def stand(arr):
    global x, y
    for i in range(len(x)):
        arr[x[i]][y[i]] = 1000
    return arr

def animate(i):
    global x, y
    arr = np.copy(empty_arr)
    check_status()
    walk()
    arr = stand(arr)
    im.set_array(arr)
    return [im]

anim = animation.FuncAnimation(fig, animate, frames=1000, interval=20, blit=True)

anim.save("animation.gif", writer=animation.PillowWriter(fps=24))
plt.show()


#f = r"./animation.gif" 
#writergif = animation.PillowWriter(fps=40) 
#anim.save(f, writer=writergif)





#3D example: https://coderedirect.com/questions/418911/animated-matplotlib-imshow


