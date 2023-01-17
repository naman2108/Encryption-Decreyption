from cryptography.fernet import Fernet
key=Fernet.generate_key()
print(key)
message=input('Enter your message').encode()
f_obj=Fernet(key)
encrypt_message=f_obj.encrypt(message)
print(encrypt_message)
decrypt_message=f_obj.decrypt(encrypt_message)
print(decrypt_message)
