#Link: https://realpython.com/python-gui-tkinter/

import tkinter as tk_practice #first thing you need to do is import the Python GUI Tkinter module

window_tk = tk_practice.Tk()#is an instance of Tkinter’s Tk class. Go ahead and create a new window and assign it to the variable

label1 = tk_practice.Label(
    text="Tkinter Practice:",
    foreground="#92C9EF",#Use foreground or fg to set the text color
    background="#5460C7",#Use background or bg to set the background color
    width= 15,#Use width to set the size horizontally
    height=5 #Use height set the size vertically
    ) #Label widgets are used to display text or images.
label1.pack() #To add a label1 you can use .pack() method

entry1 = tk_practice.Entry(
    bg="#CEE7F7",
    width=17,
)
"""When you need to get a little bit of text from a user, like a name or an email address, use an Entry widget. It’ll display a small 
text box that the user can type some text into

There are three main operations that you can perform with Entry widgets:

Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()"""
entry1.pack()

get_username = entry1.get()#You can use .get() to retrieve the text and assign it to a variable

entry2 = tk_practice.Entry(
    bg="#A6CEE8",
    width=17
)
entry2.pack()

delete_entry2 = entry2.delete(0,4)#You can delete text as well. This .delete() method takes an integer argument that tells Python which character to remove.
#If you need to remove several characters from an Entry, then pass a second integer argument to .delete() indicating the index of the character where deletion should stop. 
#Ex1: entry2.delete(1)

entry3 = tk_practice.Entry(
    bg="#8AC2E8",
    width=17
)
entry3.pack()

end_entry3 = entry3.delete(0,tk_practice.END)#tk.END for the second argument of .delete() to remove all text in Entry
"""Entry.delete() works just like string slicing. The first argument determines the starting index, and the deletion continues up to but not including 
the index passed as the second argument. Use the special constant tk.END for the second argument of .delete() to remove all text in Entry:"""

entry4 = tk_practice.Entry(
    bg="#8AC2E8",
    width=17
)
entry4.pack()

insert_entry4 = entry4.insert(0,"Insert")# .insert() will insert the new text at the specified position and shift all existing text to the right:

button1 = tk_practice.Button(
    text="Save",
    bg="#8090D9",
    fg="white", 
    width=10,
    height=1
)#Button widgets are used to display clickable buttons. You can configure them to call a function whenever they’re clicked. 
button1.pack()

textbox_tk = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk.pack()
textbox_tk.get("1.0","1.5")#1.0 as the starting index and 1.0 serve as the first line while 5 at 1.5 will serve as the number of characters this will get your input
#textbox_tk.get("1.0,tk.END")
"""Just like with Entry widgets, you can retrieve the text from a Text widget using .get(). However, calling .get() with no arguments doesnt 
return the full text in the text box like it does for Entry widgets.

Text.get() requires at least one argument. Calling .get() with a single index returns a single character. To retrieve several characters, 
you need to pass a start index and an end index."""

textbox_tk2 = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk2.pack()
textbox_tk2.delete("1.0",tk_practice.END)
""".delete() is used to delete characters from a text box. It works just like .delete() for Entry widgets."""

textbox_tk3 = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk3.pack()
textbox_tk3.delete("1.0")#If you delete that character, then the rest of the contents of the text box will shift up a line:

textbox_tk4 = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk4.pack()
textbox_tk4.insert("1.0","Insert Text")#This inserts at the beginning of the text box

textbox_tk5 = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk5.pack()
textbox_tk5.insert("2.0","\nThis will be inserted at the 2nd row because of new line")

textbox_tk6 = tk_practice.Text(
    height=5,
    width=25
)
textbox_tk6.pack()
textbox_tk6.insert(tk_practice.END,"This will be inserted at the end of the text widget")
"""Its usually impractical to try and keep track of what the index of the last character is. The best way to insert text at the end 
of a Text widget is to pass tk.END to the first parameter of .insert():"""

window_tk.mainloop()
""" tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code 
that comes after it from running until you close the window where you called the method"""