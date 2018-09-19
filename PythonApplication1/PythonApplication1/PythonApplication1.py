
import pickle

with open('Data','rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    Data=mon_depickler.load()

print(Data[1:3])

Data[1].req=2
print(sorted(Data,key=lambda Data: Data.req))

#print(Data[110].text)
#print(Data[111].text)

#for i in range(1,len(Data)):
#    Data[i].req=1
#    print(Data[i].req)

#Data[1].req=2
#testtrie=[nb for nb in Data if Data[nb].req==2]