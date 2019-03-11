import hashlib
import json
import uuid
from random import randint
from secrets import choice
from string import ascii_letters, digits

from configuration import Configuration


class Credentials:
    def __init__(self):
        with open(Configuration().get_keyfilename(), mode="r+") as keydata:
            self.keys = json.load(keydata)

    def get_keys(self):
        return self.keys

    def add_key(self, service, username, password):
        
        pass

    def get_key_by_service(self, service):
        return self.keys[service]

    @staticmethod
    def gen_password(mn=12, mx=64):
        return [
            ''.join(choice(ascii_letters + digits)
                    for _ in range(randint(mn, mx)))
        ]

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
