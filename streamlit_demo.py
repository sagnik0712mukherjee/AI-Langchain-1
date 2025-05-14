from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.globals import set_debug

set_debug(True)

st.title("Ask Me Anything 😉")

question = st.text_input("Enter the question here... ")

llm=ChatOllama(model="llama3.2:latest")

if question and llm:
    response = llm.invoke(question)
    st.write(response.content)
