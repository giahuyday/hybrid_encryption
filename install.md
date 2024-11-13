# **Project: Lab1 Seminar Knownledge Engineeering**
## **I. Install requirements library**
```python
pip install requirments.txt
```

## **II. Go to commands folder to run command line**
```command
cd commands
```

## **III. Run encrypt command**
- ### **Command to gen all output and key at same folder with encryptor and decryptor**
```python
python encryptor.py --receiver_pub_key=receiver_pub_key.pub 
                    --input_file=file_to_encrypt.txt 
                    --output_encrypted_file=output_encrypted_file.txt 
                    --output_encrypted_symmetric_key=encrypted_key.key
```

- ### **Command to gen all output and key at structured folder**
  - `data`: input and output file here
  - `key`: generate all symmetric and asymmetric key here
```python
python encryptor.py --receiver_pub_key=../key/recv_pub_key.pub 
                    --input_file=../data/input.txt 
                    --output_encrypted_file=../data/output.txt 
                    --output_encrypted_symmetric_key=../key/encrypted_key.key
```
  
- **Command line to test encryptor with `jpg` file**
```python
python encryptor.py --receiver_pub_key=../key/recv_pub_key.pub 
                    --input_file=../data/sample1.jpg 
                    --output_encrypted_file=../data/output.jpg 
                    --output_encrypted_symmetric_key=../key/encrypted_key.key
```
## **IV. Run decrypt command**
- ### **Command to gen all output and key at same folder with encryptor and decryptor**
```python
python decryptor.py --receiver_private_key=receiver_private_key.key
                    --encrypted_key=encrypted_key.key
                    --input_file=encrypted_file.txt
                    --output_decrypted_file=output_decrypted_file.txt
```

- ### **Command to gen all output and key at structured folder**
  - `data`: input and output file here
  - `key`: generate all symmetric and asymmetric key here
```python
python decryptor.py --receiver_private_key=../key/recv_private_key.key                 
                    --encrypted_key=../key/encrypted_key.key 
                    --input_file=../data/output.txt 
                    --output_decrypted_file=output_decrypted_file.txt
```

```python
python decryptor.py --receiver_private_key=../key/recv_private_key.key 
                    --encrypted_key=../key/encrypted_key.key 
                    --input_file=../data/output.jpg 
                    --output_decrypted_file=output_decrypted_file.jpg
```