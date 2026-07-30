import time

import pytest

from data.test_data import BASE_URL
from pages.users_page import UsersPage
from pages.create_user_page import CreateUserPage


@pytest.fixture
def users_pages(logged_in_user):

    logged_in_user.get(
        BASE_URL + "/dashboard/users"
    )

    users_page = UsersPage(logged_in_user)
    create_user_page = CreateUserPage(logged_in_user)

    return users_page, create_user_page


# ===========================================
# UI Tests
# ===========================================

def test_open_create_user_modal(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    assert create_user_page.is_modal_opened()


def test_create_user_required_fields_displayed(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    assert create_user_page.is_first_name_displayed()
    assert create_user_page.is_last_name_displayed()
    assert create_user_page.is_email_displayed()
    assert create_user_page.is_phone_displayed()


def test_required_fields_validation(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    create_user_page.click_save()

    assert create_user_page.is_first_name_required_displayed()
    assert create_user_page.is_last_name_required_displayed()
    assert create_user_page.is_email_required_displayed()


def test_remaining_fields_displayed(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    assert create_user_page.is_country_displayed()
    assert create_user_page.is_province_displayed()
    assert create_user_page.is_city_displayed()
    assert create_user_page.is_postal_code_displayed()
    assert create_user_page.is_address_displayed()
    assert create_user_page.is_save_button_displayed()
    assert create_user_page.is_close_button_displayed()


def test_default_status_is_active(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    assert create_user_page.get_default_status() == "Active"


def test_province_disabled_before_country_selection(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    assert create_user_page.is_province_disabled()


# ===========================================
# Functional Tests
# ===========================================

def test_create_user_successfully(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    unique = str(int(time.time()))

    create_user_page.create_user(
        first_name="Automation",
        last_name="Tester",
        email=f"automation{unique}@mail.com",
        phone="01012345678",
        team="User Test",
        country="Canada",
        province="Ontario",
        city="Toronto",
        postal_code="12345",
        address="Automation Street"
    )

    assert create_user_page.is_success_message_displayed()


def test_duplicate_email(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    create_user_page.create_user(
        first_name="Automation",
        last_name="Tester",
        email="aaqq@gmail.coom",
        phone="01012345678",
        team="User Test",
        country="Canada",
        province="Ontario",
        city="Toronto",
        postal_code="12345",
        address="Automation Street"
    )

    assert create_user_page.is_email_already_exists_displayed()


def test_invalid_email(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    create_user_page.create_user(
        first_name="Automation",
        last_name="Tester",
        email="automation.com",
        phone="01012345678",
        team="User Test",
        country="Canada",
        province="Ontario",
        city="Toronto",
        postal_code="12345",
        address="Automation Street"
    )

    assert create_user_page.is_invalid_email_displayed()

def test_province_enabled_after_select_country(users_pages):
     users_page, create_user_page = users_pages

     users_page.click_create_new_user()

     assert create_user_page.is_province_disabled()

     create_user_page.select_country("Canada")

     assert create_user_page.is_province_enabled()

def test_close_create_user_modal(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    create_user_page.click_close()

    assert create_user_page.is_modal_closed()

def test_view_users_list_after_create(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    unique = str(int(time.time()))

    create_user_page.create_user(
        first_name="Automation",
        last_name="Tester",
        email=f"automation{unique}@mail.com",
        phone="01012345678",
        team="User Test",
        country="Canada",
        province="Ontario",
        city="Toronto",
        postal_code="12345",
        address="Automation Street"
    )

    assert create_user_page.is_success_message_displayed()

    create_user_page.click_view_users_list()

    assert users_page.is_users_page_opened()

def test_search_created_user(users_pages):

    users_page, create_user_page = users_pages

    users_page.click_create_new_user()

    unique = str(int(time.time()))

    email = f"automation{unique}@mail.com"

    create_user_page.create_user(
        first_name="Automation",
        last_name="Tester",
        email=email,
        phone="01012345678",
        team="User Test",
        country="Canada",
        province="Ontario",
        city="Toronto",
        postal_code="12345",
        address="Automation Street"
    )

    create_user_page.click_view_users_list()

    users_page.search_user(email)

    assert users_page.is_user_displayed(email)