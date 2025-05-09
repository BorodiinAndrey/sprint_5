import data
from locators import MainPageLocators, RegistrationPageLocators, RegistrationErrorLocators


class TestBoard:

    def test_check_registration_happy_path(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.click(RegistrationPageLocators.not_account_button)
        ui.input_fake_email(RegistrationPageLocators.email)
        ui.input_text(RegistrationPageLocators.password, "12345")
        ui.input_text(RegistrationPageLocators.repeat_password, "12345")
        ui.click(RegistrationPageLocators.create_account)

        actual_user_name = ui.get_text(MainPageLocators.user_name)
        user_avatar = ui.get_element(MainPageLocators.user_avatar)

        assert actual_user_name == data.user_name and user_avatar is not None and user_avatar.is_displayed()

    def test_check_registration_w_not_repeat_password(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.click(RegistrationPageLocators.not_account_button)
        ui.input_fake_email(RegistrationPageLocators.email)
        ui.input_text(RegistrationPageLocators.password, "12345")
        ui.click(RegistrationPageLocators.create_account)

        error_text = ui.get_text(RegistrationErrorLocators.error_text_1)
        border_color_email = ui.get_color(RegistrationErrorLocators.email_field_color_error)
        border_color_password = ui.get_color(RegistrationErrorLocators.password_field_color_error)
        border_color_repeat_password = ui.get_color(RegistrationErrorLocators.repeat_password_field_color_error)

        assert (
            error_text == data.error_1 and
            '255, 105, 114' in border_color_email and
            '255, 105, 114' in border_color_password and
            '255, 105, 114' in border_color_repeat_password
        ), f"Ошибка: {error_text}, цвет рамки: {border_color_email, border_color_password, border_color_repeat_password}"

    def test_check_registration_existing_user(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.click(RegistrationPageLocators.not_account_button)
        ui.input_text(RegistrationPageLocators.email, "borodin_21@gmail.com")
        ui.input_text(RegistrationPageLocators.password, "12345")
        ui.input_text(RegistrationPageLocators.repeat_password, "12345")
        ui.click(RegistrationPageLocators.create_account)

        error_text = ui.get_text(RegistrationErrorLocators.error_text_2)
        border_color_email = ui.get_color(RegistrationErrorLocators.email_field_color_error)
        border_color_password = ui.get_color(RegistrationErrorLocators.password_field_color_error)
        border_color_repeat_password = ui.get_color(RegistrationErrorLocators.repeat_password_field_color_error)

        assert (
                error_text == data.error_2 and
                '255, 105, 114' in border_color_email and
                '255, 105, 114' in border_color_password and
                '255, 105, 114' in border_color_repeat_password
        ), f"Ошибка: {error_text}, цвет рамки: {border_color_email, border_color_password, border_color_repeat_password}"