from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sauce_demo():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    ).click()

    # Переход в корзину
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполнение данных покупателя
    driver.find_element(By.ID, "first-name").send_keys("Ольга")
    driver.find_element(By.ID, "last-name").send_keys("Петрова")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # Продолжить оформление
    driver.find_element(By.ID, "continue").click()

    # Ждём появления итоговой стоимости
    total = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )

    total_text = total.text

    driver.quit()

    assert total_text == "Total: $58.29"
