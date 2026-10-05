import os
import streamlit as st

from src.ui.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
    def load_UI(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout='wide')
        st.header(self.config.get_page_title())

        with st.sidebar:
            llm_options=self.config.get_llm_options()
            self.user_controls["selected_llm"]=st.selectbox("select llm",llm_options)
            if self.user_controls["selected_llm"]=="Groq":
                model_options=self.config.get_groq_model_options()
                self.user_controls["groq_api_key"] = st.text_input(
                     "Enter groq API Key",
                      type="password"
                )
                self.user_controls["selected_groq_model"]=st.selectbox("select model",model_options)
        return self.user_controls


