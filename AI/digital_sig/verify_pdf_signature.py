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
