import numpy as np

U = np.array([[3, 1 ,-5], [0, -2, 4], [0, 0, 2]])
b = np.array([1, 10, 6])

def back_substitution(U,b):
    n = len(b)
    x = np.zeros(n)
    x[n-1] = b[n-1] / U[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - U[i, i+1:n] @ x[i+1:n]) / U[i ,i]
    return x

print(back_substitution(U, b))
