# Import libraries
import os
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

options = [
    "Select",
    "Paint",
    "Editor",
    "Clock",
    "Timer",
    "Analog"
]

games = [
    "Select",
    "Pong",
    "Colors",
    "Rock-Paper-Scissors",
    "Snake"
]



def portal():
    def app():
        text = clicked.get().lower()
        open = Label(root, text ="Opening app " + text)
        open.pack()
        os.system("python " + text + ".py  > /dev/null 2>&1")
        os.system("python3 " + text + ".py > /dev/null 2>&1")
    # Create portal
    root = Tk()
    root.title("PyOS Utilities")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    # Show content
    label = Label(root, text ="Welcome to the PyOS utilities portal!")
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

def game():
    def app():
        text = clicked.get().lower()
        open = Label(root, text ="Opening game " + text)
        open.pack()
        os.system("python " + text + ".py  > /dev/null 2>&1")
        os.system("python3 " + text + ".py > /dev/null 2>&1")
    # Create portal
    root = Tk()
    root.title("PyOS Games")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    # Show content
    label = Label(root, text ="Welcome to the PyOS games portal!")
    choose = Label(root, text ="Choose a game:")
    button = Button( root , text = "Submit" , command = app)
    label.pack()
    choose.pack()
    clicked = StringVar()
    clicked.set("Select")
    drop = OptionMenu( root , clicked , *games )
    drop.pack()
    button.pack()
    # Keep portal
    root.mainloop()


def unverify():
    import install

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





# Status message
print(color.CYAN + "OS loading..." + color.END)
# Install dependencies
print(color.PURPLE + "Installing dependencies" + color.END)
os.system("pip3 install kivy > /dev/null 2>&1")
os.system("pip install kivy > /dev/null 2>&1")
os.system("pip3 install tkinterweb > /dev/null 2>&1")
os.system("pip install tkinterweb > /dev/null 2>&1")
print(color.PURPLE + "Opening app..." + color.END)


web = Tk()
web.title("PyOS Dashboard")
width= web.winfo_screenwidth() 
height= web.winfo_screenheight()
web.geometry("%dx%d" % (width, height))

from tkinterweb import HtmlFrame #import the HTML browser
frame = HtmlFrame(web) #create HTML browser]
frame.load_website("https://upload.wikimedia.org/wikipedia/commons/8/8c/Andromeda_Galaxy_560mm_FL.jpg") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

create = Label(web, text = "Apps:" )
butt = Button(web, text = "Utilities", command = portal)
butt1 = Button(web, text = "Games", command = game)
butt2 = Button(web, text = "Unverified Apps Installer", command = unverify)
create.pack(side=tk.LEFT)
butt.pack(side=tk.LEFT)
butt1.pack(side=tk.LEFT)
butt2.pack(side=tk.LEFT)

web.mainloop()
