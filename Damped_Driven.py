import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial Conditions
m = float(input('Enter a positive value for object mass (kg): '))
k = float(input('Enter a positive value for the spring constant (N/m): '))
A = float(input('How much do you want to stretch the spring (m): '))
b = float(input('Enter damping parameter (kg/s): '))
s = 60
# Additional Parameters
beta = b/(2*m)
freq = np.sqrt(k/m)
# Equation of motion
# This Example is for condition that x(0) = 0 and v(0) = 0
# a driving force of cos(t) is applied

# Solving using RK4 iterations
def f(r, t, freq):
    x = r[0]
    fx = r[1]
    dx = fx
    dfx = -(2 * beta) - freq*x + np.cos(t)
    # Np.cos(t) is the Driving force of the oscillations, feel free to change it!
    return np.array([dx, dfx], float)

start = 0.0
end = 25.0

numSteps = 100
stepSize = (end - start)/numSteps

tpoints = np.arange(start, end, stepSize)
xpoints = []
fxpoints = []

r = np.array([A,0.0], float)

#RK4 Method
for t in tpoints:
    xpoints.append(r[0])
    fxpoints.append(r[1])

    k1 = stepSize*f(r,t,freq)
    k2 = stepSize*f(r+0.5*k1,t+0.5*stepSize,freq)
    k3 = stepSize*f(r+0.5*k2,t+0.5*stepSize,freq)
    k4 = stepSize*f(r+k3,t+stepSize,freq)
    r += (k1+2.*k2+2.*k3+k4)/6

# Figure Parameters
fig = plt.figure(figsize=(18,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# For seeing just x-change
null = np.zeros(len(tpoints))

# Animation Function
def animate(frames):
    # Displacement
    ax1.plot(tpoints[:frames], xpoints[:frames], c = 'b')
    # Spring visualization
    ax2.cla()
    ax2.plot(xpoints[frames], null[frames], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
    ax2.set_xlim(min(xpoints), max(xpoints))
# Perform Simulation
simulation = animation.FuncAnimation(fig=fig, func = animate, frames = 100, interval = 40, repeat = False)

# Labels
ax1.set_xlabel('time(s)')
ax1.set_ylabel('Displacement(m)')
ax1.set_title('Displacement curve')

# To Save as GIF file
#writer = animation.PillowWriter(fps=15,
#                             metadata=dict(artist='Me'),
#                               bitrate=1800)
#simulation.save('damped_drivenCHO.gif', writer=writer)

# For Jupyter Notebook display
# from IPython.display import HTML
# HTML(simulation.to_jshtml())

from IPython.display import HTML
HTML(simulation.to_jshtml())