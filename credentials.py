from pwdfile import Pwdfile


class Credentials:
    def __init__(self):
        self.creds = Pwdfile().read()

    def get_creds(self):
        return self.creds

    def read_cred(self, service):
        return self.creds[service]

    def create_cred(self, service, username, password):
        new_entry = {
            "username": username,
            "password": password
        }
        self.creds[service] = new_entry
        Pwdfile().write(self.creds)

    def update_cred(self, service, username=None, password=None):
        current_entry = self.creds[service]
        if username is None and password is not None:
            self.creds[service] = {
                "username": current_entry["username"],
                "password": password
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

