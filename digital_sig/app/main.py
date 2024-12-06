from fastapi import FastAPI, UploadFile, File
from app.utils import remove_background
from app.insert_stamp import insert_stamp
from app.sign_pdf import sign_pdf
from app.verify_pdf_signature import verify_pdf_signature

app = FastAPI()

@app.post("/remove-background/")
async def api_remove_background(file: UploadFile = File(...)):
    img_out_path = "output.png"
    with open("input.png", "wb") as buffer:
        buffer.write(file.file.read())
    result = remove_background("input.png", img_out_path)
    return {"filename": img_out_path}

@app.post("/insert-stamp/")
async def api_insert_stamp(pdf_file: UploadFile = File(...), stamp_file: UploadFile = File(...), x: int = 350, y: int = 500, page: int = 2):
    pdf_path = "input_pdf.pdf"
    stamp_path = "stamp.png"
    output_path = "stamped_output.pdf"
    with open(pdf_path, "wb") as buffer:
        buffer.write(pdf_file.file.read())
    with open(stamp_path, "wb") as buffer:
        buffer.write(stamp_file.file.read())
    insert_stamp(pdf_path, stamp_path, output_path, x, y, page)
    return {"message": f"File PDF đã chèn dấu được lưu tại: {output_path}"}

@app.post("/sign-pdf/")
async def api_sign_pdf(pdf_file: UploadFile = File(...), private_key: UploadFile = File(...)):
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
