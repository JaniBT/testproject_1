import tkinter as tk
import math


root = tk.Tk()
root.geometry('300x300')
root.title('Számológép')

def main():
    pass



btn7es = tk.Button(root, text="7", command=main)
btn7es.grid(row=0, column=0, padx=5, pady=10)
btn8as = tk.Button(root, text="8", command=main)
btn8as.grid(row=0, column=1, padx=5)
btn9es = tk.Button(root, text="9", command=main)
btn9es.grid(row=0, column=2, padx=5)





root.mainloop()