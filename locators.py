from selenium.webdriver.common.by import By

class MainPageLocators:
    enter_and_registration_button = (By.XPATH, "//button[text()='Вход и регистрация']")
    user_name = (By.CSS_SELECTOR, "[class='profileText name']")
    user_avatar = (By.CSS_SELECTOR, "[class='circleSmall']")

class RegistrationPageLocators:
    not_account_button = (By.XPATH, "//button[text()='Нет аккаунта']")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    repeat_password = (By.NAME, "submitPassword")
    create_account = (By.XPATH, "//button[text()='Создать аккаунт']")

class RegistrationErrorLocators:
    error_text_1 = (By.XPATH, "//span[text()='Пароли не совпадают']")
    error_text_2 = (By.XPATH, "//span[text()='Ошибка']")
    email_field_color_error = (By.XPATH, "(//*[@class='input_inputError__fLUP9'])[1]")
    password_field_color_error = (By.XPATH, "(//*[@class='input_inputError__fLUP9'])[2]")
    repeat_password_field_color_error = (By.XPATH, "(//*[@class='input_inputError__fLUP9'])[3]")