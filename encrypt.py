from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def generate_key():
    public_key = get_random_bytes(16)
    private_key = get_random_bytes(16)
    
    with open("./private_key.pub", "wb") as f:
        f.write(private_key)
    
    with open("./encrypted_public.pub", "wb") as f:
        cipher = AES.new(public_key, AES.MODE_EAX, nonce=None)
        print(cipher)
        f.write(cipher)
    return public_key, private_key


for i in range(4):
    print(generate_key())