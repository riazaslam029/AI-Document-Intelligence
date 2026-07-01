import os
import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.pdf_loader import extract_pdf_text

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

### 🚀 Features

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

    st.write("Upload a PDF, DOCX, or Image file.")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "docx", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        # Save file
        file_path = save_uploaded_file(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.subheader("📄 File Information")

        file_size = uploaded_file.size / 1024

        col1, col2 = st.columns(2)

        with col1:
            st.write("**File Name:**", uploaded_file.name)
            st.write("**File Type:**", uploaded_file.type)

        with col2:
            st.write(f"**File Size:** {file_size:.2f} KB")
            st.write("**Saved Location:**", os.path.abspath(file_path))

        st.divider()

        st.info("The document has been saved successfully and is ready for processing.")
        # Extract PDF text
        if uploaded_file.name.endswith(".pdf"):

            st.divider()

            st.subheader("📖 Extracted Text")

            extracted_text = extract_pdf_text(file_path)

            st.text_area(
                "PDF Content",
                extracted_text,
                height=400
            )

# -----------------------------
# About Page
# -----------------------------
else:

    st.title("ℹ️ About")

    st.info("""
### AI Document Intelligence

**Version:** 1.0

Built with:

- 🐍 Python
- 🎈 Streamlit
- 🤖 Gemini AI
- 👁 OCR
- 🧠 NLP
""")