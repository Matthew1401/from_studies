import numpy as np

A = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [2, 4, 1, 5], [3, 5, 2, 7]])
b = np.array([3, 5, 3, 5])


def back_substitution(A,b):
    #L is a lower triangular matrix and b is a vector.
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
A0 = np.copy(A)
b0 = np.copy(b)

def gauss_elimination(A, b):
    forward_elimination(A, b)
    return back_substitution(A, b)


x = gauss_elimination(A, b)
print(x)
print(A0@x - b0)
