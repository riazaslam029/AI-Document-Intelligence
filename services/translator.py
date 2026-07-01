import os

from dotenv import load_dotenv
from google import genai

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text