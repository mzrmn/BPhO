import matplotlib.pyplot as plt
import tkinter as tk
import math
import numpy


def path_equation(theta, u, g):
    theta = math.radians(theta)
    
    vx = u * math.cos(theta)    
    vy = u * math.sin(theta)
    
    coefficient = (vy / vx) 
    square_coefficient = (g / (2 * vx**2))  
    return f"y = - {square_coefficient}x^2 + {coefficient}x + 0"


def tflight(theta, u, g):
    theta = math.radians(theta)

    return 2 * ((u * math.sin(theta)) / g) 

def hmax(theta, u, g):
    theta = math.radians(theta)
    return (u * math.sin(theta)) ** 2 / (2 * g) 

def hrange(theta, u, g):
    theta = math.radians(theta)
    return (u ** 2) * math.sin(2 * theta) / g

def rangemax(u, g):
    return u**(2 / g) 

def plot_trajectory(theta, u, g):

    angle_rad = math.radians(theta)
    t = numpy.linspace(0, tflight(theta, u, g), 100)
    x = u * math.cos(angle_rad) * t
    y = (u * math.sin(angle_rad) * t) - 0.5 * g * t ** 2

    fig, ax = plt.subplots()

    ax.plot(x, y)
    ax.set_xlim(0, max(x) + 5)
    ax.set_ylim(0, max(y) + 5)
    ax.set_xlabel("Horizontal distance (m)")
    ax.set_ylabel("Vertical distance (m)")
    ax.set_title("Trajectory")
    ax.grid(True, linestyle='-')
    plt.show()


# Constants

 # Acceleration due to gravity ASSUMING DOWNWARD AS POSITIVE (to be changed maybe)
g = 9.81 

# Initial values for velocity and angles
u = 0
theta = 0
anglehorizontalinit = 0


# Create the main window for the GUI (tkinter)
window = tk.Tk()

# Create frames 
frm_title = tk.Frame(padx=50, pady=50)
frm_v = tk.Frame(padx=30, pady=10)
frm_a = tk.Frame(padx=30, pady=10)
frm_ah = tk.Frame(padx=30, pady=10) 
frm_btn = tk.Frame(padx=30, pady=10)

lbl_v = tk.Label(master=frm_v, font=15, text="Enter the initial velocity (ms^-1): ")
lbl_a = tk.Label(master=frm_a, font=15, text="Enter the angle of projection vertically: ")
lbl_ah = tk.Label(master=frm_a, font=15, text="Enter the angle of projection horizontally: ")
ent_v = tk.Entry(master=frm_v, font=15, borderwidth=2)
ent_a = tk.Entry(master=frm_a, font=15, borderwidth=2)
ent_ah = tk.Entry(master=frm_a, font=15, borderwidth=2)
btn_calc = tk.Button(font=15, master=frm_btn, text="Calculate Trajectory", pady=5, padx=10)

frm_title.pack()

frm_v.pack()
lbl_v.pack()
ent_v.pack()

frm_a.pack()
lbl_a.pack()
ent_a.pack()

frm_ah.pack()
lbl_ah.pack()
ent_ah.pack()

frm_btn.pack()
btn_calc.pack()

def traj_calc(event):
    global u
    global theta
    global anglehorizontalinit

    anglehorizontalinit = float(ent_ah.get())
    u = float(ent_v.get())
    theta = float(ent_a.get())

    lbl_pe = tk.Label(text="Path equation (Cartesian): " + str(path_equation(theta, u, g)))
    lbl_ft = tk.Label(text="Flight time (s): " + str(tflight(theta, u, g)))
    lbl_mh = tk.Label(text="Maximum height (m): " + str(hmax(theta, u, g)))
    lbl_hr = tk.Label(text="Horizontal range (m): " + str(hrange(theta, u, g)))
    lbl_mpr = tk.Label(text="Maximum possible range / Range when angle is 45 degrees (m): " + str(rangemax(u, g)))
    
    lbl_pe.pack()
    lbl_ft.pack()
    lbl_mh.pack()
    lbl_hr.pack()
    lbl_mpr.pack()


    plot_trajectory(theta, u, g)


btn_calc.bind("<Button-1>", traj_calc)

window.mainloop()