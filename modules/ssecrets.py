import json
import random
from pathlib import Path
import cssmin
import socket

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


class DeploymentHelper():
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent

        self.data_path = BASE_DIR / "settings.json"
        self.hostname = socket.gethostname()
    
    def get_json_settings(self):
        with open(self.data_path, "r", encoding="utf") as f:
            data = json.load(f)

        if self.hostname in data["production_hostnames"] and self.hostname not in data["development_hostnames"]:
            run_settings = data["production_settings"]
            self.mode = "production"
            self.handle_both(data, run_settings)
            self.handle_production()
        else:
            run_settings = data["development_settings"]
            self.mode = "development"
            self.handle_both(data, run_settings)
            self.handle_development()

        device_settings = data["device_specific_settings"].get(self.hostname)
        
        return run_settings, device_settings

    def handle_production(self):
        pass

    def handle_development(self):
        pass

    def compress_file(self, filepath, filename):
        fn_name, fn_type = filename.split(".")
        with open(f"{filepath}{fn_name}_uncompressed.{fn_type}", "r") as f:
            file = cssmin.cssmin(f.read())

        with open(f"{filepath}{filename}", "w") as f:
            f.write(file)

    def handle_both(self, data, run_settings):

        with open(data["data_json_relpath"], "r", encoding="utf-8") as f:
            jsoncontents = json.load(f)
        jsoncontents["domainName"] = run_settings["domainName"]

        with open(data["data_json_relpath"], "w", encoding="utf-8") as f:
            json.dump(jsoncontents, f, indent=4)

        css_path = "_base_static/css/"
        self.compress_file(css_path, "base.css")
        self.compress_file(css_path, "typography.css")


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
