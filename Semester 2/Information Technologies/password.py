# -*- coding: utf-8 -*-
"""
Write a program that asks the user to enter a password and then
prints out exactly one of the following messages:

The password is secure.

examine

The password is unsafe!

A secure password must meet the following conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.
"""

print("The program will check if your password is secure or insecure.")
text = str(input("Enter the password: "))

def check_password(password: str):
    lowercase = False
    capital = False
    digit = False
    for c in password:
        if c.isupper():
            capital = True
        elif c.islower():
            lowercase = True
        elif  c.isdigit():
            digit = True

    if lowercase and capital and digit:
        return "The password is secure."
    else:
        return "The password is dangerous!"


print(check_password(text))
