import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Netflix Data Analysis')

st.markdown("""
This app performs analysis of the popular movie site known as [Netflix](https://netflix.com/)
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [kaggle](https://www.kaggle.com/shivamb/netflix-shows).
""")

# Load netflix data
df = pd.read_csv('netflix_titles.csv')


st.sidebar.header('User Input Features')
selected_type = st.sidebar.selectbox('Filter by Type', df.type.unique())
selected_category = st.sidebar.selectbox('Filter by Category', df.listed_in.unique())
selected_year = st.sidebar.selectbox('Filter by Year', list(reversed(sorted(df.release_year.unique()))))



# Filtering data
df_selected_show = df[(df.release_year==selected_year) & (df.type==selected_type) & (df.listed_in==selected_category)]

st.header('Display Netflix Stats of Selected Category(ies)')
st.write('Data Dimension: ' + str(df_selected_show.shape[0]) + ' rows and ' + str(df_selected_show.shape[1]) + ' columns.')
st.dataframe(df_selected_show)