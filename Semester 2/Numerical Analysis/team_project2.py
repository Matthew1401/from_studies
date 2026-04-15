import matplotlib.pyplot as plt
import math
import numpy as np

b = 4
x = 1.75
eps = 0.001

# Function that finds n such that n + 1 >= (b ** (n+1)) / ((5**(n+1)) * eps)
def find_n():
    n = 1
    while n < (b ** (n+1)) / ((5**(n+1)) * eps) - 1:
        n += 1
    return n

n = find_n()


# f(x) = log(1 + x/5)
def f(x):
    return math.log(1 + x/5)


# Approximation of function f(x) with the use of taylor series
def sn(x):
    suma = 0
    for k in range(1, n+1):
        suma += (((-1) ** (k+1)) * (x ** k)) / (k * (5 ** k))
    return suma


# Calculate absolute error of approximation at x.
def abs_error(x):
    n = find_n()
    approx = sn(x)
    exact = math.log(1 + x / 5)
    error = abs(approx - exact)
    return error


# Here's the section for calculation of reminder
x_vals = [x / 100 for x in range(0, 401)]
errors = [abs_error(x) for x in x_vals]
max_error = max(errors)
max_error_x = x_vals[errors.index(max_error)]

print(f"x for which the most error occurs: {max_error_x}")
print(f"The greater error on x in <0, 4>: {max_error}")
print()
print(f"n = {n}")
print(f"sn(1.75) = {sn(x)}")
print(f"log(1 + 1.75/5) = {f(x)}")


# Make a graph of a functions
# Range of x
x_vals = np.linspace(0.01, b, 400)
log_vals = [math.log(1 + x / 5) for x in x_vals]
sn_vals = [sn(x) for x in x_vals]
error_vals = [abs(s - l) for s, l in zip(sn_vals, log_vals)]

# Prepare the data
fig, axs = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.3)

# Graphs f(x) and s_n(x)
axs[0].plot(x_vals, log_vals, label='ln(1 + x/5)', color='blue')
axs[0].set_title('f(x) vs s_n(x)')
axs[0].set_ylim(0, max(log_vals) * 1.1)
axs[0].plot(x_vals, sn_vals, label='s_n(x)', color='orange')
axs[0].set_ylim(0, max(sn_vals) * 1.1)
axs[0].grid(True)

# Absolute error graph
axs[1].plot(x_vals, error_vals, label='|s_n(x) - ln(1 + x/5)|', color='red')
axs[1].set_title('Absolute error')
axs[1].set_ylim(0, max(error_vals) * 1.1)
axs[1].grid(True)

plt.xlabel('x')
plt.show()

