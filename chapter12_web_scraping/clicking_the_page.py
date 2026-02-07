from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get("https://inventwithpython.com")

linkElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Read Online"))
)

linkElem.click()