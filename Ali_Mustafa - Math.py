# Mustafa Ali
# Assignment 2 - Operations, Guesses, and Games
# Block 5
# March 3rd 2026

# This program is my own work - MA

num = int(input("Enter a number 1 or greater: "))

if num< 1: # if number is too small error checking
    num = int(input("Too small - Try again: "))

print(f"Counting from 0 to {num}: ")
for i in range(0, num + 1):
    print(i, end="   ")

print("\n")

operation = input("Choose math operations (+, -,  *): ")

while operation not in ["+", "-", "*"]:   # error checking for operation
    operation = input("Invalid input - Try again: ")

print(f"Table for {num} using {operation}:")
for i in range(1, 11):  #prints out using for loop
    if operation == "+":
        ans = num + i
    elif operation == "-":
        ans = num - i
    elif operation == "*":
        ans = num * i
    print(f"{num} {operation} {i} =", ans)
