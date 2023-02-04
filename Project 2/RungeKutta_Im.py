# ---------------------------------------------------------------------------------------------------------------- #
# Project 2 – Runge-Kutta-Fehlberg (RKF) for ODE
# Kyungchan Im
# CST - 305
# Professor Richardo Citro
# 02/05/2023
# ---------------------------------------------------------------------------------------------------------------- #
# Part 1
# ---------------------------------------------------------------------------------------------------------------- #
# Import packages to for this project
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math
import time

# The ODE is 𝑓(𝑥,𝑦)= −𝑦+𝑙𝑛𝑥 ,𝑥0=2,𝑦0=1,ℎ=0.3
# We can always change the equation and run it.
def equation(x,y, index):
    print("k{} : ".format(index), round((-y + math.log(x, math.e)), 5))
    return round((-y + math.log(x, math.e)), 5)

    
# Take initial variables for x0, y0, and h.
# n is for number of data points n = 5 => 5 data point (x1,x2,x3,x4,x5)
# Calcuation function for RungeKutta
def calculation(x0,y0,h,n):
    xn = float(x0)          
    k = float(y0)
    counter = 1
    
    x_axis = []
    y_axis = []
    
    # Calculating step size
    print('\n-------------------SOLUTION------------------')
    print('---------------------------------------------')    
    print('x0 = {}\ty0 = {}\th = {}'.format(x0,y0,h))
    print('---------------------------------------------')
    
    # will perform the n counts of calculation of Runge kutta
    # and execute the points
    for i in range(int(n)):
        index = 1
        k1 = equation(xn, k, index)
        
        index += 1
        k2 = equation((xn+(h/2)), (k+((h/2)*k1)), index)
        
        index += 1
        k3 = equation((xn+(h/2)), (k+((h/2)*k2)), index)

        index += 1
        k4 = equation((xn+h), (k+(h*k3)), index)
        
        k = round(y0 +((k1+(2*k2)+(2*k3)+k4)/6)*h,5)
        y0 = k
        xn = round(xn + h,5)
        print("x{}, y{} =".format(counter, counter),"({}, {})".format(xn, k))
        x_axis.append(xn)
        y_axis.append(k)
        print('---------------------------------------------')
        counter += 1
        
    return x_axis, y_axis

# This function performs the basic print out statements.
def Runge_Kutta():
    print("Runge Kutta Calculation\n")
    print('Enter initial conditions for x:')
    x0 = float(input())
    print('Enter initial conditions for y:')
    y0 = float(input())
    print('Enter initial conditions for h:')
    h = float(input())
    print('How many data points do you want? (n):')
    n = int(input())
    
    # Grabbing a x_axis values and y_axis values from calculation
    x_axis, y_axis = calculation(x0,y0,h,n)
    
    # return n, x_axis, and y_axis values to use outside of scope
    return x_axis, y_axis, n


# ---------------------------------------------------------------------------------------------------------------- #
# Part 2 
# ---------------------------------------------------------------------------------------------------------------- #
# Equation for ODE
def ode_function(y, x):
    return -y + math.log(x, math.e)



if __name__ == "__main__":
# Part 1
# assign x range and y range for draw a graph for RK for n points
    x_axis, y_axis, n = Runge_Kutta()

# Part 2
    # time.time() method for calculate the computation time
    start_time = time.time()

    # initial value assign
    x0 = 2
    y0 = 1
    h = 0.3

    x_range = np.arange(x0, x0 + (n)*h, h)       # creating a x-axis values upto n points
    solution = odeint(ode_function, y0, x_range)    # solve for ODE 

    print("\nODE Analysis:")
    print("x: ", x_range[:6])      # Print first 5 values 
    print("y: ", solution[:6])
    print("Number of computational steps: ", len(x_range))
    print("Computing time: %s seconds" % round((time.time() - start_time),5)) # where the program calculates the time



# Visualization
    # Plotting for RungeKutta
    plt.plot(x_range, solution, 'r-', linewidth=1,label='k=RungeKutta')

    # Plotting for ODE
    plt.plot(x_axis, y_axis,'g:', linewidth=3,label='k=ODE')

    plt.title('1500 points of RungeKutta vs ODE')   # title
    plt.xlabel('X_val')                             # x_title
    plt.ylabel('Y_val')                             # y_title
    plt.xlim([min(x_range), max(x_range)])          # x-axis range = min to max
    plt.ylim([min(solution), max(solution)])        # y-axis range = min to max
    plt.legend()

    plt.show()


# Error Evaluation
    # Calculate all individual difference index by index
    evaluation = []
    for i in range(n):
        evaluation.append(y_axis[i] - solution[i])

    # Once evaluation is done, return it to percentage
    error_eval = (sum(evaluation) / n) * 100
    error_eval = round(error_eval.item(),2)

    # Printing the comment for error evaluation
    print("Error Percentage of RK vs ODE = {}%".format(error_eval))