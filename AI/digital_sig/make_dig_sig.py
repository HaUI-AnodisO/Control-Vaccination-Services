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
