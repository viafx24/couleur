
from datetime import date
import pandas as pd

import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')

#fig = plt.figure()
#ax = plt.axes()


Date=date(2018,12,3)
Date2=date(2018,12,8)
#Date3=date(2018,12,5)
print(Date)
print(Date2)

Historique1=[[Date,5,78.3],[Date2,6,45.6]]
#Historique1=[[Date,5,78.3],[Date2,6,45.6],[Date3,8,12]]
print(Historique1)

PremierTableauPanda=pd.DataFrame(Historique1, columns=['Date','SRR','TRT'])

#print(PremierTableauPanda["SRR"].values)


PremierTableauPanda["Date"]=pd.to_datetime(PremierTableauPanda["Date"])

#df.set_index('Date', inplace=True)

PremierTableauPanda.set_index(["Date"],inplace=True)
PremierTableauPanda["SRR"].plot()
plt.show()
#print(PremierTableauPanda.dtypes)

#Ajout = pd.DataFrame([[Date,7,98.3]],columns=PremierTableauPanda.columns)  
#Ajout["Date"]=pd.to_datetime(Ajout["Date"])

#PremierTableauPanda=PremierTableauPanda.append(Ajout)

#print(PremierTableauPanda)

##plt.plot(PremierTableauPanda["Date"],PremierTableauPanda["SRR"],marker="x")
#plt.plot(PremierTableauPanda.index,PremierTableauPanda["SRR"])
#plt.xticks(rotation='vertical')
##plt.xticks(rotation=45)
#plt.show()
