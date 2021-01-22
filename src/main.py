# Importing Necessary modules 
from fastapi import FastAPI
import uvicorn
from Model import IrisModel, IrisSpecies
from mangum import Mangum
import os
 
# Declaring our FastAPI instance
description = "A REST API to serve inferences"

app_config = {
    'title': 'MyAPI',
    'description': description,
    'version': '0.0.1'
}

app = FastAPI(**app_config)
model = IrisModel()

def log_vars_and_event(event, context):
  print('## ENVIRONMENT VARIABLES')
  print(os.environ)
  print('## EVENT')
  print(event)
  print('## CONTEXT')
  print(context)

# Defining path operation for root endpoint 
@app.get('/') 
def main(): 
  return {'message': 'Welcome to my API!'} 

# Defining path operation for /name endpoint 
@app.get('/{name}') 
def hello_name(name : str):  
  return {'message': f'Welcome to my API, {name.capitalize()}!'}

# Defining path operation for /predict endpoint 
@app.post('/predict')
def predict_species(iris: IrisSpecies):
  data = iris.dict()
  prediction, probability = model.predict_species(
    data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
  )
  return {
    'prediction': prediction,
    'probability': probability
  }

# Wrap the FastAPI application in Mangum to translate Lambda events to FastAPI routes
# handler = Mangum(app)
def handler(event, context):
  log_vars_and_event(event, context)

  asgi_handler = Mangum(app)
  response = asgi_handler(event, context) # Call the instance with the event arguments
  return response