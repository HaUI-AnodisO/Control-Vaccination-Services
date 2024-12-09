# main.py
from fastapi import FastAPI
from digital_sig.main_digital_sig import app as digital_sig_router
from ocr.main_ocr import app as ocr_router

app = FastAPI(root_path="/ai")

# Thêm các router vào ứng dụng chính
app.include_router(ocr_router, prefix="/ocr", tags=["OCR APIs"])
app.include_router(digital_sig_router, prefix="/digital-sig", tags=["Digital Signature APIs"])

