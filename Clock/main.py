import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


label = Label(root, font = ("Helvetica"),background = "black",foreground = "cyan")
label.pack(anchor = 'center')
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

time()
mainloop()