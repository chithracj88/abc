from tkinter import *
top=Tk(className="Relief")
top.geometry("500x500")



B1=Button(top,text="submit1",relief=FLAT).pack()
B2=Button(top,text="submit2",relief=RAISED).pack()
B3=Button(top,text="submit3",relief=SUNKEN).pack()
B4=Button(top,text="submit4",relief=GROOVE).pack()
B5=Button(top,text="submit5",relief=RIDGE).pack()




top.mainloop()