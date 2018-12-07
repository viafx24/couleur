#  a lot of import. Maybe some are redondant but i don't know exactly which one i could remove

from tkinter import *
import pickle
from operator import attrgetter
from random import sample
import time
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg') # the place of this line may count
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
from datetime import date
import pandas as pd

import citation # my main class




# function usefull to update the number chose in the spinbox in the top centered label
def update_label():

    global Num_Value
    Num_Value=int(value.get()) # get the value of the spinbox
    label.config(text=str(Num_Value)) #show it in the label



# first function to upload the data and sort it for the learning process (present the less well known citation)
def Sort_Data():

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc, Failed_Citation

    # put everythings good for the beginning because sometimes things changes (name of the button...)
    buttonnext.config(text='         Next         ')
    buttonPlus1.config(state=NORMAL)
    buttonMinus1.config(state=NORMAL)

    # load the data and choose randomly indices (the number chose in the spinob) among the lowest score (SRR)
 
    Shuffle_Indices=list() #main list of the indices to work on
    Failed_Citation=list() # keep memory of the one i failed to remember
    iteration=0

    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()

    # fonction to sort the data: the first (second) sort  the data in reverse order (time) and then function of score(SRR)

    Data_Sorted=sorted(Data,key=attrgetter("TRT"), reverse=True)
    Data_Sorted=sorted(Data_Sorted,key=attrgetter("SRR"))

    Get_All_Indice=list()

    # sort the data to find the lowest score
    for n in range(0,Num_Value):
        Get_All_Indice.append(int(Data_Sorted[n].number))

    # shuffle the indices to make the choice random
    Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
    
    Text1.delete(1.0, END)# clear text if the user launchs a second batch of citations.
    Text1.config(height=2) #some problem with the size of the text sometimes
    label.config(text=str(iteration+1)+"/"+str(Num_Value))# show the iteration of the citation
    labelnumber.grid_remove()# the two following lines helps because of probleme with the GUI (latence)
    labelnumber.grid()
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number,font=helv84)# show the number of the citation (big size)
    labelSRR.config(text='')#remove the label of the SRR
    labelTRT.config(text='')#remove the label of the TRT

    #disabled different buttons once every things have been done
    buttonnext.config(state=DISABLED) 
    buttonStar.config(state=DISABLED)
    buttonDepreciated.config(state=DISABLED)
    buttonNormal.config(state=DISABLED)
    buttonHistorique.config(state=DISABLED)

    # to know how much time it take to find the citation.
    tic = time.time() 



# second function to load citation randomly (easier work when tired). Quite redondant with the first function
#but i didn't find a better way to group the code
def Secured_Rand_Data():

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc,Failed_Citation

    # put everythings good for the beginning because sometimes things changes (name of the button...)
    buttonnext.config(text='         Next         ')
    buttonPlus1.config(state=NORMAL)
    buttonMinus1.config(state=NORMAL)
    
    Shuffle_Indices=list()
    Failed_Citation=list()
    iteration=0

    with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()

    Get_All_Indice=list()

   
    for n in range(0,300):# contrary to the first load function, here its 300 and not NumValue
        Get_All_Indice.append(int(Data[n].number))

    # shuffle the indices to make the choice random
    Shuffle_Indices_All=sample(Get_All_Indice, len(Get_All_Indice))
    Shuffle_Indices=Shuffle_Indices_All[0:Num_Value]
    
    Secured_Random_Key()# important function to increase the security of the rand function

    Text1.delete(1.0, END)# clear text if the user launchs a second batch of citations.
    Text1.config(height=2)
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    labelnumber.grid_remove()
    labelnumber.grid()
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number,font=helv84)
    labelSRR.config(text='')
    labelTRT.config(text='')

 
    #disabled some buttons once every things have been done 
    buttonnext.config(state=DISABLED)
    buttonStar.config(state=DISABLED)
    buttonDepreciated.config(state=DISABLED)
    buttonNormal.config(state=DISABLED)
    buttonHistorique.config(state=DISABLED)
    
    tic = time.time() # to know how much time it take to find the citation.


# for paranoid personnality. the citations chosen are random. but the user can add a number of its choice to increase
# confidence in the random choice of the citation
def Secured_Random_Key():

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc, labelList, Text2 

    windows3 = Toplevel(root, bg='black')# create a third windows specific
    # create a text label inside this windows
    Text2 = Text(windows3, height=text_height, width=120, font=helv12, bg='black',fg='white',borderwidth=0,wrap=WORD)
    Text2.insert(END, Shuffle_Indices) #show the indices randomly chosen by th computer (rand function)
    Text2.grid(row=0, column=0, columnspan=4)

    #add a button for the user who want to keep an eye on the random process (add +1, +2, +3 etc.. to the  btach of citation)
    buttonSecured=Button(windows3,text='         +1         ',command=PlusOneSecured,font=helv24,bg='black',fg='white')
    buttonSecured.grid(row=1, column=0, columnspan=4)


# the function that add +1 each time the user click on the entire list of randomly chosen citations.
def PlusOneSecured():   

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc, labelList, Text2

    # add +1 to each number. there is probably a better way to do that (vectorised one).
    for n in range(0,len(Shuffle_Indices)):

        if Shuffle_Indices[n]<290:
            Shuffle_Indices[n]=Shuffle_Indices[n]+1

    # the end of this function is the habitual stuff used to clean every things before beginning (maybe some are useless)
    Text2.delete(1.0, END)
    Text2.insert(END, Shuffle_Indices)
    Text1.delete(1.0, END)# clear text if the user launchs a second batch of citations.
    Text1.config(height=2)
    label.config(text=str(iteration+1)+"/"+str(Num_Value))
    labelnumber.grid_remove()
    labelnumber.grid()
    labelnumber.config(text=Data[Shuffle_Indices[iteration]].number,font=helv84)
    labelSRR.config(text='')
    labelTRT.config(text='')

    #disabled some button once every things have been done 
    buttonnext.config(state=DISABLED)
    buttonStar.config(state=DISABLED)
    buttonDepreciated.config(state=DISABLED)
    buttonNormal.config(state=DISABLED)

    tic = time.time() # to know how much time it take to find the citation.



#function that allow to go to the next iteration (possible only after that the user click on +1 or -1)
def Next_Iteration():

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc, Failed_Citation
    
    if iteration != Num_Value-1:  #most of the case; but at the end, the process is different: there is a synthesis
        
        # cleaning and showing the number of the next citation
        iteration+=1
        Text1.delete(1.0, END)
        Text1.config(height=2)
        labelnumber.grid_remove()
        labelnumber.grid()
        labelnumber.config(text=Data[Shuffle_Indices[iteration]].number)
        labelnumber.config(font=helv84)

        label.config(text=str(iteration+1)+"/"+str(Num_Value))
        labelSRR.config(text='')
        labelTRT.config(text='')

        buttonnext.config(state=DISABLED)#disabled the button once every things have been done 
        buttonStar.config(state=DISABLED)
        buttonDepreciated.config(state=DISABLED)
        buttonNormal.config(state=DISABLED)
        buttonHistorique.config(state=DISABLED)

        tic = time.time()

    else : # if it'sthe last iteration, the next buttin change in synthesis button?.
        # some usual cleaning
        buttonnext.config(state=NORMAL)
        Text1.delete(1.0, END)
        Text1.config(height=text_height)
        labelnumber.grid_remove()
        labelnumber.grid()
        labelSRR.config(text='')
        labelTRT.config(text='')

        labelnumber.config(text='Synthèse:') # show "synthèse" word in place of a number
        labelnumber.config(font=helv24)

        # print the number of errors and the list of the failed citation
        text='Il y a '+ str(len(Failed_Citation))+ ' erreur(s) : ' + str(Failed_Citation)
        Text1.insert(END, text)
        Text1.config(font=helv18)

        # disabled some buttons since it's the end of the training session to prevent bugs and errors.
        buttonnext.config(state=DISABLED)
        buttonStar.config(state=DISABLED)
        buttonDepreciated.config(state=DISABLED)
        buttonNormal.config(state=DISABLED)
        buttonPlus1.config(state=DISABLED)
        buttonMinus1.config(state=DISABLED)
        buttonHistorique.config(state=DISABLED)


# add +1 in the database on the SRR (the user has found the citation).
def PlusOne():

    global Shuffle_Indices, iteration, Data, Num_Value,tic,toc
    
    toc = time.time() # stop the counter

    #some cleaning
    Text1.grid_remove()
    Text1.grid()
    Text1.config(height=text_height)
    Text1.delete(1.0, END)
    Text1.insert(END, Data[Shuffle_Indices[iteration]].text)#insert the text of the citation
    SetColorText()#call to a function to check the color
           
    labelnumber.config(font=helv48)
    Data[Shuffle_Indices[iteration]].SRR+=1 # add +1 at its score since the user found the citation
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)# calculate the time to find the citation
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))# show the SRR (score)
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))# show the TRT (time)

    #  reabled th functionning of some buttons
    buttonStar.config(state=NORMAL)
    buttonDepreciated.config(state=NORMAL)
    buttonNormal.config(state=NORMAL)
    buttonHistorique.config(state=NORMAL)

    # if its the last iteration, change the word next by synthesis
    if iteration == Num_Value-1:  
         buttonnext.config(state=NORMAL) # maybe useless
         buttonnext.config(text='     Synthesis     ')
    else:
        buttonnext.config(state=NORMAL)


    AjoutHistorique()# call to the function ajoutHistorique to write data in the "historique"
    Save_Data(Data) #save the data 


    
# add -1 in the database on the SRR (the user did not find the citation).
def MinusOne():

    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc, Failed_Citation

    # mainly similar to +1 with some exceptions
    toc = time.time()

    Text1.grid_remove()
    Text1.grid()
    Text1.config(height=text_height)
    Text1.delete(1.0, END)
    Text1.insert(END, Data[Shuffle_Indices[iteration]].text)
    SetColorText()
    labelnumber.config(font=helv48)

    Data[Shuffle_Indices[iteration]].SRR-=1 # the score decreases (-1) since the user didn't find the citation
    Data[Shuffle_Indices[iteration]].TRT=round(toc-tic,1)
    labelSRR.config(text=str(Data[Shuffle_Indices[iteration]].SRR))
    labelTRT.config(text=str(Data[Shuffle_Indices[iteration]].TRT))

    buttonStar.config(state=NORMAL)
    buttonDepreciated.config(state=NORMAL)
    buttonNormal.config(state=NORMAL)
    buttonHistorique.config(state=NORMAL)

    # add the current number of citation in the list of the citation that the user didnt find
    Failed_Citation.append(Data[Shuffle_Indices[iteration]].number)  

    if iteration == Num_Value-1:  
         buttonnext.config(state=NORMAL)
         buttonnext.config(text='     Synthesis     ')
    else:
        buttonnext.config(state=NORMAL)
    
    AjoutHistorique()
    Save_Data(Data)


# the three next function works together.
# this function allows the user to follow its score (SRR) or time (TRT) over time (date) to study its progress
def AjoutHistorique():

    global Shuffle_Indices, iteration, Data 

    Date=date.today()
    SRR=Data[Shuffle_Indices[iteration]].SRR
    TRT=Data[Shuffle_Indices[iteration]].TRT

    #Ajout = pd.DataFrame([[Date,SRR,TRT]],columns=Data[Shuffle_Indices[iteration]].Historique.columns) # more clean than the line just after
    Ajout = pd.DataFrame([[Date,SRR,TRT]],columns=['Date','SRR','TRT'])# creation of a table panda
    Ajout["Date"]=pd.to_datetime(Ajout["Date"])# adapting the format of the date in datetime format
    # the following line can generate bug because it modify the structure of the panda table: if some bug: verify it!
    Ajout.set_index(["Date"],inplace=True)#removing the first useless index column (maybe useful for the plot)
    # add the new line of historique (this day) to the whole historique
    Data[Shuffle_Indices[iteration]].Historique=Data[Shuffle_Indices[iteration]].Historique.append(Ajout)
    
# function to plot SRR, TRT over time
def ShowHistorique():

    global Shuffle_Indices, iteration, Data, comboExample, fig

    # This defines the Python GUI backend to use for matplotlib
    #matplotlib.use('TkAgg')# this is a comment of another person

    root.state('zoomed') # i don't know if it's usefull
    windows2 = Toplevel(root) # creating a second windows tkinter
    fig = plt.figure(1,figsize=(7,5))#creating a matplotlib figure

    plt.clf()# clean/remove previous plot to avoid "hold on effect"

    # Special type of "canvas" to allow for matplotlib graphing (code found on internet to mix matplotlib and tkinter)
    canvas = FigureCanvasTkAgg(fig, master=windows2)
    plot_widget = canvas.get_tk_widget()

    toolbarFrame = tk.Frame(master=windows2)
    toolbarFrame.grid(row=0,column=0,sticky=tk.W)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()

    # Add the plot to the tkinter widget
    plot_widget.grid(row=1, column=0,columnspan=2)

    # a different way to plot using plot as a method (python is not matlab!)
    Data[Shuffle_Indices[iteration]].Historique["SRR"].plot(marker='x')
    fig.canvas.draw()

    # combo means widget where you choose among different choice. I just follow the example found on internet
    comboExample = ttk.Combobox(windows2, 
                                values=[
                                        "SRR vs. Time", 
                                        "TRT vs. Time",
                                        "SRR vs. TRT"])                               
    comboExample.grid(column=1, row=0, sticky=tk.E) # note the tk.E because i imported different kind of library tkinter. maybe note very beautifull
    comboExample.current(0)
    comboExample.bind("<<ComboboxSelected>>", ComboFunctionPlot)

# the function that is called by the previous line
def ComboFunctionPlot(event):

    global comboExample, fig
    plt.clf()

    if comboExample.get()=="SRR vs. Time":
        Data[Shuffle_Indices[iteration]].Historique["SRR"].plot(marker='x')
        fig.canvas.draw()

    elif comboExample.get()=="TRT vs. Time":
        Data[Shuffle_Indices[iteration]].Historique["TRT"].plot(marker='x')
        fig.canvas.draw()

    elif comboExample.get()=="SRR vs. TRT":
        # a different way to plot here (matlab style)
        plt.plot(Data[Shuffle_Indices[iteration]].Historique["SRR"],Data[Shuffle_Indices[iteration]].Historique["TRT"],marker='x')
        fig.canvas.draw()

# allow the user to put emphasis on some citation that become blue
def SetStar():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Star"
    SetColorText()
    Save_Data(Data)

# allow the user to depreciate some citations that become red
def SetDepreciated():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Depreciated"
    SetColorText()
    Save_Data(Data)

# allow the user to come back to the normal state (white)
def SetNormal():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    Data[Shuffle_Indices[iteration]].Emphasis="Normal"
    SetColorText()
    Save_Data(Data)

# modification of the color of the citation function of its state
def SetColorText():
    global Shuffle_Indices, iteration, Data, Num_Value, tic, toc

    if Data[Shuffle_Indices[iteration]].Emphasis=="Normal":
        Text1.config(foreground="white")
    if Data[Shuffle_Indices[iteration]].Emphasis=="Star":
        Text1.config(foreground="blue")
    if Data[Shuffle_Indices[iteration]].Emphasis=="Depreciated":
        Text1.config(foreground="red")

def Save_Data(Data):
    #function to save the data
    with open('Data','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(Data)



# main script creating the GUI
root = Tk()# create the main windows tkinter
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.configure(bg='black')
root.state('zoomed') #full screen

# the five following allow adaptation of the GUI function of the screen used (labtop of bedroom computer)
screen_height = root.winfo_screenheight()

if screen_height==1050:
    text_height=16
else:
    text_height=9

#different policies used in the GUI/ initially, helv mean helvetica but i finally chose comic sans ms
helv84= tkFont.Font(family='Comic Sans MS', size=84)
helv48= tkFont.Font(family='Comic Sans MS', size=48)
helv36 = tkFont.Font(family='Comic Sans MS', size=36)
helv24 = tkFont.Font(family='Comic Sans MS', size=24)
helv18 = tkFont.Font(family='Comic Sans MS', size=18)
helv12 = tkFont.Font(family='Comic Sans MS', size=12)
helv8 = tkFont.Font(family='Comic Sans MS', size=8)

# label and spinbox of the GUI
label = Label(text=10,font=helv24,bg='black',fg='white')# number of iteration chosen (top middle)
value = DoubleVar(root) #usefull to pass the variable to the first function to actualize the label function of the spinbox
value.set(10)
Num_Value=int(value.get()) # global variable needed by the function
labelnumber = Label(font=helv24,bg='black',fg='white') # the number of the citation (centered)
labelSRR = Label(font=helv24,bg='black',fg='white')# to show the SRR of the citation (on the left)
labelTRT = Label(font=helv24,bg='black',fg='white')# to show the SRR of the citation (on the right)
spinbox = Spinbox(root, textvariable=value, from_=10, to=300, increment=10, font=helv24,bg='black',fg='white')
spinbox.config(command=update_label)# the call of the first function 

# configuration of the buttons and the text box
buttonSort = Button(root, text='    Sort    ',command=Sort_Data,font=helv24,bg='black',fg='white')
buttonRand = Button(root, text='    Rand    ',command=Secured_Rand_Data,font=helv24,bg='black',fg='white')
buttonnext = Button(root, text='         Next         ',command=Next_Iteration,font=helv36,bg='black',fg='white')
buttonPlus1=Button(root,text='         +1         ',command=PlusOne,font=helv36,bg='black',fg='white')
buttonMinus1=Button(root,text='         -1         ',command=MinusOne,font=helv36,bg='black',fg='white')

buttonStar= Button(root, text='S', command=SetStar,font=helv12,bg='black',fg='white')
buttonDepreciated= Button(root, text='D', command=SetDepreciated,font=helv12,bg='black',fg='white')
buttonNormal= Button(root, text='N', command=SetNormal,font=helv12,bg='black',fg='white')

buttonHistorique= Button(root, text='H', command=ShowHistorique,font=helv12,bg='black',fg='white')

Text1 = Text(root, height=text_height, width=70, font=helv18, bg='black',fg='white',borderwidth=0,wrap=WORD)

# place of the widgets on th grid
spinbox.grid(row=0, column=0, columnspan=4,sticky=W)
label.grid(row=0, column=0, columnspan=4)
buttonSort.grid(row=0,column=0, columnspan=4,sticky=E,pady=10,padx=250)
buttonRand.grid(row=0,column=0, columnspan=4,sticky=E,pady=10,padx=30)

labelnumber.grid(row=1,columnspan=4)
labelSRR.grid(row=1,column=0, columnspan=4,sticky=W, padx=30)
labelTRT.grid(row=1,column=0, columnspan=4,sticky=E, padx=30)

buttonStar.grid(row=3,column=0,columnspan=4,sticky='es',padx=400)
buttonNormal.grid(row=4,column=0,columnspan=4,sticky='e',padx=400)
buttonDepreciated.grid(row=5,column=0,columnspan=4,sticky='en',padx=400)

buttonHistorique.grid(row=3,rowspan=3, column=0, columnspan=4,sticky='w',padx=400)

Text1.grid(row=2,column=0,columnspan=4)

buttonPlus1.grid(row=3,column=0,columnspan=4, rowspan=3, sticky=W, pady=30, padx=30)
buttonnext.grid(row=3,column=0,rowspan=3, columnspan=4)
buttonMinus1.grid(row=3,column=0,rowspan=3,columnspan=4,sticky=E, pady=30, padx=30)

root.mainloop() # needed to show the GUI.