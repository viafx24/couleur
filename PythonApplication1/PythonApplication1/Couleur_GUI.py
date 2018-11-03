from tkinter import *
import pickle
from operator import attrgetter
from random import sample
import time
import tkinter.font as tkFont
import citation

def update_label():
    # update the number chose in the spinbox in the top centered label 
    global Num_Value
   
    Num_Value=int(value.get()) # get the value of the spinbox
    label.config(text=str(Num_Value)) #show itin the label

def Load_Data_And_Shuffle():

    # load the data and choose randomly indices (the number chose in the spinob) among the lowest score (SRR)

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Shuffle_Indices=list()
    iteration=0

    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()

# fonction to sort the data: the first (second) sort  the data in reverse order (time) and then function of score(SRR)

    Data_Sorted=sorted(Data,key=attrgetter("TRT"), reverse=True)
    Data_Sorted=sorted(Data_Sorted,key=attrgetter("SRR"))

    # print(Data_Sorted)
    Get_All_Indice=list()

    # sort the data to find the lowest scoer
    for n in range(0,Num_Value):
        Get_All_Indice.append(int(Data_Sorted[n].number))

    # shuffle the indices to make the choice random
    Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    
    # print(Shuffle_Indices)
    # print(Data[Shuffle_Indices[iteration]].number)
    
    Text.delete(1.0, END)# clear text if the user launchs a second batch of citations.
    Text.config(height=2)

    label.config(text=str(iteration+1)+"/"+str(Num_Value))

    labelnumber.grid_remove()
    labelnumber.grid()

    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number,font=helv72)

    labelSRR.config(text='')
    labelTRT.config(text='')
    #Text.insert(END, Data[Shuffle_Indices[iteration]].number)
    #Text.config(font=helv12)


    tic = time.time() # to know how much time it take to find the citation.

    buttonnext.config(state=DISABLED)#disabled the button once every things have been done 
    buttonStar.config(state=DISABLED)
    buttonDepreciated.config(state=DISABLED)
    buttonNormal.config(state=DISABLED)

def Next_Iteration():
#go to the next iteration (possible only after that the user click on +1 or -1)

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    iteration+=1
    
    #Text.grid_remove()
    Text.delete(1.0, END)
    Text.config(height=2)
    labelnumber.grid_remove()
    labelnumber.grid()
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number)
    labelnumber.config(font=helv72)


    tic = time.time()
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    
    labelSRR.config(text='')
    labelTRT.config(text='')

    buttonnext.config(state=DISABLED)#disabled the button once every things have been done 
    buttonStar.config(state=DISABLED)
    buttonDepreciated.config(state=DISABLED)
    buttonNormal.config(state=DISABLED)

def PlusOne():
# add +1 in the database on the SRR (the user has found the citation).

    global Shuffle_Indices, iteration, Data, Num_Value,tic,toc
    toc = time.time()
    
    Text.grid_remove()
    Text.grid()
    Text.config(height=text_height)
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    SetColorText()
           
    labelnumber.config(font=helv48)
    
    Data[Shuffle_Indices[iteration]].SRR+=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

    # disabled the button if iteration exeed the number ask in the spinbox

    buttonStar.config(state=NORMAL)
    buttonDepreciated.config(state=NORMAL)
    buttonNormal.config(state=NORMAL)

    if iteration == Num_Value-1:  
         buttonnext.config(state=DISABLED)
    else:
        buttonnext.config(state=NORMAL)


    AjoutHistorique()
    Save_Data(Data)

def MinusOne():
# add -1 in the database on the SRR (the user has found the citation).

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc
    toc = time.time()

    Text.grid_remove()
    Text.grid()

    Text.config(height=text_height)
    Text.delete(1.0, END)
    Text.insert(END, Data[Shuffle_Indices[iteration]].text)
    SetColorText()
    labelnumber.config(font=helv48)

    Data[Shuffle_Indices[iteration]].SRR-=1
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

    buttonStar.config(state=NORMAL)
    buttonDepreciated.config(state=NORMAL)
    buttonNormal.config(state=NORMAL)

    if iteration == Num_Value-1:  
         buttonnext.config(state=DISABLED)
    else:
        buttonnext.config(state=NORMAL)
    
    AjoutHistorique()
    Save_Data(Data)

def SetStar():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Star"
    SetColorText()
    Save_Data(Data)

def SetDepreciated():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Depreciated"
    SetColorText()
    Save_Data(Data)

def SetNormal():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Normal"
    SetColorText()
    Save_Data(Data)


def SetColorText():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    if Data[Shuffle_Indices[iteration]].Emphasis=="Normal":
        Text.config(foreground="white")
    if Data[Shuffle_Indices[iteration]].Emphasis=="Star":
        Text.config(foreground="blue")
    if Data[Shuffle_Indices[iteration]].Emphasis=="Depreciated":
        Text.config(foreground="red")

def AjoutHistorique():

    global Shuffle_Indices, iteration, Data 

    Date=date.today()
    SRR=Data[Shuffle_Indices[iteration]].SRR
    TRT=Data[Shuffle_Indices[iteration]].TRT

    Ajout = pd.DataFrame([[Date,SRR,TRT]],columns=Data[Shuffle_Indices[iteration]].Historique.columns)  
    Ajout["Date"]=pd.to_datetime(Ajout["Date"])
    Data[Shuffle_Indices[iteration]].Historique=Data[Shuffle_Indices[iteration]].Historique.append(Ajout)

def Save_Data(Data):
    #function to save the data
    with open('Data','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(Data)

# main script creating the GUI
root = Tk()
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.configure(bg='black')
root.state('zoomed') #full screen


def ShowHistorique():





screen_height = root.winfo_screenheight()

if screen_height==1050:
    text_height=16
else:
    text_height=9



#different policies used in the GUI
helv72= tkFont.Font(family='Comic Sans MS', size=84)
helv48= tkFont.Font(family='Comic Sans MS', size=48)
helv36 = tkFont.Font(family='Comic Sans MS', size=36)
helv24 = tkFont.Font(family='Comic Sans MS', size=24)
helv18 = tkFont.Font(family='Comic Sans MS', size=18)
helv12 = tkFont.Font(family='Comic Sans MS', size=12)

# label and spinbow of the GUI
label = Label(text=10,font=helv24,bg='black',fg='white')
value = DoubleVar(root)
value.set(10)
Num_Value=int(value.get()) # global variableneeded by the function
labelnumber = Label(font=helv24,bg='black',fg='white')
labelSRR = Label(font=helv24,bg='black',fg='white')
labelTRT = Label(font=helv24,bg='black',fg='white')
spinbox = Spinbox(root, textvariable=value, from_=10, to=300, increment=10, font=helv24,bg='black',fg='white')
spinbox.config(command=update_label)

# configuration of the buttons and the text box
button = Button(root, text='          Load          ',command=Load_Data_And_Shuffle,font=helv24,bg='black',fg='white')
buttonnext = Button(root, text='         Next         ',command=Next_Iteration,font=helv36,bg='black',fg='white')
buttonPlus1=Button(root,text='         +1         ',command=PlusOne,font=helv36,bg='black',fg='white')
buttonMinus1=Button(root,text='         -1         ',command=MinusOne,font=helv36,bg='black',fg='white')

buttonStar= Button(root, text='S', command=SetStar,font=helv12,bg='black',fg='white')
buttonDepreciated= Button(root, text='D', command=SetDepreciated,font=helv12,bg='black',fg='white')
buttonNormal= Button(root, text='N', command=SetNormal,font=helv12,bg='black',fg='white')

buttonHistorique= Button(root, text='H', command=ShowHistorique,font=helv12,bg='black',fg='white')

Text = Text(root, height=text_height, width=70, font=helv18, bg='black',fg='white',borderwidth=0,wrap=WORD)

# place of the widgets on th grid
spinbox.grid(row=0, column=0, columnspan=4,sticky=W)
label.grid(row=0, column=0, columnspan=4)
button.grid(row=0,column=0, columnspan=4,sticky=E,pady=10,padx=30)

labelnumber.grid(row=1,columnspan=4)
labelSRR.grid(row=1,column=0, columnspan=4,sticky=W, padx=30)
labelTRT.grid(row=1,column=0, columnspan=4,sticky=E, padx=30)

buttonStar.grid(row=3,column=0,columnspan=4,sticky='es',padx=400)
buttonNormal.grid(row=4,column=0,columnspan=4,sticky='e',padx=400)
buttonDepreciated.grid(row=5,column=0,columnspan=4,sticky='en',padx=400)

buttonHistorique.grid(row=3,rowspan=3, column=0, columnspan=4,sticky='w',padx=400)

Text.grid(row=2,column=0,columnspan=4)

buttonPlus1.grid(row=3,column=0,columnspan=4, rowspan=3, sticky=W, pady=30, padx=30)
buttonnext.grid(row=3,column=0,rowspan=3, columnspan=4)
buttonMinus1.grid(row=3,column=0,rowspan=3,columnspan=4,sticky=E, pady=30, padx=30)

root.mainloop()