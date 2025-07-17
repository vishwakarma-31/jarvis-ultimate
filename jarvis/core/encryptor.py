import os
from cryptography.fernet import Fernet

KEY_FILE = "jarvis.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

def encrypt_data(data: str) -> bytes:
    fernet = generate_key()
    return fernet.encrypt(data.encode())

def decrypt_data(token: bytes) -> str:
    fernet = generate_key()
    return fernet.decrypt(token).decode()