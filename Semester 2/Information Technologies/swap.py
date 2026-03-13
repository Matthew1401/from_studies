# -*- coding: utf-8 -*-

print("Program switches the places of data you input. Enter the data and each element divide with a space.")
text = input(": ")
data = text.split()

for i in range(0, len(data), 2):
    if i == len(data) - 1:
        break
    temp = data[i]
    data[i] = data[i+1]
    data[i+1] = temp

print(data)
