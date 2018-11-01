from random import randint
import pickle

class citation:
    # main class to structure the data

    def __init__(self,number,text,SRR,TRT,Emphasis):
        self.number=number
        self.text=text
        self.SRR=SRR
        self.TRT=TRT
        self.Emphasis=Emphasis

    def __repr__(self):
        return "Citation {} (text={}, SRR={}, TRT={}, Emphasis={})".format(
                self.number, self.text[:5], self.SRR, self.TRT, self.Emphasis)


    #def trainMode(self,date,req,timereq):
    #    self.data={date:[req,timereq]}

    #def trainMode(self,req):
    #    self.req=req


