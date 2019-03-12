from password import Password
from pwdfile import Pwdfile


class Credentials:
    def __init__(self):
        self.creds = Pwdfile().read()

    def get_creds(self):
        return self.creds

    def read_cred(self, service):
        return self.creds[service]

    def create_cred(self, service, username, password=None):
        if password is None:
            password = Password.generate(mn=64)

        new_entry = {
            "username": username,
            "password": Password().encrypt(password)
        }
        self.creds[service] = new_entry
        Pwdfile().write(self.creds)

    def update_cred(self, service, username=None, password=None):
        current_entry = self.creds[service]
        if username is None and password is not None:
            self.creds[service] = {
                "username": current_entry["username"],
                "password": Password().encrypt(password)
            }
        elif username is not None and password is None:
            self.creds[service] = {
                    "username": username,
                    "password": current_entry["password"]
                }
        Pwdfile().write(self.creds)

    def delete_cred(self, service):
        del self.creds[service]
        Pwdfile().write(self.creds)

