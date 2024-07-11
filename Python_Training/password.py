import re

def validate_password(password):
    if len(password) < 8:
        print("Password too short")
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):     
        return False
    if not re.search(r'\d',password): 
        return False 
    if not re.search(r'[!@#$%^&*]',password): 
        return False    
    return True

password = input("Enter your password: ")
is_valid = validate_password(password)
if is_valid:
    print("Password valid")
else:
    print("Password did not meet the specified criteria")


#Create a function that takes in a password AND RETURNS a list of COMMON CHARACTERS to build a strong password

def password_create(password):
    return f"Your password is {password} lol"

my_password = input ("Please enter password: ")
print(password_create(my_password))