import matplotlib.pyplot as plt
import timeit
import math

a = 3
b = 2

# Define constant n to use it in the program
n = 10

def recursive_seq(n): # We use pseudo algorythm
    if n == 0:
        return a
    else:
        if n == 1:
            return b
        else:
            return math.sqrt(8 * recursive_seq(n-1) + 3 * recursive_seq(n-2)) # Formula for an


def iterative_seq(n): # We use pseudo algorythm
    prev_previous = a
    previous = b
    if n == 0:
        return prev_previous
    if n == 1:
        return previous

    for k in range(2, n+1):
        current = math.sqrt(8 * previous + 3 * prev_previous)
        prev_previous = previous
        previous = current
    return current


print(f"For n = {n} an = {recursive_seq(n)} by the use of recursive function.")
print(f"For n = {n} an = {iterative_seq(n)} by the use of iterative function.")
print()

t1 = timeit.timeit(lambda: recursive_seq(n), number=1)  # We put number 1 because it was very slow compared to iterative_seq function
t2 = timeit.timeit(lambda: iterative_seq(n), number=1000) / 1000  # We put 1000 and divide it by 1000 to get more realistic result

# Command :.6f is used to get rounded result
print(f"T1 = {t1:.6f} seconds")
print(f"T2 = {t2:.6f} seconds")
print(f"T1/T2 = {t1/t2:.6f}")
print()

# Calculate a_10k in the iteration
for k in range(4, 11):
    print(f"ak = {iterative_seq(10*k)}, for k = {10*k}")
print()

# Find the least index k that satisfied inequality from the task
k = 0
while True:
    if abs(iterative_seq(k) - 11) < 1/(10**6):
        print(f"The least index k that satisfies inequality is {k-1}.")
        break
    k += 1

# Here is the code to plot the graph of the points (n, an) for n = 0, 1, ..., 30 and line y = g
# Generate values
n_values = list(range(31))  # n = 0 to 30
an_values = [iterative_seq(n) for n in n_values]  # Compute an for each n

# Plot the points
plt.scatter(n_values, an_values, color='red',  s=12, label='Sequence (n, an)')

# Add the horizontal line y = g = 11
plt.axhline(y=11, color='green', label='y = 11')

# Labels and title
plt.xlabel('n')
plt.ylabel('an')
plt.title('Graph of (n, an) with y = 11')
plt.legend()

# Show the plot
plt.show()

