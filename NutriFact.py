from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
import csv
import tkinter as tk
import datetime
import Graph
from tkinter import ttk


app = ClarifaiApp(api_key='##Your API Key Here')

def output(Upload):
    food = str(Upload)[26:len(str(Upload))-2]
    model = app.models.get('food-items-v1.0')
    image = ClImage(file_obj=open(str(food), 'rb'))
    prediction = model.predict([image])['outputs'][0]['data']['concepts']


    data = {}
    names = []

    for n in prediction:
        data[n['name']] = n['value']
        names.append(n['name'])
    return names

def file(fileName):
    csvf = open(fileName, encoding="utf-8")
    freader = csv.reader(csvf, delimiter=',', quotechar='"')
    header = next(freader)
    foods = {}
    for row in freader:
        food = row[1].split(" (")[0]
        sugar = float(row[22])
        satFats = float(row[25])
        calories = float(row[24])
        portion = int(row[2])
        if food not in foods and portion == 1:
            foods[food] = []
        if food in foods:
            foods[food].append(calories)
            foods[food].append(sugar)
            foods[food].append(satFats)
    return foods


def userinput(name):
    count = 1
    printed_name = []
    for p in name:
        printed_name.append(str(count) + ") " + p)
        count += 1
    win = tk.Tk()
    win.title("Python GUI")
    win.resizable(0, 0)

    aLabel = ttk.Label(win, text="Please enter food number separated by comma then space (Ex: 1, 3, 5)")
    aLabel.grid(column=0, row=0)
    bLabel = ttk.Label(win, text=", ".join(printed_name))
    bLabel.grid(column=0, row=1)

    def quit():
        win.destroy()


    namely = tk.StringVar()
    nameEntered = ttk.Entry(win, width=12, textvariable=namely)
    nameEntered.focus()
    nameEntered.grid(column=1, row=0)

    action = ttk.Button(win, text="Click", command=quit)
    action.grid(column=1, row=1)

    win.mainloop()


    ingredients = []
    extra = True  # Stays true until user has put in all inputs they need
    user_input = namely.get()
    food = user_input.split(", ")
    for k in food:
        i = int(k)
        if name[i-1] not in ingredients:
            ingredients.append(name[i-1])
    print("Ingredients List: " + ", ".join(ingredients))



    while extra:
        win1 = tk.Tk()
        win1.title("GUI")

        cLabel = ttk.Label(win1, text="Is there anything that's missing?")
        cLabel2 = ttk.Label(win1, text="Current ingredients: "+", ".join(ingredients))
        cLabel.grid(column=0, row=0)
        cLabel2.grid(column=0, row=1)

        def clickYes():
            global missing
            missing = "Y"
            win1.destroy()

        def clickNo():
            global missing
            missing = "N"
            win1.destroy()

        action_yes = ttk.Button(win1, text="Yes", command=clickYes)
        action_yes.grid(column=1, row=0)
        action_no = ttk.Button(win1, text="No", command=clickNo)
        action_no.grid(column=2, row=0)

        win1.mainloop()
        if missing.upper() == "N":
            extra = False
        elif missing.upper() == "Y":
            win2 = tk.Tk()
            win2.title("Python GUI")
            win2.resizable(0, 0)

            dLabel = ttk.Label(win2, text="A Label")
            dLabel.grid(column=0, row=0)

            def clickMe():
                win2.destroy()

            ttk.Label(win2, text="Type ingredient name missing").grid(column=0, row=0)
            manual_input = tk.StringVar()
            nameEntered1 = ttk.Entry(win2, width=12, textvariable=manual_input)
            nameEntered1.grid(column=0, row=1)
            nameEntered1.focus()

            action = ttk.Button(win2, text="Click", command=clickMe)
            action.grid(column=1, row=1)


            win2.mainloop()

            ingredients.append(manual_input.get())
        print("Ingredients List: " + ", ".join(ingredients))
    return ingredients

def display(cals, sugar, fats):
    win = tk.Tk()
    win.title("Python GUI")
    Label1 = ttk.Label(win, text= "Calories: " + str(cals))
    Label1.grid(column=0, row=0)
    Label1.config(font=("Courier", 44))

    Label2 = ttk.Label(win, text="Sugar: " + str(sugar))
    Label2.grid(column=0, row=1)
    Label2.config(font=("Courier", 44))
    Label3 = ttk.Label(win, text="Saturated Fats: " + str(fats))
    Label3.grid(column=0, row=2)
    Label3.config(font=("Courier", 44))


    cLabel = ttk.Label(win, text="Would you like to see the graph of the eaten calories for the previous days?")
    cLabel.grid(column=0, row=3)
    cLabel.config(font=("Courier", 20))

    def clickyes():
        win.destroy()
        d = Graph.read('data.txt')
        Graph.graph(d)



    def clickno():
        print("See you next time!")
        win.destroy()

    action_yes = ttk.Button(win, text="Yes", command=clickyes)
    action_yes.grid(column=1, row=3)
    action_no = ttk.Button(win, text="No", command=clickno)
    action_no.grid(column=2, row=3)

    win.mainloop()

def findCalories(items, foodDictionary):
    finalItems = []
    retCal = 0
    retSugar = 0
    retFats = 0
    for eachItem in items:
        possibilities = []
        for k,v in foodDictionary.items():
            if eachItem.lower() in k.lower():
                possibilities.append(k)
        possibilities.sort(key = len)
        if len(possibilities) == 1:
            finalItems.append(possibilities[0])

        printedPossibilities = []
        for x in range(len(possibilities)):
            printedPossibilities.append(str(x+1) + ") " + possibilities[x])

        import tkinter as tk
        from tkinter import ttk
        win3 = tk.Tk()
        win3.title("Python GUI")
        win3.resizable(0, 0)

        eLabel = ttk.Label(win3, text="Please select the type of " + eachItem + " you ate")
        eLabel.grid(column=0, row=1)
        fLabel = ttk.Label(win3, text=", ".join(printedPossibilities[0:10]))
        fLabel.grid(column=0, row=0)

        def quit():
            win3.destroy()

        toAdd = tk.StringVar()
        nameEntered = ttk.Entry(win3, width=12, textvariable=toAdd)
        nameEntered.focus()
        nameEntered.grid(column=0, row=2)

        action = ttk.Button(win3, text="Click", command=quit)
        action.grid(column=0, row=3)

        win3.mainloop()
        toPut = int(toAdd.get())


        print(", ".join(printedPossibilities[0:10]))
        finalItems.append(possibilities[toPut-1])

    for food in finalItems:
        retCal += foodDictionary[food][0]
        retSugar += foodDictionary[food][1]
        retFats += foodDictionary[food][2]
    display(retCal, retSugar, retFats)
    f = open("data.txt", "a")
    f.write(datetime.date.today().strftime("%j") + ":" + str(retCal) + '\n')

import tkinter as tk
from tkinter import filedialog


def write_slogan():
    print("Upload an image to get nutritional value!")

def readFile():
    Upload = tk.filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')
    if Upload != None:
        root.destroy()
        foodDict = file("Food_Display_Table.csv")
        names = output(Upload)
        ingredients = userinput(names)
        findCalories(ingredients, foodDict)

if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    root.title("Health Tracker")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    button = tk.Button(frame, text="QUIT", fg="blue", command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="Help",
                       command=write_slogan)
    slogan.pack(side=tk.LEFT)

    fileSelection = tk.Button(frame,
                              text="Choose a file",
                              command=readFile)
    fileSelection.pack(side=tk.LEFT)

    root.mainloop()
