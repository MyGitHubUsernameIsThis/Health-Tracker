from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

Data = {}
Names = []

for n in Prediction:
    Data[n['name']] = n['value']
    Names.append(n['name'])

print(Data)
print(Names)