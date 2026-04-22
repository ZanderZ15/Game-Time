from tkinter import *
from tkinter import ttk
import message


root = Tk()
root.minsize(500, 500)
frame = ttk.Frame(root, padding=10)
frame.grid()
_message = message.Message()
#col, row
# =
# x, y
ttk.Label(frame, text="Hello World!").grid(column = 5, row = 0)

change_message_button = ttk.Button(
    frame, 
    text = "Change Message", 
    command = _message.Change_Message
    ).grid(column = 4, row = 1)

say_message_button = ttk.Button(
    frame, 
    text = "Say Message", 
    command = _message.Call_Sign
    ).grid(column = 6, row = 1)

quit_button = ttk.Button(
    frame, 
    text = "Quit", 
    command = root.destroy
    ).grid(column=5, row=2)

root.mainloop() #starts listening

