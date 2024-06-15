import math

import matplotlib.pyplot as plt
import numpy as np

launchangle = float(input("Launch angle (deg): "))
launchspeed = float(input("Launch speed (ms^-1): "))
launchheight = float(input("Launch elevation (m): "))
g = float(input("Strength of gravity, g (N kg-1): "))

# launchangle = launchangle * (math.pi/180)
launchangle = math.radians(launchangle)

# timestep = float(input("Time step: "))
u = launchspeed
ux = u * math.cos(launchangle)
uy = u * math.sin(launchangle)

range = ((u**2)/g) * ((math.sin(launchangle) * math.cos(launchangle)) + (math.cos(launchangle) * math.sqrt((math.sin(launchangle)**2) + (2 * g * launchheight)/(u**2))))
x = np.linspace(0, range)

t = x / (u * math.cos(launchangle))

vx = ux
vy = uy - (g * t)
# v = math.sqrt((vx**2) + (vy**2))
y = launchheight + (x * math.tan(launchangle)) - ((g/(2*(u**2))) * (1 + (math.tan(launchangle)**2)) * x**2)

xa = (u**2 / g) * math.sin(launchangle) * math.cos(launchangle)
ya = launchheight + (u**2)/(2 * g) * (math.sin(launchangle)**2)

plt.grid()
plt.xlim([0,12])
plt.ylim([0,3.5])

plt.plot(x, y)
plt.plot(xa, ya, "x")

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.show()
