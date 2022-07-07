from tkinter import *
root=Tk(className="my first GUI")
root.geometry("500x500")
name=StringVar()
password=StringVar()

def submit():
    name_var=name.get()
    pass_var=password.get()
    print("User name is %s and password is %s" %(name_var,pass_var))


label1=Label(root,text="UserName").place(x=30,y=30)
entry1=Entry(root,textvariable=name).place(x=30,y=50)
label2=Label(root,text="Password").place(x=30,y=70)
entry2=Entry(root,textvariable=password).place(x=30,y=100)
btn1=Button(root,text="submit",command=submit).place(x=120,y=120)
root.mainloop()
