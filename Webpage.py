import tkinter
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.file_button = Button(master, text="Close", command=master.readFile)
        self.file_button.pack()

    def greet(self):
        print("Greetings!")

    def readFile(self):
        file = tkinter.filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
        if file != None:
            data = file.read()
            file.close()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()