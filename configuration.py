import json


class Config:
    def __init__(self):
        self.data = self.read()

    def get_pwdfilename(self):
        return self.data["pwdfile"]

    def set_pwdfilename(self):
        pass

    def get_secret(self):
        return self.data["secret"]

    def set_secret(self, secret):
        pass

    @staticmethod
    def read():
        with open('cfg/config.json', mode="r") as cfgfile:
            return json.load(cfgfile)

    @staticmethod
    def write(keys):
        with open('cfg/config.json', mode="w") as cfgfile:
            cfgfile.write(json.dumps(keys))
