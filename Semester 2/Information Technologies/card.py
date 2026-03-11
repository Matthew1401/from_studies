# coding: utf8


def check_card(number: str) -> bool:
    """Checks if the credit card number is valid using Luhn's algorithm."""

    number = number[::-1]
    total_sum = 0

    for i, digit in enumerate(number):
        num = int(digit)
        if i % 2 == 1:    # Double every second digit
            num *= 2
            if num > 9:
                num -= 9    # Equivalent to summing digits of numbers ≥10
        total_sum += num

    return total_sum % 10 == 0

