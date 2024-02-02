import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)

st.set_page_config(page_title='Olist Dataset')
st.header('Reviews Score - Iris Dataset')
st.markdown('Explore the variables to understand the reviews score distribution.'
            )
st.sidebar.header('Distribution of Scores based on Product Receipt Status')


plot1  = px.histogram(
        df, 
        x='score',
        y = 'produit_recu',
        color = 'score',
        title='Distribution of Scores based on Product Receipt Status')
        
    
st.plotly_chart(plot1)

plot2  = px.scatter(
        df, 
        x='score',
        y = 'retard_livraison',
        color = 'score',
        title='Distribution of Scores based Delivery Delays',
        )
        
    
st.plotly_chart(plot2)


connection.close()