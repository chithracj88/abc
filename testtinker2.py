from tkinter import *
root=Tk(className="my first GUI")
root.geometry("500x500")
Num1=IntVar()
Num2=IntVar()
sum=IntVar()
def submit():
    num1_var=Num1.get()
    num2_var=Num2.get()
    sum_var=num1_var+num2_var
    sum.set(sum_var)
    label3=Label(root,text="sum").place(x=40,y=160)
    entry3=Entry(root,textvariable=sum).place(x=30,y=150)
    

label1=Label(root,text="number1").place(x=30,y=30)
entry1=Entry(root,textvariable=Num1).place(x=30,y=50)
label2=Label(root,text="number2").place(x=30,y=70)
entry2=Entry(root,textvariable=Num2).place(x=30,y=100)
btn1=Button(root,text="submit",command=submit).place(x=120,y=120)

root.mainloop()