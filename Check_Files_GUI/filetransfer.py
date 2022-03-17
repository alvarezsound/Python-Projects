import os,time
import datetime
import shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime as dt




class ParentWindow(Frame):
          
    def __init__ (self, master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(480, 250))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

       
        def select_file1():
            self.master.filePath = filedialog.askdirectory(title="Select a File")
            self.fileText1.insert(tk.END, self.master.filePath)

        def select_file2():
            self.master.filePath = filedialog.askdirectory(title="Select a File")
            self.fileText2.insert(tk.END, self.master.filePath)

        def ask_quit():
            if messagebox.askokcancel("Exit program", "Okay to exit application?"):
                self.master.destroy()

      
        self.btnBrowse1 = Button(self.master, text="Browse...", width=8, height=1, command=lambda:select_file1())
        self.btnBrowse1.grid(row=1, column=1, padx=(30,0), pady=(70, 0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=8, height=1, command=lambda:select_file2())
        self.btnBrowse2.grid(row=2, column=1, padx=(30,0), pady=(10, 0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", width=8, height=2, command=lambda:file_transfer())
        self.btnCheck.grid(row=3, column=1, padx=(30,0), pady=(10, 0), sticky=NE)

        self.btnClose = Button(self.master, text="Close", width=8, height=2, command=lambda:ask_quit())
        self.btnClose.grid(row=3, column=4, padx=(30,0), pady=(10, 0), sticky=NE)

        self.fileText1 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
        self.fileText1.grid(row=1, column=2, columnspan=3, padx=(30,0), pady=(70, 0))

        self.fileText2 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
        self.fileText2.grid(row=2, column=2, columnspan=3, padx=(30,0), pady=(10, 0))


        def file_transfer():
            now = dt.datetime.now()
            ago = now-dt.timedelta(hours=24)
            strftime = "%H:%M %m/%d/%Y"
            src = self.fileText1.get()
            dst = self.fileText2.get()
            
            for root, dirs,files in os.walk(src):  
                for fname in files:
                    path = os.path.join(root, fname)
                    st = os.stat(path)    
                    mtime = dt.datetime.fromtimestamp(st.st_mtime)
                    if mtime > ago:
                        print("Moved:", fname, " modified within 24 hours at", mtime.strftime("%H:%M %m/%d/%Y"))
                        shutil.move(path, dst)

                        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
