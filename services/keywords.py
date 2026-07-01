import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_keywords(text):

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text