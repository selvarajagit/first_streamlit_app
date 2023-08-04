import streamlit
import pandas as pd
streamlit.title('this is first time I am learning all this')
streamlit.header('My main goals  🥣')
streamlit.text('get proficient into snowflake 🥗')
streamlit.text('get proficient into databricks 🐔')
streamlit.text('get certified in az900 🥑')
streamlit.text('get certified in aws 🍞')
streamlit.text('get certified in snowflake 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt', header=1)
streamlit.multiselect("Pick some fruits",list(my_fruit_list.index),['Strawberries','Avocado'])

streamlit.dataframe[my_fruit_list]
