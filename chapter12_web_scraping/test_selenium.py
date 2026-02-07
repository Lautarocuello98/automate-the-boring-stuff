from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://inventwithpython.com/")

try:
    elem = browser.find_element(By.CLASS_NAME, "img-thumb")
    print(f"Found <{elem.tag_name}> element with that class name!")
except:
    print("Was not able to find an element with that name")
