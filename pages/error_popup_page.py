from locators.error_popup_locators import ErrorPopupLocators
from utils.waits import wait_for_element


class ErrorPopupPage:

    def __init__(self, driver):
        self.driver = driver

    def is_login_error_displayed(self):

        return wait_for_element(
            self.driver,
            ErrorPopupLocators.LOGIN_ERROR_TITLE
        ).is_displayed()

    def dismiss_error(self):

        wait_for_element(
            self.driver,
            ErrorPopupLocators.DISMISS_BUTTON
        ).click()