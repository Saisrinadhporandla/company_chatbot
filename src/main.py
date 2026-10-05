import streamlit as st
import os
from src.ui.loadui import LoadStreamlitUI

def load_app():
    ui=LoadStreamlitUI()
    user_input=ui.load_UI()

    if not user_input:
        st.error("enter user input")
        return

    user_message=st.chat_input("enter your message")