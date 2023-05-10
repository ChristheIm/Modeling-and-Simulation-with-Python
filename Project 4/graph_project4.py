# --------------------------------------------------------------------------- #
# Kyungchan Im
# CST - 305
# Professor Richardo Citro
# Mar 8, 2023
# Project 4 – Degradation of Data Integrity
# --------------------------------------------------------------------------- #
# Import Package to use
import numpy as np                          # numpy for matrix and array
import matplotlib.pyplot as plt             # visualization package


# --------------------------------------------------------------------------- #
# Part 2 solution 1
def x_one(t):
    return np.exp(-0.05 * t)  # returns solution found from e^At

# Part 2 solution 2
def x_two(t):
    return (-1 * np.exp(-0.05 * t))


# --------------------------------------------------------------------------- #
# Visualization 
t_space = np.linspace(-100, 100, 200)  # testing 0 to 100 x points
x1space = []
x2space = []
for i in t_space:
    x1space.append(x_one(i))  # fill first solution space for solution 1
    x2space.append(x_two(i))  # fill second solution space for solution 2
    
# Drawing the chart and some labels
plt.title("Degradation of data integrity - ODE Solutions by Matrix Method")
plt.xlabel("t") # name for x-axis
plt.ylabel("x") # name for y-axis

plt.plot(t_space, x1space, label='e^-0.05t')    # plot the point
plt.plot(t_space, x2space, label='-e^-0.05t')   # plot the point

plt.ylim(-50, 50)  # y-window for -3 to 3
plt.xlim(-100, 100) # x-window for 0 to 100
plt.grid()
plt.legend()
plt.show()