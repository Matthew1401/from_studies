# -*- coding: utf-8 -*-
# I changed a format of data_RMS.txt file in case to provide better optimization for my program.

import matplotlib.pyplot as plt

Y = []
X = []

with open("data_RMS.txt", "r") as file:
    next(file)  # Skip header line
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            try:
                x_val = float(parts[0])
                y_val = float(parts[1])
                X.append(x_val)
                Y.append(y_val)
            except ValueError:
                continue  # Skip malformed lines

print("X:", X)
print("Y:", Y)
print()

# Section for calculating the regression line and all this statistic stuff
# The equation of the least squares regression line is y_pr = a + bx

n = len(X)
sum_x = sum(X)
sum_y = sum(Y)
sum_x_squared = sum(x**2 for x in X)
sum_xy = sum(x * y for x, y in zip(X, Y))


def calculate_b():
    numerator = sum_xy - (sum_x * sum_y) / n
    denominator = sum_x_squared - (sum_x**2) / n
    return numerator / denominator


b = calculate_b()
y_mean = sum_y / n
x_mean = sum_x / n
a = y_mean - b * x_mean

Y_predicted_values = [a + b * x for x in X]

# Calculating errors for our regression line
residuals = [y - y_hat for y, y_hat in zip(Y, Y_predicted_values)]
SSE = sum(r**2 for r in residuals)  # Sum of squared error
Sxx = sum((x - x_mean) ** 2 for x in X)

SE_b = (SSE / (n - 2)) ** 0.5 / Sxx ** 0.5
SE_a = (SSE / (n - 2)) ** 0.5 * ((1 / n) + (x_mean ** 2) / Sxx) ** 0.5

SST = sum([(y - y_mean) ** 2 for y in Y])
SSR = SST - SSE
R2 = SSR / SST

print(f"Slope (a) = {a}")
print(f"Intercept (b) = {b}")
print(f"Standard Error of slope (b): {SE_b}")
print(f"Standard Error of intercept (a): {SE_a:.6f}")
print()
print(f"R2 = {R2}")

# Writing the graph
plt.scatter(X, Y, label="Data points", color="royalblue")
plt.plot(X, Y_predicted_values, color='red', label=f'Fit: y = {a:.3f} + {b:.5f}x')
plt.xlabel('Masa [g]')
plt.ylabel('Ugięcie [mm]')
plt.title('Least Squares Linear Fit')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
