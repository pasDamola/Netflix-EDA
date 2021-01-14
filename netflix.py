import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Netflix Data Analysis')

st.markdown("""
This app performs analysis of the movie site known as [Netflix](https://netflix.com/)
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [kaggle](https://www.kaggle.com/shivamb/netflix-shows).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Filter by Year', list(reversed(range(1950,2022))))