import os
import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.pdf_loader import extract_pdf_text
from services.summarizer import summarize_text

# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# Sidebar
# =====================================================
st.sidebar.title("📚 AI Document Intelligence")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📤 Upload Document",
        "ℹ️ About"
    ]
)

# =====================================================
# Home Page
# =====================================================
if menu == "🏠 Home":

    st.title("📄 AI Document Intelligence Suite")

    st.markdown("""
Welcome to **AI Document Intelligence Suite**.

Analyze documents using the power of **Google Gemini AI**.

### 🚀 Features

- 📄 PDF Reader
- 📝 DOCX Reader *(Coming Soon)*
- 🖼 Image OCR *(Coming Soon)*
- 🤖 AI Summarization
- 💬 Ask Questions *(Coming Soon)*
- 🧠 Flashcards *(Coming Soon)*
- ✅ MCQ Generator *(Coming Soon)*
- 🌍 Translation *(Coming Soon)*
- 🔑 Keyword Extraction *(Coming Soon)*
""")

# =====================================================
# Upload Page
# =====================================================
elif menu == "📤 Upload Document":

    st.title("📤 Upload Document")

    st.write("Upload a PDF, DOCX, or Image file.")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "docx", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        st.success("✅ File uploaded successfully!")

        # -------------------------------------------------
        # File Information
        # -------------------------------------------------
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

        # -------------------------------------------------
        # PDF Processing
        # -------------------------------------------------
        if uploaded_file.name.lower().endswith(".pdf"):

            extracted_text = extract_pdf_text(file_path)

            st.subheader("📖 Extracted Text")

            st.text_area(
                "PDF Content",
                extracted_text,
                height=350
            )

            # ---------------------------------------------
            # Document Statistics
            # ---------------------------------------------
            word_count = len(extracted_text.split())
            char_count = len(extracted_text)

            st.subheader("📊 Document Statistics")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📝 Words", word_count)

            with col2:
                st.metric("🔤 Characters", char_count)

            st.divider()

            # ---------------------------------------------
            # AI Summary
            # ---------------------------------------------
            st.subheader("🤖 AI Summary")

            if st.button(
                "📝 Generate AI Summary",
                use_container_width=True
            ):

                with st.spinner("🤖 Gemini is analyzing your document..."):

                    try:

                        summary = summarize_text(extracted_text)

                        st.success("✅ Summary Generated Successfully!")

                        st.markdown(summary)

                        st.download_button(
                            label="📥 Download Summary",
                            data=summary,
                            file_name="summary.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    except Exception as e:

                        st.error(f"❌ {e}")

        else:
            st.info("🚀 DOCX and Image processing will be added in the next milestones.")

# =====================================================
# About Page
# =====================================================
else:

    st.title("ℹ️ About")

    st.markdown("""
## AI Document Intelligence

**Version:** 1.0

### 🛠 Built With

- 🐍 Python
- 🎈 Streamlit
- 🤖 Google Gemini AI
- 📄 PyMuPDF
- 👁 OCR (Upcoming)
- 🧠 NLP

### 👨‍💻 Developer

**Riaz Aslam**

Software Engineering Student | AI & Python Developer
""")