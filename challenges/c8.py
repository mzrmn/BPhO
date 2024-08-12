import matplotlib.pyplot as plt
import matplotlib.animation as animation

theta = int(input("Enter initial angle: "))
g = float(input("Enter g (ms^-2): "))
n_bounces = int(input("Number of bounces: "))
coefficient = 0.65
timestep = 0.005

x_Initial = 0
y_Initial = 4
x_Final = 1
y_Final = 0

def get_pos(t=0):
    x, y, vx, vy = x_Initial, y_Initial, x_Final, y_Final
    while x < n_bounces:
        t = t + timestep
        x = x + (x_Final * timestep)
        y = y + (vy * timestep)
        vy = vy - (g * timestep)
        if y < 0:
            y = 0
            vy = -vy * coefficient 
        yield x, y

def init():
    ax.set_xlim(0, n_bounces)
    ax.set_ylim(0, y_Initial)
    ax.set_xlabel('x/m')
    ax.set_ylabel('y/m')
    l.set_data(xdata, ydata)
    ball.set_center((x_Initial, y_Initial))
    return l, ball

def animate(pos):
    x, y = pos
    xdata.append(x)
    ydata.append(y)
    l.set_data(xdata, ydata)
    ball.set_center((x, y))
    return l, ball

fig, ax = plt.subplots()
ax.set_aspect('equal')

l, = ax.plot([], [], lw=2)
ball = plt.Circle((x_Initial, y_Initial), 0.08)
ax.add_patch(ball)
xdata = []
ydata = []

ball_animation = animation.FuncAnimation(fig, animate, get_pos, blit=True, interval=timestep*1000, repeat=False, init_func=init)

plt.show()
