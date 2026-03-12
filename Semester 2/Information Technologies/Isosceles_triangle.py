# -*- coding: utf-8 -*-
"""
You need to write a program that asks the user for an integer
(the size of the triangle) and then prints an isosceles triangle
composed of * characters of the given size. For example:

Specify the size of the triangle: 3
  *
 ***
*****
"""
print("This program prints a isosceles triangle for you, is you specify it's size")
text = int(input("Specify the size of the triangle: "))

def paint_triangle(size: int):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

paint_triangle(text)