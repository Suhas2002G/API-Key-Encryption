import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from dotenv import load_dotenv

load_dotenv()  

class ApiKeyProtector:
    @staticmethod
    def encrypt_api_key(api_key):
        encryption_key = os.getenv("FERNET_KEY")
        cipher = Fernet(encryption_key.encode())  
        encrypted_api_key = cipher.encrypt(api_key.encode())
        return encrypted_api_key.decode()

    @staticmethod
    def decrypt_api_key(encrypted_api_key):
        fernet_key = os.getenv("FERNET_KEY")
        cipher = Fernet(fernet_key.encode())
        return cipher.decrypt(encrypted_api_key.encode()).decode()
