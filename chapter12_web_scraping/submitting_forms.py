from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://login.metafilter.com')

userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('your_username')

passElem = browser.find_element(By.ID, 'user_pass')
passElem.send_keys('your_password')

passElem.submit()