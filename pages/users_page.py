from selenium.webdriver.common.by import By

from locators.users_locators import UsersLocators

from utils.waits import (
    wait_for_element,
    wait_for_presence_of_element,
    wait_for_url_contains,
    wait_for_overlay_to_disappear,
)


class UsersPage:

    def __init__(self, driver):
        self.driver = driver

    # ==========================================
    # Users Page
    # ==========================================

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

    # ==========================================
    # Search
    # ==========================================

    def search_user(self, value):

        search = wait_for_element(
            self.driver,
            UsersLocators.SEARCH_INPUT
        )

        search.clear()
        search.send_keys(value)

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

    # ==========================================
    # Pagination
    # ==========================================

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

    # ==========================================
    # Counters
    # ==========================================

    def get_total_users_counter(self):

        return wait_for_element(
            self.driver,
            UsersLocators.TOTAL_USERS_COUNTER
        ).text

    def get_active_users_counter(self):

        return wait_for_element(
            self.driver,
            UsersLocators.ACTIVE_USERS_COUNTER
        ).text

    def get_inactive_users_counter(self):

        return wait_for_element(
            self.driver,
            UsersLocators.INACTIVE_USERS_COUNTER
        ).text

    def get_users_count(self):

        wait_for_element(
            self.driver,
            (By.XPATH, "//tbody/tr[1]")
        )

        return len(
            self.driver.find_elements(
                By.XPATH,
                "//tbody/tr"
            )
        )

    # ==========================================
    # User Actions Menu
    # ==========================================

    def open_first_user_actions(self):

        wait_for_element(
            self.driver,
            UsersLocators.FIRST_USER_ACTIONS_BUTTON
        ).click()

    def is_details_option_displayed(self):

        self.open_first_user_actions()

        return wait_for_element(
            self.driver,
            UsersLocators.DETAILS_OPTION
        ).is_displayed()

    def is_activate_option_displayed(self):

        self.open_first_user_actions()

        return len(
            self.driver.find_elements(
                *UsersLocators.ACTIVATE_OPTION
            )
        ) > 0

    def is_deactivate_option_displayed(self):

        self.open_first_user_actions()

        return len(
            self.driver.find_elements(
                *UsersLocators.DEACTIVATE_OPTION
            )
        ) > 0


    # ==========================================
    # User Details
    # ==========================================

    def open_details(self):

        self.open_first_user_actions()

        wait_for_element(
            self.driver,
            UsersLocators.DETAILS_OPTION
        ).click()

        wait_for_url_contains(
            self.driver,
            "user-details"
        )

        wait_for_overlay_to_disappear(
            self.driver
        )

        wait_for_presence_of_element(
            self.driver,
            UsersLocators.FIRST_NAME_DETAILS_INPUT
        )

    def is_user_details_page_opened(self):

        return (
            "/dashboard/user-details/"
            in self.driver.current_url
        )

    def get_first_name(self):

        return wait_for_element(
            self.driver,
            UsersLocators.FIRST_NAME_DETAILS_INPUT
        ).get_attribute("value")

    def update_first_name(self, first_name):

        first_name_input = wait_for_element(
            self.driver,
            UsersLocators.FIRST_NAME_DETAILS_INPUT
        )

        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def update_last_name(self, value):

        element = wait_for_element(
            self.driver,
            UsersLocators.LAST_NAME_DETAILS_INPUT
        )

        element.clear()
        element.send_keys(value)

    def update_phone(self, value):

        element = wait_for_element(
            self.driver,
            UsersLocators.PHONE_DETAILS_INPUT
        )

        element.clear()
        element.send_keys(value)

    def update_city(self, value):

        element = wait_for_element(
            self.driver,
            UsersLocators.CITY_DETAILS_INPUT
        )

        element.clear()
        element.send_keys(value)

    def update_postal_code(self, value):

        element = wait_for_element(
            self.driver,
            UsersLocators.POSTAL_CODE_DETAILS_INPUT
        )

        element.clear()
        element.send_keys(value)

    def update_address(self, value):

        element = wait_for_element(
            self.driver,
            UsersLocators.ADDRESS_DETAILS_INPUT
        )

        element.clear()
        element.send_keys(value)

    def select_dropdown_option(self, locator, value):

        wait_for_element(
            self.driver,
            locator
        ).click()

        option = (
            By.XPATH,
            f"//*[normalize-space()='{value}']"
        )

        wait_for_element(
            self.driver,
            option
        ).click()

    def update_team(self, value):

        self.select_dropdown_option(
            UsersLocators.TEAM_DROPDOWN,
            value
        )

    def update_country(self, value):

        self.select_dropdown_option(
            UsersLocators.COUNTRY_DROPDOWN,
            value
        )

    def update_province(self, value):

        self.select_dropdown_option(
            UsersLocators.PROVINCE_DROPDOWN,
            value
        )

    def is_save_changes_button_enabled(self):

        return wait_for_element(
            self.driver,
            UsersLocators.SAVE_CHANGES_BUTTON
        ).is_enabled()

    def click_save_changes(self):

        wait_for_element(
            self.driver,
            UsersLocators.SAVE_CHANGES_BUTTON
        ).click()

    def is_success_message_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.USER_UPDATED_SUCCESS_MESSAGE
        ).is_displayed()

    # ==========================================
    # Create User
    # ==========================================

    def click_create_new_user(self):

        wait_for_element(
            self.driver,
            UsersLocators.CREATE_NEW_USER_BUTTON
        ).click()

    def is_create_user_modal_opened(self):

        return wait_for_element(
            self.driver,
            UsersLocators.ADD_USER_MODAL_TITLE
        ).is_displayed()

    def is_users_page_opened(self):

        return "/dashboard/users" in self.driver.current_url

    def is_user_displayed(self, value):

        return value in self.driver.page_source


    # ==========================================
    # User Actions
    # ==========================================

    def click_details(self):

        self.open_details()

    def click_activate(self):

        self.open_first_user_actions()

        wait_for_element(
            self.driver,
            UsersLocators.ACTIVATE_OPTION
        ).click()

    def click_deactivate(self):

        self.open_first_user_actions()

        wait_for_element(
            self.driver,
            UsersLocators.DEACTIVATE_OPTION
        ).click()

    def is_activate_dialog_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.ACTIVATE_DIALOG_TITLE
        ).is_displayed()

    def is_deactivate_dialog_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.DEACTIVATE_DIALOG_TITLE
        ).is_displayed()

    def click_confirm_action(self):

        wait_for_element(
            self.driver,
            UsersLocators.CONFIRM_ACTION_BUTTON
        ).click()

    def click_cancel_action(self):

        wait_for_element(
            self.driver,
            UsersLocators.CANCEL_ACTION_BUTTON
        ).click()

    def is_action_success_message_displayed(self):

        return wait_for_element(
            self.driver,
            UsersLocators.ACTION_SUCCESS_MESSAGE
        ).is_displayed()

    def activate_first_user(self):

        self.click_activate()

        self.click_confirm_action()

        return self.is_action_success_message_displayed()

    def deactivate_first_user(self):

        self.click_deactivate()

        self.click_confirm_action()

        return self.is_action_success_message_displayed()