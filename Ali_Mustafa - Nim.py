# Mustafa Ali
# Assignment 4 - Nim
# Block 5
# April 13th 2026

# This program is my own work - MA

"""
Consider any possible problems or limitations pertaining to this program.
What are they? Make the necessary modifications.

if the user was to input a letter - it would essentially break the program - and so in my isValidEntry function,
I check for if the input is even a digit so that the program doesn't crash.

"""

import random as r
import sys  # library to exit the program

TOTAL_STONES = r.randint(15, 30)

def playAgain():   # function that asks if you want to play again or not and exits the game if not
    again = input("Do you want to play again? (y/n) :")
    while again not in["y", "n"]:
        again = input("Please enter either y or n: ")
    if again == 'y':
        main()
    else:
        sys.exit()

def checkWin():   # checks if TOTAL_STONES becomes less than zero - meaning the games over
    if TOTAL_STONES <= 0:
        return True
    else:
        return False

def isValidEntry(inp):   # checks if the ntry is valid based on if its a digit and based on how many stones are left
    global TOTAL_STONES  #resets the score on every replay of the game
    if not inp.isdigit():
        return False
    elif TOTAL_STONES == 2: # if 2 stones are left
        if int(inp) == 2:
            return True
        else:
            return False
    elif TOTAL_STONES == 1: # if 1 stone is left
        if int(inp) == 1:
            return True
        else:
            return False
    else:
        if 0 < int(inp) <= 3:  # more than 3 stones left
            return True
        else:
            return False


def compTurn():   # computer's turn
    global TOTAL_STONES   #brings variable into function scope
    stonesTaken = drawStones()
    TOTAL_STONES -= stonesTaken
    print(f"The Computer took {stonesTaken} stones!")
    if checkWin():   # checks if you won
        print("Great Job! You Won :D - the AI took the last rock!")
        playAgain()   # triggers replay message


def userTurn():   # user's turn
    global TOTAL_STONES  #brings variable into function scope
    if TOTAL_STONES == 2:
        inp = input("How many stones would you like to take (1, 2 - only 2 rocks left) :")
    elif TOTAL_STONES == 1:
        inp = input("How many stones would you like to take (1 - only one rock left) :")
    else:
        inp = input("How many stones would you like to take (1, 2, 3) :")

    while not isValidEntry(inp):
        inp = input("Please enter a valid amount of stones :")

    TOTAL_STONES -= int(inp)
    if checkWin():
        print("You Lost D: - You took the last rock :/")
        playAgain()


def drawStones():   # generates random
    if TOTAL_STONES == 2:
        return r.randint(1,2)
    elif TOTAL_STONES == 1:
        return 1
    else:
        return r.randint(1, 3)

def main():
    global TOTAL_STONES
    TOTAL_STONES = r.randint(15, 30)  #resets the score on every replay of the game
    print("Welcome to the Python Nim Game! :D", "\n")
    print("**********************************")
    print(f"There are {TOTAL_STONES} stones!", "\n")
    while not checkWin():   # makes sure the game is not over
        userTurn()
        compTurn()
        if not checkWin():   # if game over dont show the score because its obviously just 0
            print(f"There are now {TOTAL_STONES} stones left!")

main()    # starts the program
