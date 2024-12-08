from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def verify_pdf_signature(pdf_path, signature_path, public_key_path):
    """
    Xác minh chữ ký số của một tệp PDF.

    Hàm này kiểm tra tính hợp lệ của chữ ký số trên một tệp PDF bằng cách sử dụng khóa công RSA để xác minh chữ ký.

    Args:
        pdf_path (str): Đường dẫn đến tệp PDF cần xác minh chữ ký.
        signature_path (str): Đường dẫn đến tệp chữ ký số cần xác minh.
        public_key_path (str): Đường dẫn đến tệp khóa công RSA dùng để xác minh chữ ký.

    Returns:
        None: Hàm chỉ in ra kết quả xác minh chữ ký (hợp lệ hoặc không hợp lệ).

    Example:
        verify_pdf_signature("signed_pdf.pdf", "signature.sig", "public.pem")
    """
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    pdf_hash = SHA256.new(pdf_data)
    with open(signature_path, "rb") as f:
        signature = f.read()
    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())
    try:
        pkcs1_15.new(public_key).verify(pdf_hash, signature)
        print("Chữ ký hợp lệ! PDF không bị thay đổi.")
    except (ValueError, TypeError):
        print("Chữ ký không hợp lệ! PDF có thể đã bị chỉnh sửa.")
