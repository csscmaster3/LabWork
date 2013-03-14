import tkinter

from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.my_button=tkinter.Button(self.main_window, text='Click ME!', command=self.do_something)


    
my_gui = MyGUI()
