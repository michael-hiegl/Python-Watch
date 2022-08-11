from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    timeString = strftime("%H:%M:%S %A")
    timeLabel.config(text=timeString)
    timeLabel.after(1000, time)

window = Tk()
window.title("Watch")

timeLabel = Label(window, font=("Arial", 150), background="black", foreground="yellow")
timeLabel.pack(anchor="center")
time()

window.mainloop()