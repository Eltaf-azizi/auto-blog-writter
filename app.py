import streamlit as st
import requests


st.title("AI-powered Blog Writter")



topic = st.text_input("Enter the Blog Topic: ")


if st.button("Generate Blog"):
    with st.splinner("Generating Blog ..."):
        requests.post()