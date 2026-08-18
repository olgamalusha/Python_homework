from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    old_url = driver.current_url
    driver.find_element(By.NAME, "custname").send_keys("Anna")
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()
    assert driver.current_url != old_url

    driver.quit()
