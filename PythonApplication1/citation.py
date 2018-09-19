class citation:

    def __init__(self,number,text):
        self.number=number
        self.text=text
        self.req=1

    def __str__(self):
        return "<Citation {} (text={}, req={})>".format(
                self.number, self.text[:10], self.req)


    #def trainMode(self,date,req,timereq):
    #    self.data={date:[req,timereq]}

    #def trainMode(self,req):
    #    self.req=req
