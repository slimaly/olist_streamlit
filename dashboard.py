import streamlit as st
import pandas as pd
import sqlite3

connection = sqlite3.connect("olist.db")

df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)



st.set_page_config(page_title='Oltis')
st.header('Oltis Customer Satisfaction')

connection.close()