import tkinter
from tkinter import filedialog

root = tkinter.Tk()
file = tkinter.filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
if file != None:
    data = file.read()
    file.close()
    print ("It worked...?" )