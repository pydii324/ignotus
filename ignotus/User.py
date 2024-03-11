import re
import check_info

class User:
    def __init__(self, token, username, password, email):
        self.token = token
        self.username = username
        self.email = email

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if check_info.check_username(value) == False:
            raise ValueError("Invalid username pattern!")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if check_info.check_password(value) == False:
            raise ValueError("Invalid password pattern!")
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if check_info.check_email(value) == False:
            raise ValueError("Invalid email pattern!")
        self._email = value