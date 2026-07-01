import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text):
    """
    Generate an AI summary for the given text.
    """

    prompt = f"""
You are an expert document summarizer.

Summarize the following document.

Requirements:
- Easy to understand
- Professional
- Around 150–200 words
- Preserve important points

Document:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text