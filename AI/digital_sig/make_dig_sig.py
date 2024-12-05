from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def create_rsa_keys():
    """
    Tạo cặp khóa RSA 2048-bit.
    
    Returns:
        tuple: Khóa riêng và khóa công.
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def create_signature(data, private_key):
    """
    Tạo chữ ký số cho dữ liệu bằng khóa riêng RSA.

    Args:
        data (str): Dữ liệu cần ký.
        private_key (bytes): Khóa riêng RSA.

    Returns:
        tuple: Chữ ký số và đối tượng băm SHA256.
    """
    hash_object = SHA256.new(data.encode('utf-8'))
    private_key_obj = RSA.import_key(private_key)
    signature = pkcs1_15.new(private_key_obj).sign(hash_object)
    return signature, hash_object

def verify_signature(data, signature, public_key):
    """
    Xác minh chữ ký số bằng khóa công RSA.

    Args:
        data (str): Dữ liệu đã được ký.
        signature (bytes): Chữ ký số cần xác minh.
        public_key (bytes): Khóa công RSA.

    Returns:
        bool: True nếu chữ ký hợp lệ, False nếu không hợp lệ.
    """
    hash_object = SHA256.new(data.encode('utf-8'))
    public_key_obj = RSA.import_key(public_key)
    try:
        pkcs1_15.new(public_key_obj).verify(hash_object, signature)
        return True
    except (ValueError, TypeError):
        return False
