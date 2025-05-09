import data
from locators import MainPageLocators, RegistrationPageLocators, RegistrationErrorLocators


class TestBoard:

    def test_check_registration_w_not_repeat_password(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.click(RegistrationPageLocators.not_account_button)
        ui.input_fake_email(RegistrationPageLocators.email)
        ui.input_password(RegistrationPageLocators.password)
        ui.click(RegistrationPageLocators.create_account)

        error_text = ui.get_error(RegistrationErrorLocators.error_text)
        border_color_email = ui.get_color(RegistrationErrorLocators.email_field_color_error)
        border_color_password = ui.get_color(RegistrationErrorLocators.password_field_color_error)
        border_color_repeat_password = ui.get_color(RegistrationErrorLocators.repeat_password_field_color_error)

        assert (
            error_text == data.error and
            '255, 105, 114' in border_color_email and
            '255, 105, 114' in border_color_password and
            '255, 105, 114' in border_color_repeat_password
        ), f"Ошибка: {error_text}, цвет рамки: {border_color_email, border_color_password, border_color_repeat_password}"
