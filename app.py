import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 AI Document Intelligence")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Upload Document",
        "About"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if menu == "Home":

    st.title("📄 AI Document Intelligence Suite")

    st.markdown("""
Welcome!

This application can analyze documents using AI.

### Features

- 📄 PDF Reader
- 📝 DOCX Reader
- 🖼 Image OCR
- 🤖 AI Summarization
- 💬 Ask Questions
- 🧠 Flashcards
- ✅ MCQ Generator
- 🌍 Translation
- 🔑 Keyword Extraction
""")

# -----------------------------
# Upload Page
# -----------------------------
elif menu == "Upload Document":

    st.title("📤 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "docx", "png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.success(f"Uploaded: {uploaded_file.name}")

        st.write("File Type:", uploaded_file.type)

        st.write("Size:", round(uploaded_file.size / 1024, 2), "KB")

# -----------------------------
# About
# -----------------------------
else:

    st.title("About")

    st.info("""
AI Document Intelligence

Version 1.0

Developed using:

- Python
- Streamlit
- Gemini AI
- OCR
- NLP
""")