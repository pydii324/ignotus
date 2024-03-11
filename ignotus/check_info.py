import re

def check_info(username, password, email):
    check_username(username)
    check_password(password)
    check_email(email)

def check_username(username):
    regex = r'^[A-Za-z][A-Za-z0-9_]{7,29}$'

    if(not re.fullmatch(regex, username)):
        return False
    else:
        return username

def check_password(password):
    regex = r'/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/'

    if(not re.fullmatch(regex, password)):
        return False
    else:
        return password

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if(not re.fullmatch(regex, email)):
        return False
    else:
        return email