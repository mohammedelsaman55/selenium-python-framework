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
# Details
# ===========================================

def test_open_user_details(users_page):

    users_page.open_details()

    assert users_page.is_user_details_page_opened()


def test_edit_first_name(users_page):

    users_page.open_details()

    unique = str(int(time.time()))

    users_page.update_first_name(
        f"Automation{unique}"
    )

    assert users_page.is_save_changes_button_enabled()

    users_page.click_save_changes()

    assert users_page.is_success_message_displayed()


# ===========================================
# Activate
# ===========================================

def test_open_activate_dialog(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_activate_option_displayed():
        pytest.skip("User is already Active")

    users_page.click_activate()

    assert users_page.is_activate_dialog_displayed()


def test_cancel_activate(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_activate_option_displayed():
        pytest.skip("User is already Active")

    users_page.click_activate()

    assert users_page.is_activate_dialog_displayed()

    users_page.click_cancel_action()

    assert not users_page.is_action_success_message_displayed()


def test_activate_user(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_activate_option_displayed():
        pytest.skip("User is already Active")

    users_page.click_activate()

    assert users_page.is_activate_dialog_displayed()

    users_page.click_confirm_action()

    assert users_page.is_action_success_message_displayed()


# ===========================================
# Deactivate
# ===========================================

def test_open_deactivate_dialog(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_deactivate_option_displayed():
        pytest.skip("User is already Inactive")

    users_page.click_deactivate()

    assert users_page.is_deactivate_dialog_displayed()


def test_cancel_deactivate(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_deactivate_option_displayed():
        pytest.skip("User is already Inactive")

    users_page.click_deactivate()

    assert users_page.is_deactivate_dialog_displayed()

    users_page.click_cancel_action()

    assert not users_page.is_action_success_message_displayed()


def test_deactivate_user(users_page):

    users_page.open_first_user_actions()

    if not users_page.is_deactivate_option_displayed():
        pytest.skip("User is already Inactive")

    users_page.click_deactivate()

    assert users_page.is_deactivate_dialog_displayed()

    users_page.click_confirm_action()

    assert users_page.is_action_success_message_displayed()