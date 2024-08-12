import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, state):
        super().__init__()

        self.title(title)
        self.state(state)

        self.tabs = Tabs(self)

        self.mainloop()

class Tabs(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        self.tab1 = ttk.Frame(self)
        self.tab2 = ttk.Frame(self)
        self.tab3 = ttk.Frame(self)
        self.tab4 = ttk.Frame(self)
        self.tab5 = ttk.Frame(self)

        self.pack(expand=1, fill="both")

        self.add(self.tab1, text="1, 2, 4")
        self.add(self.tab2, text="3, 5, 6")
        self.add(self.tab3, text="7")
        self.add(self.tab4, text="8")
        self.add(self.tab5, text="9")

        self.create_widgets_1()
        self.plot_1_simple()

        self.create_widgets_2()
        self.plot_2()

    def create_widgets_1(self):
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(4.8, 3.75)

        canvas = FigureCanvasTkAgg(self.fig, master = self.tab1)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.3, rely=0.025)

        self.theta_slider = Slider("theta", 45, self.tab1, 50, 0)
        self.theta_slider.slider = ttk.Scale(self.tab1, from_=0, to=360, orient="horizontal", length="200", variable=self.theta_slider.value, command=self.update_1)
        self.theta_slider.slider.place(x=self.theta_slider.x, y=self.theta_slider.y)

        self.u_slider = Slider("u", 20, self.tab1, 50, 25)
        self.u_slider.slider = ttk.Scale(self.tab1, from_=0, to=500, orient="horizontal", length="200", variable=self.u_slider.value, command=self.update_1)
        self.u_slider.slider.place(x=self.u_slider.x, y=self.u_slider.y)

        self.h_slider = Slider("h", 2, self.tab1, 50, 50)
        self.h_slider.slider = ttk.Scale(self.tab1, from_=0, to=500, orient="horizontal", length="200", variable=self.h_slider.value, command=self.update_1)
        self.h_slider.slider.place(x=self.h_slider.x, y=self.h_slider.y)

        self.g_slider = Slider("g", 9.81, self.tab1, 50, 75)
        self.g_slider.slider = ttk.Scale(self.tab1, from_=0, to=500, orient="horizontal", length="200", variable=self.g_slider.value, command=self.update_1)
        self.g_slider.slider.place(x=self.g_slider.x, y=self.g_slider.y)


        self.sa_check_value = tk.IntVar()
        self.sa_check_value.set(0)

        self.max_range_check_value = tk.BooleanVar()
        self.max_range_check_value.set(False)

        simple_check = ttk.Radiobutton(self.tab1, text="Simple model", variable=self.sa_check_value, value=0, command=self.model_select)
        analytic_check = ttk.Radiobutton(self.tab1, text="Analytic model", variable=self.sa_check_value, value=1, command=self.model_select)
        simple_check.place(x=0, y=130)
        analytic_check.place(x=0, y=150)

        max_range_check = ttk.Checkbutton(self.tab1, text="Max range", variable=self.max_range_check_value, command=self.plot_max_range)
        max_range_check.place(x=0, y=200)

    def model_select(self):
        if self.sa_check_value.get() == 0:
            self.plot_1_simple()
        else:
            self.plot_1_analytic()

    def update_1(self, value):
        if self.sa_check_value.get() == 0:
            launchangle = self.theta_slider.slider.get()
            launchspeed = self.u_slider.slider.get()
            launchheight = self.h_slider.slider.get()
            g = self.g_slider.slider.get()

            launchangle = math.radians(launchangle)

            timestep = 0.02

            t = np.arange(0, 10, timestep)

            u = launchspeed
            ux = u * math.cos(launchangle)
            uy = u * math.sin(launchangle)
            vx = ux
            vy = uy - (g * t)

            x = ux * t
            y = launchheight + (uy * t) - ((1/2) * g * (t**2))

            self.l.set_xdata(x)
            self.l.set_ydata(y)
    
            self.fig.canvas.draw_idle()
        else:
            launchangle = self.theta_slider.slider.get()
            launchspeed = self.u_slider.slider.get()
            launchheight = self.h_slider.slider.get()
            g = self.g_slider.slider.get()

            launchangle = math.radians(launchangle)

            u = launchspeed
            ux = u * math.cos(launchangle)
            uy = u * math.sin(launchangle)

            range = ((u**2)/g) * ((math.sin(launchangle) * math.cos(launchangle)) + (math.cos(launchangle) * math.sqrt((math.sin(launchangle)**2) + (2 * g * launchheight)/(u**2))))
            x = np.linspace(0, range)

            t = x / (u * math.cos(launchangle))

            vx = ux
            vy = uy - (g * t)

            y = launchheight + (x * math.tan(launchangle)) - ((g/(2*(u**2))) * (1 + (math.tan(launchangle)**2)) * x**2)

            xa = [(u**2 / g) * math.sin(launchangle) * math.cos(launchangle)]
            ya = [launchheight + (u**2)/(2 * g) * (math.sin(launchangle)**2)]

            self.l.set_xdata(x)
            self.l.set_ydata(y)
            self.apogee.set_data(xa, ya)

            self.fig.canvas.draw_idle()

    def plot_1_simple(self):
        launchangle = self.theta_slider.slider.get()
        launchspeed = self.u_slider.slider.get()
        launchheight = self.h_slider.slider.get()
        g = self.g_slider.slider.get()

        launchangle = math.radians(launchangle)

        timestep = 0.02

        t = np.arange(0, 10, timestep)

        u = launchspeed
        ux = u * math.cos(launchangle)
        uy = u * math.sin(launchangle)
        vx = ux
        vy = uy - (g * t)

        x = ux * t
        y = launchheight + (uy * t) - ((1/2) * g * (t**2))

        self.ax.cla()

        self.ax.grid()

        self.l, = self.ax.plot(x, y, label="Simple Model")

        self.ax.set_xlim(left = 0)
        self.ax.set_ylim(bottom = 0)

        self.ax.set_xlabel("x/m")
        self.ax.set_ylabel("y/m")

        self.ax.legend(loc="upper right")

        self.fig.canvas.draw_idle()

    def plot_1_analytic(self):
        launchangle = self.theta_slider.slider.get()
        launchspeed = self.u_slider.slider.get()
        launchheight = self.h_slider.slider.get()
        g = self.g_slider.slider.get()

        launchangle = math.radians(launchangle)

        # timestep = 0.02
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

        self.ax.cla()

        self.ax.grid()

        self.l, = self.ax.plot(x, y, label = "Analytic Model")
        self.apogee, = self.ax.plot(xa, ya, "x", label = "Apogee")

        self.ax.set_xlim(left = 0)
        self.ax.set_ylim(bottom = 0)

        self.ax.set_xlabel("x/m")
        self.ax.set_ylabel("y/m")

        self.ax.legend(loc="upper right")

        self.fig.canvas.draw_idle()

    def plot_max_range(self):
        if self.max_range_check_value.get() == True:
            u = self.u_slider.slider.get()
            h = self.h_slider.slider.get()
            g = self.g_slider.slider.get()
            theta = self.theta_slider.slider.get()

            theta = math.radians(theta)
            R_Normal = (u**2/ g) * ((math.sin(theta) * math.cos(theta)) + (math.cos(theta) * math.sqrt((math.sin(theta) ** 2) + (2*g*h) / (u**2))))

            X_Normal = np.linspace(0, R_Normal)

            #y_Max is the max height for Max Range Trajectory, not max possible height
            y_Normal = h + X_Normal * math.tan(theta) - (g * X_Normal**2) / (2 * (u * math.cos(theta))**2) #y equation from challenge 3
            
            theta_Max = math.asin(1 / math.sqrt(2 + (2 * g * h) / (u ** 2)))
            R_Max = (u ** 2 / g) * math.sqrt(1 + (2 * g * h) / u ** 2)

            x_Max = np.linspace(0, R_Max, num=500)
            y_Max = h + x_Max * math.tan(theta_Max) - (g * x_Max**2) / (2 * (u * math.cos(theta_Max))**2)

            self.ax.plot(x_Max, y_Max, linestyle = "--", label = "Max Range Trajectory")

            self.ax.legend(loc="upper right")

            self.fig.canvas.draw_idle()

    def create_widgets_2(self):
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(4.8, 3.75)

        canvas = FigureCanvasTkAgg(self.fig, master = self.tab2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.28, rely=0.025)

        self.u_slider2 = Slider("u", 150, self.tab2, 50, 25)
        self.u_slider2.slider = ttk.Scale(self.tab2, from_=0, to=500, orient="horizontal", length="200", variable=self.u_slider2.value, command=self.update_2)
        self.u_slider2.slider.place(x=self.u_slider2.x, y=self.u_slider2.y)

        self.h_slider2 = Slider("h", 0, self.tab2, 50, 50)
        self.h_slider2.slider = ttk.Scale(self.tab2, from_=0, to=500, orient="horizontal", length="200", variable=self.h_slider2.value, command=self.update_2)
        self.h_slider2.slider.place(x=self.h_slider2.x, y=self.h_slider2.y)

        self.g_slider2 = Slider("g", 9.81, self.tab2, 50, 75)
        self.g_slider2.slider = ttk.Scale(self.tab2, from_=0, to=500, orient="horizontal", length="200", variable=self.g_slider2.value, command=self.update_2)
        self.g_slider2.slider.place(x=self.g_slider2.x, y=self.g_slider2.y)


        self.sa_check_value = tk.IntVar()
        self.sa_check_value.set(0)

        self.max_range_check_value = tk.BooleanVar()
        self.max_range_check_value.set(False)

        self.input_x = ttk.Spinbox(self.tab2, from_=1, to=2000, command=self.update_2)
        self.input_y = ttk.Spinbox(self.tab2, from_=1, to=2000, command=self.update_2)
        self.input_x.place(x=0, y=130)
        self.input_y.place(x=0, y=150)

        self.input_x.set(1500)
        self.input_y.set(200)

    def update_2(self, value):
        target_x = int(self.input_x.get())
        target_y = int(self.input_y.get())

        u = self.u_slider2.slider.get()
        h = self.h_slider2.slider.get()
        g = self.g_slider2.slider.get()

        #MAX HEIGHT CALCULATIONS

        theta_Max = math.asin(1 / math.sqrt(2 + (2 * g * h) / (u**2)))
        R_Max = (u**2 / g) * math.sqrt(1 + (2 * g * h) / u**2)

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

        self.l1.set_xdata(x)
        self.l1.set_ydata(bounding_y)

        self.l2.set_xdata(x_Max)
        self.l2.set_ydata(y_Max)

        self.l3.set_xdata(x)
        self.l3.set_ydata(y_high)

        self.l4.set_xdata(x)
        self.l4.set_ydata(y_low)

        self.l5.set_xdata(x)
        self.l5.set_ydata(y_min)

        # self.l6, = self.ax.plot(target_x, target_y, "xr", label=f"{target_x, target_y}")

        self.l6.set_xdata([target_x])
        self.l6.set_ydata([target_y])

        self.fig.canvas.draw_idle()
        

    def plot_2(self):
        target_x = int(self.input_x.get())
        target_y = int(self.input_y.get())

        u = self.u_slider2.slider.get()
        h = self.h_slider2.slider.get()
        g = self.g_slider2.slider.get()

        #MAX HEIGHT CALCULATIONS

        theta_Max = math.asin(1 / math.sqrt(2 + (2 * g * h) / (u**2)))
        R_Max = (u**2 / g) * math.sqrt(1 + (2 * g * h) / u**2)

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

        self.l1, = self.ax.plot(x, bounding_y, ls=":", label="Bounding")

        self.l2, = self.ax.plot(x_Max, y_Max, ls=":" ,label="Max range")

        self.l3, = self.ax.plot(x, y_high, label="High")
        self.l4, = self.ax.plot(x, y_low, label="Low")
        self.l5, = self.ax.plot(x, y_min, ls=":", label="Min u")

        if int(h) == 0:
            self.ax.plot(0, int(h), "xg", label="Launch (0, 0)")
        else:
            self.ax.plot(0, int(h), "xg", label=f"Launch (0, {h})")
        self.l6, = self.ax.plot(target_x, target_y, "xr", label=f"{target_x, target_y}")

        plt.xlabel("x/m")
        plt.ylabel("y/m")

        plt.xlim(left = 0)
        plt.ylim(bottom = 0)
        
        # plt.title('Projectile Trajectory - Normal vs Max Range')
        plt.legend(loc="upper right")
        
        # self.ax.title('Projectile Trajectory - Normal vs Max Range')

class Slider():
    def __init__(self, label, value, tab, x, y):
        self.label_text = tk.Label(tab, text=label)
        self.value = tk.IntVar()
        self.value.set(value)
        self.label_num = tk.Label(tab, textvariable=self.value)

        # self.slider = ttk.Scale(tab, from_=0, to=500, orient="horizontal", length="200", variable=self.value, command=self.update)

        self.x = x
        self.y = y

        # self.slider.place(x=self.x, y=self.y)
        self.label_text.place(x=self.x-50, y=self.y)
        self.label_num.place(x=self.x+225, y=self.y)

App("BPhO Computational Challenge 2024", "zoomed")
