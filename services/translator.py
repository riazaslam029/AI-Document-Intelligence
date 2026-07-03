from services.gemini_client import get_client
from services.ai_utils import generate_with_retry


def translate_document(text, language):
    """
    Translate the uploaded document into the selected language.
    """

    client = get_client()

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