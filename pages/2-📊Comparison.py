import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)

st.set_page_config(page_title='Olist Dataset')
st.header('Reviews Score Comaprison - Olist Dataset')
st.markdown('Explore the variables to understand the reviews score distribution.'
            )
st.sidebar.header('Distribution of Scores')

options = st.sidebar.radio('Select comparison',
                           options=['Score VS Delayed Delivery',
                                    
                                    'Score VS Product Received'])

if options == 'Score VS Delayed Delivery':
    plot  = px.scatter(
        df, 
        x='score',
        y='retard_livraison',
        color = 'score',
        title=options
    )
    st.plotly_chart(plot)



elif options == 'Score VS Product Received':
    # Utiliser px.histogram pour afficher la fréquence des valeurs 0 et 1
    plot = px.histogram(
        df,
        x='score',
        y='produit_recu',
        color='score',  # Colorer par la valeur de produit_recu
        title=options,
        labels={'produit_recu': 'Product Received'},
        category_orders={'produit_recu': [0, 1]}  # Ordonner les catégories
    )
    st.plotly_chart(plot)



connection.close()