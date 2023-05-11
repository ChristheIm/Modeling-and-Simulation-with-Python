# ------------------------------------------------------------------------------------------------------ #
# Kyungchan Im
# CST - 305
# Professor Richardo Citro
# Apr 23, 2023
# ------------------------------------------------------------------------------------------------------ #
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(xyz, *, s=10, r=28, b=(8/3)):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

# Prompt user to enter r value
r = float(input("Enter r value for Lorenz attractor: "))

# Define the initial values and number of steps
dt = 0.01
num_steps = 10000
xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (11.8, 4.4, 2.4)

# Evaluate Lorenz attractor for the specified r value
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], r=r) * dt

# Plot the 3D attractor
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(f"Lorenz Attractor of r = {r}")

# Plot the x component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 0], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("X Coordinate")
ax.set_title(f"Lorenz Attractor: X Component (r = {r})")

# Plot the y component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 1], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Y Coordinate")
ax.set_title(f"Lorenz Attractor: Y Component (r = {r})")

# Plot the z component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 2], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Z Coordinate")
ax.set_title(f"Lorenz Attractor: Z Component (r = {r})")

plt.show()
