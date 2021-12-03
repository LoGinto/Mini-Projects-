import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Password generator")
root.geometry("500x300")

info_string = ''
my_pass = chr(randint(33, 126))


def new_pass():
    pw_entry.delete(0, END)
    try:
        pw_length = int(my_entry.get())
    except ValueError:
        pw_length = 0
        global info_string
        info_string = "Enter the number! "
        tk.messagebox.showerror("Error", message = info_string)
    my_password = ''
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)


def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    global info_string
    info_string = "Copied to clipboard"
    tk.messagebox.showinfo(title="Success",message = info_string)

lf = LabelFrame(root, text="Number of characters: ")
lf.pack(pady=20)
my_entry = Entry(lf, font=("Script", 24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text=' ', font=("Roman", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)
my_button = Button(my_frame, text="Generate Password", command=new_pass)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to clipboard", command=copyToClipboard)
clip_button.grid(row=0, column=1, padx=10)



root.mainloop()
