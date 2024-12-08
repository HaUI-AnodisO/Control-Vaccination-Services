# main.py
from fastapi import FastAPI
from digital_sig.main_digital_sig import app as digital_sig_app
from ocr.main_ocr import app as ocr_app

app = FastAPI()

# Gộp các route từ hai app
app.mount("/digital-sig", digital_sig_app)
app.mount("/ocr", ocr_app)
@app.get("/")
def read_root():
    return {"message": "Hello World"}
