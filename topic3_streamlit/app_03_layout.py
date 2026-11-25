import streamlit as st

st.title('Layout Demo')
col1, col2 = st.columns(2)
with col1:
    st.header('Column 1')
    st.write('Content on the left')
with col2:
    st.header('Column 2')
    st.write('Content on the right')

tab1, tab2 = st.tabs(['Overview', 'Details'])
with tab1:
    st.write('High-level information')
with tab2:
    st.write('Deep dive content')

with st.expander('See more'):
    st.write('Hidden content revealed on click')

st.caption('Run: streamlit run app_03_layout.py')
