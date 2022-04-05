from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("300x200+10+20")
window.title("Welcome to Python Programming")

# Button widgets
btn = Button(window,text = "This is button", fg = "Orange", bg = "blue", bd=15)
btn.place(x=50, y=50)

#label widget
lbl = Label(window,text = "Gender", fg = "blue", bg = "yellow")
lbl.place(x=50,y=10)

#text field
txt = Entry(window,font = ("verdana", 10),bd=5)
txt.place(x=50,y=130)

#radio button
radio1 = Radiobutton(window, text = "Male",value = 1)
radio2 = Radiobutton(window, text = "Female", value = 2)
radio1.place(x=50,y=25)
radio2.place(x=110,y=25)

#list box

var= StringVar()
var.set("Student1")

data = "Student1"
data1 = "Student2"
data2 = "Student3"
lstbx = Listbox(window,selectmode= 'single', height=5) #pwedeng wla height #mode= single,multiple,extended
lstbx.insert(END,data)
lstbx.insert(END,data1)
lstbx.insert(END,data2)
lstbx.place(x=50,y=200)

#combobox (top = from tkinter import ttk)
cb= ttk.Combobox(window, values = data)
cb.place(x=50,y=300)

window.mainloop()