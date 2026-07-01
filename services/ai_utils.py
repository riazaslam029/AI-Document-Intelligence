import time


def generate_with_retry(client, model, prompt, max_retries=3):
    """
    Generate AI content with retry logic and user-friendly error messages.
    """

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if hasattr(response, "text") and response.text:
                return response.text

            return "⚠️ No response was generated."

        except Exception as e:

            error = str(e)

            # Daily quota exceeded
            if "429" in error or "RESOURCE_EXHAUSTED" in error:
                return (
                    "⚠️ Gemini API daily quota has been reached.\n\n"
                    "Please try again later or use another API key."
                )

            # Gemini temporarily busy
            if "503" in error or "UNAVAILABLE" in error:

                if attempt < max_retries - 1:
                    time.sleep((attempt + 1) * 5)
                    continue

                return (
                    "⚠️ Gemini servers are currently busy.\n\n"
                    "Please try again in a few moments."
                )

            # Timeout
            if "timeout" in error.lower():
                return (
                    "⚠️ Request timed out.\n"
                    "Please try again."
                )

            # Internet issues
            if "connection" in error.lower():
                return (
                    "⚠️ Internet connection problem."
                )

            # Any other error
            return f"❌ {error}"