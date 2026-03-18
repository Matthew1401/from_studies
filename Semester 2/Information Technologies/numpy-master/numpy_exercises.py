import numpy as np

A = np.array([[0,5,1], [1,0,1], [5,5,1]])

def replace_zeros(A: np.ndarray, x):
    """
    Function modifies the array `A` (of any shape) by replacing all zero elements with `x`.
    """
    A[A == 0] = x
    return A


def centered(A):
    """
    Function returns an array made of the array `A` (of any shape) in such a way that from each
    of its elements it subtracts the arithmetic mean of all elements of `A`. The array `A` itself
    remains unchanged.
    """
    return A - np.mean(A)


def below_diagonal(A):
    """
    Function, for a square array `A` (any size greater than 1), creates a one-dimensional array whose
    k-th element is the sum of the elements of the k-th column of `A` below the main diagonal.
    """
    shape = A.shape
    if shape[0] != shape[1] or shape[0] <= 1:
        return

    n = shape[0]
    B = np.zeros(n)
    for col in range(n):
        for row in range(col + 1, n):  # Only rows below the diagonal
            B[col] += A[row, col]
    return B


def checkboard(n):
    """Function creates (and returns) a square array NumPy with alternating ones and zeros of the size
    given by the invocation argument `n`, in the form:

        >>> checkboard(2)
        array([[ 1.,  0.],
               [ 0.,  1.]])

        >>> checkboard(3)
        array([[ 1.,  0.,  1.],
               [ 0.,  1.,  0.],
               [ 1.,  0.,  1.]])

        >>> checkboard(4)
        array([[ 1.,  0.,  1.,  0.],
               [ 0.,  1.,  0.,  1.],
               [ 1.,  0.,  1.,  0.],
               [ 0.,  1.,  0.,  1.]])

        >>> checkboard(5)
        array([[ 1.,  0.,  1.,  0.,  1.],
               [ 0.,  1.,  0.,  1.,  0.],
               [ 1.,  0.,  1.,  0.,  1.],
               [ 0.,  1.,  0.,  1.,  0.],
               [ 1.,  0.,  1.,  0.,  1.]])
    """
    i, j = np.indices((n, n))
    return (i + j + 1) % 2

