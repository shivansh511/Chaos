import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# a function to calculate logistic map
def logistic_map(x_init, para=4.0, n=1000):
    """
    x_init: initial condition
    para: r value of equation x_{n+1} = rx_n(1-x_n)
    n: Number of iterations. If unspecified default n is 1000.
    
    Returns a range of iterations, and a calculated trajectory,x 
    """
    x=np.empty(n)
    x[0]=x_init

    for i in range(n-1):
        x[i+1] = x[i]*para*(1.0 - x[i])

    return range(n), x

# Initial parameters
x_init = 0.45
r_init = 2.0


X,Y = logistic_map(x_init = x_init, para = r_init)


fig, ax = plt.subplots(figsize=(14,6))
ax.set_xlabel("Iterations")
ax.set_ylabel(r"$x$")
ax.set_xlim(-0.5, 100)
ax.set_ylim(-0.1,1.1)
ax.margins(x=0)


# Slider for initial conditions
axx0 = plt.axes([0.25, 0.1, 0.65, 0.03])
x0_slider = Slider(ax = axx0, 
    label = r"$x_0$", 
    valmin = 0.0, 
    valmax = 1.0, 
    valinit = x_init)

# Slider for r value
axr = plt.axes([0.25, 0.05, 0.65, 0.03])
r_slider = Slider(ax = axr,
    label=r"$r$",
    valmin = 0.0, 
    valmax = 4.0,
    valinit = r_init )

logmap, = ax.plot(X, Y, marker="o" , markersize=4, markerfacecolor="red")
ax.set_title(r"$x_{n+1} = 2 x_n(1-x_n) $")
#logmap, = plt.plot(X, Y ,marker="o", markersize=3, color="blue")

# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)

# A function to update the trajectory ever time initial condition changes
def update(val):
    x,y = logistic_map(x_init=x0_slider.val, para = r_slider.val )
    ax.set_title(r"$x_{n+1} = $" + "{}".format(round(r_slider.val, 2)) + r"$x_n(1-x_n) $")
    logmap.set_ydata(y)
    fig.canvas.draw_idle()


# Register the update function
x0_slider.on_changed(update)
r_slider.on_changed(update)

plt.show()