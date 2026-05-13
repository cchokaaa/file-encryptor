# File Encryptor (AES-PBKDF2)

A security tool for file encryption/decryption, designed to demonstrate cryptographic engineering skills.

## Key Features
- **AES-128 (Fernet)** for data confidentiality.
- **PBKDF2 Key Derivation** with 480,000 iterations for password security.
- **Unique Salting** mechanism for every file to resist rainbow table attacks.
- **Password Strength Validator** using Regex.

## Usage
- **Encrypt**: `python main.py encrypt <file> <output.enc>`
- **Decrypt**: `python main.py decrypt <output.enc> <output.txt>`