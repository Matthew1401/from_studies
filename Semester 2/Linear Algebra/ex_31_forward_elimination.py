import numpy as np

A = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [2, 4, 1, 5], [3, 5, 2, 7]])
b = np.array([3, 5, 3, 5])

def forward_elimination(A, b):
    n = len(A)
    for k in range(n - 1):
        for i in range(k + 1, n):
            c = A[i][k] / A[k][k]
            A[i][k:n] = A[i][k:n] - c * A[k][k:n]
            b[i] = b[i] - c * b[k]

forward_elimination(A, b)


print(A)
print(b)
# print(f"A = {A}")
# print(f"b = {b}")
