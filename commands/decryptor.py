import argparse
import sys
import os

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from services import decrypt
from Crypto.Hash import SHA256

def main():
    # Tạo một parser
    parser = argparse.ArgumentParser(description="Basic Hybrid Encryption Program")

    # Thêm các argument
    parser.add_argument('--receiver_private_key', type=str, help='Receiver public key', required=True)
    parser.add_argument('--encrypted_key', type=str, help='Path to encrypted symmetric key', required=True)
    parser.add_argument('--input_file', type=str, help='Path to file need to decrypt', required=True)
    parser.add_argument('--output_decrypted_file', type=str, help='Path to output decrypted file', required=True)

    # Parse các argument
    args = parser.parse_args()

    try:
        decrypt_symmetric = decrypt.decryped_symmetric_key(args.encrypted_key ,args.receiver_private_key)
        original = decrypt.decrypt_data(decrypt_symmetric, args.input_file)
        
        with open(args.output_decrypted_file,'wb') as f:
            f.write(original)

        sender_public = open('../key/sender_private_key.key', 'rb').read()
        decrypted_hash = decrypt.decrypt_encrypted_hash(sender_public)
        
        # Print to check
        # print(decrypted_hash)
        # print(SHA256.new(original).digest())

        if(decrypted_hash == SHA256.new(original).digest()):
            print("FILE IS VALID")
        else:
            print("FILE IS INVALID")
        
    except Exception as e:
        print(f"Error while decrypted data: {e}")

if __name__ == "__main__":
    main()