import joblib
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

def train_model():
  df = pd.read_csv('iris.csv')
  model_filename = '/tmp/iris_model.pkl'
  
  X = df.drop('species', axis=1)
  y = df['species']
  rfc = RandomForestClassifier()
  model = rfc.fit(X, y)
  joblib.dump(model, model_filename)

if __name__ == '__main__':
    train_model()