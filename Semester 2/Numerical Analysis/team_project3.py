import numpy as np
import matplotlib.pyplot as plt

# Defining the function
def f(x):
    return x**2 + x - np.exp(-0.6 * (x**2)) - 2

# Defining the derivative
def df(x):
    return 2 * x + 1 + 1.2 * x * np.exp(-0.6 * x**2)

def is_increasing(a, b): return f(a) < f(b)
def is_convex(a, b): return f((a + b)/2) < (f(a) + f(b))/2

#fuction that returns a list of the left ends of all intervals containing solutions to equation 1
def intervalsFunction(steps):
    d=0.1
    intervals = [[-3 + k * d, -3 + (k + 1) * d] for k in range(steps)]
    properIntervals=[]
    for element in intervals:
        if f(element[0])*f(element[1])<0:
            properIntervals.append(element[0])
    return properIntervals


# Mixed method root finder
def mixed_method(a, b, eps):
    increasing = is_increasing(a,b)
    convex = is_convex(a, b)

    steps = 0
    if increasing == convex:
        # Using the recursive rule (2)
        p, q = a, b
        fb=f(b)
        while abs(p - q)/2 >= eps:
            fp, fq = f(p), f(q)
            p = p - ((b-p) * fp) / (fb - fp)
            q = q - fq/df(q)
            steps += 1
        x_root = (p + q) / 2
    else:
        # Using the recursive rule (3)
        p, q = b, a
        fa=f(a)
        while abs(p - q)/2 >= eps:
            fp, fq = f(p), f(q)
            p = p - ((a-p)*fp)/(fa-fp)
            q = q - fq/df(q)
            steps += 1
        x_root = (p + q) / 2

    return x_root, steps

# Main program to find roots
d = 0.1
intervals = intervalsFunction(50)
roots = []
eps=1e-6
print(intervals)

# finding roots for intervals that have them
for a in intervals:
    b = a+0.1
    root, steps = mixed_method(a, b, eps)
    roots.append((root, steps))

# Print results
print("Roots found with 6-digit precision:")
for i, (root, steps) in enumerate(roots):
    print(f"Root {i + 1}: x = {root:.6f}, steps = {steps}")

# Plotting
x_vals = np.linspace(-3, 2, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='purple')
plt.axhline(0, color='gray', linestyle='--')
for root, _ in roots:
    plt.plot(root, f(root), 'go')
plt.grid(True)
plt.title("Function f(x) and its roots")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
