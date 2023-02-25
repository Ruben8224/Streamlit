import streamlit as st
import pandas as pd

st.title("Streamlit - Search names")

DATA_URL = ("https://firebasestorage.googleapis.com/v0/b/heroes-5bb27.appspot.com/o/datasets%2Fdataset.csv?alt=media&token=a5a1ac0f-8605-4182-a7c6-37ea27f762ee")

@st.cache
def load_data_byname (name):
    data = pd.read_csv(DATA_URL)
    filtered_data_byname = data[data["name"].str.contains(name)]
    return filtered_data_byname

myname = st.text_input("Name:")
if(myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0] #Gives number of rows
    st.write(f"Total name : {count_row}")

    st.dataframe(filterbyname)
