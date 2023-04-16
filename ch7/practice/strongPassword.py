#! python3
# strongPassword.py - Use regex to detect strong passwords.


import re


def is_password_strong(password):
    # 8 character long
    # both uppercase and lowercase characters
    # at least one digit
    return