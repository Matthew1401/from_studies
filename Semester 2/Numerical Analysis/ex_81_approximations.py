# Mateusz Konieczny 05.06.2025
import numpy as np


# Define function and its derivatives for the case of our task
def f(var): return var ** 3 - 1.5 * var ** 2
def df(var): return 3 * var ** 2 - 3 * var
def d2f(var): return 6 * var - 3


# Define functions with methods to calculate approximate value of integral
def left_sum(left_end, right_end, n):
    h = (right_end - left_end) / n
    args = np.linspace(left_end, right_end, n + 1)
    args_left = args[0:n]
    riemann_sum = np.sum(f(args_left)) * h
    abs_error = np.max(abs(df(args))) * ((right_end - left_end) ** 2 / (2 * n))
    return riemann_sum, abs_error

def right_sum(left_end, right_end, n):
    h = (right_end - left_end) / n
    args = np.linspace(left_end, right_end, n + 1)
    args_right = args[1:n+1]
    riemann_sum = np.sum(f(args_right)) * h
    abs_error = np.max(abs(df(args))) * ((right_end - left_end) ** 2 / (2 * n))
    return riemann_sum, abs_error

def mid_sum(left_end, right_end, n):
    h = (right_end - left_end) / n
    args = np.linspace(left_end, right_end, n + 1)
    args_left = args[0:n]
    args_right = args[1:n+1]
    args_mid = (args_left + args_right) / 2
    riemann_sum = np.sum(f(args_mid)) * h
    abs_error = np.max(abs(d2f(args_mid))) * ((right_end - left_end) ** 3 / (24 * n ** 2))
    return riemann_sum, abs_error

def trap_sum(left_end, right_end, n):
    h = (right_end - left_end) / n
    args = np.linspace(left_end, right_end, n + 1)
    args_trap = args[1:n]
    riemann_sum = (np.sum(f(args_trap)) + (f(left_end) + f(right_end)) / 2) * h
    abs_error = np.max(np.abs(d2f(args))) * ((right_end - left_end) ** 3 / (12 * n ** 2))
    return riemann_sum, abs_error


# Define constants for the use of a program
A = 0
B = 4
N = 100000

# Run the program and print the results
print(f"Approximate values of the integral for {N} subintervals:")

left_rule = left_sum(A, B, N)
print(f"    Left rule approximation is {left_rule[0]} with error < {left_rule[1]}")

right_rule = right_sum(A, B, N)
print(f"    Right rule approximation is {right_rule[0]} with error < {right_rule[1]}")

mid_rule = mid_sum(A, B, N)
print(f"    Midpoint rule approximation is {mid_rule[0]} with error < {mid_rule[1]}")

trap_rule = trap_sum(A, B, N)
print(f"    Trapezoidal rule approximation is {trap_rule[0]} with error < {trap_rule[1]}")

'''
I believe that the best method is Midpoint rule, by a simple observation.
Also my guess is that the value of the integral is 32.00
After changes in the value B to 2 the results are near to 0, and so it is the value of the integral.
'''
