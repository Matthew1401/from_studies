# -*- coding: utf-8 -*-
"""
You need to write a program that asks the user to enter some text and prints out the number of CAPITAL LETTERS on the screen.
"""
print("This program will put out the number of capital letters you'll enter.")
text = str(input("Enter some text: "))

print("Capital letters:", sum(1 for c in text if c.isupper()))
