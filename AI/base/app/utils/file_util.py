import os
from fastapi import UploadFile
from pathlib import Path

# Utility để lưu ảnh tạm thời
def save_temp_image(image: UploadFile, temp_dir: str = 'app/temp/') -> str:
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, f"temp_{image.filename}")
    with open(file_path, "wb") as temp_file:
        temp_file.write(image.file.read())
    return file_path

# Utility để xóa ảnh tạm sau khi xử lý xong
def delete_temp_image(file_path: str) -> None:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting temporary file {file_path}: {str(e)}")
