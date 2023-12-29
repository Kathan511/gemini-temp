import streamlit as st
import google.generativeai as genai


model = genai.GenerativeModel('gemini-pro')

question=st.text_input("Enter your question.")

if question:
    response=model.generate_content(question)
    st.markdown(response)
