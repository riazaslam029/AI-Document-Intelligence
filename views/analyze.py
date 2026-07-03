import os
import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.pdf_loader import extract_pdf_text
from utils.docx_loader import extract_docx_text

from services.summarizer import summarize_text
from services.qa import ask_document
from services.flashcards import generate_flashcards
from services.mcq import generate_mcqs
from services.keywords import extract_keywords
from services.translator import translate_document
from services.ocr_service import process_image


def show():


    st.title("Analyze Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF, Word document, or image",
        type=["pdf", "docx", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        st.success("Document uploaded successfully.")

      
        # File Information

        st.subheader("File Information")

        file_size = uploaded_file.size / 1024

        col1, col2 = st.columns(2)

        with col1:
            st.write("**File Name:**", uploaded_file.name)
            st.write("**File Type:**", uploaded_file.type)

        with col2:
            st.write(f"**File Size:** {file_size:.2f} KB")
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

            with st.spinner("Extracting text from image..."):

                extracted_text = process_image(file_path)

        else:
            extracted_text = ""

        if uploaded_file.name.lower().endswith((".png", ".jpg", ".jpeg")):

            st.image(
                uploaded_file,
                caption="Uploaded Image",
                use_container_width=True
            )

            

        # Continue only if text was extracted
        if extracted_text:

            st.subheader("Extracted Text")

            st.text_area(
                "Document Content",
                extracted_text,
                height=350
            )

            from services.rag import (
                split_document,
                build_vector_store,
                rag_answer,
            )

            if "vector_index" not in st.session_state:

                chunks = split_document(extracted_text)

                index, chunks = build_vector_store(chunks)

                st.session_state.vector_index = index
                st.session_state.document_chunks = chunks
            

            else:
                index = st.session_state.vector_index
                chunks = st.session_state.document_chunks

            # Document Statistics
            
            word_count = len(extracted_text.split())
            char_count = len(extracted_text)

            st.subheader("Document Statistics")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Words", word_count)

            with col2:
                st.metric("Characters", char_count)

            st.divider()
                        
            # AI Workspace
            

            st.header("Workspace")

            (
                summary_tab,
                qa_tab,
                flashcard_tab,
                mcq_tab,
                keyword_tab,
                translation_tab
            ) = st.tabs([
                "Summary",
                "Ask Questions",
                "Flashcards",
                "MCQs",
                "Keywords",
                "Translation"
            ])

            # SUMMARY

            from utils.ui_helpers import show_ai_result

            show_ai_result(
                button_label="Generate Summary",
                spinner_text="Generating summary...",
                callback=summarize_text,
                text=extracted_text,
                download_name="summary.md",
                key="summary",
            )

            
            # ASK QUESTIONS

            with qa_tab:

                question = st.text_input(
                    "Ask a question about the document",
                    key="question_input"
                )

                if st.button(
                    "Ask",
                    key="ask_btn",
                    use_container_width=True
                ):

                    if question.strip():

                        with st.spinner("Finding answer..."):

                            from services.rag import rag_answer

                            answer = rag_answer(
                                question,
                                index,
                                chunks
                            )
                        st.success("Answer")

                        st.markdown(answer)

                    else:

                        st.warning("Please enter a question.")

            # FLASHCARDS

            show_ai_result(
                button_label="Generate Flashcards",
                spinner_text="Generating flashcards...",
                callback=generate_flashcards,
                text=extracted_text,
                download_name="flashcards.md",
                key="flashcards",
            )

            # MCQs

            show_ai_result(
                button_label="Generate MCQs",
                spinner_text="Generating MCQs...",
                callback=generate_mcqs,
                text=extracted_text,
                download_name="mcqs.md",
                key="mcqs",
            )

            # KEYWORDS

            show_ai_result(
                button_label="Extract Keywords",
                spinner_text="Extracting keywords...",
                callback=extract_keywords,
                text=extracted_text,
                download_name="keywords.md",
                key="keywords",
            )

            # TRANSLATION

            with translation_tab:

                language = st.selectbox(
                    "Translate to",
                    [
                        "Urdu",
                        "English",
                        "Arabic",
                        "French",
                        "German",
                        "Spanish"
                    ]
                )

                if st.button(
                    "Translate",
                    key="translate_btn",
                    use_container_width=True
                ):

                    with st.spinner("Translating..."):

                        translated_text = translate_document(
                            extracted_text,
                            language
                        )

                    st.success("Translation completed.")

                    st.markdown(translated_text)

                    st.download_button(
                        "Download Translation",
                        translated_text,
                        file_name="translation.md",
                        mime="text/markdown",
                        key="download_translation",
                        use_container_width=True
                    )

                else:

                    st.error(
                        "No readable text could be extracted from this document."
                    )