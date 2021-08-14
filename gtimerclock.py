from tkinter import *
import time

root = Tk()
root.title('Gclock')
root.geometry('600x400')


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")
    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000, clock)

    my_label2.config(text=day)
    my_label3.config(text= "Your Time Zone:" + time_zone)


def update():
    my_label.config(text="New text")


my_label = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica", 16))
my_label2.pack(pady=20)

my_label3 = Label(root, text="", font=("Helvetica", 16))
my_label3.pack(pady=20)

clock()

# my_label.after(5000, update)




root.mainloop()