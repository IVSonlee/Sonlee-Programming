##Link: https://realpython.com/python-gui-tkinter/
import tkinter as tkinter_practice5

window_tk = tkinter_practice5.Tk()

"""The geometry manager youll likely use most often is .grid(), which provides all the power of .pack() in a format thats easier to understand and maintain.

.grid() works by splitting a window or Frame into rows and columns. You specify the location of a widget by calling .grid() and passing the row and column indices 
to the row and column keyword arguments, respectively. Both row and column indices start at 0"""

for rows in range(3):
    window_tk.rowconfigure(rows,weight=1,minsize=120)
    window_tk.columnconfigure(rows,weight=1,minsize=100)
    for columns in range(3):
        frame2 = tkinter_practice5.Frame(master=window_tk,borderwidth=1,relief="groove")
        frame2.grid(row = rows, column = columns,padx=10,pady=5)
        #padx adds padding in the horizontal direction.pady adds padding in the vertical direction.

        label2 = tkinter_practice5.Label(master=frame2,text=f"Row {rows}\nColumn {columns}")
        label2.pack(padx=5,pady=5)#.pack() also has padx and pady parameters.

"""By using .columnconfigure() and .rowconfigure() on the window object, you can adjust how the rows and columns of the grid grow as the window is resized. Remember, the grid is attached to window, even though youre calling .grid() on each Frame widget. Both .columnconfigure() and .rowconfigure() take three essential arguments:

Index: The index of the grid column or row that you want to configure or a list of indices to configure multiple rows or columns at the same time
Weight: A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows
Minimum Size: A keyword argument called minsize that sets the minimum size of the row height or column width in pixels

weight is set to 0 by default, which means that the column or row doesnt expand as the window resizes. If every column or row is given a weight of 1, then they all grow at the same rate. If one column has a weight of 1 and another a weight of 2, then the second column expands at twice the rate of the first."""


window_tk.mainloop()