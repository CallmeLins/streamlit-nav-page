import base64
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.set_page_config(
     page_title='Sim Nav Page',
     layout="wide",
     initial_sidebar_state="expanded",
)

hide_streamlit_style = """
            <style>
            .stDeployButton {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

enter_search_js = """
<script type="text/javascript">
document.addEventListener("DOMContentLoaded", function() {
    const doc = window.parent.document // break out of the IFrame
    const inputElement = doc.querySelector(".stTextInput input");

    inputElement.addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            doc.querySelector(".stButton button").click();
        }
    });

    const searchButton = doc.querySelector(".stButton button");
    searchButton.addEventListener("click", function() {
        const query = doc.querySelector(".stTextInput input").value;
        const searchEngine = doc.querySelector('[data-baseweb="select"]').innerText.trim();

        let url;
        if (searchEngine === "Google") {
            url = `https://www.google.com/search?q=${query}`;
        } else if (searchEngine === "Bing") {
            url = `https://www.bing.com/search?q=${query}`;
        } else if (searchEngine === "Baidu") {
            url = `https://www.baidu.com/s?wd=${query}`;
        } else {
            alert("Please select a search engine");
            return;
        }

        window.open(url, "_blank");
    });
});
</script>
"""
components.html(enter_search_js, height=0)

st.title("Sim Nav Page")

search_query = st.text_input("Please input search content")
search_engine = st.selectbox("Please select a search engine", ("Google", "Bing", "Baidu"))

if st.button("Search"):
    pass  # This space intentionally left blank, as the search is handled by JavaScript

tab1, tab2, tab3= st.tabs(["💊 Most Use", "🗃 Tools", "🎞 Entertainment"])

if tab1:
    st.write("Links for Most Use:")
    st.markdown("- [Google](https://www.google.com/)")
    st.markdown("- [YouTube](https://www.youtube.com/)")
    st.markdown("- [Amazon](https://www.amazon.com/)")

# st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
st.sidebar.header('Streamlit Sim Nav Page')

st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/), as of [Streamlit v1.25.0](https://www.streamlit.io/).</small>
''', unsafe_allow_html=True)

st.sidebar.markdown('__Install and import__')

st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
st.sidebar.markdown('''<small>[Simple Nav Page v1.0](https://github.com/CallmeLins/streamlit-nav-page)  | Aug 2023 | [CallmeLins](https://CallmeLins.github.io/)</small>''', unsafe_allow_html=True)