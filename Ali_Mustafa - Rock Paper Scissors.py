# Rock, Paper, Scissors
from os import system
from random import randint
from sys import exit

class rock_paper_scissors:
    def __init__(self):  # FIX 1: Added missing 'self' parameter — without it, Python
                         # raises a TypeError when the object is created.
        self.choices = "rock", "paper", "scissors"
        self.player_wins = 0
        self.computer_wins = 0

    def _spacer_size(self, length=65):
        return '-' * length

    def _player_move(self):
        while True:
            try:
                option = int(input('Choose an option between Rock (1), Paper (2), Scissors (3): '))
                if 1 <= option <= 3:
                    break
                else:
                    print('You can only enter a number between 1 and 3.')
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')
        return option

    def _computer_move(self):
        return randint(1, 3)

    def _check_winner(self):
        if self.player_wins == self.computer_wins:
            return 'Tie.'
        elif self.player_wins > self.computer_wins:
            return 'You won the set.'
        else:
            return 'Computer wins the set.'

    def _play(self):
        times = int(input("How many times do you wish to play?: "))

        for i in range(times):
            player = self._player_move()
            computer = self._computer_move()
            print(f"You chose {self.choices[player - 1]}.")
            print(f"The computer chose {self.choices[computer - 1]}.")

            if player == computer:
                print('Tie.\n')
                print(self._spacer_size(), '\n')
            elif (player - computer) % 3 == 1:
                print('You won.\n')
                print(self._spacer_size(), '\n')
                self.player_wins += 1
            else:
                print('You lost.\n')
                print(self._spacer_size(), '\n')
                self.computer_wins += 1

        print(self._check_winner())
        input("Press a key to return to the main menu...")
        system("CLS")
        self.main()

    def main(self, length=95):
        while True:
            try:
                print('-' * length, '\n')
                print('''
                █▀█ █▀█ █▀▀ █▄▀ ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█ ░   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
                █▀▄ █▄█ █▄▄ █░█ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄ █   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
                '''.center(10))
                print('-' * length, '\n')
                print('1. Play'.center(length))
                print('2. Instructions'.center(length))
                print('3. Exit'.center(length))
                choice = int(input('\nEnter an option: '))
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')
                continue  # FIX 2: Added 'continue' — without this, a bad input causes
                          # a crash because 'choice' is undefined when the if-block runs.

            if choice == 1:
                system("CLS")
                self._play()
            elif choice == 2:           # FIX 3: Added missing menu branches — choices
                print("\nRules:\n"      # 2 and 3 were never handled, making the menu
                      "  Rock beats Scissors\n"   # non-functional.
                      "  Scissors beats Paper\n"
                      "  Paper beats Rock\n")
                input("Press a key to continue...")
            elif choice == 3:
                exit()
            else:
                print('Please enter 1, 2, or 3.')


# FIX 4: The class was never instantiated or run — added an entry point.
if __name__ == "__main__":
    game = rock_paper_scissors()  # Object instantiated here
    game.main()