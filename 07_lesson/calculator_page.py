from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{button}']"
        ).click()

    def get_result(self, expected_result):
        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(
                self.result_screen,
                expected_result
            )
        )

        return self.driver.find_element(*self.result_screen).text
