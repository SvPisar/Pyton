from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    browser.get('http://the-internet.herokuapp.com/inputs')
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        'input[type="number"]'))
    )
    input_field.send_keys("Sky")
    time.sleep(2)
    input_field.clear()

    input_field.send_keys("Pro")
    time.sleep(2)

finally:
    browser.quit()
