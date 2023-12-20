import streamlit as st
import streamlit.components.v1 as components
import webbrowser

hide_streamlit_style = """
            <style>
            .stDeployButton {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

enter_search_js = """
<script type="text/javascript">
document.addEventListener("DOMContentLoaded", function() {
    const doc = window.parent.document
    const inputElement = doc.querySelector(".stTextInput input");

    inputElement.addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            doc.querySelector(".stButton button").click();
        }
    });
});
</script>
"""
components.html(enter_search_js)
st.markdown(enter_search_js, unsafe_allow_html=True)


def search(query, search_engine):
    if search_engine == "Google":
        url = f"https://www.google.com/search?q={query}"
    elif search_engine == "Bing":
        url = f"https://www.bing.com/search?q={query}"
    elif search_engine == "Baidu":
        url = f"https://www.baidu.com/s?wd={query}"
    else:
        st.error("Please select a search engine")
        return

    webbrowser.open_new_tab(url)

st.title("Sim Nav Page")

search_query = st.text_input("Please input search content", key="keypress")
search_engine = st.selectbox("Please select a search engine", ("Google", "Bing", "Baidu"))

if st.button("Search"):
    search(search_query, search_engine)