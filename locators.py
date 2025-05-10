from selenium.webdriver.common.by import By

class MainPageLocators:
    enter_and_registration_button = (By.XPATH, "//button[text()='Вход и регистрация']")
    user_name = (By.CSS_SELECTOR, "[class='profileText name']")
    user_avatar = (By.CSS_SELECTOR, "[class='circleSmall']")
    enter = (By.XPATH, "//button[text()='Войти']")
    exit = (By.XPATH, "//button[text()='Выйти']")
    create_announcement_button = (By.XPATH, "//button[text()='Разместить объявление']")

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

class CreateAnnouncement:
    announcement_modal_text = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    name = (By.NAME, "name")
    description = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    price = (By.NAME, "price")
    choose_category_button = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]")
    choose_books_category = (By.XPATH, "//span[text()='Книги']")
    choose_city_button = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    choose_spb_city = (By.XPATH, "//span[text()='Санкт-Петербург']")
    publish_button = (By.XPATH, "//button[text()='Опубликовать']")
    footer = (By.XPATH, "//a[text()='Документация']")
    card_name = (By.XPATH, "//div[@class='about']//h2[text()='Война и мир']")
