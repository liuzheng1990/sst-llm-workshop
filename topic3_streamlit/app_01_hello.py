import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')
st.markdown('**Markdown** _formatting_ works too!')
st.metric(label='Temperature', value='27°C', delta='1.2°C')

st.caption('Run me with: pyngrok from the file app_01_hello.py')