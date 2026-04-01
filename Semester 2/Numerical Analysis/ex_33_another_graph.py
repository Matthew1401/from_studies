import numpy as np
import matplotlib.pyplot as plt
import math

a = -math.pi
b = math.pi
N = 1001
t = np.linspace(a, b, N)

for i in range(1, 6):
    number = round(0.4 * i, 2)

    x = number * np.sin(t) * (np.cos(t) ** 2)
    y = number * (np.sin(t) ** 2) * np.cos(t)
    formulas = rf'''$x(t) = {number} \sin(t) \cos^2(t)$,
    $y(t) = {number} \sin^2(t) \cos(t)$'''
    plt.plot(x, y, label=formulas)

plt.legend()

plt.axis("equal")
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()

