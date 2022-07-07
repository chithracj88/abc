from tkinter import *
root=Tk(className="Message Widget")
root.geometry("500x500")

def myfun():
    print("Button entered")

foo = Button(root,text="Press Me",command=myfun)
foo.pack()

root.mainloop()

