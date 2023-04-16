#! python3
# strongPassword.py - Use regex to detect strong passwords.


import re


    # 8 character long
    # both uppercase and lowercase characters
    # at least one digit
def is_password_strong(password):
    is_strong = has_enough_chars(password)

    print(is_strong)


def has_enough_chars(password):
    strong_pass = re.compile(r'(\w{8})+')
    
    is_strong = strong_pass.search(password)

    return bool(is_strong)


# TEST CASES
# passing
is_password_strong('abcdefgh')
is_password_strong('abcdefghijklmnop')
# failing
is_password_strong('abcde')