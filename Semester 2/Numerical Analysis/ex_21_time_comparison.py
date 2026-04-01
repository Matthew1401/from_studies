import numpy as np
from timeit import default_timer as tm

coeff = [7, -4, 3, -12, 5]
a = -5
b = 5
N = 100001
arg = np.linspace(a, b, N)

def poly1(x):
    val = 0
    for i in range(len(coeff)):
        val += coeff[i] * x ** i
    return val

def poly2(x):
    val = 0
    for k in range(len(coeff) - 1, -1, -1):
        val = coeff[k] + val * x
    return val

start_time1 = tm()
values1 = poly1(arg)
calc_time1 = tm() - start_time1

start_time2 = tm()
values2 = poly2(arg)
calc_time2 = tm() - start_time2

print(f"Time1 = {calc_time1}s\nTime2 = {calc_time2}s\nDifference of {calc_time1/calc_time2} times")
