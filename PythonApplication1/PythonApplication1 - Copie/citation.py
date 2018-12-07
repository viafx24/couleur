import pickle

class citation:
    # main class to structure the data

    def __init__(self,number,text,SRR,TRT,Emphasis, Historique):

        self.number=number
        self.text=text
        self.SRR=SRR
        self.TRT=TRT
        self.Emphasis=Emphasis
        self.Historique=Historique

    def __repr__(self):
        return "Citation {} (text={}, SRR={}, TRT={}, Emphasis={}, Historique{})".format(
                self.number, self.text[:5], self.SRR, self.TRT, self.Emphasis, self.Historique)


