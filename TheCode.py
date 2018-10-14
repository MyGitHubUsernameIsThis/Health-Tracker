from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='3186a73fc35242df941c98e012ef2e2c')

model = app.models.get("general-v1.3")

Prediction = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')['outputs'][0]['data']['concepts']

Data = {}
Names = []

for n in Prediction:
    Data[n['name']] = n['value']
    Names.append(n['name'])

print(Data)
print(Names)


from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='f2b04923b78749f99c5ce8690909a9d2')

model = app.models.get('food-items-v1.0')
image = ClImage(url='https://www.thespruceeats.com/thmb/ivY7T2DRygJN2nHwAFYqVxfbvs4=/3000x2000/filters:no_upscale():max_bytes(150000):strip_icc()/Hamburger-Hot-Dog-58add5f03df78c345bdef6ff.jpg')
Prediction = model.predict([image])['outputs'][0]['data']['concepts']


Data = {}
Names = []
PrintedNames = []
count = 1
inputIsValid = False # returns false if user input food index something that is not valid. ie: out of range or not an integer
Ingredients = []
Choosing = True  # turns false when user is done choosing which foods they ate
yesOrNo = False #Returns true once user correctly inputs either 'Y' or 'N'

for n in Prediction:
    Data[n['name']] = n['value']
    PrintedNames.append(n['name'] + ": " + str(count))
    Names.append(n['name'])
    count += 1

# print(Data)
print(PrintedNames)


while Choosing:
    inputIsValid = False
    while not inputIsValid:
        foodInput = int(input("Please enter the food number one by one (Type -1 to print out list of ingredients): "))
        if foodInput == -1:
            print(PrintedNames)
        elif Names[foodInput-1] in Ingredients:
            print("Please do not enter repeats")
        elif 0 < foodInput <= len(Names):
            Ingredients.append(Names[foodInput-1])
            inputIsValid = True

        else:
            print("Please Enter a valid number")
    print("You have currently selected: " + ", ".join(Ingredients))
    yesOrNo = False
    while not yesOrNo:
        ask = input("Is there more to add? (Type Y/N) ")
        if ask == "N":
            yesOrNo = True
            Choosing = False
        elif ask == "Y":
            yesOrNo = True
        else:
            print("Please type either Y or N")
        print("The following is the ingredients you had: " + ", ".join(Ingredients))