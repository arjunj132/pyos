# importing whole module
from tkinter import *
from tkinter.ttk import *
import datetime

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

result = ""
setting = ""
def timeConvert(time):
    miliTime = time
    hours, minutes = miliTime.split(":")
    hours, minutes = int(hours), int(minutes)
    global setting
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    global result
    result = ("%02d:%02d") % (hours, minutes)

# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M')
    string = timeConvert(string)
    lbl.config(text = result + strftime(':%S') + " " + setting)
    lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
			background = 'purple',
			foreground = 'white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()
