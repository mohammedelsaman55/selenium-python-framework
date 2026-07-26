import time

from selenium.webdriver.common.keys import Keys
from locators.profile_locators import ProfileLocators
from utils.waits import (
    wait_for_element,
    wait_for_clickable_element
)


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def is_page_title_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.PAGE_TITLE
        ).is_displayed()

    def is_profile_name_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.PROFILE_NAME
        ).is_displayed()

    def is_first_name_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.FIRST_NAME_INPUT
        ).is_displayed()

    def is_last_name_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.LAST_NAME_INPUT
        ).is_displayed()

    def is_email_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.EMAIL_INPUT
        ).is_displayed()

    def is_country_code_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.COUNTRY_CODE_INPUT
        ).is_displayed()

    def is_country_selector_dropdown_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.COUNTRY_SELECTOR_DROPDOWN
        ).is_displayed()

    def is_phone_number_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.PHONE_NUMBER_INPUT
        ).is_displayed()

    def is_password_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.PASSWORD_INPUT
        ).is_displayed()

    def is_address_field_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.ADDRESS_INPUT
        ).is_displayed()

    def is_team_dropdown_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.TEAM_DROPDOWN
        ).is_displayed()

    def is_save_changes_button_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.SAVE_CHANGES_BUTTON
        ).is_displayed()

    def is_change_photo_link_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.CHANGE_PHOTO_LINK
        ).is_displayed()

    def is_change_email_link_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.CHANGE_EMAIL_LINK
        ).is_displayed()

    def is_change_password_link_displayed(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.CHANGE_PASSWORD_LINK
        ).is_displayed()

    def get_first_name_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.FIRST_NAME_INPUT
        ).get_attribute("value")

    def get_last_name_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.LAST_NAME_INPUT
        ).get_attribute("value")

    def get_email_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.EMAIL_INPUT
        ).get_attribute("value")

    def get_phone_number_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.PHONE_NUMBER_INPUT
        ).get_attribute("value")

    def get_address_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.ADDRESS_INPUT
        ).get_attribute("value")

    def get_selected_country(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.SELECTED_COUNTRY
        ).get_attribute("title")

    def get_team_value(self):
        return wait_for_element(
            self.driver,
            ProfileLocators.TEAM_VALUE
        ).text

    def edit_first_name(self, value):

        field = wait_for_element(
            self.driver,
            ProfileLocators.FIRST_NAME_INPUT
        )

        field.click()
        field.send_keys(Keys.COMMAND, "a")
        field.send_keys(Keys.DELETE)

        if value:
            field.send_keys(value)

        field.send_keys(Keys.TAB)

    def edit_last_name(self, value):

        field = wait_for_element(
            self.driver,
            ProfileLocators.LAST_NAME_INPUT
        )

        field.click()
        field.send_keys(Keys.COMMAND, "a")
        field.send_keys(Keys.DELETE)

        if value:
            field.send_keys(value)

        field.send_keys(Keys.TAB)

    def edit_address(self, value):

        field = wait_for_element(
            self.driver,
            ProfileLocators.ADDRESS_INPUT
        )

        field.clear()
        field.send_keys(value)

    def edit_phone_number(self, value):

        field = wait_for_element(
            self.driver,
            ProfileLocators.PHONE_NUMBER_INPUT
        )

        field.click()

        current_value = field.get_attribute(
            "value"
        )

        for _ in range(
            len(current_value)
        ):
            field.send_keys(
                Keys.BACKSPACE
            )

        if value:
            field.send_keys(value)

        field.send_keys(
            Keys.TAB
        )

    def is_save_button_enabled(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.SAVE_CHANGES_BUTTON
        ).is_enabled()

    def click_save_changes(self):

        wait_for_element(
            self.driver,
            ProfileLocators.SAVE_CHANGES_BUTTON
        ).click()

    def open_country_dropdown(self):

        wait_for_element(
            self.driver,
            ProfileLocators.COUNTRY_SELECTOR_DROPDOWN
        ).click()

    def search_country(self, country_name):

        search_box = wait_for_element(
            self.driver,
            ProfileLocators.COUNTRY_SEARCH_INPUT
        )

        search_box.clear()
        search_box.send_keys(country_name)

    def select_egypt_country(self):

        wait_for_element(
            self.driver,
            ProfileLocators.COUNTRY_EGYPT_OPTION
        ).click()

    def is_success_message_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.SUCCESS_TOAST_MESSAGE
        ).is_displayed()

    def is_first_name_required_message_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.FIRST_NAME_REQUIRED_MESSAGE
        ).is_displayed()

    def is_last_name_required_message_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.LAST_NAME_REQUIRED_MESSAGE
        ).is_displayed()

    def is_phone_required_message_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.PHONE_REQUIRED_MESSAGE
        ).is_displayed()

    def open_change_password_popup(self):

        wait_for_element(
            self.driver,
            ProfileLocators.CHANGE_PASSWORD_LINK
        ).click()

    def is_change_password_popup_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.CHANGE_PASSWORD_POPUP_TITLE
        ).is_displayed()

    def is_current_password_field_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.CURRENT_PASSWORD_INPUT
        ).is_displayed()

    def is_new_password_field_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.NEW_PASSWORD_INPUT
        ).is_displayed()

    def is_confirm_password_field_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.CONFIRM_PASSWORD_INPUT
        ).is_displayed()

    def is_save_password_button_displayed(self):

        return wait_for_element(
            self.driver,
            ProfileLocators.SAVE_PASSWORD_BUTTON
        ).is_displayed()

    def enter_current_password(
            self,
            password
    ):

        field = wait_for_element(
            self.driver,
            ProfileLocators.CURRENT_PASSWORD_INPUT
        )

        field.clear()
        field.send_keys(password)
        field.send_keys(Keys.TAB)

    def enter_new_password(
            self,
            password
    ):

        field = wait_for_element(
            self.driver,
            ProfileLocators.NEW_PASSWORD_INPUT
        )

        field.clear()
        field.send_keys(password)
        field.send_keys(Keys.TAB)

    def enter_confirm_password(
            self,
            password
    ):

        field = wait_for_element(
            self.driver,
            ProfileLocators.CONFIRM_PASSWORD_INPUT
        )

        field.clear()
        field.send_keys(password)
        field.send_keys(Keys.TAB)

    def is_save_password_button_enabled(
            self
    ):

        return wait_for_element(
            self.driver,
            ProfileLocators.SAVE_PASSWORD_BUTTON
        ).is_enabled()

    def click_save_password_button(
            self
    ):

        wait_for_element(
            self.driver,
            ProfileLocators.SAVE_PASSWORD_BUTTON
        ).click()

    def is_password_changed_successfully_message_displayed(
            self
    ):

        return wait_for_element(
            self.driver,
            ProfileLocators.PASSWORD_CHANGED_SUCCESS_MESSAGE
        ).is_displayed()

    def is_passwords_do_not_match_message_displayed(
            self
    ):

        return wait_for_element(
            self.driver,
            ProfileLocators.PASSWORDS_DO_NOT_MATCH_MESSAGE
        ).is_displayed()

    def is_generic_error_message_displayed(
            self
    ):

        return wait_for_element(
            self.driver,
            ProfileLocators.GENERIC_ERROR_MESSAGE
        ).is_displayed()

    def is_address_maximum_length_message_displayed(
            self
    ):

        return wait_for_element(
            self.driver,
            ProfileLocators.ADDRESS_MAXIMUM_LENGTH_MESSAGE
        ).is_displayed()

    def logout(self):

        time.sleep(2)

        wait_for_clickable_element(
            self.driver,
            ProfileLocators.PROFILE_AVATAR
        ).click()

        wait_for_element(
            self.driver,
            ProfileLocators.LOGOUT_BUTTON
        ).click()

        wait_for_element(
            self.driver,
            ProfileLocators.CONFIRM_LOGOUT_BUTTON
        ).click()