# import basic_ledger as bl
from tkinter import *
import math
import csv

# special thanks to https://pythonprogramming.net/python-3-tkinter-basics-tutorial/

# Here, I'm creating my class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization.
    def __init__(self, master=None):
        # parameters to send through the Frame class
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        self.init_window() # init the window

    #Creation of init_window
    def init_window(self):
        # changing the title of the master widget
        self.master.title("Ledger")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        '''
        Adding a menu bar (starts)
        '''
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # create the file object
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        # added "file" to my menu
        menu.add_cascade(label="File", menu=file)
        # create the edit object
        edit = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")
        # added "edit" to my menu
        menu.add_cascade(label="Edit", menu=edit)
        '''
        Adding a menu bar (ends)
        '''

    def client_exit(self):
        exit()

root = Tk()

# define size of the window
root.geometry("600x400")
# creating the main instance
app = Window(root)
# mainloop
root.mainloop()
