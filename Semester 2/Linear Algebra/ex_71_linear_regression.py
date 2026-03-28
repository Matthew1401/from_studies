import  numpy as np
import matplotlib.pyplot as plt

def linear_reg(x, y):
    slope = np.corrcoef(x, y)[1, 0] * np.std(y)/np.std(x)
    inter = np.mean(y) - slope * np.mean(x)
    return slope, inter

data = np.loadtxt('data1.txt')
X = data[:, 0]
Y = data[:, 1]
print(X)
a, b = linear_reg(X, Y)

n = np.size(X)
x = np.linspace(X[0], X[n-1],100)
y = a*x + b

plt.plot(x, y, color='b')
plt.scatter(X, Y, color='r')
plt.grid(which='major', ls='--')
plt.xlabel('$x$')
plt.ylabel('$y$', rotation='horizontal')
plt.show()
