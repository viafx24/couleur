import csv
import pickle
from citation import citation

Data=list()
i=0
with open('Seneque_4.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')

    for line in csv_reader:
        Data.append(citation(line[0],line[1]))
        # print(Data[i].text)
        i+=1


        
Data[129].SRR=-1
Data[119].SRR=-1
Data[135].SRR=-1
Data[197].SRR=-1
Data[96].SRR=-1

# print(Data[240].text)
# print(Data[240].number)      
with open('Data','wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(Data)


print(Data)