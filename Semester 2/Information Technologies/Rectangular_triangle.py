# -*- coding: utf-8 -*-
"""
You need to write a program that asks the user for an integer
(the size of the triangle) and then prints a right triangle
(with a right angle in the lower left corner) composed of the characters *
with the given size. For example:

Specify the size of the triangle: 4
*
**
***
****
"""

print("This program prints a rectangular triangle for you, is you specify it's size")
text = int(input("Specify the size of the triangle: "))

def paint_triangle(size: int):
    if size <= 0:
        return
    else:
        for i in range(1, size+1):
            print("*" * i)

paint_triangle(text)
