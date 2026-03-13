# -*- coding: utf-8 -*-
"""
The program is to print two roots of a quadratic equation of the form

a x2 + b x + c = 0
"""

print("Solving a quadratic equation of the form a x2 + b x + c = 0")

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

coefficients = [c, b, a]

def calculate(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    if c != 0:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            x1 = (-b - discriminant ** (1 / 2)) / 2 * c
            x2 = (-b + discriminant ** (1 / 2)) / 2 * c
            solutions = (x1, x2)
            return solutions
        elif discriminant == 0:
            x0 = -b / 2 * c
            solutions = (x0)
            return solutions
        else:
            return "The equation has no real solutions"
    else:
        return "This is not a quadratic equation"

solutions = calculate(coefficients)
print(solutions)
