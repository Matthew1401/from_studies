# Program for my calculations
import math

# Data in [cm]
x_os = 4.2
x_n = [105.6, 103.1, 98.5, 93.4, 86.3, 82.7, 79.2, 75.4, 69.9, 64.9, 62.0, 59.1, 55.1, 54.7, 52.5, 50.6]
X = 0.02
r_0 = x_n[0] - x_os - X

for i in x_n:
    print(f"log((i - x_os - X) / r_0), 6")
    print(round(math.log((i - x_os - X) / r_0), 6))

for i in x_n:
    print(i / 100)