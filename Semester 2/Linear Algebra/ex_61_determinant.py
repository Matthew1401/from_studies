import numpy as np

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

A = np.array([[3,4,5],[1,7,2],[9,8,-6]], dtype=float)

print(det(A))


