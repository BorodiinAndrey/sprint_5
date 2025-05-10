import data
from locators import MainPageLocators, RegistrationPageLocators


def test_check_logout_happy_path(self, ui):
    ui.click(MainPageLocators.enter_and_registration_button)
    ui.input_text(RegistrationPageLocators.email, data.email)
    ui.input_text(RegistrationPageLocators.password, data.password)
    ui.click(MainPageLocators.enter)
    ui.click(MainPageLocators.exit)

    enter_and_registration_button = ui.get_element(MainPageLocators.enter_and_registration_button)

    assert enter_and_registration_button.is_displayed()
