from google import genai
import streamlit as st


def get_client():
    """
    Return a Gemini client using the API key entered in the sidebar.
    """

    api_key = st.session_state.get("api_key")

    if not api_key:
        st.error(
            "Please enter your Gemini API key in the sidebar before using AI features."
        )
        st.stop()

    return genai.Client(api_key=api_key)