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

# First matrix
A = np.array([[1,-1,3], [2,4,2], [-1,7,7]], dtype=float)
L,U,P,sign = PLU_factorization(A)
print(f'L = \n {L}')
print(f'U = \n {U}')
print(f'P = \n {P}')

print(f'LU - PA = \n {L@U - P@A}')
print(f'A - P^TLU = \n {A - P.T@(L@U)}')

#Second matrix
print()
print("Here we have the second matrix:")
A = np.array([[0,0,-1,2], [-1,-1,1,2], [2,1,-3,6], [0,1,-1,4]], dtype=float)
L,U,P,sign = PLU_factorization(A)
print(f'L = \n {L}')
print(f'U = \n {U}')
print(f'P = \n {P}')

print(f'LU - PA = \n {L@U - P@A}')
print(f'A - P^TLU = \n {A - P.T@(L@U)}')
