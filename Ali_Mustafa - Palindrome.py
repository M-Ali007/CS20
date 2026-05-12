# Mustafa Ali
# Exercise 2 - Palindrome
# Block 5
# May 8th 2026

# This program is my own work - MA

print("Welcome to the Grand Python Palindrome Identifier 6000!")
inp = input("Please enter your string:  ")
cleaninp = ""
for letter in inp:
    if letter.isalpha():
        cleaninp += letter

reversed_inp = cleaninp[::-1]
if cleaninp==reversed_inp:
    print("CONGRATULATIONS! - Your word IS a palindrome!!!")
else:
    print("Your word is NOT a palindrome, Better luck next time :(")