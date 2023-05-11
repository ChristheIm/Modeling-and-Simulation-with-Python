# ------------------------------------------------------------------------------------------------------ #
# Kyungchan Im
# CST - 305
# Professor Richardo Citro
# Apr 23, 2023
# ------------------------------------------------------------------------------------------------------ #
# Define Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
# ------------------------------------------------------------------------------------------------------ #
# Part 2-1)
# Define Dataset
data = [
    [1, 2.22, 1, 3.22, 0, 0, 0],
    [2, 1.76, 3.22, 4.98, 1.22, 1, 0],
    [3, 2.13, 4.98, 7.11, 1.98, 2, 1],
    [4, 0.14, 7.11, 7.25, 3.11, 2, 1],
    [5, 0.76, 7.25, 8.01, 2.25, 2, 1],
    [6, 0.7, 8.01, 8.71, 2.01, 3, 2],
    [7, 0.47, 8.71, 9.18, 1.71, 4, 3],
    [8, 0.22, 9.18, 9.4, 1.18, 3, 2],
    [9, 0.18, 9.4, 9.58, 0.4, 2, 1],
    [10, 2.41, 10, 12.41, 0, 0, 0],
    [11, 0.41, 12.41, 12.82, 1.41, 1, 0],
    [12, 0.46, 12.82, 13.28, 0.82, 2, 1],
    [13, 1.37, 13.28, 14.65, 0.28, 1, 0],
    [14, 0.27, 14.65, 14.92, 0.65, 1, 0],
    [15, 0.27, 15, 15.27, 0, 0, 0]
]

columns = [
    'Arrival Time (min)', 
    'Service Duration (min)', 
    'Service Start Time', 
    'Exit Time', 
    'Time in Queue', 
    'Number in System', 
    'Number in Queue'
]

df = pd.DataFrame(data, columns=columns)

# df = pd.read_csv('dataset.csv')

arr_time = df[df.columns[0]]
ser_time = df[df.columns[1]]
sst_time = df[df.columns[2]]
ext_time = df[df.columns[3]]
time_in_queue = df[df.columns[4]]
number_in_system = df[df.columns[5]]
number_in_queue = df[df.columns[6]]

# Visualization
# Graph 1
plt.plot(arr_time, sst_time)
plt.title('Graph 1. Arrival Time vs. Service Start Time')
plt.xlabel('Arrival Time')
plt.ylabel('Service Start Time')
plt.show()

# Graph 2
plt.plot(arr_time, ext_time)
plt.title('Graph 2. Arrival Time vs. Exit Time')
plt.xlabel('Arrival Time')
plt.ylabel('Exit Time')
plt.show()

# Graph 3
plt.plot(arr_time, time_in_queue)
plt.title('Graph 3. Arrival Time vs. Time in Queue')
plt.xlabel('Arrival Time')
plt.ylabel('Time in Queue')
plt.show()

# Graph 4
plt.plot(arr_time, number_in_system)
plt.title('Graph 4. Arrival Time vs. Number in System')
plt.xlabel('Arrival Time')
plt.ylabel('Number of Customers in System')
plt.show()

# Graph 5
plt.plot(arr_time, number_in_queue)
plt.title('Graph 5. Arrival Time vs. Number in Queue')
plt.xlabel('Arrival Time')
plt.ylabel('Number of Customers in Queue')
plt.show()

# Create a figure object with 2 rows and 3 columns of subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# Plot the data for each subplot
axs[0, 0].plot(arr_time, sst_time)
axs[0, 0].set_title('Graph 1. Arrival Time vs. Service Start Time')
axs[0, 0].set_xlabel('Arrival Time')
axs[0, 0].set_ylabel('Service Start Time')

axs[0, 1].plot(arr_time, ext_time)
axs[0, 1].set_title('Graph 2. Arrival Time vs. Exit Time')
axs[0, 1].set_xlabel('Arrival Time')
axs[0, 1].set_ylabel('Exit Time')

axs[0, 2].plot(arr_time, time_in_queue)
axs[0, 2].set_title('Graph 3. Arrival Time vs. Time in Queue')
axs[0, 2].set_xlabel('Arrival Time')
axs[0, 2].set_ylabel('Time in Queue')

axs[1, 0].plot(arr_time, number_in_system)
axs[1, 0].set_title('Graph 4. Arrival Time vs. Number in System')
axs[1, 0].set_xlabel('Arrival Time')
axs[1, 0].set_ylabel('Number of Customers in System')

axs[1, 1].plot(arr_time, number_in_queue)
axs[1, 1].set_title('Graph 5. Arrival Time vs. Number in Queue')
axs[1, 1].set_xlabel('Arrival Time')
axs[1, 1].set_ylabel('Number of Customers in Queue')

axs[1, 2].set_visible(False)

# Adjust spacing between subplots
plt.subplots_adjust(left=0.01, right=0.9, bottom=0.1, top=0.9, wspace=0.5, hspace=0.5)

# Add title to the entire figure
fig.suptitle('Customer System Visualization')

# Display the final plot
plt.show()

# ------------------------------------------------------------------------------------------------------ #
# Part 2-3)
# Define lambda and mu
lam = 125
mu = 500

# Define k
k = 5

# Define the time range and initial condition
tspan = [0, 10]
y0 = [0.1] # Initial utilization

# Define the functions that describe the differential equations
def diff_eq1(t, y):
    utilization1 = lam / mu
    return utilization1

def diff_eq2(t, y):
    utilization2 = (k/k) * lam / mu
    return utilization2

# Solve the differential equations
sol1 = solve_ivp(diff_eq1, tspan, y0, t_eval=np.linspace(tspan[0], tspan[1], 100))
sol2 = solve_ivp(diff_eq2, tspan, y0, t_eval=np.linspace(tspan[0], tspan[1], 100))

# Create a figure and plot the solutions for λ/μ and (k/k) * λ/μ on the same axes
fig, ax = plt.subplots()
ax.plot(sol1.t, sol1.y[0], label='Utilization')
ax.plot(sol2.t, sol2.y[0], label='K * Utilization', linestyle='--')

# Add a title and legend to the graph
ax.set_title('Utilization Comparison with K Factor')
ax.set_xlabel('Time t')
ax.set_ylabel('Utilization')
ax.legend()

# Show the graph
plt.show()


# Define lambda and mu
lam = 125
mu = 500

# Define k
k = 5

# Define the time range and initial condition
tspan = [0, 10]
y0 = 0.1 # Initial value for lambda

# Define the functions that describe the differential equations
def throughput_eq1(t, y):
    eq1 = lam
    return eq1

def throughput_eq2(t, y):
    eq2 = k * lam
    return eq2

# Solve the differential equations
sol1 = solve_ivp(throughput_eq1, tspan, [y0], t_eval=np.linspace(tspan[0], tspan[1], 100))
sol2 = solve_ivp(throughput_eq2, tspan, [k * y0], t_eval=np.linspace(tspan[0], tspan[1], 100))

# Create a figure and plot the solutions for λ and k * λ on the same axes
fig, ax = plt.subplots()
ax.plot(sol1.t, sol1.y[0], label='Throughput')
ax.plot(sol2.t, sol2.y[0], label='k * Throughput')

# Add a title and legend to the graph
ax.set_title('Throughput vs K*Throughput')
ax.set_xlabel('Time t')
ax.set_ylabel('Throughput')
ax.legend()

# Show the graph
plt.show()


# Define lambda, mu, and k
lam = 125
mu = 500
k = 5

# Define the time range
tspan = [0, 10]

# Define the functions that describe the mean number in the system
def system_eq1():
    result = (k/k) * (lam/mu) / (1 - (k/k) * (lam/mu))
    return result

def system_eq2():
    result = (lam/mu) / (1 - (lam/mu))
    return result

# Evaluate the functions at the specified times
t_eval = np.linspace(tspan[0], tspan[1], 100)
y1_eval = np.full_like(t_eval, system_eq1())
y2_eval = np.full_like(t_eval, system_eq2())

# Create a figure and plot the results
fig, ax = plt.subplots()
ax.plot(t_eval, y1_eval, label='((k/k)*(λ/μ))/(1-(k/k)*(λ/μ))')
ax.plot(t_eval, y2_eval, label='((1*λ/μ))/(1-(1*λ/μ))', linestyle='--')

# Add a title and legend to the graph
ax.set_title('Number in System with K factor Comparison')
ax.set_xlabel('Time t')
ax.set_ylabel('Value')
ax.legend()

# Show the graph
plt.show()


# Define lambda, mu, and k
lam = 125
mu = 500
k = 5

# Define the time range
tspan = [0, 10]

# Define the functions that describe the mean number in the system
def system_eq1():
    result = 1 / (mu - lam)
    return result

def system_eq2():
    result = 1 / ((k* mu - k* lam))
    return result

# Evaluate the functions at the specified times
t_eval = np.linspace(tspan[0], tspan[1], 100)
y1_eval = np.full_like(t_eval, system_eq1())
y2_eval = np.full_like(t_eval, system_eq2())

# Create a figure and plot the results
fig, ax = plt.subplots()
ax.plot(t_eval, y1_eval, label='1 / (μ - λ)')
ax.plot(t_eval, y2_eval, label='1 / (k * (μ - λ))')

# Add a title and legend to the graph
ax.set_title('Number in Time with K factor Comparison')
ax.set_xlabel('Time t')
ax.set_ylabel('Mean Time in System')
ax.legend()

# Show the graph
plt.show()
