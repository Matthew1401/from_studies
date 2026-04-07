import numpy as np
import math as m

# Declare the constant functions d and epsilon
d = 5
eps = 1/(10 ** (d + 1))


def anharmonic1(n):
    """Function that calculates the sum of n-th value of a series"""
    value = 0
    terms = [value]
    for k in range(1, n+1):
        value += (-1)**(k + 1) / (k ** 2)
        terms.append(value)
    return terms


def find_greatest_index(approx):
    n = 1
    terms = anharmonic1(int((1/approx)) + 1)
    while True:
        if abs(terms[n] - terms[n - 1]) < approx:
            break
        n += 1
    return n


def find_greatest_index_log(approx):
    n = 1
    terms = anharmonic1(int((1/approx)) + 1)
    while True:
        if abs(terms[n] - ((m.pi ** 2) / 12)) < approx:
            break
        n += 1
    return n

# Calculate the values from required in the task
n0 = find_greatest_index(eps)
n1 = find_greatest_index_log(eps)

a_n0 = anharmonic1(n0)[n0]
a_n1 = anharmonic1(n1)[n1]

print(f"n0: {n0}")
print(f"anharmonic(n0): {round(a_n0, d+2)}")
print(f"n1: {n1}")
print(f"anharmonic(n1): {round(a_n1, d+2)}")
print(f"π² / 12: {round(m.pi ** 2 / 12, d+2)}")
