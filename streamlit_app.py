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
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Kiwi'])
streamlit.dataframe(my_fruit_list)
