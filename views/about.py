import streamlit as st


def show():

    st.title("About")

    st.markdown(
        """
# 📄 Document Intelligence Suite

Document Intelligence Suite is a Python application designed to simplify document analysis using modern AI tools. It supports PDF, Word, and image documents, allowing users to extract text and generate useful insights from uploaded files.

---

## ✨ Key Features

- 📄 PDF document support
- 📝 DOCX document support
- 🖼 Image text extraction (OCR)
- 📑 Document summarization
- ❓ Question answering
- 🧠 Flashcard generation
- ✅ Multiple-choice question generation
- 🔑 Keyword extraction
- 🌐 Document translation
- 📥 Download generated results

---

## 🛠 Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyMuPDF
- python-docx
- EasyOCR
- Pillow
- python-dotenv

---

## 📂 Project Structure

The application follows a modular structure to keep the code organized and easy to maintain.

- **views/** – User interface pages
- **services/** – AI and document processing logic
- **utils/** – File handling and helper functions
- **uploads/** – Uploaded documents

---

## 🚀 Future Improvements

Planned enhancements include:

- Chat with documents
- Retrieval-Augmented Generation (RAG)
- Export results as PDF
- Export results as DOCX
- Support for additional document formats

---

## 👨‍💻 Developer

**Riaz Aslam**

Software Engineering Student

GitHub:
https://github.com/riazaslam029

---

Thank you for exploring Document Intelligence Suite.
"""
    )

    st.divider()

    st.caption("Version 1.0")