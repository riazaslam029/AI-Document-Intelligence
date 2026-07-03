import time


def generate_with_retry(client, model, prompt, retries=3):
    """
    Retry Gemini requests automatically if the service is temporarily unavailable.
    """

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text

        except Exception as e:

            if "503" in str(e) and attempt < retries - 1:

                time.sleep(5)

            else:

                raise

    return "⚠️ Gemini is currently busy. Please try again in a few moments."