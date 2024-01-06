import streamlit as st
from nav_page.sim_nav_page import nav
from gpt_page.gpt_page import chatgpt


st.set_page_config(
     page_title='Nav',
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon="🧬",
)


page_names_to_funcs = {
    "Navgation": nav,
    "ChatGPT": chatgpt,
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()