from tkinter import*
from tkinter import Tk, StringVar, ttk
import random
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Ghub Stock Control System")


topFrame = Frame(root, width = 1350, height = 100,bd =20, relief='raise')
topFrame.pack(side=TOP)



bottomFrame = Frame(root, width = 1350, height = 200,bd =20, relief='raise')
bottomFrame.pack(side=BOTTOM)

root.mainloop()
