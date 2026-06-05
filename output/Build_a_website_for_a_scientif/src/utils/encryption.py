python
# src/utils/encryption.py

import hashlib
import secrets

class Hasher:
    def __init__(self):
        pass

    def generate_salt(self):
        return secrets.token_bytes(16)

    def hash_password(self, password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

class Authenticator:
    def __init__(self):
        self.salt = None
        self.password_hash = None

    def create_account(self, password):
        self.salt = self.Hasher().generate_salt()
        self.password_hash = self.Hasher().hash_password(password, self.salt)
        return self.password_hash, self.salt

    def verify_password(self, password, stored_password_hash, stored_salt):
        return self.Hasher().hash_password(password, stored_salt) == stored_password_hash
