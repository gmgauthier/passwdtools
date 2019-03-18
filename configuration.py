from cfgfile import CfgFile


class Config:
    def __init__(self):
        self.cfgfile = CfgFile()
        self.data = self.cfgfile.read()

    def get_pwdfilename(self):
        return self.data["pwdfilename"]

    def set_pwdfilename(self, pwdfilename):
        self.data["pwdfilename"] = pwdfilename
        self.cfgfile.write(self.data)

    def get_secret(self):
        return self.data["secret"]

    def set_secret(self, secret):
        self.data["secret"] = secret
        self.cfgfile.write(self.data)
