import easyocr

reader = easyocr.Reader(["en"])


def extract_image_text(image_path):
    """
    Extract text from an image using EasyOCR.
    """

    results = reader.readtext(image_path)

    text = "\n".join([item[1] for item in results])

    return text