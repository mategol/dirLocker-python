from Crypto.Cipher import AES
import os
import hashlib
import random
import struct

def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def encrypt_file(input_file, output_file, secret_key, iv=[True, True], chunk_size=64*1024):
    if iv[0]:
        iv = str(random.randint(1111111111111111, 9999999999999999)).encode('utf-8')
    else:
        iv = iv.encode('utf-8')
    secret_key = hash_string(secret_key)[::2].encode('utf-8')
    encryptor = AES.new(secret_key, AES.MODE_CBC, iv)
    with open(input_file, 'rb') as input_file_data:
        with open(output_file, 'wb') as output_file_data:
            output_file_data.write(struct.pack('<Q', os.path.getsize(input_file)))
            if iv[1]:
                output_file_data.write(iv)
            while True:
                chunk = input_file_data.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += (' ' * (16-len(chunk) % 16)).encode('utf-8')
                output_file_data.write(encryptor.encrypt(chunk))

def decrypt_file(input_file, output_file, secret_key, iv=True, chunk_size=24*1024):
    with open(input_file, 'rb') as input_file_data:
        original_size = struct.unpack('<Q', input_file_data.read(struct.calcsize('Q')))[0]
        if iv:
            iv = input_file_data.read(16)
        else:
            iv = iv.encode('utf-8')
        secret_key = hash_string(secret_key)[::2].encode('utf-8')
        decryptor = AES.new(secret_key, AES.MODE_CBC, iv)
        with open(output_file, 'wb') as output_file_data:
            while True:
                chunk = input_file_data.read(chunk_size)
                if len(chunk) == 0:
                    break
                output_file_data.write(decryptor.decrypt(chunk))
            output_file_data.truncate(original_size)