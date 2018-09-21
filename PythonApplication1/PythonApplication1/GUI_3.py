from tkinter import Tk, StringVar, Label, Radiobutton
from functools import partial

def update_label(label, var):
    """
    Met à jour le texte de label en fonction de var.
    """
    text = var.get()
    label.config(text='color :' + text)


root = Tk()
choice = ['red', 'green', 'blue']
color = StringVar(root, 'red')
label_color = Label(root, text='color :' + color.get())

for i, value in enumerate(choice, 1):
    label = Label(root, text=value)
    radiobutton = Radiobutton(root, variable=color, value=value,
                              command=partial(update_label, 
                                              label_color, 
                                              color))

    label.grid(row=i, column=0)
    radiobutton.grid(row=i, column=1)


label_color.grid(row=0, column=0)
root.mainloop()
