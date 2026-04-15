import numpy as np
import matplotlib.pyplot as plt

# Parameters
a, b = 0, 2 * np.pi
n = 1000  # number of intervals (must be even number)
args = np.linspace(a, b, 2 * n + 1)
h = (b - a) / (6 * n)

# Functions x(t), y(t)
def x(t): return 5 * np.cos(t) - np.cos(5 * t)
def y(t): return 5 * np.sin(t) - np.sin(5 * t)

# Derivatives
def dx(t): return 5 * np.sin(5 * t) - 5 * np.sin(t)
def dy(t): return 5 * np.cos(t) - 5 * np.cos(5 * t)

# Simpson function for integration
def simpson_rule(fx, h):
    return h * (fx[0] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2]) + fx[-1])

# Calculate value of a function under the integral
length_integrand = np.sqrt(dx(args) ** 2 + dy(args) ** 2)
area_integrand = x(args) * dy(args)

# Calculation of an integrals
LC = simpson_rule(length_integrand, h)
AD = simpson_rule(area_integrand, h)

# Estimate error from above
# Use the fourth order derivative for extimation
def d4_area(t): return 40 * (5 * np.cos(2 * t) - 96 * np.cos(4 * t) - 486 * np.cos(6 * t) + 625 * np.cos(10 * t))
M4 = np.max(np.abs(d4_area(args)))
error_bound = (M4 * (b - a) ** 5) / (180 * (n ** 4))

# Results
print(f"Length of arc L_C ≈ {LC:.4f}")
print(f"Area A_D ≈ {AD:.4f}")
print(f"Error estimation ≤ {error_bound:.9f}")

# Plot the graps
plt.figure(figsize=(6, 6))
plt.plot(x(args), y(args), label="Curve C", color="orange")
plt.title("Parametrized Curve C")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


