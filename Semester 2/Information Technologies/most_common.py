# -*- coding: utf-8 -*-

alfabet = {chr(letter): 0 for letter in range(65, 91)}

print("Program prints as output the most common letter you'll enter in a text.")
text = input("Enter the text: ").upper()

for c in text:
    if c in alfabet:
        alfabet[c] += 1

max_count = max(alfabet.values())
most_common_letters = [letter for letter, count in alfabet.items() if count == max_count]
for char in most_common_letters:
    print(char)
