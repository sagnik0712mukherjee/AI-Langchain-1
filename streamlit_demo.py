import os
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Me Anything 😉")

with st.sidebar:
    st.title("Enter your OpanAI API KEY")
    OPENAI_API_KEY = st.text_input("OpenAI API Key")

if not OPENAI_API_KEY:
    st.info("You cannot proceed without putting your API key")
    st.stop()

llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
question = st.text_input("Enter the question here... ")

if question and llm:
    response = llm.invoke(question)
    st.write(response.content)
