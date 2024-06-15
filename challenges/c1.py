import math

import matplotlib.pyplot as plt
import numpy as np

launchangle = float(input("Launch angle (deg): "))
launchspeed = float(input("Launch speed (ms^-1): "))
launchheight = float(input("Launch height (m): "))
g = float(input("g (ms^-2): "))

# launchangle = launchangle * (math.pi/180)
launchangle = math.radians(launchangle)

timestep = 0.02

t = np.arange(0, 10, timestep)

u = launchspeed
ux = u * math.cos(launchangle)
uy = u * math.sin(launchangle)
vx = ux
vy = uy - (g * t)
# v = math.sqrt((vx**2) + (vy**2))
x = ux * t
y = launchheight + (uy * t) - ((1/2) * g * (t**2))

plt.grid()
plt.xlim([0,50])
plt.ylim([0,14])

plt.plot(x, y)

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.show()
