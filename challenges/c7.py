import math
import matplotlib.pyplot as plt
import numpy as np

# Inputs are u, h, g, and 6 different values for theta

u = float(input("Launch speed (ms^-1): "))
h = float(input("Height above ground (m): "))
g = float(input("Gravity (ms^-2): "))

# 6 different values of theta
theta_values = []
for i in range(6):
    theta = float(input(f"Launch angle {i+1} (degrees): "))
    theta_values.append(math.radians(theta))  # Convert to radians and store

t = np.linspace(0, 2.5, 500)  # Time range from 0 to 2.5 seconds, can be changed if needed

# Range vs Time plot
plt.figure(1)  
for theta in theta_values:
    r = np.sqrt(u**2 * t**2 - (g * t ** 3 * u * np.sin(theta)) + (0.25 * g**2 * t**4))
    plt.plot(t, r, label=f"Theta = {math.degrees(theta):.1f} degrees")

plt.xlabel("Time (s)")
plt.ylabel("Range (m)")
plt.title("Range vs Time for Different Launch Angles")
plt.legend()
plt.grid()

# Trajectory for Different Launch Angles
plt.figure(2) 

for theta in theta_values:
    #R_Normal for each angle
    R_Normal = (u**2 / g) * (math.sin(2 * theta) + math.sqrt(math.sin(theta)**2 + 2 * g * h / u**2))
    
    X_Normal = np.linspace(0, R_Normal, 500)
    
    # Calculating y 
    y_Normal = h + X_Normal * math.tan(theta) - (g * X_Normal**2) / (2 * (u * math.cos(theta))**2)

    # plotting the trajectories
    plt.plot(X_Normal, y_Normal, label=f"Theta = {math.degrees(theta):.1f} degrees")

#trying to scale axis 
y_max = np.max(y_Normal) # method to scale is getting highest plot and using it to get lowest point like 5 with -5 or 10 with -10
y_min = -(y_max) 

plt.ylim(bottom=y_min , top=y_max)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Trajectory for Different Launch Angles")
plt.legend(loc="upper right")
plt.grid()

plt.show()

