from services.gemini_client import get_client
from services.ai_utils import generate_with_retry


def extract_keywords(text):
    """
    Extract the most important keywords from the uploaded document.
    """

    client = get_client()

    prompt = f"""
You are an NLP expert.

Extract the 15 most important keywords from the following document.

Rules:

- Return only the keywords.
- One keyword per line.
- Do not number them.
- Do not explain anything.
- Avoid duplicate keywords.

Document:

{text}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
    )