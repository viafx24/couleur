from tkinter import *
from functools import partial

# Dessiner une mosaïque de 3 * 3 labels.
# Tous les labels sont blancs sauf celui au centre qui est rouge.
# Le label rouge à une taille de 1 sur 1 mais les labels sur ses 
# côtés ont une taille de 3 ce qui fait que le label rouge ne prend
# pas toute la place de sa cellule.
root = Tk()
Label(root, height=1, width=1, bg='white').grid(row=0, column=0)
Label(root, height=1, width=3, bg='white').grid(row=0, column=1)
Label(root, height=1, width=1, bg='white').grid(row=0, column=2)
Label(root, height=3, width=1, bg='white').grid(row=1, column=0)
label = Label(root, height=1, width=1, bg='red')
label.grid(row=1, column=1)
Label(root, height=3, width=1, bg='white').grid(row=1, column=2)
Label(root, height=1, width=1, bg='white').grid(row=2, column=0)
Label(root, height=1, width=3, bg='white').grid(row=2, column=1)
Label(root, height=1, width=1, bg='white').grid(row=2, column=2)

def update_sticky_option(label, coord, is_checked):
    '''
    Modifier le paramètre sticky d'un widget.
    '''
    sticky = label.grid_info()['sticky']
    if is_checked.get():
        sticky += coord
    else:
        sticky = sticky.replace(coord, '')
    label.grid_configure(sticky=sticky)

# Créer 4 Checkbox pour pousser les valeurs 'n', 's', 'e', et 'w'.
# au paramètre sticky du label.
for i, coord in enumerate('nsew', 3):
    is_checked = BooleanVar(root)

    Label(root, text=coord).grid(row=i, column=0)
    Checkbutton(root, variable=is_checked,
                command=partial(update_sticky_option,
                                label, coord,
                                is_checked)).grid(row=i, column=1)

root.mainloop()
