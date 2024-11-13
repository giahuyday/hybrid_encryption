from Crypto.Protocol.KDF import PBKDF2

def generate_public_key(key, recv_public):
    with open(recv_public, 'wb') as f:
        f.write(key.publickey().export_key(format='PEM'))

    return key

def generate_private_key(key, recv_private_key):
    with open(recv_private_key, 'wb') as f:
        f.write(key.export_key(format='PEM'))

    return key

def generate_symmetric_key():
    salt = b'\x15\xd2\xa4\x1e\xb7\xcc\xe2\xa07\xf2F\xe8\xee`\x9d\xbb'
    password = '20127186'
    symmetric_key = PBKDF2(password, salt, dkLen=32)
    
    return symmetric_key