from tkinter import *
root=Tk(className="my first GUI")
root.geometry("500x500")

label1=Label(root,text="UserName").place(x=30,y=30)
entry1=Entry(root).place(x=90,y=70)
btn1=Button(root,text="submit").place(x=100,y=100)
root.mainloop()