from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA

def encrypted_symmertric_key(symmetric_key, recv_public_path):
    with open(recv_public_path, 'rb') as f:
        key = RSA.importKey(f.read())
    
    cipher_rsa_encrypt = PKCS1_OAEP.new(key)
    print(cipher_rsa_encrypt)
    ciphertext = cipher_rsa_encrypt.encrypt(symmetric_key)
    
    return ciphertext

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

# key1 = RSA.generate(1024)
# data = read_data('input.txt')
# key = generate_public_key(key1, './key/recv_pub_key.pub')

# symmetric_key = generate_symmetric_key()
# print(f'Symmetric key is: {symmetric_key}')

# encrypted_symmetric = encrypted_symmertric_key(symmetric_key=symmetric_key)
# print(f'Encrypted symmetric key is: {encrypted_symmetric}')

# with open('./key/encrypted_key.key', 'wb') as f:
#     f.write(encrypted_symmetric)

# private_key = generate_private_key(key1, './key/recv_private_key.key')
# recv_private_key = read_data('./key/recv_private_key.key')

# print(f'Receiver private key is: {recv_private_key}')

# ciphered_data, iv = encrypt_data(key=symmetric_key, data=data)
# print(iv)
# write_data('output.txt', iv, ciphered_data)
