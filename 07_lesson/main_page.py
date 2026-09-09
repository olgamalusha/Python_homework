from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self, product_id):
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
