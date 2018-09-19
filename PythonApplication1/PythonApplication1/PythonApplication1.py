
import pickle
from operator import attrgetter

with open('Data','rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    Data=mon_depickler.load()

#print(Data)
#print(sorted(Data,key=lambda Data: Data.req))
#print(sorted(Data,key=attrgetter("req")))
Data_Sorted=sorted(Data,key=attrgetter("req"))



Get_All_Indice=list()
for n in range(0,len(Data_Sorted)):
    Get_All_Indice.append(Data_Sorted[n].req)

print(Get_All_Indice)
print(min(Get_All_Indice))
A=[n for n in Get_All_Indice  if n==min(Get_All_Indice)]
#A=[n for n in Get_All_Indice  if n==0]
print(A)

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