import streamlit as st

from views import home
from views import analyze
from views import about


st.set_page_config(
    page_title="Document Intelligence Suite",
    page_icon="📄",
    layout="wide"
)


st.sidebar.title("📄 Document Intelligence Suite")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Analyze Document",
        "About"
    ]
)

if menu == "Home":

    home.show()

elif menu == "Analyze Document":

    analyze.show()

else:

    about.show()