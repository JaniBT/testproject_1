from tkinter import *
from tkinter import ttk
from playsound import playsound
import random
import sys
import os


def csatornaegy():
    global label2
    comb = combo.get()
    if comb == "Rádió 1":
        playsound("C:/Users/szf1/Desktop/testproject_1/zene/zenek/Bruno.mp3")
    elif comb == "Rádió 2":
        playsound()
    elif comb == "Rádió 3":
        playsound()
    else:
        label2 = Label(root, text="Nem adott meg Rádiót!", font="Arial 10")
        label2.place(x=50, y=50)


root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)
label = Label(root, text="Zene lejátszó", fg="black", font="Arial 25 bold")
label.place(x=80, y=50)


combo = ttk.Combobox(
    state="readonly",
    values=["Rádió 1", "Rádió 2", "Rádió 3"]
)
combo.place(x=100, y=150)

btn1 = Button(root, text="Indítás", command=csatornaegy)
btn1.place(x=125, y=200)
btn2 = Button(root, text="Kilépés", command=root.destroy)
btn2.place(x=125, y=260)
root.mainloop()