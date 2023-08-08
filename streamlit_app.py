import streamlit
import pandas as pd
import numpy as np
import snowflake.connector



streamlit.title('this is first time I am learning all this')
streamlit.header('My main goals  🥣')
streamlit.text('get proficient into snowflake 🥗')
streamlit.text('get proficient into databricks 🐔')
streamlit.text('get certified in az900 🥑')
streamlit.text('get certified in aws 🍞')
streamlit.text('get certified in snowflake 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt', header=1)
streamlit.dataframe(my_fruit_list)

import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")

#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

