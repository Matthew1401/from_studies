import numpy as np
import matplotlib.pyplot as plt
import math

a = -math.pi
b = math.pi
N = 1001
t = np.linspace(a, b, N)

x = 2 * np.sin(t) * (np.cos(t) ** 2)
y = 2 * (np.sin(t) ** 2) * np.cos(t)

formulas = r'''$x(t) = 2 \sin(t) \cos^2(t)$,
$y(t) = 2 \sin^2(t) \cos(t)$'''
plt.plot(x, y, label=formulas)
plt.legend()
plt.axis("equal")
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()

