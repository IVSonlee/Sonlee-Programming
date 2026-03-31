##Link: https://realpython.com/python-gui-tkinter/

import tkinter as tkinter_practice5

window_tk = tkinter_practice5.Tk()

"""The geometry manager youll likely use most often is .grid(), which provides all the power of .pack() in a format thats easier to understand and maintain.

.grid() works by splitting a window or Frame into rows and columns. You specify the location of a widget by calling .grid() and passing the row and column indices 
to the row and column keyword arguments, respectively. Both row and column indices start at 0"""

for rows in range(3):
    for columns in range(3):
        frame2 = tkinter_practice5.Frame(master=window_tk,borderwidth=1,relief="groove")
        frame2.grid(row = rows, column = columns,padx=10,pady=5)
        #padx adds padding in the horizontal direction.pady adds padding in the vertical direction.

        label2 = tkinter_practice5.Label(master=frame2,text=f"Row {rows}\nColumn {columns}")
        label2.pack(padx=5,pady=5)

window_tk.mainloop()