##Link: https://realpython.com/python-gui-tkinter/

from asyncio import events
import tkinter as tk_practice6

window_tk = tk_practice6.Tk()

window_tk.rowconfigure([0,1],minsize=100)#[0,1] serve as index for row 0 and row 1, minsize is the minimum size of the row
window_tk.columnconfigure([0,1],minsize=100)#[0,1] serve as index for column 0 and column 1, minsize is the minimum size of the column

lbl1 = tk_practice6.Label(text="Sample1",background="green")
lbl1.grid(row = 0,column = 0, sticky="n")

lbl2 = tk_practice6.Label(text="Sample2")
lbl2.grid(row = 1, column = 0,sticky="s")

lbl3 = tk_practice6.Label(text="Sample3")
lbl3.grid(row = 2,column = 0, sticky="w")

lbl4 = tk_practice6.Label(text="Sample4")
lbl4.grid(row = 4, column = 0,sticky="e")

lbl5 = tk_practice6.Label(text="Sample5")
lbl5.grid(row = 4, column = 0,sticky="ne")

lbl6 = tk_practice6.Label(text="Sample6")
lbl6.grid(row = 4, column = 0,sticky="sw")

"""You can change the location of each label inside of the grid cell using the sticky parameter, which accepts a string containing one or more of the following letters:

"n" or "N" to align to the top-center part of the cell
"e" or "E" to align to the right-center side of the cell
"s" or "S" to align to the bottom-center part of the cell
"w" or "W" to align to the left-center side of the cell
The letters "n", "s", "e", and "w" come from the cardinal directions north, south, east, and west. Setting sticky to "n" on both labels in the previous code positions each label at the top-center of its grid cell:

You can combine multiple letters in a single string to position each label in the corner of its grid cell:

To fill the entire cell, set sticky to "nsew"""

def event_handler(event):
    print(event.char)

window_tk.bind("<Key>", event_handler)
"""To call an event handler whenever an event occurs on a widget, use .bind(). The event handler is said to be bound to the event because its called every time the event occurs."""

window_tk.mainloop()