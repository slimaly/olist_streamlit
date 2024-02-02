import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import sqlite3

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)
 
st.set_page_config(page_title='Oltis Dataset')
st.header('Prediction - Oltis Dataset')
st.markdown('Train model to make predictions for classification.')
st.sidebar.header('Train model')

launch_training = st.sidebar.button('Training')

if launch_training:
    url = f'http://localhost:8000/train_model'
    
    #envoyer la requete à fast api
    response = requests.get(url)    
    if response.status_code == 200:
        response = response.json()['Response']
        st.success(f'Model traning message: {response}')
    else: 
        st.error('Error in prediction request')
else:
    #welcome message
    url = f'http://localhost:8000/infos'

#envoyer la requete à fast api
    response = requests.get(url)

#vérifier si la requête a réussi( code 200)

    if response.status_code == 200:
        message = response.json()['Message']
        st.success(f'API welcome message : {message}')
    else:
        st.error('Error in welcome request.')


connection.close()