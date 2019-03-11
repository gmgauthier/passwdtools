import json


class Configuration:
    def __init__(self):
        with open('cfg/config.json') as cfgfile:
            self.data = json.load(cfgfile)

    def get_keyfilename(self):
        return self.data["keyfile"]
