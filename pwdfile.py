from configuration import Config
import json


class Pwdfile:
    def __init__(self):
        self.keysfile = Config().get_pwdfilename()

    def read(self):
        with open(self.keysfile, mode="r") as keydata:
            return json.load(keydata)

    def write(self, keys):
        with open(self.keysfile, mode="w") as keydata:
            keydata.write(json.dumps(keys))

