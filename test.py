# ============================================================
# Name: [Your Name]
# Date: May 20, 2026
# Course: CS20
# Description: Tic Tac Toe - Play against a friend or the computer.
#              First to get 3 in a row wins. Tie if board fills up.
# ============================================================

import random

theBoard = [' '] * 10

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def choosePlayerLetter():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O? ').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return (
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[7] == letter and board[4] == letter and board[1] == letter) or
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter) or
        (board[7] == letter and board[5] == letter and board[3] == letter) or
        (board[9] == letter and board[5] == letter and board[1] == letter)
    )

def isBoardFull(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = 0
    while move not in range(1, 10) or not isSpaceFree(board, move):
        try:
            move = int(input('Enter your move (1-9): '))
            if move not in range(1, 10):
                print('Please enter a number between 1 and 9.')
            elif not isSpaceFree(board, move):
                print('That space is already taken. Choose another.')
        except ValueError:
            print('Please enter a valid number.')
    return move

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Try to win
    for i in range(1, 10):
        boardCopy = board[:]
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Block the player from winning
    for i in range(1, 10):
        boardCopy = board[:]
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Take the center
    if isSpaceFree(board, 5):
        return 5

    # Take a corner
    for i in [1, 3, 7, 9]:
        if isSpaceFree(board, i):
            return i

    # Take any open side
    for i in [2, 4, 6, 8]:
        if isSpaceFree(board, i):
            return i

def chooseMode():
    mode = ''
    while mode not in ['1', '2']:
        mode = input('Play against (1) Computer or (2) Another Player? Enter 1 or 2: ')
    return mode

def playAgain():
    return input('Do you want to play again? (yes or no) ').lower().startswith('y')

# ============================================================
# MAIN GAME LOOP
# ============================================================
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    mode = chooseMode()
    playerLetter, computerLetter = choosePlayerLetter()
    turn = whoGoesFirst()
    print(f'{turn.capitalize()} will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You win! Congratulations!')
                gameIsPlaying = False
            elif isBoardFull(theBoard):
                drawBoard(theBoard)
                print("It's a tie!")
                gameIsPlaying = False
            else:
                if mode == '1':
                    turn = 'computer'
                # In 2-player mode, swap letters temporarily
                else:
                    playerLetter, computerLetter = computerLetter, playerLetter

        else:  # computer's turn
            if mode == '1':
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                print(f'The computer played space {move}.')

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer wins! Better luck next time.')
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a tie!")
                    gameIsPlaying = False
                else:
                    turn = 'player'
            else:
                # Two-player: second player uses the swapped letter
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Player 2 wins! Congratulations!')
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a tie!")
                    gameIsPlaying = False
                else:
                    playerLetter, computerLetter = computerLetter, playerLetter

    if not playAgain():
        print('Thanks for playing. Goodbye!')
        break