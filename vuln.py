import os

def run_system_command(user_input):
    os.system("echo " + user_input)  # 🚨 Possible command injection (critical)

def insecure_hash(data):
    import hashlib
    return hashlib.md5(data.encode()).hexdigest()  # 🚨 Use of weak hash (medium)

def unused_function():
    pass  # 🟢 No alert here
