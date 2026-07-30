from selenium.webdriver.common.keys import Keys

from locators.users_locators import UsersLocators
from utils.waits import wait_for_element
from selenium.common.exceptions import TimeoutException

class CreateUserPage:

    def __init__(self, driver):
        self.driver = driver

    # ==========================
    # Modal
    # ==========================

    def is_modal_opened(self):
        return wait_for_element(
            self.driver,
            UsersLocators.ADD_USER_MODAL_TITLE
        ).is_displayed()

    # ==========================
    # Text Fields
    # ==========================

    def enter_first_name(self, first_name):
        field = wait_for_element(
            self.driver,
            UsersLocators.FIRST_NAME_INPUT
        )
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = wait_for_element(
            self.driver,
            UsersLocators.LAST_NAME_INPUT
        )
        field.clear()
        field.send_keys(last_name)

    def enter_email(self, email):
        field = wait_for_element(
            self.driver,
            UsersLocators.EMAIL_INPUT
        )
        field.clear()
        field.send_keys(email)

    def enter_phone(self, phone):
        field = wait_for_element(
            self.driver,
            UsersLocators.PHONE_INPUT
        )
        field.clear()
        field.send_keys(phone)

    def enter_city(self, city):
        field = wait_for_element(
            self.driver,
            UsersLocators.CITY_INPUT
        )
        field.clear()
        field.send_keys(city)

    def enter_postal_code(self, postal_code):
        field = wait_for_element(
            self.driver,
            UsersLocators.POSTAL_CODE_INPUT
        )
        field.clear()
        field.send_keys(postal_code)

    def enter_address(self, address):
        field = wait_for_element(
            self.driver,
            UsersLocators.ADDRESS_INPUT
        )
        field.clear()
        field.send_keys(address)

    # ==========================
    # Dropdowns
    # ==========================

    def select_team(self, team):

        wait_for_element(
            self.driver,
            UsersLocators.TEAM_INPUT
        ).send_keys(team)

        wait_for_element(
            self.driver,
            UsersLocators.TEAM_INPUT
        ).send_keys(Keys.ENTER)

    def select_country(self, country):

        wait_for_element(
            self.driver,
            UsersLocators.COUNTRY_INPUT
        ).send_keys(country)

        wait_for_element(
            self.driver,
            UsersLocators.COUNTRY_INPUT
        ).send_keys(Keys.ENTER)

    def select_province(self, province):

        wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_INPUT
        ).send_keys(province)

        wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_INPUT
        ).send_keys(Keys.ENTER)

    # ==========================
    # Buttons
    # ==========================

    def click_save(self):
        wait_for_element(
            self.driver,
            UsersLocators.SAVE_CHANGES_BUTTON
        ).click()

    def click_close(self):
        wait_for_element(
            self.driver,
            UsersLocators.CLOSE_BUTTON
        ).click()

    # ==========================
    # Validation Messages
    # ==========================

    def is_first_name_required_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.FIRST_NAME_REQUIRED
        ).is_displayed()

    def is_last_name_required_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.LAST_NAME_REQUIRED
        ).is_displayed()

    def is_email_required_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EMAIL_REQUIRED
        ).is_displayed()

    # ==========================
    # UI Verification
    # ==========================

    def is_first_name_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.FIRST_NAME_INPUT
        ).is_displayed()

    def is_last_name_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.LAST_NAME_INPUT
        ).is_displayed()

    def is_email_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EMAIL_INPUT
        ).is_displayed()

    def is_phone_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PHONE_INPUT
        ).is_displayed()

    def is_country_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.COUNTRY_DROPDOWN
        ).is_displayed()

    def is_province_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_DROPDOWN
        ).is_displayed()

    def is_city_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.CITY_INPUT
        ).is_displayed()

    def is_postal_code_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.POSTAL_CODE_INPUT
        ).is_displayed()

    def is_address_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.ADDRESS_INPUT
        ).is_displayed()

    def is_save_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.SAVE_CHANGES_BUTTON
        ).is_displayed()

    def is_close_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.CLOSE_BUTTON
        ).is_displayed()

    def get_default_status(self):
        return wait_for_element(
            self.driver,
            UsersLocators.STATUS_VALUE
        ).text

    def is_province_disabled(self):

        element = wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_DROPDOWN
        )

        classes = element.get_attribute("class")

        return "select__control--is-disabled" in classes

    # ==========================
    # Success
    # ==========================

    def is_success_message_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.CREATE_USER_SUCCESS_MESSAGE
        ).is_displayed()

    # ==========================
    # Complete Flow
    # ==========================

    def create_user(
            self,
            first_name,
            last_name,
            email,
            phone,
            team,
            country,
            province,
            city,
            postal_code,
            address
    ):

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone(phone)

        self.select_team(team)
        self.select_country(country)
        self.select_province(province)

        self.enter_city(city)
        self.enter_postal_code(postal_code)
        self.enter_address(address)

        self.click_save()

    def is_email_already_exists_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EMAIL_ALREADY_EXISTS
        ).is_displayed()

    def is_invalid_email_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.INVALID_EMAIL_MESSAGE
        ).is_displayed()

    def is_province_enabled(self):
        element = wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_DROPDOWN
        )

        classes = element.get_attribute("class")

        return "select__control--is-disabled" not in classes

    def is_modal_closed(self):

        try:
            wait_for_element(
                self.driver,
                UsersLocators.CREATE_USER_MODAL,
                timeout=2
            )
            return False

        except TimeoutException:
            return True

    def click_view_users_list(self):

        wait_for_element(
            self.driver,
            UsersLocators.VIEW_USERS_LIST_BUTTON
        ).click()