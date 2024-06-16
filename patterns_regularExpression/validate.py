""" import re

pwd = input("Enter the password: ")
pwd_len = len(pwd)
is_valid = False

while True:
    if not re.search("[A-Z]", pwd): break
    elif not re.search ("[a-z]", pwd): break
    elif not re.search("[0-9]", pwd): break
    elif not re.search("[$@#!]", pwd): break
    elif not re.search("\s", pwd): break 
    else:
        is_valid = True
        break

if is_valid:
    print("Password is valid.")
else:
    print("Password is invalid.") """