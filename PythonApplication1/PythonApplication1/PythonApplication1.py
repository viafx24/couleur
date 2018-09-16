
import pickle

with open('Data','rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    Data=mon_depickler.load()

print(Data[101].text)
print(Data[102].text)
print(Data[106].text)
print(Data[107].text)