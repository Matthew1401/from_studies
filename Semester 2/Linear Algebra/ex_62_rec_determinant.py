import numpy as np
import random as rd

def subMatrix(A, i, j):
    B = np.delete(A, i, 0)
    return np.delete(B, j, 1)

def aux_recur_det(A, n):
    if n == 1:
        return A[0, 0]
    else:
        det = 0
        p = rd.randint(0, n-1)
        for j in range(n):
            B = subMatrix(A, p, j)
            det = det + (-1) ** (p+j) * A[p, j] * aux_recur_det(B, n-1)
        return det

def rec_det(A):
    n = A.shape[0]
    return aux_recur_det(A, n)

A = np.array([[3,4,5],[1,7,2],[9,8,-6]], dtype=float)

print(rec_det(A))
