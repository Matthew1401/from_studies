import numpy as np
import math as m

# Declare the constant functions d and epsilon
d = 2
eps = 1/(10 ** (d + 1))

def anharmonic1(n):
    """Function that calculates the sum of n-th value of a series"""
    value = 0
    for k in range(1, n+1):
        value += (-1)**(k + 1) / k
    return value


def find_greatest_index(approx):
    n = 1
    while abs(anharmonic1(n) - anharmonic1(n - 1)) >= approx:
        n += 1
    return n


def find_greatest_index_log(approx):
    n = 1
    while abs(anharmonic1(n) - m.log(2)) >= approx:
        n += 1
    return n

# Calculate the values from required in the task
n0 = find_greatest_index(eps)
n1 = find_greatest_index_log(eps)

a_n0 = anharmonic1(n0)
a_n1 = anharmonic1(n1)

print(f"n0: {n0}")
print(f"anharmonic(n0): {round(a_n0, d+2)}")
print(f"n1: {n1}")
print(f"anharmonic(n1): {round(a_n1, d+2)}")
print(f"log(2): {round(m.log(2), d+2)}")
