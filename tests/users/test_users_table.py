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


def test_users_table_displayed(
        users_page
):

    assert (
        users_page.is_users_table_displayed()
    )


def test_select_all_checkbox_displayed(
        users_page
):

    assert (
        users_page.is_select_all_checkbox_displayed()
    )


def test_user_name_header_displayed(
        users_page
):

    assert (
        users_page.is_user_name_header_displayed()
    )


def test_team_header_displayed(
        users_page
):

    assert (
        users_page.is_team_header_displayed()
    )


def test_email_header_displayed(
        users_page
):

    assert (
        users_page.is_email_header_displayed()
    )


def test_country_header_displayed(
        users_page
):

    assert (
        users_page.is_country_header_displayed()
    )


def test_province_header_displayed(
        users_page
):

    assert (
        users_page.is_province_header_displayed()
    )


def test_payments_header_displayed(
        users_page
):

    assert (
        users_page.is_payments_header_displayed()
    )


def test_phone_number_header_displayed(
        users_page
):

    assert (
        users_page.is_phone_number_header_displayed()
    )


def test_status_header_displayed(
        users_page
):

    assert (
        users_page.is_status_header_displayed()
    )


def test_actions_header_displayed(
        users_page
):

    assert (
        users_page.is_actions_header_displayed()
    )


def test_at_least_one_user_record_displayed(
        users_page
):

    assert (
        users_page.get_users_count()
        > 0
    )


def test_search_existing_user(
        users_page
):

    users_page.search_user(
        "Auto Test"
    )

    assert (
        users_page.get_first_user_name()
        == "Auto Test"
    )


def test_search_non_existing_user(
        users_page
):

    users_page.search_user(
        "XYZ123456"
    )

    assert (
        users_page.is_no_results_displayed()
    )


def test_empty_state_displayed_for_invalid_search(
        users_page
):

    users_page.search_user(
        "INVALID_USER_999999"
    )

    assert (
        users_page.is_no_results_displayed()
    )


def test_previous_button_displayed(
        users_page
):

    assert (
        users_page.is_previous_button_displayed()
    )


def test_next_button_displayed(
        users_page
):

    assert (
        users_page.is_next_button_displayed()
    )


def test_page_size_displayed(
        users_page
):

    assert (
        users_page.is_page_size_displayed()
    )


def test_showing_records_text_displayed(
        users_page
):

    assert (
        "Showing"
        in users_page.get_showing_records_text()
    )


def test_showing_records_contains_entries(
        users_page
):

    assert (
        "entries"
        in users_page.get_showing_records_text()
    )