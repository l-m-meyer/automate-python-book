#! python3
# strongPassword.py - Use regex to detect strong passwords.


import re


    # at least one digit
def is_password_strong(password):
    is_strong = has_enough_chars(password)

    if is_strong:
        is_strong = has_upper_and_lower_chars(password)

    print(is_strong, password)


def has_enough_chars(password):
    '''validates that password is at least 8 characters long'''
    strong_pass = re.compile(r'(\w{8})+')
    
    is_strong = strong_pass.search(password)

    return bool(is_strong)


def has_upper_and_lower_chars(password):
    '''validates that password has both uppercase and lowercase letters'''
    strong_pass = re.compile(r'[A-Z]+[a-z]+')

    is_strong = strong_pass.findall(password)

    return bool(is_strong)




# TEST CASES
# passing
is_password_strong('AbCdEfGh')
is_password_strong('ABCdefgh')
is_password_strong('ABCdefghIJKlmnOP')
is_password_strong('AbCdEfGhIJklmnOpqR')
# failing
is_password_strong('abcdefgh')
is_password_strong('abcdefghijklmnop')
is_password_strong('abcde')
is_password_strong('abcdefgh')
is_password_strong('ABCDEFGH')