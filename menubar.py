from tkinter import *
parent=Tk()
parent.geometry("500x500")
varlist=StringVar()
varlist.set("Menu")

om=OptionMenu(parent,varlist,"Yellow","Pink","Red","Brown","Black","Blue")
om.pack()
parent.mainloop()

