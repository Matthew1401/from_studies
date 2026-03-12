# coding: utf8

def check_pesel(pesel: str):
    """Validates a PESEL number and returns the birthdate if valid."""

    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    if len(pesel) != 11 or not pesel.isdigit():
        return None

    # Weights for the first 10 digits (used to calculate check digit)
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3] # Weights for first 10 digits
    check_digit = sum(int(d) * w for d, w in zip(pesel[:10], weights)) % 10
    check_digit = (10 - check_digit) % 10

    if check_digit != int(pesel[-1]):
        return None

    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Setting the year and shifting the month value
    if 81 <= month <= 92: # Years 1800-1899
        year += 1800
        month -= 80
    elif 61 <= month <= 72:  # Years 2200-2299
        year += 2200
        month -= 60
    elif 41 <= month <= 52:  # Years 2100-2199
        year += 2100
        month -= 40
    elif 21 <= month <= 32:  # Years 2000-2099
        year += 2000
        month -= 20
    elif 1 <= month <= 12:  # Years 1900-1999
        year += 1900
    else: # Return None if none of the above statements holds
        return None

    return f"{months[month]} {day}, {year}"


def check_pesel_file(filename):
    """Reads PESEL numbers from a file and writes birthdate to an output file."""

    with open(filename, "r") as file, open("data.out", "a") as output:
        for pesel in file:
            result = check_pesel(pesel.strip())
            output.write((result if result else "-") + "\n")

