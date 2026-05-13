import sys
import getpass
from encryptor import encrypt_file, decrypt_file
from password_utils import check_password_strength

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py [encrypt/decrypt] [input_file] [output_file]")
        return

    mode, in_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]
    password = getpass.getpass("Enter password (hidden): ")

    if mode == "encrypt":
        is_strong, errors = check_password_strength(password)
        if not is_strong:
            print("❌ Security Alert: Weak Password")
            for e in errors: print(f"  - {e}")
            return

    try:
        if mode == "encrypt":
            encrypt_file(in_file, out_file, password)
            print(f"✅ Success: File '{in_file}' encrypted.")
        else:
            decrypt_file(in_file, out_file, password)
            print(f"✅ Success: File '{in_file}' decrypted.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()