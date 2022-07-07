from tkinter import *
root=Tk(className="my first GUI")
root.geometry("500x500")

label1=Label(root,text="LABEL")
label1.pack()

def hide():
    label1.pack_forget()
        
def show():
    label1.pack()
        



btn1=Button(root,text="click to hide",command=hide).pack()


btn2=Button(root,text="click to recover",command=show).pack()

root.mainloop()