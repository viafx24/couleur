from tkinter import *
from functools import partial
import pickle
from operator import attrgetter
from random import shuffle, sample
from citation import Save_Data
import time

import tkinter.font as tkFont

def update_label():
    global Num_Value
    """
    Écrit 'min' ou 'max' dans label en fonction de la valeur
    du textvariable de spinbox
    """
    #value = var.get()
    #if value == spinbox.cget('from'):
    #    label.config(text='Min')
    #elif value == spinbox.cget('to'):
    #    label.config(text='Max')

    #value = var.get()
    
    Num_Value=int(value.get())
    label.config(text=str(Num_Value))

def Load_Data_And_Shuffle():

    global Shuffle_Indices, iteration, Data, Num_Value


    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()


    Data_Sorted=sorted(Data,key=attrgetter("SRR"))
    Get_All_Indice=list()

    for n in range(0,Num_Value):
        Get_All_Indice.append(int(Data_Sorted[n].number))

    Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    
    #labelnumber.config(text=Data[Shuffle_Indices[iteration]].number)
    label.config(text=str(iteration)+"/"+str(Num_Value))

def Next_Iteration():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    
    Text.delete(1.0, END)
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number)
    tic = time.time()
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    iteration+=1
    
def PlusOne():
    global Shuffle_Indices, iteration, Data, Num_Value,tic,toc
    toc = time.time()
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    Data[Shuffle_Indices[iteration]].SRR+=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

def MinusOne():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    toc = time.time()
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    Data[Shuffle_Indices[iteration]].SRR-=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))


root = Tk()
root.state('zoomed')
helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
#root.attributes("-fullscreen", True)

Shuffle_Indices=list()
iteration=0


label = Label(text=10,font=helv36)
value = DoubleVar(root)
value.set(10)
Num_Value=int(value.get())
labelnumber = Label(text='',font=helv36)
labelSRR = Label(text='',font=helv36)
labelTRT = Label(text='',font=helv36)
#label = Label(font=helv36)

spinbox = Spinbox(root, textvariable=value, from_=10, to=300, increment=10, font=helv36)
#spinbox.config(command=partial(update_label, spinbox, label, value, iteration))
spinbox.config(command=update_label)


button = Button(root, text='Load',command=Load_Data_And_Shuffle,font=helv36)
buttonnext = Button(root, text='Next',command=Next_Iteration,font=helv36)
buttonPlus1=Button(root,text='+1',command=PlusOne,font=helv36)
buttonMinus1=Button(root,text='-1',command=MinusOne,font=helv36)

Text = Text(root, height=10, width=100)


spinbox.grid(row=0, column=0)
label.grid(row=0, column=1)
button.grid(row=0,column=3)

labelnumber.grid(row=1,column=0)

Text.grid(row=3,column=0,columnspan=4)

labelSRR.grid(row=4,column=0)
labelTRT.grid(row=4,column=1)
buttonPlus1.grid(row=5,column=0)
buttonnext.grid(row=5,column=1)

buttonMinus1.grid(row=5,column=2)
root.mainloop()



        #print(Get_All_Indice)

    #Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    #print(Shuffle_Indices)
    #Text.delete(1.0, END)
    #Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    #iteration+=1

    #for n in Shuffle_Indices:
    #    print(n)
    #    Answer=input("tape o/n/*:")
    #    if Answer=="o":

    #        Data[n].SRR+=1
    #        print("Bien joué! Nouveau Req pour {}: {}".format(n,Data[n].SRR))
    #        Save_Data(Data)
    #        print("data saved")
    #    elif Answer=="n":

    #        Data[n].SRR-=1
    #        print("Raté! Nouveau Req pour {}: {}".format(n,Data[n].SRR))
    #        Save_Data(Data)
    #        print("data saved")
    #    else:
    #        print("sortie de l'exercice")
    #        break
