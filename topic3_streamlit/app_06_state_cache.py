import time
import streamlit as st

st.title('Session State & Cache')

# Session State
if 'counter' not in st.session_state:
    st.session_state.counter = 0

inc = st.button('Increment counter')
if inc:
    st.session_state.counter += 1
st.write('Counter:', st.session_state.counter)

# Cached function (data cache)
@st.cache_data
def expensive_computation(n):
    time.sleep(2)  # Simulate expensive work
    return sum(range(n))

n = st.number_input('Compute sum up to n', min_value=1, max_value=1_000_000, value=100_000, step=1000)
if st.button('Run computation'):
    result = expensive_computation(int(n))
    st.success(f'Result: {result}')

st.caption('Run: streamlit run app_06_state_cache.py')
