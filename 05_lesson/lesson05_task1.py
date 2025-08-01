from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/classattr")
button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
browser.quit()
