#! python3
# 2048.py


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# navigate to game website
def open_game():
    global browser
    browser = webdriver.Chrome()
    browser.get('https://gabrielecirulli.github.io/2048/')


# TODO: send up direction


# TODO: send down direction


# TODO: send left direction


# TODO: send right direction


# TODO: play game


# TODO: handle game over


def main():
    open_game()


if __name__ == '__main__':
    main()