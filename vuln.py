import os

def insecure_input():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 🚨 Command injection (critical)

def weak_hash():
    from argon2 import PasswordHasher
    password = "password123"
    ph = PasswordHasher()
    hashed = ph.hash(password)  # ✅ Strong hash using Argon2
