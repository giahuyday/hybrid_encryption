import argparse
import sys
import os

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from services import encrypt, key_generator as generator
from Crypto.PublicKey import RSA

def main():
    # Tạo một parser
    parser = argparse.ArgumentParser(description="Basic Hybrid Encryption Program")

    # Thêm các argument
    parser.add_argument('--receiver_pub_key', type=str, help='Receiver public key', required=True)
    parser.add_argument('--input_file', type=str, help='File which need to be encrypted', required=True)
    parser.add_argument('--output_encrypted_file', type=str, help='Output file', required=True)
    parser.add_argument('--output_encrypted_symmetric_key', type=str, help='Path to output encrypted symmetric key', required=True)

    # Parse các argument
    args = parser.parse_args()

    try:
        key = RSA.generate(1024)
        
        # Generated symmetric key and asymmetric RSA keys
        RSA_public = generator.generate_public_key(key, args.receiver_pub_key)
        RSA_private = generator.generate_private_key(key, '../key/recv_private_key.key')
        symmetric = generator.generate_symmetric_key()
        
        # Encrypted symmetric key
        encrypted_symmetric = encrypt.encrypted_symmertric_key(symmetric_key=symmetric, recv_public_path=args.receiver_pub_key)
        with open(args.output_encrypted_symmetric_key, 'wb') as f:
            f.write(encrypted_symmetric)
        
        data = encrypt.read_data(args.input_file)
        ciphered_data, iv = encrypt.encrypt_data(key=symmetric, data=data)
        
        print(iv)
        encrypt.write_data(args.output_encrypted_file, iv, ciphered_data)
        
    except Exception as e:
        print(f"Error while encrypted data: {e}")

if __name__ == "__main__":
    main()