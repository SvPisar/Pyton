import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    calculator = CalculatorPage(driver)

    calculator.open_page()

    calculator.set_delay("45")

    calculator.calculate("7+8=")

    calculator.wait_for_result("15")
    assert calculator.get_result() == "15"
    driver.quit()
