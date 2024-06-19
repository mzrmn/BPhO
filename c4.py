import math
 
import matplotlib.pyplot as plt
import numpy as np
 
#inputs are u, h, g, theta
 
#launchSpeed
u = float(input("Launch speed (ms^-1): "))
#launchHeight
h = float(input("Height above ground (m): "))
#gravity
g = float(input("gravity (ms^-2): "))
#launchAngle
theta = float(input("Launch angle (degrees): "))
 
theta = math.radians(theta) # works when converting to radians and idk why
 
 
R_Normal = (u**2/ g) * ((math.sin(theta) * math.cos(theta)) + (math.cos(theta) * math.sqrt((math.sin(theta) ** 2) + (2*g*h) / (u**2))))
 
print(R_Normal)
#MAX HEIGHT CALCULATIONS
 
theta_Max = math.asin(1 / math.sqrt(2 + (2 * g * h) / (u ** 2)))
theta_Max = math.degrees(theta_Max)
R_Max = (u ** 2 / g) * math.sqrt(1 + (2 * g * h) / u ** 2)
 
print(theta_Max)
print(R_Max)
 
X_Normal = np.linspace(0, R_Normal)
 
#y_Max is the max height for Max Range Trajectory, not max possible height
y_Normal = h + X_Normal * math.tan(theta) - (g * X_Normal**2) / (2 * (u * math.cos(theta))**2) #y equation from challenge 3
 
theta_Max = math.radians(theta_Max)
x_Max = np.linspace(0, R_Max, num=500)
y_Max = h + x_Max * math.tan(theta_Max) - (g * x_Max**2) / (2 * (u * math.cos(theta_Max))**2)
 
plt.plot(X_Normal, y_Normal, label="Normal Trajectory")
plt.plot(x_Max, y_Max,"-",label = "Max Range Trajectory")
#plotting actual max and normal point

plt.plot(R_Normal,0,"oy") # plt.annotate("(X, Y)", (target_x, target_y), textcoords="offset points", xytext=(20, -10), ha='center')
plt.plot(R_Max,0,"oy")

norm = "(" + str(int(R_Normal)) + ",0)"
max = "(" + str(int(R_Max)) + ",0)"

plt.annotate(norm, (R_Normal, 0), textcoords="offset points", xytext=(20, 15), ha='center')
plt.annotate(max, (R_Max, 0), textcoords="offset points", xytext=(20, 15), ha='center')

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.xlim(left = 0)
plt.ylim(bottom = 0)
 
plt.title('Projectile Trajectory - Normal vs Max Range')
plt.legend(loc="upper right")
plt.grid()
plt.show()
