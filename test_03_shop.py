import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs", {"credentials_enable_service": False,
                  "profile.password_manager_enabled": False})
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Оформление заказа с несколькими товарами")
@allure.description("Проверка суммы при покупке 3-х товаров через PageObject")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    with allure.step("Авторизация под стандартным пользователем"):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление трёх товаров в корзину"):
        products = ProductsPage(driver)
        products.add_product("sauce-labs-backpack")
        products.add_product("sauce-labs-bolt-t-shirt")
        products.add_product("sauce-labs-onesie")
        products.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart = CartPage(driver)
        cart.click_checkout()

    with allure.step("Заполнение формы покупателя и получение суммы"):
        checkout = CheckoutPage(driver)
        checkout.fill_info("Иван", "Петров", "123456")
        total = checkout.get_total()

    with allure.step("Проверка, что сумма включает $58.29"):
        assert "$58.29" in total

    with allure.step("Закрытие браузера"):
        driver.quit()
