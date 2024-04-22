from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

f = Fernet(key)

message = 'Hello, World!'
encrypted = f.encrypt(message.encode())
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)

file_key_path = 'data/key'
with open(file_key_path, 'wb') as file_key:
    file_key.write(key)

# Encrypt file
file_path = 'data/text.txt'
with open(file_path, 'rb') as file_to_encrypt:
    file_data = file_to_encrypt.read()

encrypted_data = f.encrypt(file_data)

with open(file_path, 'wb') as file_to_encrypt:
    file_to_encrypt.write(encrypted_data)

print(encrypted_data)

# Decrypt file

with open(file_path, 'rb') as file_to_decrypt:
    crypted_data = file_to_decrypt.read()

file_decrypt_path = 'data/text_decrypt.txt'
with open(file_decrypt_path, 'wb') as file_to_decrypt:
    encrypted_data = f.decrypt(crypted_data)
    file_to_decrypt.write(encrypted_data)

print(encrypted_data)