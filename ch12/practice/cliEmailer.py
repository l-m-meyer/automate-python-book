#! python3
# cliEmailer.py - Logs in and sends an email from command line arguments.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip
import sys,re


# get email and message string from command line arguments
def get_recipient_msg():
    if len(sys.argv) > 1:
        to_email = sys.argv[1]
        msg = sys.argv[2:]

    valid_email = validate_email(to_email)
    if not valid_email:
        print('Invalid email')
        to_email = get_email()

    if not msg:
        print('No messge passed...')
        msg = pyip.inputStr('Enter a message: ')

    return to_email, msg


# validate email using regex
def validate_email(email):
    pat = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

    return pat.match(email)
    

# get email and validate input
def get_email():
    email = pyip.inputEmail('Please enter a valid email: ')
    check = validate_email(email)
    if not check:
        return get_email()


# get password and validate input
def get_password():
    return pyip.inputPassword('Please enter your email password: ')


# TODO: login to user email


# TODO: create new message


# TODO: target input field for recipient email address


# TODO: target input field for message body


# TODO: populate email and message body


# TODO: send email


# TODO: close browser


def main():
    to_email, msg = get_recipient_msg()
    user_email = get_email()
    user_pass = get_password()
    return


if __name__== '__main__':
    main()