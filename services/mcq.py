import os

from dotenv import load_dotenv
from google import genai

from services.ai_utils import generate_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_mcqs(text):

    prompt = f"""
You are an expert teacher.

Create 10 multiple-choice questions from the document.

Rules:

- Each question must have four options.
- Mention the correct answer.
- Give a one-line explanation.
- Use Markdown formatting.

Example:

## Question 1

What is AI?

A) ...

B) ...

C) ...

D) ...

✅ Correct Answer:
B

Explanation:
...

Document:

{text}
"""

    return generate_with_retry(
        client,
        "gemini-2.5-flash",
        prompt
    )