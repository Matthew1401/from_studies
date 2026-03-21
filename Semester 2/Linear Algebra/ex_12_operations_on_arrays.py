import numpy as np

A = np.array([[4, 5], [1, 2], [5, 6]])
B = np.array([[4, 3, 7], [1, 2, 6], [2, 0, 4]])
C = np.array([[2], [6], [1]])
D = np.array([[5, 4, 3, -7], [2, 1, 7, 5]])
E = np.array([[1, 5, 6], [7, 1, 3], [4, 0, 6]])
F = np.array([[2, 0, 1], [1, 7, 4]])
G = np.array([[8, 6, 4]])

#Displaying the column and rows size of above matrices
print(f"The number of rows of A = {A.shape[0]}, the number of columns of A = {A.shape[1]}.")
print(f"The number of rows of B = {B.shape[0]}, the number of columns of B = {B.shape[1]}.")
print(f"The number of rows of C = {C.shape[0]}, the number of columns of C = {C.shape[1]}.")
print(f"The number of rows of D = {D.shape[0]}, the number of columns of D = {D.shape[1]}.")
print(f"The number of rows of E = {E.shape[0]}, the number of columns of E = {E.shape[1]}.")
print(f"The number of rows of F = {F.shape[0]}, the number of columns of F = {F.shape[1]}.")
print(f"The number of rows of G = {G.shape[0]}, the number of columns of G = {G.shape[1]}.")

#Displaying the given entrie
print("\n")
print(f"a12 = {A[0, 1]}")
print(f"b23 = {B[1, 2]}")
print(f"c31 = {C[2, 0]}")
print(f"d24 = {D[1, 3]}")
print(f"e22 = {E[1, 1]}")
print(f"f12 = {F[0, 1]}")
print(f"g13 = {G[0, 2]}")

#Operation on matrices
print("\n")
print(f"E + B = \n{E+B}\n")
print(f"B - E = \n{B-E}\n")
print(f"7E = \n{7*E}\n")
print(f"C^T = \n{C.T}\n")
print(f"EB = \n{E@B}\n")
print(f"BE = \n{B@E}\n")
print(f"D^T = \n{D.T}\n")
print(f"GC = \n{G@C}\n")
print(f"E^TE = \n{E.T@E}\n")
print(f"CC^T = \n{C@C.T}\n")
print(f"FC = \n{F@C}\n")
