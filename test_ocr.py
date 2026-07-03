from services.ocr_service import process_image

image_path = "/home/riaz/Pictures/Screenshots/12.png"   # Replace with the path to any image that contains text

text = process_image(image_path)

print(text)