from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage:
    """
    PageObject для страницы со списком товаров
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор ProductsPage.

        """
        self.driver = driver

    def add_product(self, product_id: str) -> None:
        """
        Добавляет товар в корзину по его идентификатору.

        """
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
