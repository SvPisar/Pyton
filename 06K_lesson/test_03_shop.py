from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_total_price_firefox():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 800)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        def add_to_cart(item_name):
            button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    f"//div[text()='{item_name}']/../../..//button"
                ))
            )
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", button
            )
            button.click()

        add_to_cart("Sauce Labs Backpack")
        add_to_cart("Sauce Labs Bolt T-Shirt")
        add_to_cart("Sauce Labs Onesie")

        cart = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart.click()

        checkout = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout.click()

        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Jumba")
        driver.find_element(By.ID, "last-name").send_keys("Juice")
        driver.find_element(By.ID, "postal-code").send_keys("718214")

        continue_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView(true);", continue_btn
        )
        continue_btn.click()

        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text.strip()
        assert total_text == "Total: $58.29"

    finally:
        driver.quit()
