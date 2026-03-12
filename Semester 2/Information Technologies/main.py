# coding: utf8

import card
import pesel


assert pesel.check_pesel('90090515836') == 'September 5, 1990', "The function did not return the date of birth according to the indicated format"
assert pesel.check_pesel('01261051813') == 'June 10, 2001', "The function did not return the date of birth according to the indicated format"
assert pesel.check_pesel('87832165181') == 'March 21, 1887', "The function did not return the date of birth according to the indicated format"
assert pesel.check_pesel('90090525836') is None, "Function returned `None` for invalid PESEL value"
assert pesel.check_pesel('01261031813') is None, "Function returned `None` for invalid PESEL value"
assert pesel.check_pesel('87832165581') is None, "Function returned `None` for invalid PESEL value"
assert pesel.check_pesel('123456789') is None, "Function returned None for invalid and too short PESEL value"

pesel.check_pesel_file('data.txt')
with open('data.out', 'r') as result:
    correct = ['September 5, 1990', 'March 21, 1887', '-', 'June 10, 2001', '-']
    assert correct == [line.rstrip() for line in result.readlines()], "The resulting file is incorrect"

assert card.check_card('4929134138580797'), "Function did not return True for a valid card number"
assert card.check_card('370594756527911'), "Function did not return True for a valid card number"
assert card.check_card('79927398713'), "Function did not return True for a valid card number"
assert not card.check_card('79927398710'), "Function did not return False for incorrect card number"
