#Link: https://realpython.com/python-gui-tkinter/

import tkinter as tkinter_practice3

window_tk = tkinter_practice3.Tk()

frame1 = tkinter_practice3.Frame(master=window_tk, width=500, height=100, bg="#276FF5")
frame1.pack()

frame2 = tkinter_practice3.Frame(master=window_tk, width=400, height=100, bg="#5E8FEB")
frame2.pack()

frame3 = tkinter_practice3.Frame(master=window_tk, width=300, height=100, bg="#82A6E8")
frame3.pack()

""".pack() accepts some keyword arguments for more precisely configuring widget placement. For example, you can set the fill keyword 
argument to specify in which direction the frames should fill. The options are tk.X to fill in the horizontal direction, tk.Y to fill 
vertically, and tk.BOTH to fill in both directions. 

Notice that the width is not set on any of the Frame widgets. width is no longer necessary because each frame sets .pack() to fill horizontally, 
overriding any width you may set. """

frame4 = tkinter_practice3.Frame(master=window_tk, height=50, bg="#1EC7FF")
frame4.pack(fill=tkinter_practice3.X)

frame5 = tkinter_practice3.Frame(master=window_tk, height=50, bg="#71C1DC")
frame5.pack(fill=tkinter_practice3.X)

frame6 = tkinter_practice3.Frame(master=window_tk, height=50, bg="#A2D5E7")
frame6.pack(fill=tkinter_practice3.BOTH)

"""The side keyword argument of .pack() specifies on which side of the window the widget should be placed. These are the available options:

tk.TOP
tk.BOTTOM
tk.LEFT
tk.RIGHT
If you dont set side, then .pack() will automatically use tk.TOP and place new widgets at the top of the window, or at the topmost portion of 
the window that isnt already occupied by a widget.

This time, you have to specify the height keyword argument on at least one of the frames to force the window to have some height."""

frame7 = tkinter_practice3.Frame(master=window_tk,width=200,bg="#1EF3A8")
frame7.pack(fill=tkinter_practice3.Y,side=tkinter_practice3.LEFT)

frame8 = tkinter_practice3.Frame(master=window_tk,width=200,height=30,bg="#76F2C6")
frame8.pack(fill=tkinter_practice3.Y,side=tkinter_practice3.LEFT)

frame9 = tkinter_practice3.Frame(master=window_tk,width=200,bg="#B4EFDB")
frame9.pack(fill=tkinter_practice3.Y,side=tkinter_practice3.LEFT)



frame10 = tkinter_practice3.Frame(master=window_tk, width=200, height=50,bg="#6815EF")
frame10.pack(fill=tkinter_practice3.X,side=tkinter_practice3.TOP)

frame11 = tkinter_practice3.Frame(master=window_tk, height=50,bg="#9356F4")
frame11.pack(fill=tkinter_practice3.X,side=tkinter_practice3.TOP)

frame12 = tkinter_practice3.Frame(master=window_tk, height=50,bg="#B18DEC")
frame12.pack(fill=tkinter_practice3.X,side=tkinter_practice3.TOP)

"""To make the layout truly responsive, you can set an initial size for your frames using the width and height attributes. Then, set the fill keyword argument 
of .pack() to tk.BOTH and set the expand keyword argument to True:

The difference is that now you can resize the window however you want, and the frames will expand and fill the window responsively:"""

frame13 = tkinter_practice3.Frame(master=window_tk,width=300,height=70,bg="#A7EC27")
frame13.pack(fill=tkinter_practice3.BOTH,expand=True)

frame14 = tkinter_practice3.Frame(master=window_tk,width=300,height=50,bg="#98BB57")
frame14.pack(fill=tkinter_practice3.BOTH,expand=True)

frame15 = tkinter_practice3.Frame(master=window_tk,width=300,height=50,bg="#55633A")
frame15.pack(fill=tkinter_practice3.BOTH,expand=True)

window_tk.mainloop()

