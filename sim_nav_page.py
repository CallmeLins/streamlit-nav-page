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
components.html(enter_search_js)

st.title("Sim Nav Page")

search_query = st.text_input("Please input search content")
search_engine = st.selectbox("Please select a search engine", ("Google", "Bing", "Baidu"))

if st.button("Search"):
    pass  # This space intentionally left blank, as the search is handled by JavaScript