import streamlit as st


def show():

    st.title("📄 Document Intelligence Suite")

    st.write(
        """
Document Intelligence Suite helps you analyze PDF, Word, and image documents
using modern AI tools. Upload your document to generate summaries, answer
questions, create study material, extract key information, and translate
content—all from a single interface.
"""
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📂 Supported Documents")

        st.markdown(
            """
- PDF (.pdf)
- Microsoft Word (.docx)
- Images (.png, .jpg, .jpeg)
"""
        )

    with col2:

        st.subheader("🤖 AI Features")

        st.markdown(
            """
- Document Summarization
- Question Answering
- Flashcard Generation
- Multiple Choice Questions (MCQs)
- Keyword Extraction
- Document Translation
- Image Text Extraction (OCR)
"""
        )

    st.divider()

    st.subheader("🚀 Getting Started")

    st.markdown(
        """
1. Open the **Analyze Document** page.
2. Upload a supported PDF, Word document, or image.
3. Review the extracted text.
4. Choose any AI tool to analyze the document.
5. Download the generated results when finished.
"""
    )

    st.divider()

    st.subheader("💡 Tips")

    st.info(
        """
• Larger documents may take slightly longer to process.

• For the best OCR results, upload clear, high-resolution images.

• AI-generated responses may vary depending on document content.
"""
    )

    st.divider()

    st.caption(
        "Version 1.0 • Built with Python, Streamlit and Google Gemini"
    )