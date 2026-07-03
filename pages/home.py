import streamlit as st


def show():

    st.title("📄 Document Intelligence Suite")

    st.write("""
Analyze PDF and Word documents using Google's Gemini AI.

Upload a document to:

- Generate concise summaries
- Ask questions about the content
- Create flashcards
- Generate multiple-choice questions
- Extract keywords
- Translate documents
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Supported Documents")

        st.markdown("""
- PDF (.pdf)
- Microsoft Word (.docx)
""")

    with col2:

        st.subheader("Available Features")

        st.markdown("""
- Document Summary
- Question Answering
- Flashcards
- MCQ Generator
- Keyword Extraction
- Translation
""")

    st.info(
        "OCR and Chat with Document (RAG) will be available in upcoming versions."
    )