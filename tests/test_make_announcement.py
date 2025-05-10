import data
from locators import MainPageLocators, RegistrationPageLocators, CreateAnnouncement


class TestCreateAnnouncement:

    def test_check_create_announcement_w_not_authorization(self, ui):
        ui.click(MainPageLocators.create_announcement_button)
        modal_tittle = ui.get_text(CreateAnnouncement.announcement_modal_text)

        assert modal_tittle == 'Чтобы разместить объявление, авторизуйтесь'

    def test_check_create_announcement_w_authorization(self, ui):
        ui.click(MainPageLocators.enter_and_registration_button)
        ui.input_text(RegistrationPageLocators.email, data.email)
        ui.input_text(RegistrationPageLocators.password, data.password)
        ui.click(MainPageLocators.enter)
        ui.get_element(MainPageLocators.user_avatar)
        ui.click(MainPageLocators.create_announcement_button)
        ui.input_text(CreateAnnouncement.name, data.name)
        ui.click(CreateAnnouncement.choose_category_button)
        ui.click(CreateAnnouncement.choose_books_category)
        ui.scroll_to_element(CreateAnnouncement.footer)
        ui.click(CreateAnnouncement.choose_city_button)
        ui.click(CreateAnnouncement.choose_spb_city)
        ui.input_text(CreateAnnouncement.description, data.description)
        ui.input_text(CreateAnnouncement.price, data.price)
        ui.click(CreateAnnouncement.publish_button)
        ui.scroll_to_element(MainPageLocators.user_avatar)
        ui.click(MainPageLocators.user_avatar)
        ui.scroll_to_element(CreateAnnouncement.footer)

        assert data.name == ui.get_text(CreateAnnouncement.card_name)
