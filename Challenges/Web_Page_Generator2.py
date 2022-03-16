from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser

class ParentWindow(Frame):
          
    def __init__ (self, master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 500))
        self.master.title('Create HTML page')
        self.master.config(bg='lightgray')

        # create/overwrite file function
        def create_html():
            with open('new.html', 'w') as file:
                file.write(self.Text.get('1.0', 'end'))
            print("html file created successfully!")

        # open file function
        def open_file():
            webbrowser.open_new_tab('new.html')
            print("html file opened successfully!")

        # close window function
        def ask_quit():
            if messagebox.askokcancel("Exit program", "Okay to exit application?"):
                self.master.destroy()

        # GUI Elements   
        self.Text = Text(self.master, font=("Helvetica", 16), fg='black', bg='white', height=15, width=48)
        self.Text.grid(row=0, column=0, padx=(30,0), pady=(30, 0))
        self.Text.insert(1.0, "<html>\n\t<body>\n\t\t<h1>\n\t\t\tInsert Headline\n\t\t</h1>\n\t</body>\n</html>")

        self.btnCreate = Button(self.master, text="Create", width=8, height=2, command=lambda:create_html())
        self.btnCreate.grid(row=1, column=0, padx=(30,0), pady=(30, 0), sticky=NW)

        self.btnOpen = Button(self.master, text="Open", width=8, height=2, command=lambda:open_file())
        self.btnOpen.grid(row=1, column=0, padx=(30,0), pady=(30, 0), sticky=NE)
        
        self.btnClose = Button(self.master, text="Close", width=8, height=2, command=lambda:ask_quit())
        self.btnClose.grid(row=2, column=0, padx=(30,0), pady=(30, 0), sticky=NE)

        

        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
