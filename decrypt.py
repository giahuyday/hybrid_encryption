from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from encrypt import read_data

def decryped_symmetric_key(encrypted_key):
    ciphertext = read_data('./key/encrypted_key.key')  
    key = open('./key/recv_private_key.key').read()  
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)
    
    return message

symmertric_key = decryped_symmetric_key('./key/encrypted_key.key')
print(f'Decrypted symmertric key is: {symmertric_key}')