from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class ParentWindow(Frame):
          
    def __init__ (self, master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(480, 250))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')
        

        def select_file1():
            self.master.filePath = filedialog.askopenfilename(title="Select a File")
            self.fileText1.insert(tk.END, self.master.filePath)

        def select_file2():
            self.master.filePath = filedialog.askopenfilename(title="Select a File")
            self.fileText2.insert(tk.END, self.master.filePath)

        def ask_quit():
            if messagebox.askokcancel("Exit program", "Okay to exit application?"):
                self.master.destroy()

        self.btnBrowse1 = Button(self.master, text="Browse...", width=8, height=1, command=lambda:select_file1())
        self.btnBrowse1.grid(row=1, column=1, padx=(30,0), pady=(70, 0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=8, height=1, command=lambda:select_file2())
        self.btnBrowse2.grid(row=2, column=1, padx=(30,0), pady=(10, 0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", width=8, height=2)
        self.btnCheck.grid(row=3, column=1, padx=(30,0), pady=(10, 0), sticky=NE)

        self.btnClose = Button(self.master, text="Close", width=8, height=2, command=lambda:ask_quit())
        self.btnClose.grid(row=3, column=4, padx=(30,0), pady=(10, 0), sticky=NE)

        self.fileText1 = Text(self.master, font=("Helvetica", 16), fg='black', bg='white', height=1, width=30)
        self.fileText1.grid(row=1, column=2, columnspan=3, padx=(30,0), pady=(70, 0))

        self.fileText2 = Text(self.master, font=("Helvetica", 16), fg='black', bg='white', height=1, width=30)
        self.fileText2.grid(row=2, column=2, columnspan=3, padx=(30,0), pady=(10, 0))

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
