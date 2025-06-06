import os
from flask import Flask
from cryptography.fernet import Fernet
from modules.api_encryption import ApiKeyProtector

app = Flask(__name__)


# STEP 1 : Generate a Fernet Encryption Key and Save it in .env this is one time
key = Fernet.generate_key()
print(key.decode())


# STEP 2 : Encrypt Your API Key
encrypted_api_key = ApiKeyProtector.encrypt_api_key('example@api_key_2025')
print(encrypted_api_key)


# STEP 3 : Create .env File and store encrypted_api_key received from step 2 


# STEP 4 : Decrypt and Use the API Key 
encrypted_api_key = os.getenv("SAMPLE_ENCRYPED_API")
decrypted_api_key = ApiKeyProtector.decrypt_api_key(encrypted_api_key)
print(decrypted_api_key)



if __name__ == '__main__':
    app.run(debug=True, port=5050)