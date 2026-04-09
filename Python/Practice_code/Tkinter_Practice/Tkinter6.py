import tkinter as tk_practice6

window_tk = tk_practice6.Tk()

window_tk.rowconfigure([0,1],minsize=200)#[0,1] serve as index for row 0 and row 1, minsize is the minimum size of the row
window_tk.columnconfigure([0,1],minsize=200)#[0,1] serve as index for column 0 and column 1, minsize is the minimum size of the column

lbl1 = tk_practice6.Label(text="Sample1")
lbl1.grid(row = 0,column = 0, sticky="n")

lbl2 = tk_practice6.Label(text="Sample2")
lbl2.grid(row = 1, column = 0,sticky="s")

lbl1 = tk_practice6.Label(text="Sample3")
lbl1.grid(row = 2,column = 0, sticky="n")

lbl2 = tk_practice6.Label(text="Sample4")
lbl2.grid(row = 4, column = 0,sticky="s")

window_tk.mainloop()