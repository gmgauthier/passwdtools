import json


class Config:
    def __init__(self):
        self.cfg_file = '/Volumes/GMGAUTHIER/keys/pwdtools/config.json'
        self.data = self.read()

    def get_pwdfilename(self):
        return self.data["pwdfilename"]

    def set_pwdfilename(self, pwdfilename):
        self.data["pwdfilename"] = pwdfilename
        self.write(self.data)

    def get_secret(self):
        return self.data["secret"]

    def set_secret(self, secret):
        self.data["secret"] = secret
        self.write(self.data)

    def read(self):
        with open(self.cfg_file, mode="r") as cfgfile:
            return json.load(cfgfile)

    def write(self, keys):
        with open(self.cfg_file, mode="w") as cfgfile:
            cfgfile.write(json.dumps(keys))
