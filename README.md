# AI Document Intelligence

<div align="center">

**Analyze, understand, and transform documents with AI.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://ai-document-intelligence-fsomujrral6fehfzc7ue.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)

</div>

AI Document Intelligence is a Streamlit application for extracting and understanding content from PDFs, Word documents, and images. It combines OCR and Google Gemini to provide practical tools for summarization, question answering, study material generation, keyword extraction, and translation.

## ✨ Features

| Capability | Description |
| --- | --- |
| 📄 Multi-format input | Process PDF, DOCX, PNG, JPG, and JPEG files |
| 🧾 Text extraction | Extract text from digital documents and images with OCR |
| 📝 Summarization | Create concise summaries of uploaded documents |
| 💬 Question answering | Ask questions and receive answers grounded in document content |
| 🧠 Study tools | Generate flashcards and multiple-choice questions |
| 🔑 Keyword extraction | Identify important terms and concepts |
| 🌍 Translation | Translate extracted document content into other languages |
| 📊 Document insights | Review extracted text and basic document statistics |
| ⬇️ Export | Download generated results for later use |

## 🚀 Try the live application

Use the hosted application without installing anything:

**[Open AI Document Intelligence](https://ai-document-intelligence-fsomujrral6fehfzc7ue.streamlit.app/)**

You will need a Google Gemini API key. The key is entered in the application and used only for the current session; it is not stored in this repository.

## 🛠️ Technology stack

| Layer | Technology |
| --- | --- |
| Application | Python and Streamlit |
| Generative AI | Google Gemini 2.5 Flash via `google-genai` |
| OCR | EasyOCR and OpenCV |
| PDF processing | PyMuPDF |
| Word processing | `python-docx` |
| Image processing | Pillow |
| Data and utilities | NumPy, pandas, scikit-image, python-dotenv |

## ⚙️ Run locally

### Prerequisites

- Python 3.10 or newer
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Installation

```bash
git clone https://github.com/riazaslam029/AI-Document-Intelligence.git
cd AI-Document-Intelligence

python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and start Streamlit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown by Streamlit, enter your Gemini API key in the sidebar, and upload a supported document.

## 🧭 How it works

1. Upload a PDF, DOCX, or image.
2. The application extracts text using the appropriate document loader or OCR pipeline.
3. Select an analysis tool such as summary, Q&A, flashcards, MCQs, keywords, or translation.
4. Review the generated result and download it when needed.

## 📁 Project structure

```text
AI-Document-Intelligence/
├── app.py                    # Streamlit entry point
├── requirements.txt          # Python dependencies
├── services/                 # AI-powered analysis services
│   ├── flashcards.py
│   ├── gemini_client.py
│   ├── keywords.py
│   ├── mcq.py
│   ├── ocr_service.py
│   ├── qa.py
│   ├── summarizer.py
│   └── translator.py
├── utils/                    # File loading, OCR, and UI helpers
└── views/                    # Home, analysis, and about pages
```

## 🔐 Security and privacy

- Never commit API keys or other secrets.
- API keys should be entered through the application sidebar or supplied through a secure deployment configuration.
- Uploaded documents are used for the current analysis workflow and should not contain sensitive information unless your deployment and provider policies allow it.

## 🗺️ Roadmap

- Chat with documents
- Retrieval-augmented generation (RAG)
- Semantic search
- PDF and DOCX result exports
- Additional file formats and language support
- AI-powered insights dashboard

## 🤝 Contributing

Contributions, suggestions, and issue reports are welcome. Before opening a pull request:

1. Create a focused branch from `main`.
2. Keep changes scoped and document user-facing behavior.
3. Run the relevant tests before submitting.
4. Include a clear description of the problem and solution.

## 👨‍💻 Maintainer

**Riaz Aslam** — Software Engineering Student

- GitHub: [@riazaslam029](https://github.com/riazaslam029)
- LinkedIn: [Riaz Aslam](https://www.linkedin.com/in/riaz-aslam-0bb69b310/)

## 📄 License

This project is released under the [MIT License](LICENSE).

If you find the project useful, consider giving it a ⭐ on GitHub.
