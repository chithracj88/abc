from tkinter import *
top=Tk()
top.geometry("500x500")

checkvar1=StringVar()
checkvar2=StringVar()

C1=Checkbutton(top,text="music",variable=checkvar1,onvalue="musicrock",offvalue="")
C2=Checkbutton(top,text="video",variable=checkvar2,onvalue="videorock",offvalue="")

C1.pack()
C2.pack()

l1=Label(top,textvariable=checkvar1)
l1.pack()
l2=Label(top,textvariable=checkvar2)
l2.pack()
top.mainloop()