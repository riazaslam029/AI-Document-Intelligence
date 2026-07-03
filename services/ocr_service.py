from utils.ocr import extract_image_text


def process_image(image_path):
    """
    Process an uploaded image and return extracted text.
    """

    return extract_image_text(image_path)