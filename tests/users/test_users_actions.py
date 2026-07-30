import pytest

from data.test_data import BASE_URL
from pages.users_page import UsersPage


@pytest.fixture
def users_page(logged_in_user):

    logged_in_user.get(
        BASE_URL + "/dashboard/users"
    )

    return UsersPage(
        logged_in_user
    )


def test_actions_menu_opened(
        users_page
):

    users_page.open_first_user_actions()

    assert True


def test_details_option_displayed(
        users_page
):

    users_page.open_first_user_actions()

    assert (
        users_page.is_details_option_displayed()
    )


def test_activate_or_deactivate_option_displayed(
        users_page
):

    users_page.open_first_user_actions()

    assert (
        users_page.is_activate_option_displayed()
        or
        users_page.is_deactivate_option_displayed()
    )


def test_actions_menu_contains_two_options(
        users_page
):

    users_page.open_first_user_actions()

    count = 0

    if users_page.is_details_option_displayed():
        count += 1

    if users_page.is_activate_option_displayed():
        count += 1

    if users_page.is_deactivate_option_displayed():
        count += 1

    assert count == 2