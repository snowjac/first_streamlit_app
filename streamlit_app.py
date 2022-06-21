import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 and Blueberry Muesli')
streamlit.text('🥬 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Soft-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado on Toast')
streamlit.header('🍌🥭 Build your own Smoothie 🫐🥝')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
