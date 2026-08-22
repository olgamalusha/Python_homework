from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    wait = WebDriverWait(driver, 10)
    hello = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    driver.save_screenshot("screenshot.png")

    assert hello.text == "Hello World!"

    driver.quit()
