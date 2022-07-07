from tkinter import *
root=Tk()
root.geometry("500x600")
canvas1= Canvas(root,width=500, height=500,bd=3,relief=RIDGE)
canvas1.create_line(15,25,200,25,fill="red",dash=(8,2))
canvas1.create_rectangle(50,40,100,70,fill="red",outline='blue')
canvas1.create_line(55,85,155,85,105,180,55,85 )
canvas1.pack()
root.mainloop()
