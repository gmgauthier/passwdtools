import json


class CfgFile:
    def __init__(self):
        self.cfg_file = '/Volumes/GMGAUTHIER/keys/pwdtools/config.json'

    def read(self):
        with open(self.cfg_file, mode="r") as cfgfile:
            return json.load(cfgfile)

    def write(self, keys):
        with open(self.cfg_file, mode="w") as cfgfile:
            cfgfile.write(json.dumps(keys))
