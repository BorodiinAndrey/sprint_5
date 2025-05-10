import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui_helpers import UIHelpers


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture()
def ui(driver):
    return UIHelpers(driver)
