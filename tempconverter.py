# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:18:33 2022

@author: ASUS
"""


from tkinter import Tk, Frame, Entry, Label, StringVar, OptionMenu, Button
from tkinter import RIGHT, SUNKEN

conversion = {'unit': 'C F K R'.split(),
			  'scale': [1., 1.8, 1., 1.8],
			  'offset': [0., 32., 273.15, 491.67]}
        
def convert():
    """Convert Temperature"""
    unit_from = unit_in_menu.get()
    unit_to = unit_out_menu.get()
    
    ifrom = conversion['unit'].index(unit_from)
    ito = conversion['unit'].index(unit_to)
    
    a_from = conversion['scale'][ifrom]
    b_from = conversion['offset'][ifrom]
    
    a_to = conversion['scale'][ito]
    b_to = conversion['offset'][ito]
    
    T = float(entry_in.get())
    C = (T - b_from)/a_from
    T = a_to * C + b_to
    
    label_out['text'] = '%.2f' % (T)
    
    return

# Main Window
window = Tk()
window.title('Temperature Converter')
window.resizable(width=False, height=False)

# Input Frame and Units Menu
frame_in = Frame(master=window)
entry_in = Entry(master=frame_in, width=10, justify=RIGHT)
entry_in.bind(sequence='<Return>', func=lambda event: convert())

unit_in_menu = StringVar(master=window)
unit_in_menu.set(conversion['unit'][0])
unit_in = OptionMenu(frame_in, unit_in_menu, *list(conversion['unit']))
entry_in.grid(row=0, column=0)
unit_in.grid(row=0, column=1)

# Output Frame and Units Menu
frame_out = Frame(master=window)
label_out = Label(master=frame_out, width=10, bg='white', fg='black',
                     relief=SUNKEN, anchor='e')

unit_out_menu = StringVar(master=window)
unit_out_menu.set(conversion['unit'][0])
unit_out = OptionMenu(frame_out, unit_out_menu, *list(conversion['unit']))
label_out.grid(row=0, column=0)
unit_out.grid(row=0, column=1)

# Conversion Button
button = Button(master=window, text='\N{RIGHTWARDS BLACK ARROW}',
                   command=convert)

sections = [frame_in, button, frame_out]
for i,sec in enumerate(sections):
    sec.grid(row=0, column=i, padx=10, pady=10)
    
# Run Main Window
window.mainloop()
