from services.gemini_client import get_client
from services.ai_utils import generate_with_retry


def ask_document(document_text, question):
    """
    Answer questions using only the uploaded document.
    """

    client = get_client()

    prompt = f"""
You are an intelligent document assistant.

Answer ONLY using the uploaded document.

Rules:
- Do not make up information.
- If the answer is not present in the document, reply:
  "I couldn't find this information in the document."
- Keep the answer clear and concise.

Document:

{document_text}

Question:

{question}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
    )