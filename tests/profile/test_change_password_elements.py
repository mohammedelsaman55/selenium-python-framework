from pages.profile_page import ProfilePage


def test_current_password_field_displayed(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    assert (
        profile_page.is_current_password_field_displayed()
    )


def test_new_password_field_displayed(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    assert (
        profile_page.is_new_password_field_displayed()
    )


def test_confirm_password_field_displayed(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    assert (
        profile_page.is_confirm_password_field_displayed()
    )


def test_save_password_button_displayed(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_change_password_popup()

    assert (
        profile_page.is_save_password_button_displayed()
    )