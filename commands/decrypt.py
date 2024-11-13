from Crypto.Cipher import PKCS1_OAEP, AES 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA

def decryped_symmetric_key(encrypted_key):
    ciphertext= ""
    with open('./key/encrypted_key.key', 'rb') as f:
        ciphertext = f.read()

    with open('./key/recv_private_key.key', 'rb') as f:
        key = RSA.importKey(f.read())
    print(ciphertext)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)

    return message

def decrypt_data(key, file_path):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        decrypt_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    print(original)

symmertric_key = decryped_symmetric_key('./key/encrypted_key.key')
print(f'Decrypted symmertric key is: {symmertric_key}')
decrypt_data(symmertric_key, 'output.txt')