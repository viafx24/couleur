from tkinter import Tk, DoubleVar, Label, Spinbox
from functools import partial

def update_label(spinbox, label, var):
    """
    Écrit 'min' ou 'max' dans label en fonction de la valeur
    du textvariable de spinbox
    """
    value = var.get()
    if value == spinbox.cget('from'):
        label.config(text='Min')
    elif value == spinbox.cget('to'):
        label.config(text='Max')

root = Tk()
value = DoubleVar(root)
label = Label(text=4)
spinbox = Spinbox(root, textvariable=value, from_=4, to=8, increment=0.5)
spinbox.config(command=partial(update_label, spinbox, label, value))

spinbox.grid(row=0, column=0)
label.grid(row=1, column=0)

root.mainloop()
