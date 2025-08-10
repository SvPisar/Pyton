from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    PageObject для страницы оформления заказа
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор CheckoutPage.
        """
        self.driver = driver

    def fill_info(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет форму оформления заказа: имя, фамилию и почтовый индекс.

        """
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получает итоговую сумму из блока оплаты.

        текст с итоговой суммой
        """
        total = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total.text
