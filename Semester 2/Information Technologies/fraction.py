"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (TypeError if not),
- method `decimal` returning the decimal value of the fraction.
"""
from math import gcd


class Fraction:
    """
    Fraction class.
    """

    def __init__(self, nom, denom):
        if denom == 0:
            raise ValueError("The denominator cannot be 0")
        if not isinstance(nom, int) or not isinstance(denom, int):
            raise TypeError("Both attributes must be integers!")

        # Simplifying a fraction
        common = gcd(nom, denom)
        nom = nom // common
        denom = denom // common

        # Changing the sign
        if denom < 0:
            nom = -nom
            denom = -denom

        self.nom = nom
        self.denom = denom

    def __str__(self):
        if self.denom == 1:
            return f"{self.nom}"
        return f"{self.nom}/{self.denom}"

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom

    def __add__(self, other):
        result_nom = self.nom * other.denom + other.nom * self.denom
        result_denom = self.denom * other.denom
        return Fraction(result_nom, result_denom)

    def __sub__(self, other):
        result_nom = self.nom * other.denom - other.nom * self.denom
        result_denom = self.denom * other.denom
        return Fraction(result_nom, result_denom)

    def __mul__(self, other):
        result_nom = self.nom * other.nom
        result_denom = self.denom * other.denom
        return Fraction(result_nom, result_denom)

    def __truediv__(self, other):
        if other.nom == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        result_nom = self.nom * other.denom
        result_denom = self.denom * other.nom
        return Fraction(result_nom, result_denom)

    @property
    def decimal(self):
        return self.nom / self.denom
