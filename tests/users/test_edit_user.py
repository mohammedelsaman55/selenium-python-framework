import time

import pytest

from data.test_data import BASE_URL
from pages.users_page import UsersPage


@pytest.fixture
def users_page(logged_in_user):

    logged_in_user.get(
        BASE_URL + "/dashboard/users"
    )

    return UsersPage(logged_in_user)


# ===========================================
# UI Tests
# ===========================================

def test_open_edit_user_page(users_page):

    users_page.open_details()

    assert users_page.is_user_details_page_opened()


def test_save_button_disabled_before_changes(users_page):

    users_page.open_details()

    assert not users_page.is_save_changes_button_enabled()


def test_save_button_enabled_after_first_name_change(users_page):

    users_page.open_details()

    current_name = users_page.get_first_name()

    users_page.update_first_name(
        current_name + " Test"
    )

    assert users_page.is_save_changes_button_enabled()


# ===========================================
# Functional Tests
# ===========================================

def test_update_first_name(users_page):

    users_page.open_details()

    unique = str(int(time.time()))

    new_name = "Automation" + unique

    users_page.update_first_name(new_name)

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()

def test_update_last_name(users_page):

    users_page.open_details()

    unique = str(int(time.time()))

    users_page.update_last_name(
        "Tester" + unique
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_phone(users_page):

    users_page.open_details()

    users_page.update_phone(
        "01099998888"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_team(users_page):

    users_page.open_details()

    users_page.update_team(
        "User Test"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_country(users_page):

    users_page.open_details()

    users_page.update_country(
        "Canada"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_province(users_page):

    users_page.open_details()

    users_page.update_country("Canada")

    users_page.update_province(
        "Ontario"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_city(users_page):

    users_page.open_details()

    users_page.update_city(
        "Toronto"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_postal_code(users_page):

    users_page.open_details()

    users_page.update_postal_code(
        "12345"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_update_address(users_page):

    users_page.open_details()

    users_page.update_address(
        "Automation Street"
    )

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


def test_updated_data_persist_after_refresh(users_page):

    users_page.open_details()

    unique = str(int(time.time()))

    new_name = "Automation" + unique

    users_page.update_first_name(new_name)

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()

    users_page.driver.refresh()

    users_page.open_details()

    assert users_page.get_first_name() == new_name