import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)



st.set_page_config(page_title='Oltis')
st.header('Oltis Dataset')
st.markdown('Use this dashboard to understand the data and to make predictions.')
st.image('olist_pic.png')



connection.close()