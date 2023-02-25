import pandas as pd 
import streamlit as st 
import datetime

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

#create the title for the web app
st.title("My First Streamlit App")
sidebar = st.sidebar
sidebar.title("This is the sidebar")
sidebar.write("You can add any element to the sidebar")

#Give user the corrent date

today = datetime.date.today()
today_date = st.date_input('current date', today)

st.success('current date: ´%s´' % (today_date))

#Display the content of the dataset if checknox is true

st.header("Dataset")
agree = sidebar.checkbox("show DataSet Overview ?")
if agree:
    st.dataframe(titanic_data)
    
# Select the embarl town of the passanger and then display the dataset with this selection
selected_town = sidebar.radio("Select Embark Town", titanic_data['embark_town'].unique())

st.write("Selected Embark Town:", selected_town)
st.write(titanic_data.query(f"""embark_town==@selected_town"""))
st.markdown("___")

#select a range of the fare and then display the dataset with this selection

optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimun Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximun Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)

subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

#Display of the dataset
st.dataframe(subset_fare)