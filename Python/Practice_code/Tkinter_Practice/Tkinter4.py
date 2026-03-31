#Link: https://realpython.com/python-gui-tkinter/

import tkinter as tkinter_practice4

window_tk = tkinter_practice4.Tk()

frame1 = tkinter_practice4.Frame(master=window_tk,height=100,width=300,borderwidth=4,relief="solid")
frame1.pack()

"""You can use .place() to control the precise location that a widget should occupy in a window or Frame. You must provide two keyword arguments, 
x and y, which specify the x- and y-coordinates for the top-left corner of the widget. Both x and y are measured in pixels, not text units.

Keep in mind that the origin, where x and y are both 0, is the top-left corner of the Frame or window."""

label1 = tkinter_practice4.Label(master=frame1,text="I am using place() instead of pack",bg="#ED9E8C")
label1.place(x=50,y=30)

Entry1 = tkinter_practice4.Entry(master=frame1,width=20)
Entry1.place(x=85,y=60)

window_tk.mainloop()