from tkinter import *
from functools import partial
import pickle
from operator import attrgetter
from random import shuffle, sample
from citation import Save_Data

import tkinter.font as tkFont

def update_label(spinbox, label, var, increment):
    """
    Écrit 'min' ou 'max' dans label en fonction de la valeur
    du textvariable de spinbox
    """
    #value = var.get()
    #if value == spinbox.cget('from'):
    #    label.config(text='Min')
    #elif value == spinbox.cget('to'):
    #    label.config(text='Max')

    value = var.get()
    label.config(text=str(value))

def Load_Data_And_Shuffle(value):

    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()

    #print(Data)
    #print(sorted(Data,key=lambda Data: Data.req))
    #print(sorted(Data,key=attrgetter("req")))
    Data_Sorted=sorted(Data,key=attrgetter("req"))

    pool_train=value

    Get_All_Indice=list()
    for n in range(0,pool_train):
        Get_All_Indice.append(int(Data_Sorted[n].number))

    print(Get_All_Indice)

    Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    print(Shuffle_Indices)
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    iteration+=1

    #for n in Shuffle_Indices:
    #    print(n)
    #    Answer=input("tape o/n/*:")
    #    if Answer=="o":

    #        Data[n].req+=1
    #        print("Bien joué! Nouveau Req pour {}: {}".format(n,Data[n].req))
    #        Save_Data(Data)
    #        print("data saved")
    #    elif Answer=="n":

    #        Data[n].req-=1
    #        print("Raté! Nouveau Req pour {}: {}".format(n,Data[n].req))
    #        Save_Data(Data)
    #        print("data saved")
    #    else:
    #        print("sortie de l'exercice")
    #        break

root = Tk()
root.state('zoomed')
helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
#root.attributes("-fullscreen", True)

iteration=0
value = DoubleVar(root)

label = Label(text=10,font=helv36)
#label = Label(font=helv36)

spinbox = Spinbox(root, textvariable=value, from_=10, to=300, increment=10, font=helv36)
spinbox.config(command=partial(update_label, spinbox, label, value, iteration))


button = Button(root, text='Training',command=partial(training, int(value.get()),iteration),font=helv36)
buttonnext = Button(root, text='next',command=partial(training, int(value.get()),),font=helv36)

Text = Text(root, height=2, width=30)


spinbox.grid(row=0, column=0)
label.grid(row=0, column=1)
button.grid(row=0,column=2)
Text.grid(row=3,column=0)

root.mainloop()


