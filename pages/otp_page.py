from locators.otp_locators import OtpLocators
from utils.waits import wait_for_element


class OtpPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_otp(self, otp):

        wait_for_element(
            self.driver,
            OtpLocators.OTP_INPUTS
        )

        otp_inputs = self.driver.find_elements(
            *OtpLocators.OTP_INPUTS
        )

        for i in range(len(otp)):
            otp_inputs[i].send_keys(otp[i])

    def verify_code(self):

        wait_for_element(
            self.driver,
            OtpLocators.VERIFY_BUTTON
        ).click()

    def is_otp_title_displayed(self):
        return wait_for_element(
            self.driver,
            OtpLocators.OTP_TITLE
        ).is_displayed()

    def is_empty_otp_message_displayed(self):
        return wait_for_element(
            self.driver,
            OtpLocators.EMPTY_OTP_MESSAGE
        ).is_displayed()

    def is_invalid_otp_message_displayed(self):
        return wait_for_element(
            self.driver,
            OtpLocators.INVALID_OTP_MESSAGE
        ).is_displayed()

    def click_resend_code(self):
        wait_for_element(
            self.driver,
            OtpLocators.RESEND_CODE_BUTTON
        ).click()

    def get_timer_value(self):
        return wait_for_element(
            self.driver,
            OtpLocators.OTP_TIMER
        ).text