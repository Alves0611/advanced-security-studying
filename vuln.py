import os
import subprocess

def command_injection():
    user_input = input("Enter a command: ")
    subprocess.call(user_input, shell=True)  # 🚨 Command Injection

def hardcoded_secrets():
    stripe_key = "sk_test_51H7v2fSgF4y8XX"  # 🚨 Simulated Stripe secret
    github_token = "ghp_FAKEGitHubToken1234567890abcd"  # 🚨 Simulated GitHub token
    print("Stripe Key:", stripe_key)
    print("GitHub Token:", github_token)
