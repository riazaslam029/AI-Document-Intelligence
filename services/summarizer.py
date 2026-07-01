import os
import time

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

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            if hasattr(response, "text") and response.text:
                return response.text

            return "⚠️ No summary was generated."

        except Exception as e:

            error_message = str(e)

            # Retry only if Gemini is temporarily unavailable
            if "503" in error_message:

                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 5
                    time.sleep(wait_time)
                    continue

                return (
                    "⚠️ Google Gemini is currently experiencing high demand.\n\n"
                    "Please wait a minute and try again."
                )

            # Return any other unexpected error
            return f"❌ Error: {error_message}"