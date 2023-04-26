#! python3
# cliEmailer.py - Logs in and sends an email from command line arguments.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyinputplus as pyip
import sys,re, time


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
    return email


# get password and validate input
def get_password():
    return pyip.inputPassword('Please enter your email password: ')


# get sender email client
def get_email_client(email):
    client = email.split('@')[1]
    return client


# get sender credentials
def get_sender_credentials():
    email = get_email()
    password = get_password()
    client = get_email_client(email)
    return email, password, client


# navigate to email client
def open_email_client(client):
    try:
        # connect
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-webgl')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('detach', True)
        service = Service('chromedriver.exe')
        global browser
        browser = webdriver.Chrome(service=service, options=chrome_options)
        browser.get(f'https://{client}')
    except Exception as e:
        print(str(e))


# enters email credentials into correct input field
def enter_email(email):
    try:
        email_login = browser.find_element(By.XPATH, '//input[@type="email"]')
        email_login.send_keys(email)
        print('Email entered... Success!')
        time.sleep(5)
    except:
        print('Faliure in email input...')


# enters password credentials into correct input field
def enter_password(password):
    try:
        password_login = browser.find_element(By.XPATH, '//input[@type="password"]')
        password_login.send_keys(password)
        print('Password entered... Success!')
        password_login.submit()
    except:
        print('Failure in password input...')


# finds and clicks "next" button for login flow
def click_next():
    try:
        next_button = browser.find_element(By.TAG_NAME, 'button')
        next_button.click()
        print('Next button clicked... Success!')
        time.sleep(5)
    except:
        print('No next button...')


# finds and clicks "sign in" button for login flow
def click_sign_in():
    try:
        sign_in = browser.find_element(By.LINK_TEXT, 'Sign in')
        sign_in.click()
    except:
        pass


# login to user email
def login_to_email(email, password):
    click_sign_in()
    enter_email(email)
    click_next()
    
    try:
        enter_email(email)
    except:
        enter_password(password)
    finally:
        click_next()
        time.sleep(5)
        enter_password(password)


# TODO: create new message


# TODO: target input field for recipient email address


# TODO: target input field for message body


# TODO: populate email and message body


# TODO: close browser


# send email
def send_email(to_email, msg, from_email, user_pass, client):
    open_email_client(client)
    login_to_email(from_email, user_pass)


def main():
    to_email, msg = get_recipient_msg()
    from_email, user_pass, client = get_sender_credentials()
    send_email(to_email, msg, from_email, user_pass, client)


if __name__== '__main__':
    main()