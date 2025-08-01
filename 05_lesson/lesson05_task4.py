from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(2)

    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(2)

    success_message = driver.find_element(By.ID, "flash")
    if "You logged into a secure area!" in success_message.text:
        print("Авторизация прошла успешно!")
    else:
        print("Ошибка авторизации.")
    time.sleep(2)

finally:
    driver.quit()
