# import basic_ledger as bl
from tkinter import *
from gui_database import *
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
        filemenu = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        filemenu.add_command(label="Exit", command=self.client_exit)
        filemenu.add_command(label="Open a ledger")
        # added "file" to my menu
        menu.add_cascade(label="File", menu=filemenu)
        # create the edit object
        helpmenu = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        helpmenu.add_command(label="help info")
        helpmenu.add_command(label="About the app", command=self.app_info_window)
        # added "edit" to my menu
        menu.add_cascade(label="Help", menu=helpmenu)
        '''
        Adding a menu bar (ends)
        '''

    def client_exit(self):
        exit()

    # the window that shows up after clicking "About the app"
    def app_info_window(self):
        app_info_win = Toplevel()
        app_info_win.title("About the app")
        app_info_win.geometry("300x200")
        app_info_label = Label(app_info_win, text=app_info_txt())
        app_info_label.pack()

root = Tk()

# define size of the window
root.geometry("600x400")
# creating the main instance
app = Window(root)
# mainloop
root.mainloop()
