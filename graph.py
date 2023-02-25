import streamlit as st 
import numpy as np 
import pandas as pd 

char_data = pd.DataFrame(
    np.random.rand(500, 5),
    columns=['a', 'b', 'c', 'd', 'e'] 
)

st.line_chart(char_data)