# Library imports
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib

# Class which describes a single flower measurements
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float

# Class for training the model and making predictions
class IrisModel:
    # Class constructor which loads the model
    def __init__(self):
        self.model_fname_ = '/iris_model.pkl'
        self.model = joblib.load(self.model_fname_)
            
    # Make a prediction based on the user-entered data
    # Returns the predicted species with its respective probability
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_length]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability