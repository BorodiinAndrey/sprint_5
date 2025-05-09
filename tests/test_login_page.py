import data
from locators import MainPageLocators, RegistrationPageLocators


class TestLoginPage:

    def test_check_login_page_happy_path(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.input_text(RegistrationPageLocators.email, data.email)
        ui.input_text(RegistrationPageLocators.password, data.password)
        ui.click(MainPageLocators.enter)

        actual_user_name = ui.get_text(MainPageLocators.user_name)
        user_avatar = ui.get_element(MainPageLocators.user_avatar)

        assert actual_user_name == data.user_name and user_avatar is not None and user_avatar.is_displayed()

    def test_check_logout_happy_path(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.input_text(RegistrationPageLocators.email, data.email)
        ui.input_text(RegistrationPageLocators.password, data.password)
        ui.click(MainPageLocators.enter)
        ui.click(MainPageLocators.exit)

        enter_and_registration_button = ui.get_element(MainPageLocators.enter_and_registration_button)

        assert enter_and_registration_button.is_displayed()
