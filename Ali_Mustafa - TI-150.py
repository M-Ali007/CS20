# Mustafa Ali
# Assignment 3 - TI-150
# Block 5
# March 27th 2026

# This program is my own work - MA

"""
Limitations -

“Consider any possible problems or limitations pertaining to this program.
What are they? Make the necessary modifications.”

My code can get issues when dividing by 0, and so to mitigate this issue, I have checked for the specific error
and I have used a try except statement to catch it and tell the user that the input is bad.
"""

#imports
import tkinter as tk
from tkinter import ttk

def add(value):
    my_text.insert(tk.END, value) #adds value to the textbox

def clear():
    my_text.delete("1.0", tk.END) # clears the values in the text box

def calculate():
    expression = my_text.get("1.0", tk.END) # gets the contents of the textbox
    try:
        result = eval(expression) #Python Function that takes a string and returns answer
    except SyntaxError:
        result = "ERROR - PROPER EXPRESSION ONLY PLEASE" # Error checking for bad input
    except ZeroDivisionError:
        result = "Undefined - You cannot divide by zero" # Error chekcing for zero divisions

    my_text.delete("1.0", tk.END)
    my_text.insert(tk.END, result)

# Button mappings to loop through to creating all the buttons 
buttons = {
    "7":  {"column": 1, "row": 3, "command": add},
    "8":  {"column": 2, "row": 3, "command": add},
    "9":  {"column": 3, "row": 3, "command": add},
    "4":  {"column": 1, "row": 4, "command": add},
    "5":  {"column": 2, "row": 4, "command": add},
    "6":  {"column": 3, "row": 4, "command": add},
    "1":  {"column": 1, "row": 5, "command": add},
    "2":  {"column": 2, "row": 5, "command": add},
    "3":  {"column": 3, "row": 5, "command": add},
    "0":  {"column": 2, "row": 6, "command": add},
    "+":  {"column": 4, "row": 3, "command": add},
    "-":  {"column": 4, "row": 4, "command": add},
    "*":  {"column": 4, "row": 5, "command": add},
    "/":  {"column": 4, "row": 6, "command": add},
}


root = tk.Tk() # creates tkinter instance
root.title("MustaCalc") # window name
frame = ttk.Frame(root, padding=10) # initializes tkinter frame
frame.grid() # initializes grid layout
my_text = tk.Text(frame, wrap='word', height=2, width=20) # main text box
my_text.grid(column=1, row=2, columnspan=4, sticky='ew') # creates grid layout

# for loop loops through the dictionary to create the buttons
for label, pos in buttons.items():
    tk.Button(frame, text=label, width=4, height=2, command=lambda v=label: add(v)).grid(
        column=pos["column"], row=pos["row"]
    )

# Clear, equals to and close buttons seperate because they have different functions
tk.Button(frame, text="C", width=4, height=2, command=clear).grid(column=1, row=6)
tk.Button(frame, text="=", width=4, height=2, command=calculate).grid(column=3, row=6)
tk.Button(frame, text="x", width=1, height=1,command=root.destroy).grid(column=4, row=1)
root.mainloop() # starts tkinter render loop

