# Mateusz Konieczny 22.05.2025
import matplotlib.pyplot as plt
import numpy as np

# Define constants
D = 8
EPS = 10**-D

# Define the function f(x) = x^3 − 4x^2 + 3x + 1
def f(x):
    return 1 + x*(3 + x*(-4 + x))

def g(e, x):
    f_x = f(x)
    f_e = f(e)
    return x - (((e - x) * f_x)/(f_e - f_x))

# Function finds the root of the equation f (x) = 0 in the interval [left, right]
def secant(left, right, eps):
    if f(left) * f(right) >= 0:
        raise Exception("The method fails: f(left) and f(right) must have opposite signs.")

    x = left
    x_new = g(right, x)
    step_counter = 0

    while abs(x_new - x) > eps:
        x = x_new
        x_new = g(right, x)
        step_counter += 1

    return x_new, step_counter

# Functions to check the nature of function
def is_increasing(a, b): return f(a) < f(b)
def is_decreasing(a, b): return f(a) > f(b)
def is_convex(a, b): return f((a + b)/2) < (f(a) + f(b))/2
def is_concave(a, b): return f((a + b)/2) > (f(a) + f(b))/2


def secant_auto(a, b, eps):
    # Check monotonicity and convexity
    inc = is_increasing(a, b)
    dec = is_decreasing(a, b)
    convex = is_convex(a, b)
    concave = is_concave(a, b)

    # Chose respective start point
    if (inc and convex) or (dec and concave):
        return secant(a, b, eps)
    elif (inc and concave) or (dec and convex):
        return secant(b, a, eps)
    return None

# Looking for all the roots in those intervals
intervals = [(-2, 0), (0.5, 1.5), (2, 3)]
roots = []

for a, b in intervals:
    try:
        root, steps = secant_auto(a, b, EPS)
        root = round(root, D+1)
        print(f"Root in the interval [{a}, {b}] is x = {root}, number of steps: {steps}")
        roots.append(root)
    except Exception as e:
        print(f"Error in the interval [{a}, {b}]: {e}")

# Making a graph
x_vals = np.linspace(-2.5, 3.5, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8)

# Declaring the roots
for r in roots:
    plt.plot(r, 0, 'ro')  # red dots
    plt.text(r, 0.1, f'{r:.4f}', ha='center', color='red')

plt.title('Graph of the function f(x) = x³ − 4x² + 3x + 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
