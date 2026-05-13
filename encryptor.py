import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a secure key using PBKDF2HMAC with 480,000 iterations."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(input_file: str, output_file: str, password: str):
    """Encrypts file and prepends a 16-byte random salt."""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    with open(output_file, 'wb') as file:
        file.write(salt + f.encrypt(data))

def decrypt_file(input_file: str, output_file: str, password: str):
    """Extracts salt and decrypts the encrypted file content."""
    with open(input_file, 'rb') as file:
        salt = file.read(16)
        encrypted_data = file.read()
    key = derive_key(password, salt)
    f = Fernet(key)
    try:
        decrypted_data = f.decrypt(encrypted_data)
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)
    except Exception:
        raise Exception("Decryption failed: Invalid password or corrupted file.")