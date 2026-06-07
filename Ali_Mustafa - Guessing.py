# Mustafa Ali
# Assignment 2 - Operations, Guesses, and Games
# Block 5
# March 3rd 2026

# This program is my own work - MA

import random

print("Guessing Game")
print("\n")
print("Instructions: Try to guess the number between 1 and 100")
tries = 1
randnum = random.randint(1, 100)  # creates random number
win = False
while not win: # keeps on asking until you win
    num = int(input("Enter number (1 to 100): "))
    if num > randnum: # guess more than random number
        print("Too high! ", end="")
        tries+=1
    elif num < randnum:  # guess less than random number
        print("Too low! ", end="")
        tries+=1
    elif num == randnum: # guess the same as the random number
        print("That's correct!")
        print("\n")
        print(f"It took you {tries} tries to correctly guess {randnum}")