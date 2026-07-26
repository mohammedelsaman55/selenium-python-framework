from pages.login_page import LoginPage
from pages.otp_page import OtpPage
from pages.error_popup_page import ErrorPopupPage

from data.test_data import (
    BASE_URL,
    VALID_EMAIL,
    VALID_PASSWORD,
    VALID_OTP
)

from utils.waits import wait_for_url_contains


def test_page_title_displayed(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    assert login_page.is_page_title_displayed()


def test_email_placeholder(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    assert (
        login_page.get_email_placeholder()
        == "Enter your email address"
    )


def test_password_placeholder(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    assert (
        login_page.get_password_placeholder()
        == "Enter your password"
    )


def test_login_button_text(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    assert (
        login_page.get_login_button_text()
        == "Login"
    )


def test_password_hidden_by_default(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    assert (
        login_page.get_password_field_type()
        == "password"
    )


def test_password_visibility_toggle(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.show_password()

    assert (
        login_page.get_password_field_type()
        == "text"
    )


def test_empty_email(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "",
        VALID_PASSWORD
    )

    assert (
        login_page.is_email_required_message_displayed()
    )


def test_empty_password(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        ""
    )

    assert (
        login_page.is_password_required_message_displayed()
    )


def test_invalid_email_format(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "invalid-email",
        VALID_PASSWORD
    )

    assert (
        login_page.is_invalid_email_message_displayed()
    )


def test_login_with_enter(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login_with_enter(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    assert otp_page.is_otp_title_displayed()


def test_invalid_login(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        "WrongPassword123"
    )

    error_popup = ErrorPopupPage(driver)

    assert error_popup.is_login_error_displayed()


def test_valid_login(driver):

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
        VALID_OTP
    )

    otp_page.verify_code()

    wait_for_url_contains(
        driver,
        "/dashboard/profile"
    )

    assert "/dashboard/profile" in driver.current_url


def test_email_with_leading_spaces(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        f"   {VALID_EMAIL}",
        VALID_PASSWORD
    )

    assert (
        login_page.is_invalid_email_message_displayed()
    )


def test_email_with_trailing_spaces(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        f"{VALID_EMAIL}   ",
        VALID_PASSWORD
    )

    assert (
        login_page.is_invalid_email_message_displayed()
    )