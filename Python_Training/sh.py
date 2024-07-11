#sha-256  encrytion method used in cybersecurity
import hashlib

def hash_password(password):
    password_bytes = password.encode('utf-8') 
    hash_object = hashlib.sha256(password_bytes)
    password_hash = hash_object.hexdigest()
    return password_hash

password = input('Enter password: ')
hasshed_password =hash_password(password)
print(f"Your hash_paasword is: {hasshed_password}")


#create a code to check  if the password meets certian criteria