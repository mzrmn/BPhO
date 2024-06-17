import math

import matplotlib.pyplot as plt
import numpy as np

target_x = int(input("X coord: "))
target_y = int(input("Y coord: "))
# launchangle = float(input("Launch angle (deg): "))
launchspeed = float(input("Launch speed (ms^-1): "))
# launchheight = float(input("Launch elevation (m): "))
launchheight = 0
g = float(input("g (ms^-2): "))

# launchangle = launchangle * (math.pi/180)
# launchangle = math.radians(launchangle)

# timestep = 0.02

min_u = math.sqrt(g) * math.sqrt(target_y + math.sqrt(target_x**2 + target_y**2))

u = launchspeed

a = (g / (2*(u**2))) * target_x**2
b = -target_x
c = target_y - launchheight + ((g*(target_x**2)) / (2*(u**2)))

discriminant = b**2 - (4 * a * c)
# range = ((u**2)/g) * ((math.sin(launchangle) * math.cos(launchangle)) + (math.cos(launchangle) * math.sqrt((math.sin(launchangle)**2) + (2 * g * launchheight)/(u**2))))
x = np.linspace(0, target_x)

# high ball
high_angle = math.atan((-b + math.sqrt(discriminant)) / (2 * a))
high_time = x / (u * math.cos(high_angle))
y_high = launchheight + (x * math.tan(high_angle)) - ((g/(2*(u**2))) * (1 + (math.tan(high_angle)**2)) * x**2)

# low ball
low_angle = math.atan((-b - math.sqrt(discriminant)) / (2 * a))
low_time = x / (u * math.cos(low_angle))
y_low = launchheight + (x * math.tan(low_angle)) - ((g/(2*(u**2))) * (1 + (math.tan(low_angle)**2)) * x**2)

# min
min_angle = math.atan((target_y + math.sqrt(target_x**2 + target_y**2)) / target_x)
min_time = x / (min_u * math.cos(min_angle))
y_min = launchheight + (x * math.tan(min_angle)) - ((g/(2*(min_u**2))) * (1 + (math.tan(min_angle)**2)) * x**2)

# ux = u * math.cos(launchangle)
# uy = u * math.sin(launchangle)

# vx = ux
# vy = uy - (g * t)
# v = math.sqrt((vx**2) + (vy**2))

# xa = (u**2 / g) * math.sin(launchangle) * math.cos(launchangle)
# ya = launchheight + (u**2)/(2 * g) * (math.sin(launchangle)**2)

plt.grid()

plt.plot(x, y_high, label="high ball")
plt.plot(x, y_low, label="low ball")
plt.plot(x, y_min, label="min u")
plt.legend(loc="upper right")
# plt.plot(xa, ya, "x")
plt.plot(target_x, target_y, "oy")
plt.annotate("(X, Y)", (target_x, target_y), textcoords="offset points", xytext=(20, -10), ha='center')

plt.xlim(left=0)
plt.ylim(bottom=launchheight)

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.show()
