from pages.login_page import LoginPage
from pages.otp_page import OtpPage

from data.test_data import (
    BASE_URL,
    VALID_EMAIL,
    VALID_PASSWORD
)


def test_otp_title(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    assert otp_page.is_otp_title_displayed()


def test_empty_otp(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    otp_page.verify_code()

    assert otp_page.is_empty_otp_message_displayed()


def test_invalid_otp(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    otp_page.enter_otp(
        "1111"
    )

    otp_page.verify_code()

    assert (
        otp_page.is_invalid_otp_message_displayed()
    )


def test_resend_otp(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    otp_page.click_resend_code()

    assert (
        otp_page.get_timer_value()
        == "3:00"
    )