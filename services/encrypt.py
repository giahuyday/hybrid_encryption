from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

def encrypt_with_RSA(key, data):
    cipher_rsa_encrypt = PKCS1_OAEP.new(key)
    ciphertext = cipher_rsa_encrypt.encrypt(data)
    
    return ciphertext

def encrypted_symmertric_key(symmetric_key, recv_public_path):
    with open(recv_public_path, 'rb') as f:
        key = RSA.importKey(f.read())
    
    return encrypt_with_RSA(key, symmetric_key)

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


# Hash encrypted output and encrypted it with RSA
def hash_data(private_key, data):
    hash_data = SHA256.new(data=data).digest()

    key = RSA.import_key(private_key)
    cipher_rsa_encrypt = PKCS1_OAEP.new(key=key)
    ciphertext = cipher_rsa_encrypt.encrypt(hash_data)
    
    return ciphertext
