# Mustafa Ali
# Assignment 3 - Penny Pitch
# Block 5
# May 28th 2026

# This program is my own work - MA

import random, sys, time


# --- Board Setup ---

# The game board: 5 rows, each with 5 hidden slots (all start as [  X  ])
board = {
    1: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    2: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    3: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    4: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
    5: ["[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]", "[  X  ]"],
}

# --- Functions ---

# Prints all 5 rows of the board
def printBoard():
    for r in board:
        print(*board[r])


# Randomly places prizes in 3+ slots per row
def setPrizes():
    for r in board:
        randomIndices = []

        # Pick at least 3 random slot indices for this row
        while len(randomIndices) <= 2:
            randomIndices.append(random.randint(0, 4))

        # Assign a random prize to each selected slot
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


# Randomly reveals 2 slots per row and returns what was won
def checkWinnings():
    winnings = []

    for r in board:
        # Pick 2 different random slot indices
        randomIndices = [random.randint(0, 4), random.randint(0, 4)]
        while randomIndices[0] == randomIndices[1]:
            randomIndices[1] = random.randint(0, 4)

        # Mark revealed slots as won and collect their contents
        for index in randomIndices:
            winnings.append(board[r][index])
            board[r][index] = "[ WON ]"

    return winnings


# Asks the player if they want to play again, restarts or exits accordingly
def playAgain():
    again = input("Do you want to play again? (y/n) :")

    # Keep asking until valid input
    while again not in ["y", "n"]:
        again = input("Please enter either y or n: ")

    if again == 'y':
        # Reset the board and restart
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

        # Ask the player if they want to pay to play
        ans = input("Do you want to pay 10 Bitcoin to play? (y/n) : ")
        while ans not in ["y", "n"]:
            ans = input("Please enter either y or n: ")

        if ans == "y":
            print()
            print("ALRIGHT !!! LETS GET THIS STARTED :D")
        elif ans == "n":
            break

        print()

        # Simulate throwing 10 pennies one by one
        pennies = 0
        while pennies <= 9:
            pennies += 1
            print(f"Throwing bitcoin {pennies}...")
            time.sleep(1)

        print()

        # Set prizes and reveal winnings
        setPrizes()
        winnings = checkWinnings()

        print()
        printBoard()

        # Tally up what the player actually won
        finalWinnings = []
        numWin = 0

        for win in winnings:
            match win:
                case "[ 💰 ]":
                    finalWinnings.append("some Money")
                    numWin += 1
                case "[ 🧸 ]":
                    finalWinnings.append("a Teddy Bear")
                    numWin += 1
                case "[ 🚲 ]":
                    finalWinnings.append("a Bicycle")
                    numWin += 1
                case "[ 🛳️  ]":
                    finalWinnings.append("a Cruise Ship Ticket")
                    numWin += 1
                case "[ 💎 ]":
                    finalWinnings.append("a Diamond")
                    numWin += 1
                case "[  X  ]":
                    pass


        # Build and print the winnings summary sentence
        text = "You won "
        for i in range(numWin):
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