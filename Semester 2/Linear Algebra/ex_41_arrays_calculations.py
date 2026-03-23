import numpy as np

A = np.array([[0.0003, 3], [1, 1]], dtype=float)
b = np.array([2.0001, 1] ,dtype=float)
x = np.zeros(2)

c = A[1,0]/A[0,0]
A[1,:] = A[1,:] - c * A[0,:]
b[1] = b[1] - c * b[0]
x[1] = b[1] / A[1,1]
x[0] = (b[0] - A[0,1] * x[1]) / A[0,0]

for i in range(3, 8):
    x1_r = round(x[1], i)
    x0_r = (b[0] - A[0,1] * x1_r) / A[0,0]
    err = np.abs((x[0] - x0_r) / x[0]) * 100
    print(f"i = {i}, x1 = {x1_r}, x0 = {x0_r}, error = {err}%")

print()
# System (2) now:
A1 = np.array([[1, 1], [0.0003, 3]], dtype=float)
b1 = np.array([1, 2.0001], dtype=float)
x1 = np.zeros(2)

c1 = A1[1,0]/A1[0,0]
A1[1,:] = A1[1,:] - c1 * A1[0,:]
b1[1] = b1[1] - c1 * b1[0]
x1[1] = b1[1] / A1[1,1]
x1[0] = (b1[0] - A1[0,1] * x1[1]) / A1[0,0]
print(x1)

for i in range(3, 8):
    x1_r = round(x1[1], i)
    x0_r = (b1[0] - A1[0,1] * x1_r) / A1[0,0]
    err = np.abs((x1[0] - x0_r) / x1[0]) * 100
    print(f"i = {i}, x1 = {x1_r}, x0 = {x0_r}, error = {err}%")
