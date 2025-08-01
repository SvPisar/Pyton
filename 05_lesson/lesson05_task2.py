from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/dynamicid")
button = browser.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]").click()
browser.quit()
