import streamlit as st
import pandas as pd
import plotly.express as px
import json
import requests
import numpy as np
import sqlite3
import pickle

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset", connection)

st.set_page_config(page_title='Prediction')
st.header('Prediction - Oltis Dataset')
st.markdown('Using RandomForestClassifier, make predictions for classification the score data should fall into'
            'The prediction will appear on the graphs below to untuit how the prediction was made.')
st.sidebar.header('Make Prediction')

retard_livraison = st.sidebar.text_input('Delivery Delay')
temps_livraison = st.sidebar.text_input('Delivery Time')
produit_recu = st.sidebar.text_input('Product Delivery Status')
score = df[['score']]  # Utilisez une DataFrame pour x avec une seule colonne
make_pred_API = st.sidebar.button('Predict')

# Charger le modèle RandomForestClassifier à partir du fichier pickle
with open('main_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

plot1 = px.scatter(
    df,
    x='score',
    y='retard_livraison',
    color='score',
    title='Score VS Delivery Delay'
)

plot2 = px.histogram(
    df,
    x='score',
    y='produit_recu',
    color='score',  # Colorer par la valeur de produit_recu
    labels={'produit_recu': 'Product Received'},
    category_orders={'produit_recu': [0, 1]}
)

if make_pred_API:
    # Créer un DataFrame pour la prédiction
    produit_recu_value = 1 if produit_recu.lower() == 'yes' else 0

    p1_df = pd.DataFrame({
        'retard_livraison': [float(retard_livraison)],  # Assurez-vous que les données sont dans le bon format
        'temps_livraison': [float(temps_livraison)],
        'produit_recu': [float(produit_recu_value)],
        'score': [float(score.iloc[0])]
    })

    # Faire la prédiction avec le modèle RandomForestClassifier
    score_pred = model.predict(p1_df[['score', 'retard_livraison', 'temps_livraison', 'produit_recu']].values.reshape(1, -1))[0]

    st.success(f'Prediction Result: {score_pred}')
    

    plot1.add_scatter(
        x=p1_df['score'],
        y=p1_df['retard_livraison'],
        mode='markers',
        name=str(score_pred),
        marker=dict(
            color='red',
            size=10,
            symbol='circle',
            line=dict(
                color='white',
                width=2
            )
        ))

    plot2.add_scatter(
        x=p1_df['score'],
        y=p1_df['produit_recu'],
        mode='markers',
        name=str(score_pred),
        marker=dict(
            color='red',
            size=10,
            symbol='circle',
            line=dict(
                color='white',
                width=2
            )
        ))

st.plotly_chart(plot1)
st.plotly_chart(plot2)

connection.close()
