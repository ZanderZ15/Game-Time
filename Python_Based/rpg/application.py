from tkinter import *
from tkinter import ttk
import mod1

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Change Message").grid(column=1, row=0)
ttk.Button(frame, text="Call Message").grid(column=1, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
instance = mod1.Message()
instance.Call_Sign()
instance.Change_Message()
instance.Call_Sign()
root.mainloop()

