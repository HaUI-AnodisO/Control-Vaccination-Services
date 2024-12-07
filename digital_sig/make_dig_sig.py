from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1. Tạo cặp khóa (khóa riêng và khóa công khai)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Lưu khóa vào file (tùy chọn)
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# 2. Dữ liệu cần ký (ví dụ: nội dung phiếu xác nhận)
data = "Phiếu xác nhận đã tiêm chủng lần 1, ngày 05/12/2024."

# 3. Tạo hash của dữ liệu
hash_object = SHA256.new(data.encode('utf-8'))

# 4. Tạo chữ ký số bằng khóa riêng
private_key_obj = RSA.import_key(private_key)
signature = pkcs1_15.new(private_key_obj).sign(hash_object)

print("Chữ ký số:", signature.hex())

# 5. Xác minh chữ ký số bằng khóa công khai
public_key_obj = RSA.import_key(public_key)

try:
    pkcs1_15.new(public_key_obj).verify(hash_object, signature)
    print("Chữ ký hợp lệ!")
except (ValueError, TypeError):
    print("Chữ ký không hợp lệ!")
