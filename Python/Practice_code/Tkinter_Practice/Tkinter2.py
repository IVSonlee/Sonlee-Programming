#Link: https://realpython.com/python-gui-tkinter/

import tkinter as tkinter_practice2

window_tk = tkinter_practice2.Tk()
frame_tk = tkinter_practice2.Frame()

#Frame widgets are important for organizing the layout of your widgets in an application.
frame1 = tkinter_practice2.Frame() 
frame2 = tkinter_practice2.Frame()

"""An empty Frame widget is practically invisible. Frames are best thought of as containers for other widgets. You can assign a widget to a frame by 
setting the widgets master attribute:"""

label1 = tkinter_practice2.Label(master=frame1,text="This is Frame 1")
label1.pack()

""" If you omit the master argument when creating a new widget instance, then itll be placed inside of the top-level window by default"""

label2 = tkinter_practice2.Label(master=frame2,text="This is Frame 2")
label2.pack()

#frame.pack() packs the frame into the window so that the window sizes itself as small as possible to encompass the frame
frame2.pack()
frame1.pack()

"""Adjusting Frame Appearance With Reliefs
Frame widgets can be configured with a relief attribute that creates a border around the frame. You can set relief to be any of the following values:

tk.FLAT: Has no border effect (the default value)
tk.SUNKEN: Creates a sunken effect
tk.RAISED: Creates a raised effect
tk.GROOVE: Creates a grooved border effect
tk.RIDGE: Creates a ridged effect"""

border_types = {"border1" : tkinter_practice2.FLAT,"border2" : tkinter_practice2.SUNKEN, "border3" : tkinter_practice2.RAISED, "border4" : tkinter_practice2.GROOVE, 
                "border5" : tkinter_practice2.RIDGE}
""" create a dictionary whose keys are the names of the different relief effects available in Tkinter. The values are the corresponding Tkinter objects."""

for border_keys,border_values in border_types.items():
    #To apply the border effect, you must set the borderwidth attribute to a value greater than 1. This attribute adjusts the width of the border in pixels.
    frame3 = tkinter_practice2.Frame(master=window_tk,relief=border_values,borderwidth=5)
    #creates a new Frame widget and assigns it to the window.tk object. The relief attribute is set to the corresponding relief in the border_types

    frame3.pack(side=tkinter_practice2.LEFT)#The side keyword argument tells Tkinter in which direction to pack the frame objects.
    
    Label1 = tkinter_practice2.Label(master=frame3,text=border_keys)
     
    Label1.pack()


window_tk.mainloop()