from fastapi import FastAPI
from make_pred import make_prediction
from train_model import make_model_save

import numpy as np 
import pandas as pd

app = FastAPI()

@app.get("/infos")
def read_root():
    return {'Message': 'Hello, welcome on my dashboard!'}

@app.get('/train_model')
def train_model():
    make_model_save()
    print('Training in progress')
    return {'Response' : 'Training completed'}

@app.get('/{x1}/{x2}/{x3}/{x4}')
def get_pred(x1: float, x2: float, x3: float, x4: float):
    p1 =[x1,x2,x3,x4]
    x = np.array([p1])
    
   
    col_headers = ['score','retard_livraison', 'temps_livraison', 'produit_recu']

    x_df = pd.DataFrame(x, columns=col_headers)
    print('x', x_df)


    prediction = make_prediction(x_df)

    print(prediction)

    return {'prediction' : prediction}





