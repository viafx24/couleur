
import pickle

with open('Data','rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    Data=mon_depickler.load()

print(Data[101].text)
print(Data[110].text)