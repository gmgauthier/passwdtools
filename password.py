import hashlib
import uuid
from random import randint
from secrets import choice
from string import ascii_letters, digits
from cryptography.fernet import Fernet

from configuration import Config


class Password:
    def __init__(self):
        self.encryption_key = Config().get_secret()

    def get_encryption_key(self):
        pass

    @staticmethod
    def generate(mn=16, mx=64):
        return ''.join(
                choice(ascii_letters + digits) for _ in range(randint(mn, mx)))

    @staticmethod
    def encrypt(plain_password):
        pass

    @staticmethod
    def decrypt(encrypted_password):
        pass

    @staticmethod
    def hash_password(password):
        salt = uuid.uuid4().hex
        return hashlib.sha512(
            salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha512(
            salt.encode() + user_password.encode()).hexdigest()

    @staticmethod
    def dsa_encode(password):
        hash_object = hashlib.new('DSA')
        hash_object.update(password)
        return hash_object.h
