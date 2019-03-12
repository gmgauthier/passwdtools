from random import randint
from secrets import choice
from string import ascii_letters, digits
from cryptography.fernet import Fernet, InvalidToken

from configuration import Config


class Password:
    def __init__(self):
        self.encryption_key = Config().get_secret()
        if self.encryption_key is None:
            self.set_encryption_key()
        else:  # just take what's given
            self.cipher = Fernet(self.encryption_key)

    def get_encryption_key(self):
        return self.encryption_key

    def set_encryption_key(self):
        self.encryption_key = Fernet.generate_key()
        Config().set_secret(self.encryption_key.decode())  # store as string
        # Don't forget to update the cipher!!!
        self.cipher = Fernet(self.encryption_key)

    def encrypt(self, plain_password):
        return self.cipher.encrypt(plain_password.encode())

    def decrypt(self, encrypted_password):
        try:
            return self.cipher.decrypt(encrypted_password).decode()
        except InvalidToken:
            return "ERROR: Invalid Encryption Key"

    @staticmethod
    def generate(mn=16, mx=64):
        return ''.join(
            choice(ascii_letters + digits) for _ in range(randint(mn, mx))
        )
