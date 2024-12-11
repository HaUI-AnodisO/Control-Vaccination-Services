# Copyright 2024 HaUI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from fastapi import FastAPI, UploadFile, File, Form, APIRouter
from fastapi.responses import FileResponse
from digital_sig.utils import remove_background
from digital_sig.insert_stamp import insert_stamp
from digital_sig.sign_pdf import sign_pdf
from digital_sig.verify_pdf_signature import verify_pdf_signature
from digital_sig.make_dig_sig import create_rsa_keys, create_signature, verify_signature
app = APIRouter()

@app.post("/remove-background/")
async def api_remove_background(file: UploadFile = File(...)):
    """
    API để xử lý hình ảnh và loại bỏ nền.

    Args:
        file (UploadFile): Tệp hình ảnh để loại bỏ nền.

    Returns:
        dict: Đường dẫn đến tệp hình ảnh đã xử lý.
    """
    img_out_path = "output.png"
    with open("input.png", "wb") as buffer:
        buffer.write(file.file.read())
    result = remove_background("input.png", img_out_path)
    return {"filename": img_out_path}

@app.post("/insert-stamp/")
async def api_insert_stamp(pdf_file: UploadFile = File(...), stamp_file: UploadFile = File(...), x: int = 350, y: int = 500, page: int = 2):
    """
    API để chèn một con dấu vào một trang cụ thể của tệp PDF.

    Args:
        pdf_file (UploadFile): Tệp PDF.
        stamp_file (UploadFile): Tệp hình ảnh con dấu.
        x (int): Tọa độ x của vị trí con dấu.
        y (int): Tọa độ y của vị trí con dấu.
        page (int): Số trang cần chèn con dấu.

    Returns:
        dict/FileResponse: Tệp PDF đã chèn con dấu hoặc thông báo lỗi.
    """
    pdf_content = await pdf_file.read()
    stamp_content = await stamp_file.read()

    pdf_path = "input_pdf.pdf"
    stamp_path = "stamp.png"
    with open(pdf_path, "wb") as f:
        f.write(pdf_content)
    with open(stamp_path, "wb") as f:
        f.write(stamp_content)

    output_path = "stamped_output.pdf"

    try:
        insert_stamp(pdf_path, stamp_path, output_path, x, y, page)
    except Exception as e:
        return {"error": str(e)}

    if os.path.exists(output_path):
        return FileResponse(output_path, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename={output_path}"})
    else:
        return {"error": "Failed to create the stamped PDF."}

@app.post("/create-digital-signature/")
async def api_create_digital_signature(data: str = Form(...)):
    """
    API để tạo chữ ký số và xác minh chữ ký.

    Args:
        data (str): Dữ liệu cần ký.

    Returns:
        dict: Cặp khóa RSA, chữ ký số và kết quả xác minh.
    """
    private_key, public_key = create_rsa_keys()
    signature, hash_object = create_signature(data, private_key)
    is_valid = verify_signature(data, signature, public_key)

    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key)

    return {
        "private_key": private_key.decode('utf-8'),
        "public_key": public_key.decode('utf-8'),
        "signature": signature.hex(),
        "is_valid": is_valid
    }

@app.post("/sign-pdf/")
async def api_sign_pdf(pdf_file: UploadFile = File(...), private_key: UploadFile = File(...)):
    """
    API để ký một tệp PDF bằng chữ ký số.

    Args:
        pdf_file (UploadFile): Tệp PDF cần ký.
        private_key (UploadFile): Tệp chứa khóa riêng RSA để ký.

    Returns:
        dict: Thông báo về kết quả ký và vị trí lưu chữ ký.
    """
    pdf_path = "signed_pdf.pdf"
    private_key_path = "private.pem"
    signature_path = "signature.sig"
    with open(pdf_path, "wb") as buffer:
        buffer.write(pdf_file.file.read())
    with open(private_key_path, "wb") as buffer:
        buffer.write(private_key.file.read())
    sign_pdf(pdf_path, private_key_path, signature_path)
    return {"message": f"Chữ ký số được lưu tại: {signature_path}"}

@app.post("/verify-pdf-signature/")
async def api_verify_pdf_signature(pdf_file: UploadFile = File(...), signature: UploadFile = File(...), public_key: UploadFile = File(...)):
    """
    API để xác minh chữ ký số của một tệp PDF.

    Args:
        pdf_file (UploadFile): Tệp PDF đã được ký.
        signature (UploadFile): Tệp chữ ký cần xác minh.
        public_key (UploadFile): Tệp chứa khóa công RSA để xác minh chữ ký.

    Returns:
        dict: Thông báo kết quả xác minh chữ ký.
    """
    pdf_path = "signed_pdf.pdf"
    signature_path = "signature.sig"
    public_key_path = "public.pem"
    with open(pdf_path, "wb") as buffer:
        buffer.write(pdf_file.file.read())
    with open(signature_path, "wb") as buffer:
        buffer.write(signature.file.read())
    with open(public_key_path, "wb") as buffer:
        buffer.write(public_key.file.read())
    verify_pdf_signature(pdf_path, signature_path, public_key_path)
    return {"message": "Chữ ký đã được xác minh!"}
