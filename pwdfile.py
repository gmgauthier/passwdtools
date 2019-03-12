from configuration import Config
import json


class Pwdfile:
    def __init__(self):
        self.pwdsfile = Config().get_pwdfilename()

    def read(self):
        with open(self.pwdsfile, mode="r") as pwddata:
            return json.load(pwddata)

    def write(self, keys):
        with open(self.pwdsfile, mode="w") as pwddata:
            pwddata.write(json.dumps(keys))

