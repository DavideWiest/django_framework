import json
import random

from cryptography.fernet import Fernet
import hashlib

with open("settings.json", "r", encoding="utf") as f:
    data = json.load(f)

class EncryptionOperator():
    def __init__(self, encryption_token):
        self.encryption_token = encryption_token
        self.fernet = Fernet(self.encryption_token)
        
    def decrypt(self, arg):
        arg = arg.encode()
        resp = self.fernet.decrypt(arg)
        resp = resp.decode()
        return resp

    def encrypt(self, arg):
        arg = arg.encode()
        resp = self.fernet.encrypt(arg)
        resp = resp.decode()
        return resp

class SecretOperator():
    def __init__(self, encryption_token=None):
        if encryption_token != None:
            self.eo = EncryptionOperator(encryption_token)

    def get_json_secrets(self, file="secrets.json", is_secure=False):
        if not is_secure:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        
        else:
            with open(file, "r", encoding="utf-8") as f:
                dec_file = self.eo.decrypt(f.read())
            return json.loads(dec_file)

class PassManager():
    def __init__(self):
        self.ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"

    def encrypt(self, password):
        salt = "".join(random.choice(self.ALPHABET) for i in range(16))

        password = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

        return salt, password

    def encrypt_with_salt(self, salt, password):
        password = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

        return password
