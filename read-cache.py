import streamlit as st
import pandas as pd

st.title('Streamlit con atributo cache')

DATA_URL = ('dataset.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    return data

data_load_state = st.text('load data...')
data = load_data(1000)
data_load_state.text("Done! (usin st.cache)")

st.dataframe(data)
