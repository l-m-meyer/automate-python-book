#! python3
# selenium.py


from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('display-3')
    print(f'Found {elem.tag_name} element with that class name!')
except:
    print('Was not able to find an element with that name.')