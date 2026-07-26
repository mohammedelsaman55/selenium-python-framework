from locators.login_locators import LoginLocators
from utils.waits import wait_for_element
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):

        wait_for_element(
            self.driver,
            LoginLocators.EMAIL
        ).send_keys(email)

        wait_for_element(
            self.driver,
            LoginLocators.PASSWORD
        ).send_keys(password)

        wait_for_element(
            self.driver,
            LoginLocators.LOGIN_BUTTON
        ).click()

    def is_email_required_message_displayed(self):

        return wait_for_element(
            self.driver,
            LoginLocators.EMAIL_REQUIRED_MESSAGE
        ).is_displayed()

    def is_password_required_message_displayed(self):
        return wait_for_element(
            self.driver,
            LoginLocators.PASSWORD_REQUIRED_MESSAGE
        ).is_displayed()

    def is_invalid_email_message_displayed(self):
        return wait_for_element(
            self.driver,
            LoginLocators.INVALID_EMAIL_MESSAGE
        ).is_displayed()

    def is_page_title_displayed(self):
        return wait_for_element(
            self.driver,
            LoginLocators.PAGE_TITLE
        ).is_displayed()

    def get_email_placeholder(self):
        return wait_for_element(
            self.driver,
            LoginLocators.EMAIL
        ).get_attribute("placeholder")

    def get_password_placeholder(self):
        return wait_for_element(
            self.driver,
            LoginLocators.PASSWORD
        ).get_attribute("placeholder")

    def get_login_button_text(self):
        return wait_for_element(
            self.driver,
            LoginLocators.LOGIN_BUTTON
        ).text

    def get_password_field_type(self):
        return wait_for_element(
            self.driver,
            LoginLocators.PASSWORD
        ).get_attribute("type")

    def show_password(self):
        wait_for_element(
            self.driver,
            LoginLocators.PASSWORD_VISIBILITY_BUTTON
        ).click()


    def login_with_enter(self, email, password):
        wait_for_element(
            self.driver,
            LoginLocators.EMAIL
        ).send_keys(email)

        wait_for_element(
            self.driver,
            LoginLocators.PASSWORD
        ).send_keys(password + Keys.ENTER)