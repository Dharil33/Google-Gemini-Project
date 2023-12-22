from dotenv import load_dotenv
from PIL import Image
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def gemini_response(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.header("Gemini Vision Application")

input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an Image..",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True) 

submit = st.button("Tell me about the Image")

if submit:
    response = gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)