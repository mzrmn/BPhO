import math
 
import matplotlib.pyplot as plt
import numpy as np

target_x = int(input("X coord: "))
target_y = int(input("Y coord: "))
#launchSpeed
u = float(input("Launch speed (ms^-1): "))
#launchHeight
h = float(input("Height above ground (m): "))
#gravity
g = float(input("Gravity (ms^-2): "))
#launchAngle
# theta = float(input("Launch angle (degrees): "))
 
# theta = math.radians(theta)
 
# R_Normal = (u**2/ g) * ((math.sin(theta) * math.cos(theta)) + (math.cos(theta) * math.sqrt((math.sin(theta) ** 2) + (2*g*h) / (u**2))))

#MAX HEIGHT CALCULATIONS

theta_Max = math.asin(1 / math.sqrt(2 + (2 * g * h) / (u**2)))
R_Max = (u**2 / g) * math.sqrt(1 + (2 * g * h) / u**2)

print(math.degrees(theta_Max))

# x_Normal = np.linspace(0, R_Normal)

#y_Max is the max height for Max Range Trajectory, not max possible height
# y_Normal = h + x_Normal * math.tan(theta) - (g * x_Normal**2) / (2 * (u * math.cos(theta))**2) #y equation from challenge 3

x_Max = np.linspace(0, R_Max)
y_Max = h + x_Max * math.tan(theta_Max) - (g * x_Max**2) / (2 * (u * math.cos(theta_Max))**2)


# c3 -----------
min_u = math.sqrt(g) * math.sqrt(target_y + math.sqrt(target_x**2 + target_y**2))

a = (g / (2*(u**2))) * target_x**2
b = -target_x
c = target_y - h + ((g*(target_x**2)) / (2*(u**2)))

discriminant = b**2 - (4 * a * c)
# range = ((u**2)/g) * ((math.sin(launchangle) * math.cos(launchangle)) + (math.cos(launchangle) * math.sqrt((math.sin(launchangle)**2) + (2 * g * launchheight)/(u**2))))
x = np.linspace(0, R_Max)

# high ball
high_angle = math.atan((-b + math.sqrt(discriminant)) / (2 * a))
high_time = x / (u * math.cos(high_angle))
y_high = h + (x * math.tan(high_angle)) - ((g/(2*(u**2))) * (1 + (math.tan(high_angle)**2)) * x**2)

# low ball
low_angle = math.atan((-b - math.sqrt(discriminant)) / (2 * a))
low_time = x / (u * math.cos(low_angle))
y_low = h + (x * math.tan(low_angle)) - ((g/(2*(u**2))) * (1 + (math.tan(low_angle)**2)) * x**2)

# min
min_angle = math.atan((target_y + math.sqrt(target_x**2 + target_y**2)) / target_x)
min_time = x / (min_u * math.cos(min_angle))
y_min = h + (x * math.tan(min_angle)) - ((g/(2*(min_u**2))) * (1 + (math.tan(min_angle)**2)) * x**2)


# c5 -------
bounding_y = ((u**2 / (2*g)) - ((g/(2*(u**2))) * (x**2))) + h

plt.plot(x, bounding_y, ls=":", label="Bounding")

# plt.plot(x_Normal, y_Normal, label="Normal Trajectory")
plt.plot(x_Max, y_Max, ls=":" ,label="Max range")

plt.plot(x, y_high, label="High")
plt.plot(x, y_low, label="Low")
plt.plot(x, y_min, ls=":", label="Min u")
#plotting actual max and normal point

# plt.annotate("(X, Y)", (target_x, target_y), textcoords="offset points", xytext=(20, -10), ha='center')

# plt.plot(R_Normal,0,"oy")
# plt.plot(R_Max,0,"oy")

if int(h) == 0:
    plt.plot(0, int(h), "xg", label="Launch (0, 0)")
else:
    plt.plot(0, int(h), "xg", label=f"Launch (0, {h})")
plt.plot(target_x, target_y, "xr", label=f"{target_x, target_y}")

# norm = f"({int(R_Normal)},0)"
# max = f"({int(R_Max)},0)"

# plt.annotate(norm, (R_Normal, 0), textcoords="offset points", xytext=(20, 15), ha='center')
# plt.annotate(max, (R_Max, 0), textcoords="offset points", xytext=(20, 15), ha='center')

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.xlim(left = 0)
plt.ylim(bottom = 0)
 
plt.title('Projectile Trajectory - Normal vs Max Range')
plt.legend(loc="upper right")
plt.grid()
plt.show()
