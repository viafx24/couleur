from functools import partial
from tkinter import *
from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial

def update_label(label, stringvar):
    """
    Met à jour le texte d'un label en utilisant une StringVar.
    """
    text = stringvar.get()
    label.config(text=text)
    stringvar.set('merci')

root = Tk()
text = StringVar(root)
label = Label(root, text='')
entry_name = Entry(root, textvariable=text)
button = Button(root, text='clic', 
                command=partial(update_label, label, text))

label.grid(column=0, row=0)
entry_name.grid(column=0, row=1)
button.grid(column=0, row=2)

root.mainloop()