
from tkinter import Frame,Tk,Label,Button, IntVar
from functools import partial

class VotingBox(Frame):
    def __init__(self, *args, question='', options=None, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        Label(self, text=question).grid(column=0, row=0,
                                        columnspan=len(options))
        self.int_vars = {}
        for num_col, option in enumerate(options):
            self.int_vars[option] = IntVar(self)
            Button(self, text=option,
                   command=partial(self._update_int_var,
                                   option)).grid(column=num_col,
                                                 row=1)
            label = Label(self, textvariable=self.int_vars[option])
            label.grid(column=num_col, row=2)
    def _update_int_var(self, option):
        int_var = self.int_vars[option]
        int_var.set(int_var.get() + 1)

root = Tk()
VotingBox(root,
          question='Que pensez-vous de tkinter ?',
          options=[':-)', ':-|', ':-(']).grid()
root.mainloop()
