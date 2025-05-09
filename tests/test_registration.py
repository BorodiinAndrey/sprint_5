from locators import RegistrationLocators


class TestBoard:

    def test_check_registration_form_true_email(self, ui):
        ui.wait_and_click(RegistrationLocators.enter_and_registration_button)
        ui.wait_and_click(RegistrationLocators.not_account_button)
        ui.input_fake_email(RegistrationLocators.input_fake_email)



