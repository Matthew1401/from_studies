# Mateusz Konieczny 22.05.2025
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

def is_increasing(a, b):
    return f(a) < f(b)

def is_decreasing(a, b):
    return f(a) > f(b)

def is_convex(a, b):
    return f((a + b) / 2) < (f(a) + f(b)) / 2

def is_concave(a, b):
    return f((a + b) / 2) > (f(a) + f(b)) / 2


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

a = 2
b = 3
x_star, n_steps = secant_auto(a, b, EPS)
print(f"Solution to f(x)=0 in the interval [{a}, {b}] is {round(x_star, D+1)} calculated in {n_steps} steps")

a = -1
b = 0
x_star, n_steps = secant_auto(a, b, EPS)
print(f"Solution to f(x)=0 in the interval [{a}, {b}] is {round(x_star, D+1)} calculated in {n_steps} steps")

a = 1
b = 2
x_star, n_steps = secant_auto(a, b, EPS)
print(f"Solution to f(x)=0 in the interval [{a}, {b}] is {round(x_star, D+1)} calculated in {n_steps} steps")
