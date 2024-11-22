from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Dict
import os
import textwrap
import google.generativeai as genai
import PIL.Image

# Configure Gemini API
os.environ["GEMINI_API_KEY"] = 'AIzaSyDPwsWtk_tcdP6vNQZV0GH4NeaTUi7SsZY'
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

with open('prompt.txt', "r", encoding="utf-8") as file:
    prompt_content = file.read()
# Initialize FastAPI app
app = FastAPI()

def to_markdown(text):
    return textwrap.indent(text.replace("\u2022", "  *"), "> ", predicate=lambda _: True)

# Parse string to JSON
def parse_string_to_json(input_string: str) -> Dict:
    lines = input_string.split("\n")
    return {
        "full_name": lines[0].strip() if len(lines) > 0 else "",
        "date_of_birth": lines[1].strip() if len(lines) > 1 else "",
        "id_card_number": lines[2].strip() if len(lines) > 2 else "",
        "gender": lines[3].strip() if len(lines) > 3 else "",
        "address": lines[4].strip() if len(lines) > 4 else "",
    }

@app.post("/generate-content")
async def generate_content(prompt: str = prompt_content, image: UploadFile = File(...)):
    try:
        # Save uploaded image temporarily
        temp_image_path = f"temp_{image.filename}"
        with open(temp_image_path, "wb") as temp_file:
            temp_file.write(await image.read())

        # Open image
        img2 = PIL.Image.open(temp_image_path)

        # Generate content
        response = model.generate_content([prompt, img2], stream=True)
        response.resolve()

        # Process response
        response_text = response.text

        # Clean up temporary file
        os.remove(temp_image_path)

        return {
            "raw_text": response_text,
            "markdown": to_markdown(response_text),
            "json_data": parse_string_to_json(response_text)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

