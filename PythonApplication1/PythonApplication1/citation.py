from random import randint
import pickle

class citation:

    def __init__(self,number,text):
        self.number=number
        self.text=text
        self.req=randint(0,10)

    def __repr__(self):
        return "Citation {} (text={}, req={})".format(
                self.number, self.text[:5], self.req)


    #def trainMode(self,date,req,timereq):
    #    self.data={date:[req,timereq]}

    #def trainMode(self,req):
    #    self.req=req

def Save_Data(Data):
    with open('Data','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(Data)
