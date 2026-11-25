import streamlit as st
import pandas as pd

st.title('File Upload')
uploaded = st.file_uploader('Upload a CSV file', type=['csv'])
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.success('File loaded! Preview below:')
    st.dataframe(df.head())
else:
    st.info('Awaiting file upload...')

st.caption('Run: streamlit run app_05_upload.py')