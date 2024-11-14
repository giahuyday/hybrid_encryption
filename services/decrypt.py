from Crypto.Cipher import PKCS1_OAEP, AES 
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA


def decryped_symmetric_key(encrypted_key_path, private_path):
    ciphertext= ""
    with open(encrypted_key_path, 'rb') as f:
        ciphertext = f.read()

    with open(private_path, 'rb') as f:
        key = RSA.importKey(f.read())

    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)

    return message

def decrypt_data(key, file_path):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        decrypt_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    
    return original

def decrypt_encrypted_hash(sender_public):
    encrypted_hash = open('../data/encrypted_hash.bin', 'rb').read()
    
    sender_public_key = RSA.import_key(sender_public)
    cipher = PKCS1_OAEP.new(sender_public_key)
    message = cipher.decrypt(encrypted_hash)
    
    return message