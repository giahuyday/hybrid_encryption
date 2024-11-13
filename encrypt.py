from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA

def generate_public_key(recv_public):
    key = RSA.generate(1024)

    with open(recv_public, 'wb') as f:
        f.write(key.publickey().export_key(format='PEM'))

    return key

def generate_private_key(recv_private_key):
    key = RSA.generate(1024)

    with open(recv_private_key, 'wb') as f:
        f.write(key.export_key(format='PEM'))

    return key

def generate_symmetric_key():
    salt = b'\x15\xd2\xa4\x1e\xb7\xcc\xe2\xa07\xf2F\xe8\xee`\x9d\xbb'
    password = '20127186'
    symmetric_key = PBKDF2(password, salt, dkLen=32)
    
    return symmetric_key

def encrypted_symmertric_key(symmetric_key):
    salt = b'\x15\xd2\xa4\x1e\xb7\xcc\xe2\xa07\xf2F\xe8\xee`\x9d\xbb'
    password = read_data('./key/recv_pub_key.pub')
    
    print(password)
    key = PBKDF2(password, salt, dkLen=32)

    return  key

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
key = generate_public_key('./key/recv_pub_key.pub')

symmetric_key = generate_symmetric_key()
print(f'Symmetric key is: {symmetric_key}')

encrypted_symmetric = encrypted_symmertric_key('./key/recv_pub_key.pub')
print(f'Encrypted symmetric key is: {encrypted_symmetric}')
with open('./key/encrypted_key.key', 'wb') as f:
    f.write(encrypted_symmetric)

private_key = generate_private_key('./key/recv_private_key.key')
recv_private_key = read_data('./key/recv_private_key.key')

print(f'Receiver private key is: {recv_private_key}')

ciphered_data, iv = encrypt_data(key=symmetric_key, data=data)
print(iv)
write_data('output.txt', iv, ciphered_data)
