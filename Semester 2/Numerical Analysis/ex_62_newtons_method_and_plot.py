import numpy as np
import matplotlib.pyplot as plt

# Constants and tolerance
EPS = 1e-8
A = -2
B = 4

# Define the function and its derivative
def f(x):
    return 1 + x*(3 + x*(-4 + x))  # f(x) = x^3 − 4x^2 + 3x + 1

def df(x):
    return 3 + x*(-8 + 3*x)  # f'(x) = 3x^2 - 8x + 3

# Newton's method
def newton(x0, eps, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < eps:  # Avoid division by zero
            return None
        x_new = x - fx / dfx
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return None

# Find all roots in the interval [A, B] by trying multiple initial guesses
def find_all_roots(a, b, step=0.1, eps=1e-8):
    roots = []
    x_vals = np.arange(a, b, step)
    for x0 in x_vals:
        root = newton(x0, eps)
        if root is not None:
            # Round to reduce duplicates due to floating point errors
            root_rounded = round(root, 6)
            if not any(abs(root_rounded - r) < 1e-5 for r in roots):
                roots.append(root_rounded)
    return sorted(roots)

# Calculate all distinct roots
all_roots = find_all_roots(A, B)

# Plot the function and the roots
x_plot = np.linspace(A, B, 400)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label='f(x)')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(all_roots, [0]*len(all_roots), color='red', label='Roots')
plt.title('Function f(x) and its Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
