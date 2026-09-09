from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calculator = CalculatorPage(driver)

    calculator.set_delay("45")

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    result = calculator.get_result("15")

    assert result == "15"

    driver.quit()
