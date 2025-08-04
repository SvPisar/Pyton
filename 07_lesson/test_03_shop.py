import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product("sauce-labs-backpack")
    products.add_product("sauce-labs-bolt-t-shirt")
    products.add_product("sauce-labs-onesie")
    products.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Иван", "Петров", "123456")
    total = checkout.get_total()

    assert "$58.29" in total
    driver.quit()
