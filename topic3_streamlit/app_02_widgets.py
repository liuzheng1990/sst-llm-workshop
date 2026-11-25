import streamlit as st

st.title('Widgets Demo')
name = st.text_input('Your name', 'John Doe')
age = st.number_input('Your age', min_value=0, max_value=120, value=30, step=1)
level = st.slider('Satisfaction level', 0, 10, 7)
choice = st.selectbox('Favorite language', ['Python', 'JavaScript', 'Go', 'Rust'])
agree = st.checkbox('I agree to the terms')

if st.button('Submit'):
    st.success(f'Hello {name}! You are {age} years old. Level: {level}, Language: {choice}. Agreement: {agree}')

st.caption('Run: streamlit run app_02_widgets.py')