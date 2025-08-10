from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """
    PageObject для страницы корзины.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CartPage
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """
        Нажимает на кнопку
        """
        checkout_button: WebElement = self.driver.find_element(
            By.ID, "checkout")
        checkout_button.click()
