import math
import matplotlib.pyplot as plt
import numpy as np
 

u = float(input("Launch speed (ms^-1): "))
h = float(input("Height above ground (m): "))
g = float(input("Gravity (ms^-2): "))
theta = float(input("Launch angle (degrees): "))

theta = math.radians(theta) 

# Normal trajectory
R_Normal = (u ** 2 / g) * (math.sin(theta) * math.cos(theta) + 
                         math.cos(theta) * math.sqrt(math.sin(theta)** 2 + 2 * g * h / u ** 2))

# Max Range trajectory
theta_Max = math.asin(1 / math.sqrt(2 + 2 * g * h / u ** 2))
R_Max = (u ** 2 / g) * math.sqrt(1 + 2 * g * h / u ** 2)

#  the function for s and s_max
def z_func(z):
    return 0.5 * math.log(abs(math.sqrt(1 + z ** 2) + z)) + 0.5 * z * math.sqrt(1 + z ** 2)

a = u**2 / (g * (1 + math.tan(theta)**2))
b = math.tan(theta)
c = math.tan(theta) - g * R_Normal * (1 + math.tan(theta) ** 2) / u ** 2
s = a * (z_func(b) - z_func(c))

a_max = u**2 / (g * (1 + math.tan(theta_Max)**2))
b_max = math.tan(theta_Max)
c_max = math.tan(theta_Max) - g * R_Max * (1 + math.tan(theta_Max)**2) / u ** 2
s_max = a_max * (z_func(b_max) - z_func(c_max))
# ↑↑↑ s and s_max using function and variables from challenge

print(f"Range (R_Normal): {R_Normal:.2f} m")
print(f"Range (R_Max): {R_Max:.2f} m")
print(f"Trajectory Length (s): {s:.2f} m")
print(f"Max Trajectory Length (s_max): {s_max:.2f} m")

# trajectories from c4
X_Normal = np.linspace(0, R_Normal, 500)
y_Normal = h + X_Normal * math.tan(theta) - (g * X_Normal**2) / (2 * (u * math.cos(theta)) ** 2)

x_Max = np.linspace(0, R_Max, 500)
y_Max = h + x_Max * math.tan(theta_Max) - (g * x_Max**2) / (2 * (u * math.cos(theta_Max)) ** 2)

# both plots with labels
plt.plot(X_Normal, y_Normal, label=f"θ={math.degrees(theta):.1f}°, T={R_Normal/(u*math.cos(theta)):.2f}s", color="blue")
plt.plot(x_Max, y_Max, "--", label=f"θ_max={math.degrees(theta_Max):.1f}°, T={R_Max/(u*math.cos(theta_Max)):.2f}s", color="red")


plt.plot(R_Normal, 0, "oy")
plt.plot(R_Max, 0, "oy") # the end points (not really necessary)

# annotations
plt.annotate(f"({R_Normal:.2f}, 0)", (R_Normal, 0), textcoords="offset points", xytext=(10, 10), ha='center')
plt.annotate(f"({R_Max:.2f}, 0)", (R_Max, 0), textcoords="offset points", xytext=(10, 10), ha='center')

# the labels
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.title('Projectile Trajectory - Normal vs Max Range')
plt.legend(loc="upper right")
plt.grid()
plt.show()
