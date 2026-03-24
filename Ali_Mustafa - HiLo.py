# Mustafa Ali
# Assignment 2 - Operations, Guesses, and Games
# Block 5
# March 3rd 2026

# This program is my own work - MA

import random

def rand():  # random number gen function
    return random.randint(0,13)

def byebye(points): # bye message function
    print("Thank you for playing the HiLo game presented by Mustafa Games inc.")

def bet(rd, rpoint, predict): # main logic function
    if predict == 0 and rd > 7:
        print(f"YOU WON! You just gained {rpoint*2} points!")
        return rpoint*2
    elif predict == 1 and rd < 7:
        print(f"YOU WON! You just gained {rpoint*2} points!")
        return rpoint*2
    else:
        print(f"YOU LOST! You just lost {rpoint} points")
        return -rpoint


points = 1000

print("""
High Low Game

RULES
Numbers 1 through 6 are low 
Numbers 8 through 13 are high
Number 7 is neither high nor low

You have 1000 points
""")

lose = False

while not lose: # keeps on asking until you run out of points or you don't want to play anymore
    risk = int(input("Enter points to risk: "))
    predict = int(input("Predict <1=High, 0=Low>: "))

    points += bet(rand(), risk, predict)

    print(f"You have {points} left")

    if points <= 0:    # checks if you ran out of points
        lose = True
        break

    again = input("Would you like to play again? (y/n) ")
    if again == "n":  # checks if you do not want to play anymore
        lose = True

byebye(points)