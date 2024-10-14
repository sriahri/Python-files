from cryptography.fernet import Fernet  # We are importing the library for generating private key

message = input("Enter your message: ")
key = Fernet.generate_key()
fernet = Fernet(key)
# Encode Msg
encMessage = fernet.encrypt(bytes(message, 'utf-8'))
print("original string: ", message)
print("encrypted string: ", encMessage)
# decode it to string with decode methods
decMessage = fernet.decrypt(encMessage)
print("decrypted string: ", decMessage)
