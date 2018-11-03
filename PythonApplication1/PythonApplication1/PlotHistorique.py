import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import matplotlib
from datetime import date
import pandas as pd

def callbackFunc(event):
    plt.clf()
    #print(comboExample.get())

    if comboExample.get()=="SRR vs. Time":
        plt.plot(PremierTableauPanda["Date"],PremierTableauPanda["SRR"])
        fig.canvas.draw()

    elif comboExample.get()=="TRT vs. Time":
        plt.plot(PremierTableauPanda["Date"],PremierTableauPanda["TRT"])
        fig.canvas.draw()

    elif comboExample.get()=="SRR vs. TRT":
        plt.plot(PremierTableauPanda["SRR"],PremierTableauPanda["TRT"])
        fig.canvas.draw()


#app = tk.Tk() 
#app.geometry('200x100')

#labelTop = tk.Label(app,
#                    text = "Choose your favourite month")
#labelTop.grid(column=0, row=0)



# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')

# Initialize an instance of Tk
root = tk.Tk()

# Initialize matplotlib figure for graphing purposes
fig = plt.figure(1,figsize=(8,6))


# Special type of "canvas" to allow for matplotlib graphing

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

toolbarFrame = tk.Frame(master=root)
toolbarFrame.grid(row=1,column=0,sticky=tk.W)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
toolbar.update()

# Add the plot to the tkinter widget
plot_widget.grid(row=0, column=0,columnspan=2)

# Example data (note: default calculations for angles are in radians)

Date=date.today()
Date2=date(2018,12,9)
Date3=date(2019,1,10)

Historique1=[[Date,5,78.3],[Date2,6,45.6],[Date3,10,25.8]]

PremierTableauPanda=pd.DataFrame(Historique1, columns=['Date','SRR','TRT'])
PremierTableauPanda["Date"]=pd.to_datetime(PremierTableauPanda["Date"])

plt.plot(PremierTableauPanda["Date"],PremierTableauPanda["SRR"])

comboExample = ttk.Combobox(root, 
                            values=[
                                    "SRR vs. Time", 
                                    "TRT vs. Time",
                                    "SRR vs. TRT"])                               
comboExample.grid(column=1, row=1, sticky=tk.E)
comboExample.current(0)
comboExample.bind("<<ComboboxSelected>>", callbackFunc)

root.mainloop()
