
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    return b64encode(ciphertext).decode('utf-8')

def decrypt_rsa(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = b64decode(encrypted_message)
    decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')
    return decrypted_message

# 生成RSA密钥对
private_key, public_key = generate_rsa_key_pair()

# 加密和解密示例
message = "Hello, RSA!"
encrypted_message = encrypt_rsa(message, public_key)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_rsa(encrypted_message, private_key)
print(f"Decrypted Message: {decrypted_message}")
