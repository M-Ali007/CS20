# Mustafa Ali
# Assignment 3 - Penny Pitch
# Block 5
# May 28th 2026

# This program is my own work - MA

import random, sys, time
from collections import Counter

# --- Board Setup ---

# 5x5 grid where each slot starts hidden as "[  X  ]"
# Keys are row numbers (1–5), values are lists of 5 slot strings
board = {
    1: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    2: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    3: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    4: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    5: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
}

# --- Functions ---

# Prints each row of the board on its own line using * to unpack the slot list
def printBoard():
    for r in board:
        print(*board[r])


# Randomly hides prizes in slots across every row before the player throws
# Selects at least 3 slot indices per row (duplicates allowed, so a slot can be
# overwritten with a different prize — meaning fewer than 3 distinct slots may end up with prizes)
def setPrizes():
    for r in board:
        randomIndices = []

        # Keep adding indices until we have at least 3 (may contain duplicates)
        while len(randomIndices) <= 2:
            randomIndices.append(random.randint(0, 4))

        # Replace each selected slot with a randomly chosen prize emoji
        for index in randomIndices:
            rNum = random.randint(1, 5)
            match rNum:
                case 1:
                    board[r][index] = f"[ 💰 ]"
                case 2:
                    board[r][index] = f"[ 🧸 ]"
                case 3:
                    board[r][index] = f"[ 🚲 ]"
                case 4:
                    board[r][index] = f"[ 🛳️  ]"
                case 5:
                    board[r][index] = f"[ 💎 ]"


# Reveals exactly 2 distinct slots per row (10 total across the board)
# Replaces each revealed slot with "[ WON ]" and returns a flat list of what was uncovered
def checkWinnings():
    winnings = []

    for r in board:
        # Pick 2 different random slot indices
        randomIndices = [random.randint(0, 4), random.randint(0, 4)]
        while randomIndices[0] == randomIndices[1]:
            randomIndices[1] = random.randint(0, 4)

        # Record the slot's content then mark it as revealed
        for index in randomIndices:
            winnings.append(board[r][index])
            board[r][index] = "[ WON ]"

    return winnings


# Prompts the player to play again; resets the board and restarts via main() if yes, exits if no
def playAgain():
    again = input("Do you want to play again? (y/n) :")

    # Keep asking until valid input
    while again not in ["y", "n"]:
        again = input("Please enter either y or n: ")

    if again == 'y':
        # Overwrite the global board with a fresh hidden grid, then re-enter main()
        global board
        board = {
            1: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
            2: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
            3: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
            4: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
            5: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
        }
        main()
    else:
        sys.exit()


# --- Main Game Loop ---

def main():
    print("Welcome to the Python Penny (Bitcoin) Pitch Master AKA PPPM 6000!")
    print()

    while True:
        printBoard()
        print("This is your Board with INSANE hidden Prizes!!")

        # Ask the player whether they want to spend 10 Bitcoin to play this round
        ans = input("Do you want to pay 10 Bitcoin to play? (y/n) : ")
        while ans not in ["y", "n"]:
            ans = input("Please enter either y or n: ")

        if ans == "y":
            print()
            print("ALRIGHT !!! LETS GET THIS STARTED :D")
        elif ans == "n":
            break

        print()

        # Animate throwing each of the 10 bitcoins one at a time with a 1-second delay
        pennies = 0
        while pennies <= 9:
            pennies += 1
            print(f"Throwing bitcoin {pennies}...")
            time.sleep(1)

        print()

        # Hide prizes on the board, then reveal the player's 10 random slots
        setPrizes()
        winnings = checkWinnings()

        print()
        printBoard()

        # Convert raw emoji slot strings into readable prize names (blank "[  X  ]" slots are skipped)
        finalWinnings = []

        for win in winnings:
            match win:
                case "[ 💰 ]":
                    finalWinnings.append("some Money")
                case "[ 🧸 ]":
                    finalWinnings.append("a Teddy Bear")
                case "[ 🚲 ]":
                    finalWinnings.append("a Bicycle")
                case "[ 🛳️  ]":
                    finalWinnings.append("a Cruise Ship Ticket")
                case "[ 💎 ]":
                    finalWinnings.append("a Diamond")
                case "[  X  ]":
                    pass


        # Count how many of each prize the player got; only prizes with 3+ matches are awarded
        # Then assemble a grammatically correct "You won X, Y, and Z." summary string
        countedList = Counter(finalWinnings)
        prizeList = []
        numWin = 0

        for key, value, *_ in countedList.items():
            if int(value) >= 3:
                prizeList.append(key)
                numWin += 1

        text = "You won "
        if numWin == 0:
            text += "Nothing D;"
        else:
            for i in range(numWin):
                if numWin == 1:
                    text += f"{finalWinnings[i]}."
                else:
                    if i == numWin - 1:
                        text += f"and {finalWinnings[i]}."
                    elif i < numWin:
                        text += finalWinnings[i] + ", "

        print()
        print(text)
        print()

        playAgain()
        break


# --- Entry Point ---
main()
