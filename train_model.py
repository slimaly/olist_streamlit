import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import sqlite3

def make_model_save():
    # Connexion à la base de données
    connection = sqlite3.connect("olist.db")

    # Charger les données à partir de la base de données
    df = pd.read_sql_query("SELECT * FROM TrainingDataset", connection)

    # Séparer la cible (y) et les caractéristiques (x)
    y = df['score']
    x = df[['score', 'produit_recu', 'retard_livraison', 'temps_livraison']]  # Ajoutez les colonnes nécessaires

    # Séparer l'ensemble d'entraînement de l'ensemble de test
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

    # Créer et entraîner le modèle RandomForestClassifier
    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(x_train, y_train)

    # Sauvegarder le modèle dans un fichier pickle
    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)

    # Fermer la connexion à la base de données
    connection.close()

# Appeler la fonction pour créer et sauvegarder le modèle
make_model_save()

