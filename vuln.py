import os
import subprocess

def command_injection():
    user_input = input("Enter a command: ")
    subprocess.call(user_input, shell=True)  # 🚨 Vulnerável a command injection

def hardcoded_secret():
    api_key = "sk_test_51H7v2fSgF4y8XX"  # 🚨 Exemplo de segredo hardcoded
    print("API Key:", api_key)
