from cryptography.fernet import Fernet
import os
import sys

ENC_KEY = bytes(os.environ.get('ENC_KEY'),'utf-8')
if ENC_KEY is None:
    exit(1)

def decrypt_string(enc_string):
    enc_string = enc_string[2:][:-1]
    # print(f"String to decrypt: {enc_string}")
    f = Fernet(ENC_KEY)
    return f.decrypt(bytes(enc_string,'utf-8')).decode()

if len(sys.argv) == 2:
    password = decrypt_string(sys.argv[1])
    print(password)
    exit(0)
else:
    exit(1)