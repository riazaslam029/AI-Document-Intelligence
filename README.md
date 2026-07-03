# 📄 Document Intelligence Suite

Document Intelligence Suite is a Python-based web application that helps users analyze PDF, Word, and image documents using Google Gemini AI. The application extracts text from uploaded documents and provides multiple AI-powered tools to summarize, understand, and study the content.

---

## Features

- 📄 PDF document support
- 📝 Microsoft Word (.docx) support
- 🖼 Image OCR (PNG, JPG, JPEG)
- 📑 AI-powered document summarization
- ❓ Question answering based on document content
- 🧠 Flashcard generation
- ✅ Multiple Choice Question (MCQ) generation
- 🔑 Keyword extraction
- 🌐 Document translation
- 📥 Download generated results

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyMuPDF
- python-docx
- EasyOCR
- Pillow
- python-dotenv

---

## Project Structure

```
AI-Document-Intelligence/
│
├── services/
│   ├── summarizer.py
│   ├── qa.py
│   ├── flashcards.py
│   ├── mcq.py
│   ├── keywords.py
│   ├── translator.py
│   └── ocr_service.py
│
├── utils/
│   ├── file_handler.py
│   ├── pdf_loader.py
│   ├── docx_loader.py
│   └── ui_helpers.py
│
├── views/
│   ├── home.py
│   ├── analyze.py
│   └── about.py
│
├── uploads/
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/riazaslam029/AI-Document-Intelligence.git
```

Move into the project directory

```bash
cd AI-Document-Intelligence
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Open the application.
2. Navigate to **Analyze Document**.
3. Upload a PDF, DOCX, or image.
4. Review the extracted text.
5. Use any AI tool to analyze the document.
6. Download the generated results if needed.

---

## Screenshots

> Add screenshots after deployment.

Example:

```
assets/
└── screenshots/
    ├── home.png
    ├── analyze.png
    ├── summary.png
    └── translation.png
```

---

## Future Improvements

- Chat with documents
- Retrieval-Augmented Generation (RAG)
- Export results as PDF
- Export results as DOCX
- Additional document formats
- Improved OCR accuracy

---

## Developer

**Riaz Aslam**

Software Engineering Student

GitHub

https://github.com/riazaslam029

LinkedIn

https://www.linkedin.com/in/riaz-aslam-0bb69b310/

---

## License

This project is licensed under the MIT License.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
