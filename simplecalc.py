# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 05:28:48 2022

@author: ASUS
"""


import tkinter as tk
import calcfunctions as f


# ============================== Action Function ==============================
def printout(pressed):
    """
    This function defines the action if the button is pressed
    """    
    if pressed == '(-)':
        # if (-) button is pressed, the number displayed will be negated by
        # calling function f.negation
        text = display.get('1.0', tk.END).strip()
        number = str(f.negation(text))
        display.delete('1.0', tk.END)
    elif pressed == 'Del':
        # if Del is pressed, it deletes last character on display
        text = display.get('1.0', tk.END).strip()
        number = text[:-1]
        display.delete('1.0', tk.END)
    elif pressed == 'C':
        # if C is pressed, it clears all characters displayed
        number = ''
        display.delete('1.0', tk.END)
    elif pressed == '=':
        # if = is pressed, it calls function f.equalto to execute the calculation
        text = display.get('1.0', tk.END).strip()
        number = f.equalto(text)
        display.delete('1.0', tk.END)
    else:
        # if other than above are pressed (such as numbers), the pressed button
        # is printed on display
        number = pressed
    display.insert(tk.END, number)
    
    return


# ================================ Main Window ================================
window = tk.Tk() # inisiating the tkinter root window
window.title('Calculator') # naming the window
window.resizable(width=False, height=False) # set window to unresizable

# ====================== Main Frames (Output and Input) =======================
frame_out = tk.Frame(master=window) # create and attach frame to root window
frame_in = tk.Frame(master=window) # create and attach frame to root window
frame_out.grid(row=0, column=0, padx=10, pady=10) # locate frame using grid
frame_in.grid(row=1, column=0, padx=10, pady=10) # locate frame using grid

# =========================== Input Frame & Widgets ===========================
# frame for Numbers Input
frame_num = tk.Frame(master=frame_in)
# generating buttons for numbers and attach them to the frame_num
n = 0
for i in range(3):
    for j in range(3):
        n += 1
        text = '%s'%n
        button = tk.Button(master=frame_num, text=text, width=4, height=2,
                   command=lambda m=text : printout(m))
        button.grid(row=i, column=j, padx=2, pady=2)

# generating buttons for negative, 0, and dot symbol
adnum = '(-) 0 .'.split()
for j in range(3):
    text = adnum[j]
    button = tk.Button(master=frame_num, text=text, width=4, height=2,
               command=lambda m=text : printout(m))
    button.grid(row=3, column=j, padx=2, pady=2)

# Frame for Operators
frame_op = tk.Frame(master=frame_in)
# generating buttons for calculation operators stored in f.OPERS
n = 0
for i in range(4):
    for j in range (2):
        text = f.OPERS[n]
        button = tk.Button(master=frame_op, text=text, width=4, height=2,
                   command=lambda m=text: printout(m))
        button.grid(row=i, column=j, padx=2, pady=2)
        n += 1

frame_num.grid(row=0, column=0) # locate frame using grid
frame_op.grid(row=0, column=1) # locate frame using grid
        

# =========================== Output Frame Widgets ============================
display = tk.Text(master=frame_out, width=26, height=4, bg='white', fg='black',
                     relief=tk.SUNKEN)
display.pack()

# ============================== Run Main Window ==============================
window.mainloop()
