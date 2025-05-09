from selenium.webdriver.common.by import By

class RegistrationLocators:
    enter_and_registration_button = (By.XPATH, "//button[text()='Вход и регистрация']")
    not_account_button = (By.XPATH, "//button[text()='Нет аккаунта']")
    input_fake_email = (By.XPATH, "//form[@class='popUp_shell__LuyqR']//input[@name='email']")