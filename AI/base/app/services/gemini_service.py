import os
import textwrap
from PIL import Image
import google.generativeai as genai
from app.core.config import generation_config
from parsing_service import parse_string_to_json
# Cấu hình Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Utility để format văn bản thành Markdown
def to_markdown(text: str) -> str:
    return textwrap.indent(text.replace("\u2022", "  *"), "> ", predicate=lambda _: True)

# Đọc nội dung từ file prompt.txt
def load_prompt() -> str:
    with open("app/data/prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

# Tạo nội dung với Gemini
def generate_content(prompt: str, image_path: str) -> dict:
    try:
        img2 = Image.open(image_path)

        # Sinh nội dung từ API Gemini
        response = model.generate_content([prompt, img2], stream=True)
        response.resolve()

        # Trả về dữ liệu
        response_text = response.text

        return {
            "raw_text": response_text,
            "markdown": to_markdown(response_text),
            "json_data": parse_string_to_json(response_text)
        }
    except Exception as e:
        raise RuntimeError(f"Error generating content: {str(e)}")
