"""Password"""
import hashlib

def password(code):
    """Hash password"""

    hashcode = hashlib.sha512(code.encode()).hexdigest().upper()
    print(hashcode)

password(input())
