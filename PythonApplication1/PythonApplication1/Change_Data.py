#import csv
import pickle
from citation import citation


with open('Data_Old','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data_Old=mon_depickler.load()


# creation of the main list of citation
Data=list()
Emphasis="Normal"
for i in range(0,len(Data_Old)):
     Data.append(citation(Data_Old[i].number,Data_Old[i].text,Data_Old[i].SRR,Data_Old[i].TRT,Emphasis))

with open('Data','wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(Data)

#show the result
print(Data)


#for i in 
## import the data from the csv
#with open('Seneque_Pour_Couleur_2.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file,delimiter='\t')

#    for line in csv_reader:
#        Data.append(citation(line[0],line[1]))
#        # print(Data[i].text)
#        if i<101:
#            Data[i].SRR=2

#        if i<201 and i>100:
#            Data[i].SRR=1
       
#        if i<301 and i>200:
#            Data[i].SRR=0
       

#        i+=1

# chechinf for the place on the screen        
#Data[129].SRR=-1
#Data[119].SRR=-1
#Data[135].SRR=-1
#Data[197].SRR=-1
#Data[96].SRR=-1

# write on a file "Data"     
#with open('Data','wb') as fichier:
#    mon_pickler = pickle.Pickler(fichier)
#    mon_pickler.dump(Data)

##show the result
#print(Data)