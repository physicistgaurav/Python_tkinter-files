
# #CALCULATOR

from  tkinter import *

root = Tk()
root.title("Simple G Calculator")

e= Entry(root, width=42, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# e.insert(0, "Perform")
def button_add():
    return

def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    return

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global  f_num
    global math
    math ="addition"
    f_num= int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "square_root":
        e.insert(0, f_num / int(second_number))
    if math == "dot":
        e.insert(0, f_num / int(second_number))

def button_sub():
    first_number = e.get()
    global  f_num
    global math
    math ="subtraction"
    f_num= int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global  f_num
    global math
    math ="division"
    f_num= int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global  f_num
    global math
    math ="multiplication"
    f_num= int(first_number)
    e.delete(0,END)

def button_percent():
    first_number = e.get()
    global  f_num
    global math
    math ="percentage"
    f_num= int(first_number)
    e.insert(0, f_num / 100)

def button_sq():
    first_number = e.get()
    global  f_num
    global math
    math ="square"
    f_num= int(first_number)
    e.delete(0,END)
    e.insert(0,f_num * f_num)

def button_sqr():
    first_number = e.get()
    global  f_num
    global math
    math ="sqaure_root"
    f_num= int(first_number)
    e.delete(0,END)
    e.insert(0,f_num+1)

def button_dot():
    first_number = e.get()
    global  f_num
    global math
    math ="dot"
    f_num= int(first_number)
    e.delete(0,END)

# Define button
button_1 = Button(root, text= "1", padx=50, pady=20,command=lambda: button_click(1))
button_2 = Button(root, text= "2", padx=50, pady=20,command=lambda: button_click(2))
button_3 = Button(root, text= "3", padx=50, pady=20,command=lambda: button_click(3))
button_4 = Button(root, text= "4", padx=50, pady=20,command=lambda: button_click(4))
button_5 = Button(root, text= "5", padx=50, pady=20,command=lambda: button_click(5))
button_6 = Button(root, text= "6", padx=50, pady=20,command=lambda: button_click(6))
button_7 = Button(root, text= "7", padx=50, pady=20,command=lambda: button_click(7))
button_8 = Button(root, text= "8", padx=50, pady=20,command=lambda: button_click(8))
button_9 = Button(root, text= "9", padx=50, pady=20,command=lambda: button_click(9))
button_0 = Button(root, text= "0", padx=50, pady=20,command=lambda: button_click(0))
button_add = Button(root, text= "+", padx=50, pady=20,command= button_add)
button_equal = Button(root, text= "=", padx=100, pady=20,command= button_equal)
button_sub = Button(root, text= "-", padx=50, pady=20,command=button_sub)
button_div = Button(root, text= "/", padx=50, pady=20,command=button_div)
button_mul = Button(root, text= "*", padx=50, pady=20,command=button_mul)
button_del = Button(root, text= "<", padx=50, pady=20,command=lambda: button_click())
button_sq = Button(root, text= "^", padx=50, pady=20,command= button_sq)
button_sqr = Button(root, text= "sqr", padx=50, pady=20,command= button_sqr)
button_dot = Button(root, text= ". ", padx=50, pady=20,command= button_dot)
button_percent = Button(root, text= "%", padx=50, pady=20,command= button_percent)
button_fsb = Button(root, text= "(", padx=50, pady=20,command=lambda: button_click)
button_bsb = Button(root, text= ")", padx=50, pady=20,command=lambda: button_click)
button_clear = Button(root, text="C", padx=50, pady=20, command=button_clear)


# Put buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_dot.grid(row=4, column=1)
button_percent.grid(row=4,column=2)

button_div.grid(row=1,column=3)
button_mul.grid(row=2,column=3)
button_add.grid(row=4,column=3)
button_sub.grid(row=3,column=3)

button_del.grid(row=1,column=5)
button_fsb.grid(row=2,column=5)
button_sq.grid(row=3,column=5)

button_clear.grid(row=1,column=6)
button_bsb.grid(row=2,column=6)
button_sqr.grid(row=3,column=6)

button_equal.grid(row=4, column=5, columnspan=5)
root.mainloop()
