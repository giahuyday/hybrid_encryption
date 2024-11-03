# **Project: Lab1 Seminar Cong Nghe Tri Thuc**
## I. Install requirements library
```python
pip install requirments.txt
```

## Run encrypt command
```python
python encryptor.py --receiver_pub_key=receiver_pub_key.pub 
                    --input_file=file_to_encrypt.txt 
                    --output_encrypted_file=output_encrypted_file.txt 
                    --output_encrypted_symmetric_key=encrypted_key.key
```

## Run decrypt command
```python
python decryptor.py --receiver_private_key=receiver_private_key.key
                    --encrypted_key=encrypted_key.key
                    --input_file=encrypted_file.txt
                    --output_decrypted_file=output_decrypted_file.txt
```