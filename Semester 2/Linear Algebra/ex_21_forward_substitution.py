import numpy as np

def forward_substitution(L, b):
    n = len(b)
    x = np.zeros(n)
    x[0] = b[0] / L[0, 0]
    for i in range(1, n):
        x[i] = (b[i] - L[i, 0:i] @ x[0:i]) / L[i ,i]
    return x

L = np.array([[2, 0 ,0], [4, -2, 0], [-5, 1, 3]])
b = np.array([6, 10, 1])
print(forward_substitution(L, b))
