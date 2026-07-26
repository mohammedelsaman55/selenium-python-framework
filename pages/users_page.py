from selenium.webdriver.common.by import By

from locators.users_locators import UsersLocators
from utils.waits import wait_for_element


class UsersPage:

    def __init__(self, driver):
        self.driver = driver

    def is_page_title_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PAGE_TITLE
        ).is_displayed()

    def is_create_new_user_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.CREATE_NEW_USER_BUTTON
        ).is_displayed()

    def is_search_input_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.SEARCH_INPUT
        ).is_displayed()

    def is_bulk_actions_dropdown_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.BULK_ACTIONS_DROPDOWN
        ).is_displayed()

    def is_add_filter_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.ADD_FILTER_BUTTON
        ).is_displayed()

    def is_reset_filter_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.RESET_FILTER_BUTTON
        ).is_displayed()

    def is_reset_sorting_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.RESET_SORTING_BUTTON
        ).is_displayed()

    def is_export_pdf_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EXPORT_PDF_BUTTON
        ).is_displayed()

    def is_export_csv_button_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EXPORT_CSV_BUTTON
        ).is_displayed()

    def is_users_table_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.USERS_TABLE
        ).is_displayed()

    def is_select_all_checkbox_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.SELECT_ALL_CHECKBOX
        ).is_displayed()

    def is_user_name_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.USER_NAME_HEADER
        ).is_displayed()

    def is_team_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.TEAM_HEADER
        ).is_displayed()

    def is_email_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.EMAIL_HEADER
        ).is_displayed()

    def is_country_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.COUNTRY_HEADER
        ).is_displayed()

    def is_province_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PROVINCE_HEADER
        ).is_displayed()

    def is_payments_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PAYMENTS_HEADER
        ).is_displayed()

    def is_phone_number_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.PHONE_NUMBER_HEADER
        ).is_displayed()

    def is_status_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.STATUS_HEADER
        ).is_displayed()

    def is_actions_header_displayed(self):
        return wait_for_element(
            self.driver,
            UsersLocators.ACTIONS_HEADER
        ).is_displayed()

    def get_users_count(self):

        wait_for_element(
            self.driver,
            (
                By.XPATH,
                "//tbody/tr[1]"
            )
        )

        return len(
            self.driver.find_elements(
                By.XPATH,
                "//tbody/tr"
            )
        )

    def search_user(self, user_name):

        search_input = wait_for_element(
            self.driver,
            UsersLocators.SEARCH_INPUT
        )

        search_input.clear()
        search_input.send_keys(user_name)

        wait_for_element(
            self.driver,
            UsersLocators.SEARCH_ICON
        ).click()

    def get_first_user_name(self):

        return wait_for_element(
            self.driver,
            UsersLocators.FIRST_USER_NAME
        ).text

    def is_no_results_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.NO_RESULTS_MESSAGE
        ).is_displayed()

    def is_previous_button_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.PREVIOUS_BUTTON
        ).is_displayed()

    def is_next_button_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.NEXT_BUTTON
        ).is_displayed()

    def is_page_size_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.PAGE_SIZE_VALUE
        ).is_displayed()

    def get_showing_records_text(self):

        return wait_for_element(
            self.driver,
            UsersLocators.SHOWING_RECORDS_TEXT
        ).text