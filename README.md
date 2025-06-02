# API Key Encryption Demo with Python and Fernet

This repository demonstrates how to **encrypt an API key**, store the encrypted key in a `.env` file, and **decrypt it securely at runtime** in a Python application using the `cryptography` library (Fernet symmetric encryption).

---

## Why Encrypt API Keys?

- Protect your API keys from accidental exposure
- Add an extra security layer beyond plain environment variables
- Useful if you need to store keys in files or databases but want to keep them safe

---

## Prerequisites

- Install required packages:

```bash
pip install flask cryptography python-dotenv
```

---

## Step 1: Generate a Fernet Encryption Key

Run this Python snippet once to generate and save your secret key:

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())
```

**Save this key securely** — you will use it to encrypt and decrypt your API key.

---

## Step 2: Encrypt Your API Key

Create a file named `encrypt_key.py`:

```python
from cryptography.fernet import Fernet

# Replace with your Fernet key generated in Step 1
encryption_key = b'YOUR_FERNET_KEY_HERE'
cipher = Fernet(encryption_key)

# Your plaintext API key
api_key = "your-plain-api-key"
encrypted_api_key = cipher.encrypt(api_key.encode())

print(encrypted_api_key.decode())
```

Run the script:

```bash
python encrypt_key.py
```

Copy the printed encrypted API key for the next step.

---

## Step 3: Create Your .env File

Create a `.env` file in your project directory with the following content:

```ini
FERNET_KEY=YOUR_FERNET_KEY_HERE
ENCRYPTED_API_KEY=YOUR_ENCRYPTED_API_KEY_HERE
```

**Example:**

```ini
FERNET_KEY=cRJn2PYR1Nq6g7TcAl-Qqv8TfjKd_9jq1qmhQGx2QJk=
ENCRYPTED_API_KEY=gAAAAABlYF5zZ4b5QwV1cxY…
```

---

## Step 4: Decrypt and Use the API Key in Your Python App

Create `app.py`:

```python
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

fernet_key = os.getenv("FERNET_KEY")
encrypted_api_key = os.getenv("ENCRYPTED_API_KEY")

cipher = Fernet(fernet_key.encode())
api_key = cipher.decrypt(encrypted_api_key.encode()).decode()

print("Decrypted API Key:", api_key)

# Use api_key securely in your application logic below
```

Run your app:

```bash
python app.py
```

You should see:

```
Decrypted API Key: your-plain-api-key
```

---

## Security Tips

- **Do NOT** commit your `.env` file or encryption key to version control
- Keep the Fernet key secure — ideally in environment variables or a secret manager
- Encrypting keys adds security but your app still needs access to the key to decrypt
- For production, consider managed secret stores like AWS Secrets Manager, HashiCorp Vault, or GCP Secret Manager

---

