import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import *
from PIL import ImageTk, Image



def write_slogan():
    #x = tk.simpledialog.askstring("What do you need help with?", "whatWillYouEat?")
    choices = ['thing0', 'thing', 'thing2']
    variable = StringVar(root)
    variable.set('GB')

    w = OptionMenu(root, variable, *choices)
    w.pack()
    print(w)

def readFile():
    file = tk.filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
    if file != None:
        data = file.read()
        file.close()
        print(file)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
root.title("Health Tracker")


button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.RIGHT)
slogan = tk.Button(frame,
                   text="Help",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

fileSelection = tk.Button(frame,
                          text = "Choose a file",
                          command=readFile)
fileSelection.pack(side=tk.LEFT)


root.mainloop()