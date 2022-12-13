import streamlit as st 
import pandas

st.header("Hello world !")
st.title ("My Parents Restaurant")
st.text ("\U0001F601 Poha")
st.text ("Upama")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(my_fruit_list)

