from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UIHelpers:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
        return element
