import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time parameters
dt = 0.01
num_steps = 500

# Initial conditions
x0, y0, z0 = 0.0, 1.0, 1.05

# Arrays to store the trajectory
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Initial values
xs[0], ys[0], zs[0] = x0, y0, z0

# Lorenz system equations
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Integrate the Lorenz equations
for i in range(num_steps):
    dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
    xs[i + 1] = xs[i] + dx * dt
    ys[i + 1] = ys[i] + dy * dt
    zs[i + 1] = zs[i] + dz * dt

# Set up the figure and 3D axis
fig = plt.figure(dpi=300)
ax = fig.add_subplot(111, projection='3d', facecolor='white')
#ax.set_xlabel('X Axis')
#ax.set_ylabel('Y Axis')
#ax.set_zlabel('Z Axis')
#ax.xaxis.label.set_color('white')
#ax.yaxis.label.set_color('white')
#ax.zaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

# Function to update the plot
def update(num, xs, ys, zs, line):
    line.set_data(xs[:num], ys[:num])
    line.set_3d_properties(zs[:num])
    return line,

# Create the animation
line, = ax.plot(xs, ys, zs, lw=1.2, color='cyan')
ani = animation.FuncAnimation(fig, update, frames=num_steps, fargs=(xs, ys, zs, line), interval=1, blit=True)

# Save the animation
ani.save('lorenz_attractor_high_quality.mp4', writer='ffmpeg', fps=30)

plt.show()
