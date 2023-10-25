from tkinter import *
from tkinter import ttk
from playsound import playsound
import random
import sys
import os


root = Tk()
root.geometry = ("400x400")

def csatornaegy():
    playsound()


combo = ttk.Combobox(
    state="readonly",
    values=["Rádió 1", "Rádió 2", "Rádió 3"]
)
combo.place(x=180, y=200)
root.mainloop()