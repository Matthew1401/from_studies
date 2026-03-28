import  numpy as np
import matplotlib.pyplot as plt

X = np.array([0, -2.5, -0.5, 2, 0.2, 2.5])
Y = np.array([0.72, 36.3825, -0.525, 0, 0.33264, 3.58875])
Y0 = np.copy(Y)

# Function to calculate the coefficient matrix for an array X
def coefficient_matrix(x):
    n = len(x)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = x[i] ** j
    return A

# By the back_substitution, forward_elimination and gauss_elimination functions we calculate the coefficients
# for a polynomial P
def back_substitution(A,b):
    n = len(b)
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - A[i, i+1:n] @ x[i+1:n]) / A[i ,i]
    return x

def forward_elimination(A, b):
    n = len(b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            c = A[i][k] / A[k][k]
            A[i][k:n] = A[i][k:n] - c * A[k][k:n]
            b[i] = b[i] - c * b[k]
    return [A ,b]

def gauss_elimination(A, b):
    forward_elimination(A, b)
    return back_substitution(A, b)

A = coefficient_matrix(X)
b = np.copy(Y)

# Here we calculate the coefficients for polynomial
coefficients = gauss_elimination(A, b)

def horner(t, a):
    n = len(a)
    S = a[-1]
    for i in range (n-2, -1, -1):
        S = S * t + a[i]
    return S
print(coefficients)

# Some basic calculations
print(f'P(13) - P(-3) = {horner(13, coefficients) - horner(-3, coefficients)}')
print(f'P(1.5) / P(0.5) = {horner(1.5, coefficients) / horner(0.5, coefficients)}')

# Sketch the graph of the f-n P
def polynomial_graph():
    x = np.linspace(min(X), max(X), 100)
    y = horner(x, coefficients)

    plt.plot(x, y, color='b')
    plt.scatter(X, Y0, color='r')
    plt.grid(which='major', ls='--')
    plt.xlabel('$x$')
    plt.ylabel('$y$', rotation='horizontal')
    plt.show()

polynomial_graph()
