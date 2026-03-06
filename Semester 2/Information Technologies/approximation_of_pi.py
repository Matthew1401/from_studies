# -*- coding: utf-8 -*-
"""
You should write a program that counts 10,000 consecutive approximations of the number ?
according to Wallis' formula:

         ?
        ___    4n2
    ? = | |  ———————
        | |  4n2 - 1
       n = 1

Every hundredth approximation (for N ? 100, 200, 300...) should be printed on the screen.
"""

print("Program counts 10,000 approximations of the number pi")
input("Press enter to start")


def count():
    pi = 2
    for n in range(1, 10001):
        approx = (4 * (n ** 2)) / (4 * (n ** 2) - 1)
        pi *= approx
        if n % 100 == 0:
            print(f"For n = {n} pi equals {pi}")


count()
