from OrganizeGUI import VotingBox
root = Tk()
VotingBox(root,
          question='Que pensez-vous de tkinter ?',
          options=[':-)', ':-|', ':-(']).grid()
root.mainloop()
