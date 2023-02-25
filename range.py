import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/calculadora-93291.appspot.com/o/dataset%2Fdataset.csv?alt=media&token=aece42f0-de97-4967-8116-f94caa65d8df')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_cvs(DATA_URL)
    filtered_data_byrange = data[ (data ['index'] >= startid) & (data ['index'] <= endid) ]
    
    return filtered_data_byrange

startid = st.text_input('Start index :')
endid = st.text_input('End index :')
btnRange = st.button('Seach by range')

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0] #Gives number of row
    st.write(f"Total ites : {count_row}")
    
    st.dataframe(filterbyrange)