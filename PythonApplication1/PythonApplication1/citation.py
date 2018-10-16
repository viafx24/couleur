from random import randint
import pickle

class citation:
    # main class to structure the data

    def __init__(self,number,text):
        self.number=number
        self.text=text
        self.SRR=0
        self.TRT=0

    def __repr__(self):
        return "Citation {} (text={}, SRR={}, TRT={})".format(
                self.number, self.text[:5], self.SRR, self.TRT)


    #def trainMode(self,date,req,timereq):
    #    self.data={date:[req,timereq]}

    #def trainMode(self,req):
    #    self.req=req


