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


def show():


    st.title("Analyze Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF or DOCX document",
        type=["pdf", "docx"]
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
        
        extracted_text = ""

        if uploaded_file.name.lower().endswith(".pdf"):

            extracted_text = extract_pdf_text(file_path)

        elif uploaded_file.name.lower().endswith(".docx"):

            extracted_text = extract_docx_text(file_path)

        # Continue only if text was extracted
        if extracted_text:

            st.subheader("Extracted Text")

            st.text_area(
                "Document Content",
                extracted_text,
                height=350
            )

            
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

            with summary_tab:

                st.write("Generate a concise summary of the document.")

                if st.button(
                    "Generate Summary",
                    key="summary_btn",
                    use_container_width=True
                ):

                    with st.spinner("Generating summary..."):

                        summary = summarize_text(extracted_text)

                    st.success("Summary generated successfully.")

                    st.markdown(summary)

                    st.download_button(
                        "Download Summary",
                        summary,
                        file_name="summary.md",
                        mime="text/markdown",
                        key="download_summary",
                        use_container_width=True
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

                            answer = ask_document(
                                extracted_text,
                                question
                            )

                        st.success("Answer")

                        st.markdown(answer)

                    else:

                        st.warning("Please enter a question.")

            # FLASHCARDS

            with flashcard_tab:

                st.write(
                    "Generate study flashcards from the document."
                )

                if st.button(
                    "Generate Flashcards",
                    key="flashcard_btn",
                    use_container_width=True
                ):

                    with st.spinner("Generating flashcards..."):

                        flashcards = generate_flashcards(
                            extracted_text
                        )

                    st.success("Flashcards generated.")

                    st.markdown(flashcards)

                    st.download_button(
                        "Download Flashcards",
                        flashcards,
                        file_name="flashcards.md",
                        mime="text/markdown",
                        key="download_flashcards",
                        use_container_width=True
                    )

            # MCQs

            with mcq_tab:

                st.write(
                    "Generate multiple-choice questions."
                )

                if st.button(
                    "Generate MCQs",
                    key="mcq_btn",
                    use_container_width=True
                ):

                    with st.spinner("Generating MCQs..."):

                        mcqs = generate_mcqs(
                            extracted_text
                        )

                    st.success("MCQs generated.")

                    st.markdown(mcqs)

                    st.download_button(
                        "Download MCQs",
                        mcqs,
                        file_name="mcqs.md",
                        mime="text/markdown",
                        key="download_mcqs",
                        use_container_width=True
                    )

            # KEYWORDS

            with keyword_tab:

                st.write(
                    "Extract important keywords from the document."
                )

                if st.button(
                    "Extract Keywords",
                    key="keyword_btn",
                    use_container_width=True
                ):

                    with st.spinner("Extracting keywords..."):

                        keywords = extract_keywords(
                            extracted_text
                        )

                    st.success("Keywords extracted.")

                    st.markdown(keywords)

                    st.download_button(
                        "Download Keywords",
                        keywords,
                        file_name="keywords.md",
                        mime="text/markdown",
                        key="download_keywords",
                        use_container_width=True
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