import os

UPLOAD_FOLDER = "uploads"

def save_uploaded_file(uploaded_file):
    """
    Save the uploaded file to the uploads folder.
    """

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path