# Import Streamlit
import streamlit as st
import numpy as np
import pandas as pd

#Header
st.title('🎈 Attrition Prediction')
st.write('Hello world!')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Attrition Dataset**')
  df = pd.read_csv('https://github.com/CoFaiz/Bytebrains/blob/master/dataset_final_bytebrains_stage2.csv')
  df

  st.write('**X**')
  X_raw = df.drop('StockOptionLevel', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='Attrition', y='count' )



