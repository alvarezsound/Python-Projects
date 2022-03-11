#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.10.2
#
# Author:       Jeff A
#
# Purpose:      Student Tracking Assignment
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_tracker_gui
import student_tracker_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(700,500)
        self.master.maxsize(700,500)
        student_tracker_func.center_window(self,700,500)
        self.master.title("Student Tracking")
        self.master.configure(bg="#a88d32")

        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracker_func.ask_quit(self))
        arg = self.master

        student_tracker_gui.load_gui(self)
        
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: student_tracker_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) 
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Student Tracker") 
        menubar.add_cascade(label="Help", menu=helpmenu) 

        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
