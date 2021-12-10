from tkinter import *

root = Tk()
root.title("Installer")


blank = Label(root, text="")
directions = Label(root, text="Welcome to the external app download center")
warning = Label(root, text="DO NOT INSTALL APPS THAT YOU DO NOT TRUST A 100%")
directions1 = Label(root, text = "To install/open on the current master, enter the URL of the file:")
enter = Entry(root)
def install():
    import urllib.request
    urllib.request.urlretrieve(str(enter.get()), "unverified.py")
    open = __import__("unverified.py")


submit = Button(root, text = "Submit", command = install)


directions.pack()
warning.pack()
blank.pack()
directions1.pack()
enter.pack()
submit.pack()

root.mainloop()