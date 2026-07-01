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

### 🚀 Current Features

- 📄 PDF Upload
- 📖 PDF Text Extraction
- 🤖 AI Summarization
- 📊 Document Statistics
- 📥 Download AI Summary

### 🔜 Upcoming Features

- 💬 Ask Questions
- 🧠 Flashcards
- ✅ MCQ Generator
- 🔑 Keyword Extraction
- 🌍 Translation
- 📝 DOCX Reader
- 🖼 Image OCR
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

        # -------------------------------------------------
        # Save Uploaded File
        # -------------------------------------------------
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

            # ---------------------------------------------
            # Extracted Text
            # ---------------------------------------------
            st.subheader("📖 Extracted Text")

            st.text_area(
                "PDF Content",
                extracted_text,
                height=350
            )

            # ---------------------------------------------
            # Document Statistics
            # ---------------------------------------------
            st.subheader("📊 Document Statistics")

            word_count = len(extracted_text.split())
            char_count = len(extracted_text)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📝 Words", word_count)

            with col2:
                st.metric("🔤 Characters", char_count)

            st.divider()

            # =============================================
            # AI Workspace
            # =============================================
            st.subheader("🤖 AI Workspace")

            summary_tab, ask_tab, flashcards_tab, mcq_tab, keywords_tab, translate_tab = st.tabs([
                "📑 Summary",
                "❓ Ask AI",
                "🧠 Flashcards",
                "✅ MCQs",
                "🔑 Keywords",
                "🌍 Translate"
            ])

            # =============================================
            # Summary Tab
            # =============================================
            with summary_tab:

                st.write("Generate an AI summary of your document.")

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

            # =============================================
            # Ask AI
            # =============================================
            with ask_tab:

                st.info("🚧 Coming Soon")

            # =============================================
            # Flashcards
            # =============================================
            with flashcards_tab:

                st.info("🚧 Coming Soon")

            # =============================================
            # MCQs
            # =============================================
            with mcq_tab:

                st.info("🚧 Coming Soon")

            # =============================================
            # Keywords
            # =============================================
            with keywords_tab:

                st.info("🚧 Coming Soon")

            # =============================================
            # Translation
            # =============================================
            with translate_tab:

                st.info("🚧 Coming Soon")

        else:

            st.info("🚀 DOCX and Image processing will be added in upcoming milestones.")

# =====================================================
# About Page
# =====================================================
else:

    st.title("ℹ️ About")

    st.markdown("""
## 📄 AI Document Intelligence

**Version:** 1.0

### 🛠 Technologies Used

- 🐍 Python
- 🎈 Streamlit
- 🤖 Google Gemini AI
- 📄 PyMuPDF
- 👁 OCR *(Upcoming)*
- 🧠 Natural Language Processing

### 👨‍💻 Developer

**Riaz Aslam**

Software Engineering Student | Python Developer | AI Enthusiast

---

This project is being developed step by step with a focus on clean architecture, modular code, and modern AI capabilities.
""")