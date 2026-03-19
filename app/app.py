import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.chatbot import ask 

st.title("AI Knowledge Assistant")
question = st.text_input("Ask something")

if question:
    answer = ask(question)
    st.write(answer)