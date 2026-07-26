from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.otp_page import OtpPage

from data.test_data import (
    BASE_URL,
    VALID_PASSWORD,
    TEMP_PASSWORD,
    VALID_EMAIL,
    VALID_OTP
)
from utils.waits import (
    wait_for_url_contains
)


def test_open_change_password_popup(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    assert (
        profile_page.is_change_password_popup_displayed()
    )


def test_passwords_do_not_match_validation(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    profile_page.enter_current_password(
        VALID_PASSWORD
    )

    profile_page.enter_new_password(
        TEMP_PASSWORD
    )

    profile_page.enter_confirm_password(
        "Test@123456b"
    )

    profile_page.click_save_password_button()

    assert (
        profile_page.is_passwords_do_not_match_message_displayed()
    )


def test_change_password_successfully(
        logged_in_user
):

    old_password = (
        VALID_PASSWORD
    )

    new_password = (
        TEMP_PASSWORD
    )

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    profile_page.enter_current_password(
        old_password
    )

    profile_page.enter_new_password(
        new_password
    )

    profile_page.enter_confirm_password(
        new_password
    )

    profile_page.click_save_password_button()

    wait_for_url_contains(
        logged_in_user,
        "/login"
    )

    login_page = LoginPage(
        logged_in_user
    )

    login_page.login(
        VALID_EMAIL,
        new_password
    )

    otp_page = OtpPage(
        logged_in_user
    )

    otp_page.enter_otp(
        VALID_OTP
    )

    otp_page.verify_code()

    wait_for_url_contains(
        logged_in_user,
        "/dashboard/profile"
    )

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    profile_page.enter_current_password(
        new_password
    )

    profile_page.enter_new_password(
        old_password
    )

    profile_page.enter_confirm_password(
        old_password
    )

    profile_page.click_save_password_button()

    wait_for_url_contains(
        logged_in_user,
        "/login"
    )


def test_login_with_restored_password(
        driver
):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(
        driver
    )

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(
        driver
    )

    otp_page.enter_otp(
        VALID_OTP
    )

    otp_page.verify_code()

    wait_for_url_contains(
        driver,
        "/dashboard/profile"
    )

    assert (
        "/dashboard/profile"
        in
        driver.current_url
    )