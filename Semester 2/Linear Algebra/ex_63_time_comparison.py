import  numpy as np
import random as rd
import timeit as tm

n = 8
A = np.zeros((n, n), dtype=float)
for i in range(n):
    for j in range(n):
        A[i, j] = rd.randint(1, 20)

# PLU method
def PLU_factorization(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.copy(A)
    P = np.eye(n, n)
    sign = 1

    for k in range(n):
        i_max = np.argmax(np.abs(U[k:n,k])) + k
        if i_max != k:
            L[[k, i_max], :] = L[[i_max, k], :]
            U[[k, i_max], :] = U[[i_max, k], :]
            P[[k, i_max], :] = P[[i_max, k], :]
            sign *= -1
        L[k:n, k] = U[k:n, k]
        U[k, k:n] = (1 / U[k,k]) * U[k, k:n]
        if k < n:
            for i in range(k+1, n):
                U[i, k:n] = U[i, k:n] - U[i, k] * U[k, k:n]
    return L,U,P,sign

def det_triangular_matrix(T):
    n = len(T)
    det = 1
    for i in range (n):
        det *= T[i, i]
    return det

def det(A):
    L, U, P, sign = PLU_factorization(A)
    return sign * det_triangular_matrix(L)

time1 = tm.default_timer()
print(f'det of A using PLU = {det(A)}')
T1 = tm.default_timer() - time1
print(f'Time for first algorithm: {T1}')

# Laplace expansion
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

time2 = tm.default_timer()
print(f'det of A using laplace = {rec_det(A)}')
T2 = tm.default_timer() - time2
print(f'Time for the second: {T2}')
print(f'T2/T1 = {T2/T1}')
