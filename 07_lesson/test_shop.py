from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)

    main_page.add_product(
        "add-to-cart-sauce-labs-backpack"
    )
    main_page.add_product(
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    main_page.add_product(
        "add-to-cart-sauce-labs-onesie"
    )

    main_page.go_to_cart()

    cart_page = CartPage(driver)

    cart_items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in cart_items
    assert "Sauce Labs Bolt T-Shirt" in cart_items
    assert "Sauce Labs Onesie" in cart_items

    cart_page.checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.fill_form(
        "Ольга",
        "Петрова",
        "123456"
    )

    total = checkout_page.get_total()

    driver.quit()

    assert total == "$58.29"
