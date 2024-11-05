from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad


def generate_key(recv_public):
    salt = b'\x15\xd2\xa4\x1e\xb7\xcc\xe2\xa07\xf2F\xe8\xee`\x9d\xbb'
    password = read_data(recv_public)
    key = PBKDF2(password, salt, dkLen=32)

    return key

def encrypted_symmertric_key(key):
    pass

def encrypt_data(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))

    return ciphered_data, cipher.iv

def write_data(file_path, iv, data):
    with open(file_path, 'wb') as f:
        f.write(iv)
        f.write(data)

def read_data(file_path):
    data = ""
    with open(file_path, 'rb') as f:
        data = f.read()

    return data


def decrypt_data(key, file_path):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        decrypt_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    print(original)


data = read_data('input.txt')
key = generate_key()
ciphered_data, iv = encrypt_data(key=key, data=data)
print(iv)
write_data('output.txt', iv, ciphered_data)

decrypt_data(key, 'output.txt')