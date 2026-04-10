import numpy as np
import math as m


def harmonic1(d):
    """Function finds the least n satisfying the inequality 1/n < ε, say n0 and calculates value sn0 for series 1/n"""
    EPS = 1 / (10 ** (d + 1))
    n = 1
    while 1/n >= EPS:
        n += 1
    return sum(1 / k for k in range(1, n + 1))

for i in range(2, 6):
    print(harmonic1(i))
