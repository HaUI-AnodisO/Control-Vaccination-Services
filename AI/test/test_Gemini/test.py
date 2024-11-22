import os

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

# Used to securely store your API key
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
    generation_config=generation_config)

import PIL.Image

img2 = PIL.Image.open("nhap-canh-trai-phep-con-ca-gan-dung-chung-minh-thu-gia-cong-dan-viet-nam.jpg")
prompt_file_path = "prompt.txt"
with open(prompt_file_path, "r", encoding="utf-8") as file:
    prompt_content = file.read()
response = model.generate_content(
    [
        prompt_content,
        img2,
    ],
    stream=True,
)
response.resolve()

to_markdown(response.text)

print('candidates',response.candidates)

print('response', response)

import json

response_text = response.text
print(response_text)

# Ghi dữ liệu thô vào file output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(response_text)

# Hàm chuyển đổi chuỗi đầu vào sang định dạng JSON
def parse_string_to_json(input_string):
    # Tách các thông tin dựa trên định dạng (giả sử các thông tin được phân cách bởi dấu xuống dòng hoặc dấu phân cách nào đó)
    lines = input_string.split("\n")
    
    # Tạo một từ điển để lưu thông tin
    data = {
        "full_name": lines[0].strip() if len(lines) > 0 else "",
        "date_of_birth": lines[1].strip() if len(lines) > 1 else "",
        "id_card_number": lines[2].strip() if len(lines) > 2 else "",
        "gender": lines[3].strip() if len(lines) > 3 else "",
        "address": lines[4].strip() if len(lines) > 4 else "",
    }
    
    # Chuyển đổi sang chuỗi JSON
    return data

# Chuyển đổi chuỗi đầu vào thành JSON
input_string = response_text
json_data = parse_string_to_json(input_string)

# Ghi dữ liệu JSON vào file output.json
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được lưu vào file output.json")
