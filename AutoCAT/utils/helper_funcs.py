'''
helper_funcs.py
------------
    A place for some quality of life functions.
'''
import os
import re

from dotenv import load_dotenv


def print_admin_info():
    '''Prints the account info for the admin user.'''
    load_dotenv()
    email = os.environ.get("ADMIN_EMAIL")
    pswd = "{}{}{}".format(os.environ.get('ADMIN_PASSWORD')[0],
                           '*' * len(os.environ.get('ADMIN_PASSWORD')),
                            os.environ.get('ADMIN_PASSWORD')[-1])

    print(f"ADMIN_EMAIL: {email} \nADMIN_PASSWORD: {pswd}")


def check_email(email_address):
    regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    return True if re.search(regex, email_address) else False