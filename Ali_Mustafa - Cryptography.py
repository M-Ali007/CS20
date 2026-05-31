# Mustafa Ali
# Assignment 1 - Cryptography
# Block 5
# May 8th 2026

# This program is my own work - MA

# "Consider any possible problems or limitations pertaining to this program.
# What are they? Make the necessary modifications."

# 1. UPPERCASE LETTERS - The original letters list only had lowercase,
#    so any uppercase input would crash. Fixed by converting input to lowercase.
#
# 2. SPACES - The encode() function skipped spaces with 'pass' but still
#    tried to add a shifted letter after. Fixed by using 'continue' so
#    spaces are preserved in the output.
#
# 3. CIPHER SHIFT OF EXACTLY 26 - The condition was "newIndex > 26"
#    so a shift of exactly 26 would go out of range. Fixed with ">= 26".
#
# 4. SPECIAL CHARACTERS/NUMBERS - Any non-letter character (like "!" or "3")
#    would crash with a ValueError. Fixed by skipping non-letter characters.
#
# 5. DECODE FUNCTION PRINT - The decode function printed "ENCODED" instead
#    of "DECODED". Fixed the label.

# The alphabet stored as a list so we can find letter positions by index
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode():
    print("Welcome to the Encoder 6000!")
    print()

    # Get the string and convert to lowercase to handle uppercase input
    string = input("Please Enter your string: ").lower()

    # Get and validate the shift number
    cipherNum = input("Please enter how much you want your cipher to shift the letters: ")
    while not cipherNum.isdigit():
        cipherNum = input("Please enter a valid number: ")

    newString = ""

    for letter in string:
        # Preserve spaces as spaces
        if letter == " ":
            newString += " "
            continue  # Skip to next letter (was 'pass' before - this was a bug)

        # Skip any characters that aren't in the alphabet (e.g. "!", "3")
        if letter not in letters:
            continue

        # Find the letter's position and shift it
        ind = letters.index(letter)
        newIndex = ind + int(cipherNum)

        # Wrap around if the index goes past the end of the alphabet
        if newIndex >= 26:  # Was "> 26" before - this was a bug
            newIndex = newIndex - 26

        newString += letters[newIndex]

    print()
    print(f"Your ENCODED string is {newString}!")
    print()

    # Ask if the user wants to see the original string decoded
    choice = input("Do you want to decode your encoded string? (y/n) : ")
    while choice not in ["y", "n"]:
        choice = input("Please enter a valid answer - (y,n)  : ")

    if choice == "y":
        print(string)  # Show the original string
    elif choice == "n":
        pass


def decode():
    print("Welcome to the Decoder 6000!")
    print()

    # Get the encoded string and convert to lowercase to handle uppercase input
    string = input("Please Enter your string: ").lower()

    # Get and validate the shift number used during encoding
    cipherNum = input("Please enter how much you had previously encoded your string: ")
    while not cipherNum.isdigit():
        cipherNum = input("Please enter a valid number: ")

    newString = ""

    for letter in string:
        # Preserve spaces as spaces
        if letter == " ":
            newString += " "
            continue

        # Skip any characters that aren't in the alphabet
        if letter not in letters:
            continue

        # Find the letter's position and shift it backwards
        ind = letters.index(letter)
        newIndex = ind - int(cipherNum)

        # Wrap around if the index goes before the start of the alphabet
        if newIndex < 0:
            newIndex = newIndex + 26

        newString += letters[newIndex]

    print()
    print(f"Your DECODED string is {newString}!")  # Was "ENCODED" before - this was a bug


# --- Main Program ---

print("Welcome to the Python Cryptography 6000!")
print()

# Ask user whether they want to encode or decode
choice = input("Would you like to ENCODE or DECODE a string? (a, b)  : ")
while choice not in ["a", "b"]:
    choice = input("Please enter a valid answer - (a,b)  : ")

if choice == "a":
    encode()
elif choice == "b":
    decode()