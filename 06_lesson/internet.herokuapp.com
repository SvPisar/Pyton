from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com")

# Явное ожидание: ждать появления элемента с текстом "A/B Testing"
element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "A/B Testing"))
    )
print(f"Элемент {element.text} найден и виден")

driver.quit()
