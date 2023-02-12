import streamlit as st 
import pandas

import requests
import snowflake.connector
from urllib.error import URLError



st.title ("My Parents Restaurant")
st.text ("\U0001F601 Poha")
st.text ("Upama")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

try:
  fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice :
    st.error ('Please select a fruit to know info')
  else:  
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)
except URLError e:
  st.error()
  
#st.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#st.dataframe(fruityvice_normalized)

st.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()

st.dataframe(my_data_row)

fruit_to_add = st.text_input('What fruit would you like to add ')
st.write('The user wants to add  ', fruit_to_add)
