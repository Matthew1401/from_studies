# -*- coding: utf-8 -*-

print("Program deletes every third character from the text.")
text = input("Enter the text: ")

def delete_character(txt):
    new_text = ""
    count = 0
    for i in txt:
        count += 1
        if count == 3:
            count = 0
            continue
        else:
            new_text += i
    return new_text

print(delete_character(text))