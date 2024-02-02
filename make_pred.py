import json
import pickle

def make_prediction(x):
    with open('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pickle.load(fichier_modele)

    predictions_out = loaded_model.predict(x)

    with open('encoder.json') as json_file:
       data = json.load(json_file)

    prediction_string = data[str(int(predictions_out))]

    return prediction_string