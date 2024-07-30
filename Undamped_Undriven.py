import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial Conditions
m = float(input('Enter a positive value for object mass (kg): '))
k = float(input('Enter a positive value for the spring constant (N/m): '))
A = float(input('How much do you want to stretch the spring (m): '))
s = 60

# Additional Parameters
freq = np.sqrt(k / m)
time = np.linspace(0, s, 100)


# Equation of motion
def pos(t):
    return A * np.sin(freq * t)


# Figure Parameters
fig = plt.figure(figsize=(18, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)


# For seeing just x-change
null = np.zeros(len(pos(time)))


# Animation Function
def animate(frames):
    # Displacement
    ax1.plot(time[:frames], pos(time[:frames]), c='b')
    # Spring visualization
    ax2.cla()
    ax2.plot(pos(time[frames]), null[frames], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
    ax2.set_xlim(min(pos(time)), max(pos(time)))
    ax2.set_ylim(-0.01, 0.01)


# Perform Simulation
simulation = animation.FuncAnimation(fig=fig, func=animate, frames=len(time), interval=40, repeat=False)

# Labels
ax1.set_xlabel('time(s)')
ax1.set_ylabel('Displacement(m)')
ax1.set_title('Displacement curve')

# To Save as GIF file
# writer = animation.PillowWriter(fps=15,
#                              metadata=dict(artist='Me'),
#                              bitrate=1800)
# simulation.save('undamped_undrivenCHO.gif', writer=writer)

from IPython.display import HTML
HTML(simulation.to_jshtml())