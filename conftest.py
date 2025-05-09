import pytest
from selenium import webdriver
from ui_helpers import UIHelpers


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture()
def ui(driver):
    return UIHelpers(driver)
