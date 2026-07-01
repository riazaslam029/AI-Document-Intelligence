import os

from dotenv import load_dotenv
from google import genai

from services.ai_utils import generate_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_flashcards(text):
    """
    Generate flashcards from the uploaded document.
    """

    prompt = f"""
You are an expert teacher.

Create 10 study flashcards from the document.

Rules:

- Question first
- Answer below it
- Keep answers concise
- Use Markdown formatting

Example:

### Question 1
What is Artificial Intelligence?

**Answer**

Artificial Intelligence is the simulation of human intelligence by machines.

Document:

{text}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
)