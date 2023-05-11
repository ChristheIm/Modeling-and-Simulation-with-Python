# Alexander Peltier, Kyungchan Im

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simps
from scipy import pi

partTwo = lambda x: (0.1216 * x) + 20.121

# Graph steps
steps = 100

# calculate and graph left, mid, and right sums given a function and its parameters
def graphRiemannApproximation(f, lower, upper, n, title):

    # get x at equally spaced n+1 points between lower and upper
    x1 = np.linspace(lower, upper, n + 1)

    # get x at equally spaced steps * n+1 points between lower and upper
    x2 = np.linspace(lower, upper, steps * n + 1)

    # This is pretty handy. It will copy the number of steps in the np.array and generate y values for each x
    y1 = f(x1)
    y2 = f(x2)

    # Left subplot
    plt.subplot(1, 3, 1)
    plt.plot(x2, y2, 'r')

    # Populate x and y
    xLeft = x1[:-1]
    yLeft = y1[:-1]

    # plot, add blue dots
    plt.plot(xLeft, yLeft, 'b.')
    # add rectangles
    plt.bar(xLeft, yLeft, width=(upper - lower) / n)

    # give that baby a title!
    plt.title('Left')


    # Midpoint subplot
    plt.subplot(1, 3, 2)
    plt.plot(x2, y2, 'y')

    # Where do the dots go? There! and there!
    x_midpoint = np.linspace(lower + (upper-lower)/(2*n), upper - (upper-lower)/(2*n), n)
    y_mid = f(x_midpoint)

    # plot, add blue dots
    plt.plot(x_midpoint, y_mid, 'b.')
    # add rectangles
    plt.bar(x_midpoint, y_mid, width=(upper - lower) / n)

    # Title it.
    plt.title('Midpoint')

    # Right subplot
    plt.subplot(1, 3, 3)
    plt.plot(x2, y2, 'g')

    # Populate x and y
    x_right = x1[1:]
    y_right = y1[1:]

    # The dots. They are everywhere.
    plt.plot(x_right, y_right, 'b.')
    plt.bar(x_right, y_right, width=-(upper - lower) / n)

    # Oooo thats nice.
    plt.title('Right')

    # Give the whole figure a friggen title. Ain't that cool?
    plt.suptitle(f"Riemann Sum Approximation for ${title}$")

    # Show our hard work.
    plt.show()

# Call the function for all three parts (and sub-parts!)
graphRiemannApproximation(partTwo, 0, 30, 3, "partTwo")

# calculate left, mid, and right sums given a function and its parameters
def RiemannApproximation(f, lower,upper, n, part):
    
    print("\nPart\t", part)

    # Get steps
    steps = (upper - lower) / n

    # Left step size
    x_left = np.linspace(lower, upper - steps, n)
    # Midpoint step size
    x_midpoint = np.linspace(lower + steps/2, upper - steps / 2, n)
    # Right step size
    x_right = np.linspace(lower + steps, upper, n)

    # Get approximations
    leftSum = np.sum(f(x_left) * steps)
    midSum = np.sum(f(x_midpoint) * steps)
    rightSum = np.sum(f(x_right) * steps)

    print("Left Ans:\t", leftSum)
    print("Midpoint Ans:\t", midSum )
    print("Right Ans:\t", rightSum)

RiemannApproximation(partTwo, 0, 30, 1, "Part 2")

