import streamlit
import pandas as pd
import numpy as np

streamlit.title('this is first time I am learning all this')
streamlit.header('My main goals  🥣')
streamlit.text('get proficient into snowflake 🥗')
streamlit.text('get proficient into databricks 🐔')
streamlit.text('get certified in az900 🥑')
streamlit.text('get certified in aws 🍞')
streamlit.text('get certified in snowflake 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt', header=1)
#streamlit.dataframe[my_fruit_list]

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

streamlit.dataframe(df)  # Same as st.write(df)


import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")

#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
streamlit.dataframe[fruityvice_normalized]

