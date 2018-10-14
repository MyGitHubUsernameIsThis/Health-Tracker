from tkinter import *
from PIL import ImageTk,Image
import tkinter
from tkinter import filedialog

root = Tk()
file = tkinter.filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
if file != None:
    data = file.read()
    file.close()
    img = ImageTk.PhotoImage(Image.open(file))
    panel = tkinter.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
canvas.create_image(20, 20, anchor=NW, image=img)
root.mainloop()


