# Mustafa Ali
# Functions and Strings
# Block 5
# March 10

# This program is my own work - MA

# main function calls each function and passes in required arguements
def explore_string():
    string = get_input()
    explore_chars(string)
    sum_digits(string)

# Prompt the user for a sentence. Error check the string to ensure it has a length of 10 or more and ends with a period then return the string
def get_input():
    print("Enter 10 or more chars ending with a period:")
    inp = input("-> ")
    while len(inp) < 10 or inp[-1] != '.':
        inp = input("-> Error! Try again: ")
    return inp

# Print out the original string, then determine and output the string length, second char,
# second last char, Switch the first three chars with the last three
# chars and then Display the resulting string
def explore_chars(inp):
    print(f"Original:  {inp}")
    print(f"Length:    {len(inp)} chars")
    print(f"2nd char:  {inp[1]}")
    print(f"2nd last:  {inp[-2]}")
    remove = inp[3: -3]
    switch = inp[-3:] + remove + inp[:3]
    print(f"Switched:  {switch}")

# Sum together all of the digits in the string and print it
def sum_digits(inp):
    sumd = 0
    for char in inp:
        if char.isdigit():
            sumd += int(char)
    print(f"Digit sum: {sumd}")

explore_string() # main function call
