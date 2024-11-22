from getpass import getpass

def get_username():
    username = input('Please enter your username\n>')
    return username.strip()

def get_password():
    password = getpass('Please enter your password\n>')
    return password.strip()

def get_two_factor():
    two_factor = input('Please enter your 2FA\n>')
    return two_factor.strip()