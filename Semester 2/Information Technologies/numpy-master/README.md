# NumPy Exercises

1. Write a function `replace_zeros(A, x)` that modifies the array `A` (of any shape) by replacing all zero elements with `x`.

2. Write a function `centered(A)` that returns an array made of the array `A` (of any shape) in such a way that from each of its elements it subtracts the arithmetic mean of all elements of `A`. The array `A` itself should remain unchanged.

3. Write a function `below_diagonal(A)` that, for a square array `A` (any size greater than 1), creates a one-dimensional array whose _k_-th element is the sum of the elements of the _k_-th column of `A` below the main diagonal.

4. Write a function `checkboard(n)` that creates (and returns) a square array NumPy with alternating ones and zeros, of the size given by the invocation argument `n`, in the form:

   ```python
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
   ```