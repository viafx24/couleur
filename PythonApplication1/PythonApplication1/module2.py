
from datetime import date
import pandas as pd

import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')

#fig = plt.figure()
#ax = plt.axes()


Date=date.today()
Date2=date(2018,12,9)
print(Date)
print(Date2)

Historique1=[[Date,5,78.3],[Date2,6,45.6]]
print(Historique1)

PremierTableauPanda=pd.DataFrame(Historique1, columns=['Date','SRR','TRT'])

#print(PremierTableauPanda["SRR"].values)


PremierTableauPanda["Date"]=pd.to_datetime(PremierTableauPanda["Date"])

#print(PremierTableauPanda.dtypes)

Ajout = pd.DataFrame([[Date,7,98.3]],columns=PremierTableauPanda.columns)  
Ajout["Date"]=pd.to_datetime(Ajout["Date"])

PremierTableauPanda=PremierTableauPanda.append(Ajout)

print(PremierTableauPanda)

plt.plot(PremierTableauPanda["Date"],PremierTableauPanda["SRR"])
plt.show()
