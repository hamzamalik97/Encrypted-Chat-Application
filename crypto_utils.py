from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

KEY = b'ThisIsASecretKey'  # 16 bytes key

def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    
    return iv + ":" + ct

def decrypt_message(enc_message):
    iv, ct = enc_message.split(":")
    
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    
    return pt.decode('utf-8')