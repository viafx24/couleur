import tkinter as tk
from tkinter import *
root = Tk()

Text1 = Text(root, height=70, width=70, font=12, bg='black',fg='white',borderwidth=0,wrap=WORD)
Text1.grid(row=2,column=0,columnspan=4)

windows3 = Toplevel(root)
Text2=Text(windows3)

root.mainloop()