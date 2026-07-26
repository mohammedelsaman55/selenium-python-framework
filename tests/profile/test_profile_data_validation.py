from pages.profile_page import ProfilePage


def test_first_name_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_first_name_value()
        != ""
    )


def test_last_name_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_last_name_value()
        != ""
    )


def test_email_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_email_value()
        != ""
    )


def test_phone_number_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_phone_number_value()
        != ""
    )


def test_address_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_address_value()
        != ""
    )


def test_selected_country_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_selected_country()
        != ""
    )


def test_team_value_loaded(logged_in_user):

    profile_page = ProfilePage(logged_in_user)

    assert (
        profile_page.get_team_value()
        != ""
    )