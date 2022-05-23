from tkinter import *

window = Tk()
window.geometry("400x180+20+10")

def findSmallest():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfSmallest.set(min(L))
    
lbl2 = Label(window,text = "Enter the first number:")
lbl2.place(x=10,y=10)
conOfent2 = StringVar()
ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.place(x=160,y=10)
lbl3 = Label(window,text = "Enter the second number:")
lbl3.place(x=10,y=40)
conOfent3=StringVar()
ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.place(x=160,y=40)
lbl4 = Label(window,text="Enter the third number:")
lbl4.place(x=10,y=70)
conOfent4 = StringVar()
ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.place(x=160,y=70)

btn1 = Button(window,text = "Find the smallest number",command=findSmallest)
btn1.place(x=230,y=100)
lbl5 = Label(window,text="The smallest number among the three is: ")
lbl5.place(x=10,y=130)
conOfSmallest = StringVar()
ent5 = Entry(window,bd=3,state="readonly",textvariable=conOfSmallest)
ent5.place(x=240,y=130)

mainloop()