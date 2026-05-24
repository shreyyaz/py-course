import random
import string
chars=" "+ string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
print(f"chars: {chars}")
print(f"key  : {key}")


#ENCRYPT
plain_text=input("ENTER A MESSAGE TO ENCRYPT: ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"ORIGINAL MESSAGE: {plain_text}")
print(f"ENCRYPTED MESSAGE: {cipher_text}")

#DECRYPT
cipher_text=input("ENTER A MESSAGE TO DECRYPT: ")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars [index]
print(f"ENCRYPTED MESSAGE: {cipher_text}")
print(f"DECRYPTED MESSAGE: {plain_text}")

