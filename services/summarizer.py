import os
import time

from dotenv import load_dotenv
from google import genai

from services.ai_utils import generate_with_retry

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text):
    """
    Generate an AI summary of the uploaded document.
    """

    # Limit very large documents to reduce API load
    text = text[:12000]

    prompt = f"""
You are an expert document analyst.

Summarize the following document.

Instructions:
- Use clear headings.
- Use bullet points where appropriate.
- Keep only the important information.
- Make the summary easy to understand.
- Do not add information that is not present in the document.

Document:

{text}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
)

