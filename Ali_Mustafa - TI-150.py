# Mustafa Ali
# Assignment 3 - TI-150
# Block 5
# March 6th 2026

# This program is my own work - MA

import tkinter as tk
from tkinter import ttk

TBT = ""

def add(value):
    my_text.insert(tk.END, value)

def clear():
    my_text.delete("1.0", tk.END)

def calculate():
    expression = my_text.get("1.0", tk.END)
    try:
        result = eval(expression)
    except SyntaxError:
        result = "ERROR - PROPER EXPRESSION ONLY PLEASE"
    except ZeroDivisionError:
        result = "Undefined - You cannot divide by zero"

    my_text.delete("1.0", tk.END)
    my_text.insert(tk.END, result)

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


root = tk.Tk()
root.title("MustaCalc")
frame = ttk.Frame(root, padding=10)
frame.grid()
my_text = tk.Text(frame, wrap='word', height=2, width=20)
my_text.grid(column=1, row=2, columnspan=4, sticky='ew')
for label, pos in buttons.items():
    tk.Button(frame, text=label, width=4, height=2, command=lambda v=label: add(v)).grid(
        column=pos["column"], row=pos["row"]
    )
tk.Button(frame, text="C", width=4, height=2, command=clear).grid(column=1, row=6)
tk.Button(frame, text="=", width=4, height=2, command=calculate).grid(column=3, row=6)
tk.Button(frame, text="x", width=1, height=1,command=root.destroy).grid(column=4, row=1)
root.mainloop()

