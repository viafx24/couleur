from tkinter import *
import pickle
from operator import attrgetter
from random import sample
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

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    iteration=0

    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()


    Data_Sorted=sorted(Data,key=attrgetter("SRR"))
    Get_All_Indice=list()

    for n in range(0,Num_Value):
        Get_All_Indice.append(int(Data_Sorted[n].number))

    Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number,font=helv48)
    tic = time.time()
    

def Next_Iteration():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    iteration+=1
    Text.delete(1.0, END)
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number)
    tic = time.time()
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    
    labelSRR.config(text='')
    labelTRT.config(text='')

    buttonnext.config(state=DISABLED)



def PlusOne():
    global Shuffle_Indices, iteration, Data, Num_Value,tic,toc
    toc = time.time()
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    

    Data[Shuffle_Indices[iteration]].SRR+=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

    if iteration == Num_Value-1:  
         buttonnext.config(state=DISABLED)
    else:
        buttonnext.config(state=NORMAL)
    Save_Data(Data)

def MinusOne():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    toc = time.time()
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)


    Data[Shuffle_Indices[iteration]].SRR-=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

    buttonnext.config(state=NORMAL)

    if iteration == Num_Value-1:  
         buttonnext.config(state=DISABLED)
    else:
        buttonnext.config(state=NORMAL)

    Save_Data(Data)


def Save_Data(Data):
    with open('Data','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(Data)


root = Tk()

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.configure(bg='black')
#root.configure(fg='white')

root.state('zoomed')
#helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
#helv36 = tkFont.Font(family='Arial', size=36, weight='bold')
#helv36 = tkFont.Font(family='Arial', size=36)
#helv36 = tkFont.Font(family='Calibri', size=36)
helv48= tkFont.Font(family='Comic Sans MS', size=48)
helv36 = tkFont.Font(family='Comic Sans MS', size=36)
helv24 = tkFont.Font(family='Comic Sans MS', size=24)
helv18 = tkFont.Font(family='Comic Sans MS', size=18)

#root.attributes("-fullscreen", True)

Shuffle_Indices=list()



label = Label(text=10,font=helv24,bg='black',fg='white')
value = DoubleVar(root)
value.set(10)
Num_Value=int(value.get())
labelnumber = Label(font=helv24,bg='black',fg='white')
labelSRR = Label(font=helv24,bg='black',fg='white')
labelTRT = Label(font=helv24,bg='black',fg='white')
#label = Label(font=helv36)

spinbox = Spinbox(root, textvariable=value, from_=10, to=300, increment=10, font=helv24,bg='black',fg='white')
#spinbox.config(command=partial(update_label, spinbox, label, value, iteration))
spinbox.config(command=update_label)


button = Button(root, text='          Load          ',command=Load_Data_And_Shuffle,font=helv24,bg='black',fg='white')
buttonnext = Button(root, text='         Next         ',command=Next_Iteration,font=helv36,bg='black',fg='white')
buttonPlus1=Button(root,text='         +1         ',command=PlusOne,font=helv36,bg='black',fg='white')
buttonMinus1=Button(root,text='         -1         ',command=MinusOne,font=helv36,bg='black',fg='white')

Text = Text(root, height=9, width=70, font=helv18, bg='black',fg='white',borderwidth=0,wrap=WORD)


spinbox.grid(row=0, column=0, columnspan=4,sticky=W)
label.grid(row=0, column=0, columnspan=4)
button.grid(row=0,column=0, columnspan=4,sticky=E,pady=10,padx=30)

labelnumber.grid(row=1,columnspan=4)

Text.grid(row=2,column=0,columnspan=4)

labelSRR.grid(row=1,column=0, columnspan=4,sticky=W, padx=30)
labelTRT.grid(row=1,column=0, columnspan=4,sticky=E, padx=30)
buttonPlus1.grid(row=4,column=0,columnspan=4,sticky=W, pady=30, padx=30)
buttonnext.grid(row=4,column=0,columnspan=4)

buttonMinus1.grid(row=4,column=0,columnspan=4,sticky=E, pady=30, padx=30)
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
