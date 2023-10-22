import tkinter as tk
import sys
import os


def main():
    root2 = tk.Tk()
    root2.geometry('200x200')
    root2.title('Hülye vagy')
    szam = txtfield.get()
    if szam == '':
        lbl2 = tk.Label(root2, text=f"Erre a számra gondoltál: Semmi")
    else:
        lbl2 = tk.Label(root2, text=f"Erre a számra gondoltál: {szam}")
    lbl2.pack()
    root2.mainloop()



root = tk.Tk()
root.geometry('300x200')
root.title('Szám kitalálós')

lbl1 = tk.Label(root, text='Gondolj egy számra 1 és 15 között:')
lbl1.pack()
txtfield = tk.Entry()
txtfield.pack()
btn1 = tk.Button(root, text='Kattints ide', command=main)
btn1.pack()


root.mainloop()