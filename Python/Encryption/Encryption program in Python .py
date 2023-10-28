# Encryption program in Python 

import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
Plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for i in Plain_text:
    index = chars.index(i)
    cipher_text +=key[index]

print("\n")
print(f"orginal_message:{Plain_text}")
print(f"Encrypted_message:{cipher_text}")

print("\n")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
Plain_text = ""

for i in cipher_text:
    index = key.index(i)
    Plain_text +=chars[index]

print("\n")
print(f"Encrypted_message:{cipher_text}")
print(f"Orginal_message:{Plain_text}")