
import pickle
from operator import attrgetter
from random import shuffle
from random import sample
from citation import Save_Data

with open('Data','rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    Data=mon_depickler.load()

#print(Data)
#print(sorted(Data,key=lambda Data: Data.req))
#print(sorted(Data,key=attrgetter("req")))
Data_Sorted=sorted(Data,key=attrgetter("req"))

pool_train=10

Get_All_Indice=list()
for n in range(0,pool_train):
    Get_All_Indice.append(int(Data_Sorted[n].number))

print(Get_All_Indice)

Shuffle_Indices=sample(Get_All_Indice, len(Get_All_Indice))
print(Shuffle_Indices)

for n in Shuffle_Indices:
    print(n)
    Answer=input("tape o/n/*:")
    if Answer=="o":

        Data[n].req+=1
        print("Bien joué! Nouveau Req pour {}: {}".format(n,Data[n].req))
        Save_Data(Data)
        print("data saved")
    elif Answer=="n":

        Data[n].req-=1
        print("Raté! Nouveau Req pour {}: {}".format(n,Data[n].req))
        Save_Data(Data)
        print("data saved")
    else:
        print("sortie de l'exercice")
        break


#Suffle_Indices=shuffle(Get_All_Indice)
#print(Suffle_Indices)
#print(Get_All_Indice)


#print(min(Get_All_Indice))
#A=[n for n in Get_All_Indice  if n==min(Get_All_Indice)]
##A=[n for n in Get_All_Indice  if n==0]
#print(A)

#print(A)
#for n in range(1,len(Data_Sorted)):
#    if 
#    Data_Sorted_inf= Data_Sorted()



#Data_Sorted=[n for n in Data_Sorted if Data_Sorted[n]<2]
#print(Data[110].text)
#print(Data[111].text)

#for i in range(1,len(Data)):
#    Data[i].req=1
#    print(Data[i].req)

#Data[1].req=2
#testtrie=[nb for nb in Data if Data[nb].req==2]