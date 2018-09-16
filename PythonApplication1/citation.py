class citation:

    def __init__(self,number,text):
        self.number=number
        self.text=text


    def trainMode(self,date,req,timereq):
        self.data={date:[req,timereq]}
