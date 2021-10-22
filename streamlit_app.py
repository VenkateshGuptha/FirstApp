import streamlit as st
from PIL import Image
import pymongo

degree_symbol = (u'\N{DEGREE SIGN}')
data = "Data"
st.title("Game")

col1, col2, col3 = st.columns(3)
col1.header('Puzzle - 1')
puzzle1_image = Image.open('icon.png')
col1.image(puzzle1_image, use_column_width=True)
if col1.button("Calculate"):
    col1.write("Calculating.......")

iterations = col3.slider("Heading", 0, 360, 0, 1)
col3.text(str(iterations) + degree_symbol)
col3.text("Blocks list")
col3.radio("Block A. Directions -", ('Left', 'Right', 'North', 'South'))
col3.radio("Block B. Directions -", ('Left', 'Right', 'North', 'South'))
col3.radio("Block C. Directions -", ('Left', 'Right', 'North', 'South'))
col3.radio("Block D. Directions -", ('Left', 'Right', 'North', 'South'))
