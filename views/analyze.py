import os
import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.pdf_loader import extract_pdf_text
from utils.docx_loader import extract_docx_text
from utils.ui_helpers import show_ai_result

from services.summarizer import summarize_text
from services.qa import ask_document
from services.flashcards import generate_flashcards
from services.mcq import generate_mcqs
from services.keywords import extract_keywords
from services.translator import translate_document


def show():

    st.title("📂 Analyze Document")

    st.write(
        """
Upload a PDF, Word document, or image to extract text and analyze it using the available AI tools.
"""
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "docx", "png", "jpg", "jpeg"],
    )

    if uploaded_file is None:
        return

    file_path = save_uploaded_file(uploaded_file)

    st.success("Document uploaded successfully.")

    # File Information

    with st.container():

        st.subheader("📄 File Information")

        file_size = uploaded_file.size / 1024

        col1, col2 = st.columns(2)

        with col1:
            st.write("**File Name:**", uploaded_file.name)
            st.write("**File Type:**", uploaded_file.type)

        with col2:
            st.write(f"**File Size:** {file_size:.2f} KB ")
            st.write("**Saved Location:**", os.path.abspath(file_path))

    st.divider()

    # Extract Text

    if uploaded_file.name.lower().endswith(".pdf"):

        extracted_text = extract_pdf_text(file_path)

    elif uploaded_file.name.lower().endswith(".docx"):

        extracted_text = extract_docx_text(file_path)

    elif uploaded_file.name.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True,
        )
        from services.ocr_service import process_image
        with st.spinner("Extracting text from image..."):

            extracted_text = process_image(file_path)

    else:

        extracted_text = ""

    if not extracted_text:

        st.error("No readable text could be extracted from this document.")

        return

    # Statistics

    word_count = len(extracted_text.split())
    char_count = len(extracted_text)

    st.subheader("📊 Document Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Words", word_count)

    with col2:
        st.metric("Characters", char_count)

    st.divider()

    # Extracted Text

    st.subheader("📖 Extracted Text")

    with st.expander(
        "View Extracted Text",
        expanded=False,
    ):

        st.text_area(
            "Document Content",
            extracted_text,
            height=350,
        )

    st.divider()

    # AI Workspace

    st.header("🤖 AI Workspace")

    st.caption(
        "Choose one of the tools below to analyze your document."
    )

    (
        summary_tab,
        qa_tab,
        flashcard_tab,
        mcq_tab,
        keyword_tab,
        translation_tab,
    ) = st.tabs(
        [
            "Summary",
            "Ask Questions",
            "Flashcards",
            "MCQs",
            "Keywords",
            "Translation",
        ]
    )

    # Summary

    with summary_tab:

        st.write(
            "Generate a concise summary of the uploaded document."
        )

        show_ai_result(
            button_label="Generate Summary",
            spinner_text="Generating summary...",
            callback=summarize_text,
            text=extracted_text,
            download_name="summary.md",
            key="summary",
        )

    # Question Answering

    with qa_tab:

        st.write(
            "Ask questions about the uploaded document."
        )

        question = st.text_input(
            "Enter your question",
            placeholder="Example: What is the main idea of this document?",
            key="question_input",
        )

        if st.button(
            "Get Answer",
            key="ask_btn",
            use_container_width=True,
        ):

            if question.strip():

                with st.spinner("Searching for the answer..."):

                    # Verify the parameter order in services/qa.py
                    answer = ask_document(
                        question,
                        extracted_text,
                    )

                st.success("Answer generated successfully.")

                st.markdown(answer)

            else:

                st.warning("Please enter a question.")

    # Flashcards

    with flashcard_tab:

        st.write(
            "Generate study flashcards from the document."
        )

        show_ai_result(
            button_label="Generate Flashcards",
            spinner_text="Generating flashcards...",
            callback=generate_flashcards,
            text=extracted_text,
            download_name="flashcards.md",
            key="flashcards",
        )

    # MCQs

    with mcq_tab:

        st.write(
            "Generate multiple-choice questions from the document."
        )

        show_ai_result(
            button_label="Generate MCQs",
            spinner_text="Generating MCQs...",
            callback=generate_mcqs,
            text=extracted_text,
            download_name="mcqs.md",
            key="mcqs",
        )

    # Keywords

    with keyword_tab:

        st.write(
            "Extract the most important keywords from the document."
        )

        show_ai_result(
            button_label="Extract Keywords",
            spinner_text="Extracting keywords...",
            callback=extract_keywords,
            text=extracted_text,
            download_name="keywords.md",
            key="keywords",
        )

    # Translation

    with translation_tab:

        st.write(
            "Translate the extracted text into another language."
        )

        language = st.selectbox(
            "Translate to",
            [
                "Urdu",
                "English",
                "Arabic",
                "French",
                "German",
                "Spanish",
            ],
        )

        if st.button(
            "Translate Document",
            key="translate_btn",
            use_container_width=True,
        ):

            with st.spinner("Translating document..."):

                translated_text = translate_document(
                    extracted_text,
                    language,
                )

            st.success("Translation completed successfully.")

            st.markdown(translated_text)

            st.download_button(
                "Download Translation",
                translated_text,
                file_name="translation.md",
                mime="text/markdown",
                use_container_width=True,
            )

    st.divider()

    st.caption(
        "Document Intelligence Suite • Version 1.0"
    )