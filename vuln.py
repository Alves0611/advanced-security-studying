import os

def insecure_input():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 🚨 Command injection (critical)

def weak_hash():
    import hashlib
    password = "password123"
    hashed = hashlib.md5(password.encode()).hexdigest()  # 🚨 Weak hash (medium)
