# coding: utf-8
import random


def interest(A, n, p):
    return A * (1 + p/100) ** n


def celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)


def convert_to_usd(pln):
    return pln / 4.25


def calc_netto(brutto, vat=23):
    return brutto / (1 + (vat/100))


def get_short_words(text, n=5):
    return [word for word in text.split() if len(word) < n]


def message(data: dict):
    if "name" and "role" and "movie" in data:
        return f"In {data['movie']}, {data['name']} is a {data['role']}."
    else:
        return None


def throw(n):
    return sum(random.randint(1, 6) for _ in range(n))
    
def histogram():
    results = {i: 0 for i in range(2, 13)}

    for _ in range(500):
        results[throw(2)] += 1

    for value in range(2, 13):
        print(f"{value:2d}: {'#' * results[value]}")



# Below is the code to validate the function:

def almost_equal(a, b, e=1e-2):
    try:
        return abs(a - b) < e
    except TypeError:
        return False


assert almost_equal(interest(20, 5, 2), 22.082), "Function `interest` returned an invalid value"

assert almost_equal(celsius(100), 37.778), "Function `celsius` returned an invalid value"

assert almost_equal(convert_to_usd(17), 4.00), "Function `convert_to_usd` returned an invalid value"

assert almost_equal(calc_netto(50, 20), 41.67), "Function `calc_netto` returned an invalid value"

assert almost_equal(calc_netto(70), 56.91), "Function `calc_netto` (with default VAT) returned an incorrect value"

assert get_short_words("Litwo ojczyzno moja ty jesteś jak zdrowie", 3) == ['ty'], "Function `get_short_words` returned an invalid value"

assert get_short_words("Litwo ojczyzno moja ty jesteś jak zdrowie") == ['moja', 'ty', 'jak'], "Function `get_short_words` (with default n) returned an invalid value"

assert message({"name": "Han Solo", "role": "smuggler", "movie": "Star Wars"}) == "In Star Wars, Han Solo is a smuggler.", "Function `message` returned an invalid value for valid data"

assert message({"name": "Bilbo Baggins", "role": "burglar"}) is None, "Function `message` returned an invalid value for invalid data"

assert 2 <= throw(2) <= 12, "The `throw` function returned a value that is definitely not correct"


import sys
import re
from io import StringIO
_pattern = re.compile(r"^( \d|\d\d): #*$")
_stdout = sys.stdout
sys.stdout = StringIO()
try:
    histogram()
finally:
    _hist = sys.stdout.getvalue().split("\n")[:-1]
    sys.stdout = _stdout

for _line in _hist:
    assert _pattern.match(_line), f"The `histogram` function printed an incorrect line '{_line}'"


print("OK")
