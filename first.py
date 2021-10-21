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


client = pymongo.MongoClient("mongodb+srv://kneehighrobotics:trimblehack2021@cluster0.ar4vy.mongodb.net/sample_airbnb?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
#client = pymongo.MongoClient("mongodb+srv://kneehighrobotics:trimblehack2021/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.sample_airbnb
my_collections = db.listingsAndReviews
#col1.write(my_collections.find().count())
data, list(my_collections.find({"name": "Ribeira Charming Duplex"}))

'''for item in my_collections.find():
    col1.write(item['name'])'''