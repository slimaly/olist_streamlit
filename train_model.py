import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import json
import pickle
import sqlite3
import numpy as np


def make_model_save():

    connection = sqlite3.connect("olist.db")
    df = pd.read_sql_query("SELECT * FROM TrainingDataset", connection)

   
    # Separate Target and Features : x and y datas
    y = df['score']
    x = df(['retard_livraison', 'temps_livraison', 'produit_recu'], axis=1)

    # Separate TrainSet / TestSet
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

    # Train model
    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(x_train, y_train)

    # Save model
    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)
