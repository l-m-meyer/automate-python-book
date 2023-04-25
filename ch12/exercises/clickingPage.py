#! python3
# clickingPage.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
type(linkElem)
linkElem.click()



browser.get('https://login.metafilter.com')
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('L')
passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('no')
passwordElem.submit()


browser.get('https://nostarch.com')
htmElem = browser.find_element(By.TAG_NAME, 'html')
htmElem.send_keys(Keys.END)
htmElem.send_keys(Keys.HOME)
browser.back()
browser.forward()
browser.refresh()
browser.quit()