from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.header("Google's Gemini LLM Application")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask a question")

if submit:
    response = gemini_response(input)
    st.subheader("The Response is")
    st.write(response)