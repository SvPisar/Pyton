from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CLASS_NAME, "screen")
    DIGIT_BUTTON = (By.XPATH, "//span[text()='{}']")
    OPERATOR_BUTTON = (By.XPATH, "//span[text()='{}']")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium\
            -webdriver-java/slow-calculator.html"

    def open_page(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_digit(self, digit):
        button = self.driver.find_element(
            self.DIGIT_BUTTON[0],
            self.DIGIT_BUTTON[1].format(digit))
        button.click()

    def click_operator(self, operator):
        button = self.driver.find_element(
            self.OPERATOR_BUTTON[0],
            self.OPERATOR_BUTTON[1].format(operator))
        button.click()

    def calculate(self, expression):
        for char in expression:
            if char.isdigit():
                self.click_digit(char)
            else:
                self.click_operator(char)

    def wait_for_result(self, expected_result, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.RESULT_DISPLAY,
                expected_result))

    def get_result(self):
        return self.driver.find_element(*self.RESULT_DISPLAY).text
