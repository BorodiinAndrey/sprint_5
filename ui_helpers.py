from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import data


class UIHelpers:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.fake = Faker()

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.get_element(locator).click()

    def input_fake_email(self, locator):
        element = self.get_element(locator)
        email = self.fake.email()
        element.send_keys(email)

    def input_password(self, locator):
        self.get_element(locator).send_keys(data.password)

    def get_error(self, locator):
        return self.get_element(locator).text

    def get_color(self, locator):
        return self.get_element(locator).value_of_css_property('border')
