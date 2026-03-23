import numpy as np


def back_substitution(U, b):
    n = len(b)
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / U[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - U[i][i:n] @ x[i:n]) / U[i][i]
    return x


def pivot_forward_elimination(A, b):
    n = len(A)
    for k in range(n - 1):
        i_max = np.argmax(np.abs(A[k:n, k])) + k
        if i_max != k:
            A[[k, i_max], :] = A[[i_max, k], :]
            b[[k, i_max]] = b[[i_max, k]]
        for i in range(k + 1, n):
            c = A[i][k] / A[k][k]
            A[i][k:n] = A[i][k:n] - c * A[k][k:n]
            b[i] = b[i] - c * b[k]


def pivot_gauss_elimination(A, b):
    pivot_forward_elimination(A, b)
    print(A)
    return back_substitution(A, b)


A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]], dtype=float)
b = np.array([-38, -34, -20], dtype=float)
A0 = np.copy(A)
b0 = np.copy(b)

x = pivot_gauss_elimination(A, b)
print(A0 @ x - b0)
print(x)
