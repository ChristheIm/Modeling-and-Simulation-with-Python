# ------------------------------------------------------------------------------------------ #
# Kyungchan Im
# CST - 305
# Professor Richardo Citro
# Project 6 – Numeric Computations with Taylor Polynomials
# ------------------------------------------------------------------------------------------ #
# import packages to draw the graph for DE
import numpy as np
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------------------------ #
# Part 1a solution with visualization
# define the solution
def part_one_a(x):
    # equation found from taylor series n<=4
    # f(x) = 1 - x - (1/3) * x^3 - 1/12 * x^4
    y_a = 1 - x - (1/3 * x ** 3) - (1/12 * x ** 4)
    return y_a

# generate x values with higher resolution
x_val_a = np.linspace(0, 14, 1000)
# generate corresponding y values
y_val_a = part_one_a(x_val_a)

# plot the graph
plt.title('Part 1a) Taylor series to n<=4')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x_val_a, y_val_a)

# add label for equation in the graph
plt.text(8.5, -100, r'$f(x) = 1 - x - \frac{1}{3}x^3 - \frac{1}{12}x^4$', fontsize=12)

# add point at x=3.5
point_val = round(part_one_a(3.5), 3)
plt.plot(3.5, point_val, marker='o', markersize=5, color="red")
plt.text(2, -300, '({}, {})'.format(3.5, point_val), fontsize=10)

plt.show()

# ------------------------------------------------------------------------------------------ #
# Part 1b solution with visualization
# define the solution
def part_one_b(x):
    # equation found from second order taylor polynomial
    # f(x) = 6 + (x-3) - 11/2(x-3)^2
    y_b = 6 + (x-3) - 11/2 * ((x-3) ** 2)
    return y_b

# generate x values with higher resolution
x_val_b = np.linspace(0, 9, 1000)

# generate corresponding y values
y_val_b = part_one_b(x_val_b)

# plot the graph
plt.title('Part 1b) Second Order Taylor polynomial')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x_val_b, y_val_b)

# add labels at (2.9, part_one_b(2.9)), (3.0, part_one_b(3.0)), and (3.1, part_one_b(3.1))
plt.text(2.25, -10, '({}, {:.2f})'.format(2.999, part_one_b(2.99)), fontsize=10)
plt.plot([2.999], [part_one_b(2.999)], marker='o', markersize=5, color="red")

# add label for equation
plt.text(5.5, 5, r'$f(x) = 6 + (x-3) - \frac{11}{2}(x-3)^2$', fontsize=10)

plt.show()

# ------------------------------------------------------------------------------------------ #
# Part 2
# assign constant value for a0 and a1
a0 = 1
a1 = 1

# General Solution define
def general_solution(x):
    y = a0 * (1 + (-1 / 8 * (x ** 2)) + (1 / 128 * (x ** 4)) + (-13 / 15360 * (x ** 6)) + (403 / 3440640 * (x ** 8)) + (
                -7657 / 412876800 * (x ** 10))) + a1 * (
                    x + (-1 / 24 * (x ** 3)) + (7 / 1920 * (x ** 5)) + (-7 / 15360 * (x ** 7)) + (
                        301 / 4423680 * (x ** 9)))

    return y

# generate x values with higher resolution
x_val = np.linspace(0, 9, 1000)
# generate corresponding y values
y_val = general_solution(x_val)

# plot the graph
plt.title('Part 2: Power Series Solution with n <= 8')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x_val, y_val)

# draw the graph
plt.show()

# ------------------------------------------------------------------------------------------ #