from fastapi import Depends
from app.services.gemini_service import load_prompt

# Dependency để lấy nội dung từ prompt.txt
def get_prompt_content() -> str:
    return load_prompt()
