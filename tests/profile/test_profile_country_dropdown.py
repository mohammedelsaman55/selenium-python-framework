from pages.profile_page import ProfilePage


def test_country_dropdown_opens(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_country_dropdown()

    assert (
        profile_page.is_country_selector_dropdown_displayed()
    )


def test_search_country(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_country_dropdown()

    profile_page.search_country(
        "Egypt"
    )

    assert True


def test_select_country(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.open_country_dropdown()

    profile_page.search_country(
        "Egypt"
    )

    profile_page.select_egypt_country()

    assert (
        "Egypt"
        in
        profile_page.get_selected_country()
    )