import tkinter as tkinter_practice2

window_tk = tkinter_practice2.Tk()
frame_tk = tkinter_practice2.Frame()

#Frame widgets are important for organizing the layout of your widgets in an application.
frame1 = tkinter_practice2.Frame()
frame2 = tkinter_practice2.Frame()

label1 = tkinter_practice2.Label(master=frame1,text="This is Frame 1")
label1.pack()

label2 = tkinter_practice2.Label(master=frame2,text="This is Frame 2")
label2.pack()

#frame.pack() packs the frame into the window so that the window sizes itself as small as possible to encompass the frame
frame2.pack()
frame1.pack()


window_tk.mainloop()