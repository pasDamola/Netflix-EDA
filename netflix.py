import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter


st.title('Netflix Data Analysis')

st.markdown("""
This app performs analysis of the popular movie site known as [Netflix](https://netflix.com/)
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [kaggle](https://www.kaggle.com/shivamb/netflix-shows).
""")

# Load netflix data
df = pd.read_csv('netflix_titles.csv')

def countries_with_most_titles(data_frame, column_name, limit):
   return(dict(Counter(data_frame[column_name].values).most_common(limit)))

countries_data = countries_with_most_titles(df, 'country', 11)
countries_df = pd.DataFrame(list(countries_data.items()), columns = ['country','no_of_titles']) 
countries_df = countries_df.drop(countries_df.index[2])

# remove 2020 from list of years
list_of_years = list(reversed(sorted(df.release_year.unique())))
store_2020 = list_of_years.pop(0)


st.sidebar.header('User Input Features')
selected_type = st.sidebar.selectbox('Filter by Type', df.type.unique())
selected_category = st.sidebar.selectbox('Filter by Category', df.listed_in.unique())
selected_year = st.sidebar.selectbox('Filter by Year', list_of_years)

# Filtering data
df_selected_show = df[(df.release_year==selected_year) & (df.type==selected_type) & (df.listed_in==selected_category)]

st.header('Display Netflix Stats of Selected Category(ies)')
st.write('Data Dimension: ' + str(df_selected_show.shape[0]) + ' rows and ' + str(df_selected_show.shape[1]) + ' columns.')
st.dataframe(df_selected_show)

st.header('Top 10 countries with the most titles')
st.dataframe(countries_df)
