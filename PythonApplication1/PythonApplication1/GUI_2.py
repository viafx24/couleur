from tkinter import Tk, BooleanVar, Label, Checkbutton
from functools import partial

def update_label(label, var):
    """
    Met à jour le texte d'un label en utilisant un BooleanVar.
    """
    text = var.get()
    label.config(text=str(text))

root = Tk()
is_checked = BooleanVar(root, '1')
label = Label(root, text=str(is_checked.get()))
checkbox = Checkbutton(root, variable=is_checked, 
                       command=partial(update_label, label,
                                       is_checked))

label.grid(row=0, column=0)
checkbox.grid(row=1, column=0)
root.mainloop()



