# Mustafa Ali
# Assignment 1 - Cryptography
# Block 5
# May 8th 2026

# This program is my own work - MA

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = input("Please Enter your string ")
cipherNum = input("Please enter how much you want your cipher to shift the letters: ")
while not cipherNum.isdigit():
    cipherNum = input("Please enter a valid number: ")
newString = ""
for letter in string:
    ind = letters.index(letter)
    newIndex = ind + int(cipherNum)
    newString += letters[newIndex]

print(newString)


