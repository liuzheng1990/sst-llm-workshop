import streamlit as st
import pandas as pd
import numpy as np

st.title('Data and Charts')
df = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(10, 100, size=10),
    'z': np.random.randn(10)
})
st.subheader('DataFrame preview')
st.dataframe(df)

st.subheader('Line chart')
st.line_chart(df[['x', 'y']].set_index('x'))

st.subheader('Bar chart')
st.bar_chart(df[['x', 'y']].set_index('x'))

st.subheader('Map (random points)')
map_df = pd.DataFrame({
    'lat': np.random.uniform(1.28, 1.36, 20),
    'lon': np.random.uniform(103.78, 103.95, 20)
})
st.map(map_df)

st.caption('Run: streamlit run app_04_charts.py')
