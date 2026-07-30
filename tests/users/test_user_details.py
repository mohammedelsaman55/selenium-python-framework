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


def test_open_user_details(users_page):

    users_page.open_details()

    assert users_page.is_user_details_page_opened()


def test_first_name_is_displayed(users_page):

    users_page.open_details()

    assert users_page.get_first_name() != ""


def test_save_changes_button_disabled_by_default(users_page):

    users_page.open_details()

    assert not users_page.is_save_changes_button_enabled()


def test_edit_first_name_enables_save_button(users_page):

    users_page.open_details()

    original_name = users_page.get_first_name()

    users_page.update_first_name(
        original_name + "1"
    )

    assert users_page.is_save_changes_button_enabled()


def test_update_first_name(users_page):

    users_page.open_details()

    original_name = users_page.get_first_name()

    users_page.update_first_name(
        original_name + "1"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()
