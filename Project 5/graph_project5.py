##########################################################################################
# import the packages for drawing a lorenz graph
import numpy as np
import matplotlib.pyplot as plt
##########################################################################################
# define the lorenz function.
# initial values are assigned s = 10, b = 8/3
def lorenz(xyz, *, s=10, r=28, b=(8/3)):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
        Point of interest in three-dimensional space.
    s, r, b : float
        Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

# setting the number of steps and increment of t
dt = 0.01
num_steps = 10000


xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (11.8, 4.4, 2.4)  # Set initial values

# Step through "time", calculating the partial derivatives at the current point
# Define the values of r to plot [8 = neutral, 15 = in-between, 28 = chaotic]
##########################################################################################
# Neutral r = 8
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], r=8) * dt

# Plot the 3D attractor
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(f"Lorenz Attractor of Neutral State (r = 8)")        

# Plot the x component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 0], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("X Coordinate")
ax.set_title(f"Lorenz Attractor: X Component (r = 8)")

# Plot the y component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 1], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Y Coordinate")
ax.set_title(f"Lorenz Attractor: Y Component (r = 8)")

# Plot the z component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 2], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Z Coordinate")
ax.set_title(f"Lorenz Attractor: Z Component (r = 8)")


plt.show()
##########################################################################################
# In-between r = 15
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], r=15) * dt

# Plot the 3D attractor
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(f"Lorenz Attractor of In-between State (r = 15)")        

# Plot the x component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 0], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("X Coordinate")
ax.set_title(f"Lorenz Attractor: X Component (r = 15)")

# Plot the y component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 1], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Y Coordinate")
ax.set_title(f"Lorenz Attractor: Y Component (r = 15)")

# Plot the z component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 2], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Z Coordinate")
ax.set_title(f"Lorenz Attractor: Z Component (r = 15)")


plt.show()
##########################################################################################
# Chaotic r = 28
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], r=28) * dt

# Plot the 3D attractor
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(f"Lorenz Attractor of In-between State (r = 28)")        

# Plot the x component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 0], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("X Coordinate")
ax.set_title(f"Lorenz Attractor: X Component (r = 28)")

# Plot the y component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 1], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Y Coordinate")
ax.set_title(f"Lorenz Attractor: Y Component (r = 28)")

# Plot the z component
fig, ax = plt.subplots()
ax.plot(xyzs[:, 2], lw=0.5)
ax.set_xlabel("Time Step")
ax.set_ylabel("Z Coordinate")
ax.set_title(f"Lorenz Attractor: Z Component (r = 28)")


plt.show()
##########################################################################################