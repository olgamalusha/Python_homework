from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "OTgyMmRkMTEtYTU1Yi00MzIwLThhZTAtZGQ2NDgwNDhiYzI3"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/foyijo9462")
    user1_url = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "YzQ2MmVjNjItMmVkMC00MzJhLThlMjktZTFiMjg5ODk2OWQw"
        })

    driver.refresh()
    driver.get("https://gitflic.ru/user/9462tan671")
    user2_url = driver.current_url

    assert user1_url != user2_url

    driver.quit()
