import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 10)


def test_form(driver, wait):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        field = wait.until(EC.presence_of_element_located(
            (By.NAME, field_name)))
        field.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-outline-primary"]'
                        ).click()

    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in valid_fields:
        fieldID = wait.until(EC.presence_of_element_located(
            (By.ID, field_name)))
        assert fieldID.value_of_css_property(
            "background-color") == "rgba(209, 231, 221, 1)"

    zip_code = wait.until(EC.presence_of_element_located(
            (By.ID, "zip-code")))
    zip_code_bg = zip_code.value_of_css_property("background-color")
    assert zip_code_bg == "rgba(248, 215, 218, 1)"
