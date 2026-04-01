import numpy as np
import matplotlib.pyplot as plt

coeff = [0, -3, 0, 1]
a = -2
b = 2
N = 1001
args = np.linspace(a, b, N)


def f(x):
    val = 0
    for k in range(len(coeff) - 1, -1, -1):
        val = coeff[k] + val * x
    return val


values = f(args)
plt.plot(args, values)
plt.axhline(y=0, color="black", linestyle="--")
plt.axvline(x=0, color="black", linestyle="--")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Graph of $f(x)=x^3-3x$')

plt.show()

