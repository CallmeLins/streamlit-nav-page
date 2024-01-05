import streamlit as st
from navpage.sim_nav_page import nav



st.set_page_config(
     page_title='Nav',
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon="🧬",
)


page_names_to_funcs = {
    "Navgation": nav,
    # "Plotting Demo": plotting_demo,
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()