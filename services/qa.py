import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_document(document_text, question):

    prompt = f"""
Answer ONLY using the uploaded document.

Document:
{document_text}

Question:
{question}
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            if "503" in str(e):

                time.sleep(5)

            else:

                raise

    return "⚠️ Gemini is currently busy. Please try again in a few moments."