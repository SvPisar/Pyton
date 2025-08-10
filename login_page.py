from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    PageObject для страницы входа (Login Page)
    """

    def __init__(self, driver: WebDriver) -> None:
        """ Конструктор LoginPage """
        self.driver = driver
        self.url = "https://www.saucedemo.com"

    def open(self) -> None:
        """
        Открывает страницу входа
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход по заданным логину и паролю
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
