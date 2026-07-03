




def extract_image_text(image_path):
    """
    Extract text from an image using EasyOCR.
    """
    import easyocr
    reader = easyocr.Reader(["en"])
    results = reader.readtext(image_path)

    text = "\n".join([item[1] for item in results])

    return text