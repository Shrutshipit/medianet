import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="My AI App", layout="centered")

st.title("My Gemini AI App")

# API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-1.5-flash")

# User input
user_input = st.text_area("Enter your prompt")

if st.button("Generate"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter something.")
