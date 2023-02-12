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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

try:
  fruit_choice = st.text_input('What fruit would you like information about')
  if not fruit_choice:
    st.error ('Please select a fruit to know info')
  else:  
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()
  
#st.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#st.dataframe(fruityvice_normalized)

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
if st.button ('Get Fruit load list '):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe (my_data_rows)
  
#import snowflake.connector
#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchall()

#st.dataframe(my_data_row)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+  fruit_to_add  +"')" )
    return 'thanks fro adding' +  new_fruit 
  
fruit_to_add = st.text_input('What fruit would you like to add ')
if st.button ('Add a fruit to the list '):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function =insert_row_snowflake (fruit_to_add)
  st.text(back_from_function)
st.write('The user wants to add  ', fruit_to_add)
