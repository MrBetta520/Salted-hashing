import hashlib
import os

def my_hash(m):
    #Generate random nonce
    nonce_bytes = os.urandom(32)

    nonce = nonce_bytes.hex()

    concatenated = nonce + m
    
    sha256_hash = hashlib.sha256(concatenated.encode('utf-8'))

    h_hex = sha256_hash.hexdigest()
    
    return nonce, h_hex
