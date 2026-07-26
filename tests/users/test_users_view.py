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


def test_users_page_title_displayed(
        users_page
):

    assert (
        users_page.is_page_title_displayed()
    )


def test_create_new_user_button_displayed(
        users_page
):

    assert (
        users_page.is_create_new_user_button_displayed()
    )


def test_search_input_displayed(
        users_page
):

    assert (
        users_page.is_search_input_displayed()
    )


def test_bulk_actions_dropdown_displayed(
        users_page
):

    assert (
        users_page.is_bulk_actions_dropdown_displayed()
    )


def test_add_filter_button_displayed(
        users_page
):

    assert (
        users_page.is_add_filter_button_displayed()
    )


def test_reset_filter_button_displayed(
        users_page
):

    assert (
        users_page.is_reset_filter_button_displayed()
    )


def test_reset_sorting_button_displayed(
        users_page
):

    assert (
        users_page.is_reset_sorting_button_displayed()
    )


def test_export_pdf_button_displayed(
        users_page
):

    assert (
        users_page.is_export_pdf_button_displayed()
    )


def test_export_csv_button_displayed(
        users_page
):

    assert (
        users_page.is_export_csv_button_displayed()
    )