# Mateusz Konieczny 15.05.2025

# Define constants
A = 2
B = 3
D = 8
EPS = 10**-D

# Define the function f(x) = x^3 − 4x^2 + 3x + 1
def f(x):
    return 1 + x*(3 + x*(-4 + x))

# Define the derivative of a function f
def df(x):
    return 3 + x*(-8 + 3*x)

# Function finds the root of the equation f (x) = 0 in the interval [left, right]
def newton(left, right, eps):
    if f(left) * f(right) >= 0:
        raise Exception("The method fails: f(left) and f(right) must have opposite signs.")

    x = right
    n = 0  # Number of iterations

    while True:
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise Exception("Derivative is zero. Newton's method fails.")

        x_new = x - fx / dfx
        n += 1

        if abs(x_new - x) < eps:
            break

        x = x_new

    return x_new, n

def is_increasing(a, b):
    return f(a) < f(b)

def is_convex(a, b):
    return f((a + b) / 2) < (f(a) + f(b)) / 2

def newton_auto(a, b, eps):
    # Check monotonicity and convexity
    inc = is_increasing(a, b)
    convex = is_convex(a, b)

    # Chose respective start point
    if (inc and convex) or (not inc and not convex):
        return newton(a, b, eps)
    else:
        return newton(b, a, eps)

x_star, n_steps = newton_auto(A, B, EPS)
print(f"Solution to f(x)=0 in the interval [{A}, {B}] is {round(x_star, D+1)} calculated in {n_steps} steps")
