import os

from dotenv import load_dotenv
from google import genai

from services.ai_utils import generate_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def translate_document(text, language):

    prompt = f"""
Translate the following document into {language}.

Rules:

- Preserve the original meaning.
- Keep formatting where possible.
- Do not explain anything.
- Return only the translated text.

Document:

{text}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
    )