from pages.profile_page import ProfilePage


def test_profile_title(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_page_title_displayed()


def test_profile_name(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_profile_name_displayed()


def test_first_name_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_first_name_field_displayed()


def test_last_name_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_last_name_field_displayed()


def test_email_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_email_field_displayed()


def test_country_selector_dropdown_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_country_selector_dropdown_displayed()


def test_phone_number_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_phone_number_field_displayed()


def test_password_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_password_field_displayed()


def test_address_field_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_address_field_displayed()


def test_team_dropdown_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_team_dropdown_displayed()


def test_save_changes_button_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_save_changes_button_displayed()


def test_change_photo_link_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_change_photo_link_displayed()


def test_change_email_link_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_change_email_link_displayed()


def test_change_password_link_displayed(logged_in_user):
    profile_page = ProfilePage(logged_in_user)
    assert profile_page.is_change_password_link_displayed()