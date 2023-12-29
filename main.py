import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCO0_pqNDii2T1oReljBxyA_2g26oI1ElI")


model = genai.GenerativeModel('gemini-pro')

question=st.text_input("Enter your question.")

if question:
    response=model.generate_content(question)
    st.markdown(response)
