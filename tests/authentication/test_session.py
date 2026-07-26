import time

from pages.profile_page import ProfilePage

from data.test_data import (
    BASE_URL
)

from utils.waits import wait_for_url_contains


def test_logout(logged_in_user):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.logout()

    wait_for_url_contains(
        logged_in_user,
        "/dashboard/login"
    )

    assert "/dashboard/login" in logged_in_user.current_url


def test_access_dashboard_after_logout(logged_in_user):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.logout()

    wait_for_url_contains(
        logged_in_user,
        "/dashboard/login"
    )

    logged_in_user.get(
        BASE_URL + "/dashboard/profile"
    )

    assert "/dashboard/login" in logged_in_user.current_url


def test_access_login_while_logged_in(logged_in_user):

    time.sleep(5)

    logged_in_user.get(
        BASE_URL + "/dashboard/login"
    )

    assert (
        logged_in_user.current_url
        == BASE_URL + "/dashboard/profile"
    )


def test_session_timeout(logged_in_user):

    logged_in_user.delete_all_cookies()

    logged_in_user.refresh()

    wait_for_url_contains(
        logged_in_user,
        "/dashboard/login"
    )

    assert (
        "/dashboard/login"
        in logged_in_user.current_url
    )