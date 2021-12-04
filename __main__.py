# Import libraries
import os
from tkinter import * 
from tkinter.ttk import *

# Create colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Get app
def app():
    text = clicked.get().lower()
    open = Label(root, text ="Opening app " + text)
    open.pack()
    os.system("python3 " + text + ".py")
    

# Dropdown options
options = [
    "Select",
    "Paint",
    "Editor",
    "Pong",
    "Clock",
    "Timer",
    "Analog"
]

# Status message
print(color.CYAN + "OS loading..." + color.END)
# Install dependencies
os.system("pip3 install kivy > /dev/null 2>&1")
os.system("pip install kivy > /dev/null 2>&1")

# Create portal
root = Tk()
root.title("PyOS Portal")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
# Show content
label = Label(root, text ="Welcome to the PyOS portal!")
choose = Label(root, text ="Choose a program:")
button = Button( root , text = "Submit" , command = app)
label.pack()
choose.pack()
clicked = StringVar()
clicked.set("Select")
drop = OptionMenu( root , clicked , *options )
drop.pack()
button.pack()

# Keep portal
root.mainloop()