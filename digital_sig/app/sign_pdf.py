from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def sign_pdf(pdf_path, private_key_path, signature_path):
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    pdf_hash = SHA256.new(pdf_data)
    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())
    signature = pkcs1_15.new(private_key).sign(pdf_hash)
    with open(signature_path, "wb") as f:
        f.write(signature)
    print(f"Chữ ký số được lưu tại: {signature_path}")
