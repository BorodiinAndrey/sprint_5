from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class UIHelpers:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.fake = Faker()

    def wait_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
        return element

    def input_fake_email(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        email = self.fake.email()
        element.send_keys(email)
        return element
