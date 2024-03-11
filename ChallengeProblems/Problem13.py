"""
Problem Statement - ASCII CODE -
Caesar Cipher Encryption and Decryption. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
"""
def encrypt(message, shift):
    encrypted_text = ''.join([chr(ord(char) + shift) for char in message])
    return encrypted_text

def decrypt(message, shift):
    decrypted_message = ''.join([chr(ord(char) - shift) for char in message])
    return decrypted_message


encrypted_message= encrypt("Hey Geek! What's your progress?", 5)
print("Encrypted Message :", encrypted_message)
decrypted_message = decrypt(encrypted_message, 5)
print("Decrypted Message :", decrypted_message)
